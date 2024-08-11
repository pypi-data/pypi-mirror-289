import os
import requests
import asyncio
import websockets
import json
from rich import print
from typing import List
from rich.progress import Progress
import base64
from digifoam.constants import CLI_PROXY_SERVER_URL
from digifoam.utils import if_obj, is_text_file
from digifoam.types import FileTree, FileNode, FolderNode

from rich.console import Console
from rich.live import Live
from rich.spinner import Spinner
from datetime import datetime


def create_project(user_key: str, tree: FileTree):
    try:
        response = requests.post(
            f"{CLI_PROXY_SERVER_URL}/create-project",
            json={"user_key": user_key, "file_tree": tree},
        )
        return response.json()
    except Exception as e:
        raise e


def create_debug_project(user_key: str, prompt: str, tree: FileTree):
    try:
        response = requests.post(
            f"{CLI_PROXY_SERVER_URL}/create-debug-project",
            json={"user_key": user_key, "prompt": prompt, "file_tree": tree},
        )
        return response.json()
    except Exception as e:
        raise e


def upload_files(file_tree: FileTree, project_id: str):
    try:
        with Progress() as progress:
            task = progress.add_task("[green]Syncing files...", total=len(file_tree))

            for node in file_tree:
                if node["type"] == "file":
                    upload_file(node, project_id, progress, task)
                else:
                    upload_folder(node, project_id, progress, task)

    except Exception as e:
        print(f"[bold red]An error occurred during file upload:[/bold red] {str(e)}")
        raise


def upload_file(node: FileNode, project_id: str, progress: Progress, task):
    path = node["path"]
    size = os.path.getsize(path)

    if if_obj(path):
        file_content = b"Geometry file not supported for displaying on editor."
        filename = os.path.basename(path)
    elif not is_text_file(path):
        file_content = b"File format not supported for displaying on editor."
        filename = os.path.basename(path)
    elif size > 100 * 1024:  # 100KB in bytes
        file_content = b"File is too large to display on editor. Supports up to 100KB."
        filename = os.path.basename(path)
    else:
        with open(path, "rb") as f:
            file_content = f.read()
        filename = path

    response = requests.post(
        f"{CLI_PROXY_SERVER_URL}/upload-files",
        files={"file": (filename, file_content)},
        data={"case_id": project_id, "file_path": path},
    )

    response_data = response.json()
    if response.status_code != 200 or "error" in response_data:
        print(
            f"[bold red]Error uploading file[/bold red] {path}: {response_data.get('error', 'Unknown error')}"
        )

    progress.update(task, advance=1)


def upload_folder(node: FolderNode, project_id: str, progress: Progress, task):
    for child in node["children"]:
        if child["type"] == "file":
            upload_file(child, project_id, progress, task)
        else:
            upload_folder(child, project_id, progress, task)


async def create_case(
    user_id: str, sim_type: str, case_description: str, geometries: List[str]
):
    ws_server = CLI_PROXY_SERVER_URL.replace("http://", "").replace("https://", "")
    ws_protocol = "wss://" if CLI_PROXY_SERVER_URL.startswith("https://") else "ws://"
    uri = f"{ws_protocol}{ws_server}/ws/new?user_id={user_id}"

    console = Console()
    spinner = Spinner("dots", text="Creating case...")

    async with websockets.connect(uri) as websocket:
        # Send user_id, simulationType, and caseDescription as JSON
        await websocket.send(
            json.dumps(
                {
                    "user_id": user_id,
                    "sim_type": sim_type,
                    "case_description": case_description,
                    "geometries": geometries,
                }
            )
        )

        with Live(spinner, console=console, refresh_per_second=10) as live:
            while True:
                response = await websocket.recv()
                data = json.loads(response)
                if data.get("stage") == "INIT":
                    spinner.text = data.get("message")
                elif data.get("stage") == "FINISHED":
                    live.stop()
                    console.print(data.get("message"))
                    return data.get("case_id")


def download_case_files(case_id: str, relative_directory: str):
    # Make a request to fetch /download-files
    response = requests.get(
        f"{CLI_PROXY_SERVER_URL}/download-files", json={"case_id": case_id}
    )

    if response.status_code == 200:
        data = response.json()
        file_contents = data.get("files", [])

        # Create the relative directory if it doesn't exist
        os.makedirs(relative_directory, exist_ok=True)

        # Process and save each file
        for file in file_contents:
            file_name = file["name"]
            file_content = base64.b64decode(file["content"])

            file_path = os.path.join(relative_directory, file_name)

            # Ensure the directory for this file exists
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            # Write the file content
            with open(file_path, "wb") as f:
                f.write(file_content)

        print(
            f"Created {len(file_contents)} files to [bold green]{relative_directory}[/bold green]"
        )
    else:
        print(f"Error downloading files: {response.status_code}")


def create_case_sync(
    user_id: str, sim_type: str, case_description: str, geometries: List[str]
):
    return asyncio.run(create_case(user_id, sim_type, case_description, geometries))


async def listen_for_changes(case_id: str):
    # Remove http:// or https:// from the beginning of the URL
    ws_server = CLI_PROXY_SERVER_URL.replace("http://", "").replace("https://", "")
    # Use wss:// for https connections, ws:// for http
    ws_protocol = "wss://" if CLI_PROXY_SERVER_URL.startswith("https://") else "ws://"
    uri = f"{ws_protocol}{ws_server}/ws/link?case_id={case_id}"
    try:
        async with websockets.connect(uri) as websocket:
            while True:
                try:
                    message = await asyncio.wait_for(websocket.recv(), timeout=1)
                    payload = json.loads(message)
                    timestamp = datetime.now().strftime("%H:%M:%S")

                    if payload["type"] == "file_update":
                        data = payload["data"]
                        path = payload["metadata"]["fileName"]
                        # Convert base64 to text
                        text_content = base64.b64decode(data).decode("utf-8")
                        with open(path, "w", encoding="utf-8") as f:
                            f.write(text_content)
                        print(f"[{timestamp}] [green]File updated:[/green] {path}")
                    elif payload["type"] == "file_created":
                        data = payload["data"]
                        path = payload["metadata"]["fileName"]
                        text_content = base64.b64decode(data).decode("utf-8")

                        # Use current directory if path doesn't have a directory component
                        dir_path = os.path.dirname(path)
                        if dir_path:
                            os.makedirs(dir_path, exist_ok=True)
                        else:
                            path = os.path.join(os.getcwd(), path)

                        with open(path, "w", encoding="utf-8") as f:
                            f.write(text_content)
                        print(f"[{timestamp}] [green]File created:[/green] {path}")
                    elif payload["type"] == "file_deleted":
                        path = payload["meta_data"]["fileName"]

                        # Ensure the path is within the current working directory
                        abs_path = os.path.abspath(path)
                        if os.path.commonpath([abs_path, os.getcwd()]) == os.getcwd():
                            if os.path.exists(abs_path):
                                os.remove(abs_path)
                                print(f"[{timestamp}] [red]File deleted:[/red] {path}")

                                # Check if the parent folder is empty
                                parent_folder = os.path.dirname(abs_path)
                                if parent_folder != os.getcwd() and not os.listdir(
                                    parent_folder
                                ):
                                    os.rmdir(parent_folder)
                                    print(
                                        f"[{timestamp}] [red]Empty folder deleted:[/red] {parent_folder}"
                                    )
                            else:
                                print(
                                    f"[{timestamp}] [yellow]File not found for deletion:[/yellow] {path}"
                                )
                        else:
                            print(
                                f"[{timestamp}] [bold red]Security warning:[/bold red] Attempted to delete file outside of working directory: {path}"
                            )
                    elif payload["type"] == "file_renamed":
                        old_path = payload["meta_data"]["oldFileName"]
                        new_path = payload["meta_data"]["newFileName"]

                        # Ensure both paths are within the current working directory
                        abs_old_path = os.path.abspath(old_path)
                        abs_new_path = os.path.abspath(new_path)

                        if (
                            os.path.commonpath([abs_old_path, os.getcwd()])
                            == os.getcwd()
                            and os.path.commonpath([abs_new_path, os.getcwd()])
                            == os.getcwd()
                        ):
                            if os.path.exists(abs_old_path):
                                # Create the directory for the new path if it doesn't exist
                                os.makedirs(
                                    os.path.dirname(abs_new_path), exist_ok=True
                                )
                                os.rename(abs_old_path, abs_new_path)
                                print(
                                    f"[{timestamp}] [yellow]File renamed:[/yellow] {old_path} -> {new_path}"
                                )
                            else:
                                print(
                                    f"[{timestamp}] [yellow]File not found for renaming:[/yellow] {old_path}"
                                )
                        else:
                            print(
                                f"[{timestamp}] [bold red]Security warning:[/bold red] Attempted to rename file outside of working directory: {old_path} -> {new_path}"
                            )

                except asyncio.TimeoutError:
                    pass
    except websockets.exceptions.InvalidStatusCode as e:
        print(
            f"[{timestamp}] [bold red]Failed to connect to WebSocket server:[/bold red] {e}"
        )
        print("[yellow]Please contact support if the issue persists.[/yellow]")
    except Exception as e:
        print(
            f"[{timestamp}] [bold red]An error occurred:[/bold red] {e}, please contact support."
        )
        # traceback.print_exc()


def listen_for_changes_sync(case_id: str):
    try:
        asyncio.run(listen_for_changes(case_id))
    except KeyboardInterrupt:
        print("\n[yellow]Connection closed.[/yellow]")
    finally:
        pass
