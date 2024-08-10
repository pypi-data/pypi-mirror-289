import typer
import os
from dotenv import load_dotenv
from rich import print
from rich.prompt import Prompt
from digifoam.utils import create_file_tree
from digifoam.constants import WEB_SERVER_URL
import shutil
from digifoam.api import (
    create_project,
    create_debug_project,
    upload_files,
    listen_for_changes_sync,
    create_case_sync,
    download_case_files,
)

load_dotenv()

app = typer.Typer()

global_user_id = "4c2a43d2-bad0-4b6a-bb8c-24bbf4fd805e"


@app.command()
def new(
    name: str = typer.Argument(..., help="Name of the project"),
    geometry: str = typer.Option(
        None, "--geometry", "-g", help="Path to geometry file or directory"
    ),
):
    """Create a new project from your text descriptions."""
    print(f"Creating new project: {name}")

    # Check if geometry is provided
    if geometry:
        if not os.path.exists(geometry):
            print(
                f"[bold red]Error:[/bold red] Geometry path '{geometry}' does not exist."
            )
            raise typer.Exit(code=1)

        # Get a list of all geometries, including nested files
        geometries = []
        for root, _, files in os.walk(geometry):
            for file in files:
                rel_path = os.path.relpath(os.path.join(root, file), geometry)
                geometries.append(rel_path)

        print("Using geometry:")
        for geom in geometries:
            print(f" - [bold blue]{geom}[/bold blue]")
        # TODO: Add logic to process the geometry file or directory
    else:
        print("No geometry specified. Creating case without geometry.")

    simulation_type = Prompt.ask(
        "[bold green]What type of simulation is this?[/bold green]"
    )
    case_description = Prompt.ask("[bold green]Please describe your case[/bold green]")

    case_id = create_case_sync(
        global_user_id, simulation_type, case_description, geometries
    )

    download_case_files(case_id, name)

    # get the relative path of all files in geometry
    if geometry:
        target_dir = os.path.join(name, "constant", "triSurface")
        os.makedirs(target_dir, exist_ok=True)
        for item in os.listdir(geometry):
            source_path = os.path.join(geometry, item)
            target_path = os.path.join(target_dir, item)
            if os.path.isdir(source_path):
                shutil.copytree(source_path, target_path)
            else:
                shutil.copy2(source_path, target_path)

    print(f"Project '{name}' created successfully! ")


@app.command()
def debug(
    log_files_path: str = typer.Argument(..., help="Directories with log files"),
    prompt: str = typer.Option(
        None, "--prompt", "-p", help="Additional prompt for debugging"
    ),
):
    """Debug with digifoam AI."""
    print(f"Debugging {log_files_path}")
    if not os.path.exists(log_files_path):
        print(f"[bold red]Error:[/bold red] Path '{log_files_path}' does not exist.")
        raise typer.Exit(code=1)

    if os.path.isfile(log_files_path):
        print(f"Debugging file: [bold]{log_files_path}[/bold]")
        paths = [log_files_path]
    else:
        print(f"Debugging files in directory: [bold]{log_files_path}[/bold]")
        paths = []
        for root, dirs, files in os.walk(log_files_path):
            for file in files:
                file_path = os.path.join(root, file)
                paths.append(file_path)

    if log_files_path == ".":
        paths = [p[2:] if p.startswith("./") else p for p in paths]

    # can we parse the path to see if log* exists?
    log_files = [p for p in paths if "log." in p]
    if len(log_files) <= 0:
        print(f"[bold red]No log* files found in {log_files_path}[/bold red]")
        return

    tree = create_file_tree(paths)
    data = create_debug_project(global_user_id, prompt, tree)
    case_id = data["case_id"]

    # Add a message for uploading files
    upload_files(tree, case_id)

    # digifoam link to case_id
    print(f"[bold green]Go to digifoam link to continue...[/bold green]")
    print(f"digifoam link [link]{WEB_SERVER_URL}/link/{case_id}?debug=True[/link]")

    listen_for_changes_sync(case_id)


@app.command()
def link(path: str = typer.Argument(..., help="Path to file or directory")):
    """link to the DigiFOAM editor for the specified directory or file."""
    if not os.path.exists(path):
        print(f"[bold red]Error:[/bold red] Path '{path}' does not exist.")
        raise typer.Exit(code=1)

    if os.path.isfile(path):
        print(f"Editing file: [bold]{path}[/bold]")
        paths = [path]
    else:
        print(f"Editing files in directory: [bold]{path}[/bold]")
        paths = []
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                paths.append(file_path)

    if path == ".":
        paths = [p[2:] if p.startswith("./") else p for p in paths]

    # create metadata of all files and their paths
    tree = create_file_tree(paths)
    data = create_project(global_user_id, tree)
    case_id = data["case_id"]

    # Add a message for uploading files
    upload_files(tree, case_id)

    # digifoam link to case_id
    print(f"digifoam link [link]{WEB_SERVER_URL}/link/{case_id}[/link]")

    listen_for_changes_sync(case_id)


@app.command()
def run(
    command: str = typer.Argument(..., help="Bash script or OpenFOAM command to run"),
    working_directory: str = typer.Option(
        ".", "--dir", "-d", help="Working directory for the command"
    ),
):
    """Run a bash script or OpenFOAM command and print the results in real-time."""
    import subprocess
    import sys
    import os
    import re
    import time
    import select

    print(f"[bold]Running command:[/bold] {command}")
    print(f"[bold]Working directory:[/bold] {working_directory}")

    try:
        # Run the command
        process = subprocess.Popen(
            command,
            shell=True,
            cwd=working_directory,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True,
        )

        time.sleep(1)

        # Function to find the most recently updated log file
        def get_latest_log_file():
            log_files = []
            for root, _, files in os.walk(working_directory):
                for file in files:
                    if file.startswith("log"):
                        log_path = os.path.join(root, file)
                        log_files.append(log_path)
            return max(log_files, key=os.path.getmtime) if log_files else None

        last_position = 0
        last_log_file = None

        # Print output in real-time and tail the most recent log file
        while process.poll() is None:
            # Use select to check if there's output to read
            readable, _, _ = select.select(
                [process.stdout, process.stderr], [], [], 0.1
            )

            for stream in readable:
                line = stream.readline()
                if line:
                    if stream == process.stderr:
                        print(f"[bold yellow]STDERR: {line.strip()}[/bold yellow]")
                    else:
                        print(f"STDOUT: {line.strip()}")

            # Find and tail the most recent log file
            current_log_file = get_latest_log_file()
            if current_log_file and current_log_file != last_log_file:
                last_log_file = current_log_file
                last_position = 0
                print(
                    f"\n[bold cyan]Tailing log file: {current_log_file}[/bold cyan]\n"
                )

            if current_log_file:
                with open(current_log_file, "r") as log:
                    log.seek(last_position)
                    new_lines = log.readlines()
                    if new_lines:
                        log_filename = os.path.basename(current_log_file)
                        for line in new_lines:
                            print(
                                f"[bold green]{log_filename}:[/bold green] {line.strip()}"
                            )
                        last_position = log.tell()

            sys.stdout.flush()  # Ensure output is flushed immediately

        # Wait for the process to complete
        return_code = process.wait()

        if return_code != 0:
            print(
                f"[bold red]Error:[/bold red] Command failed with return code {return_code}"
            )
            raise typer.Exit(code=1)

        # Check log files for specific errors
        error_patterns = [
            r"Segmentation fault \(core dumped\)",
            r"Floating point exception",
            r"FOAM FATAL (?:IO )?ERROR",
            r"Cannot find file",
            r"No convergence",
        ]
        error_regex = re.compile("|".join(error_patterns), re.IGNORECASE)

        # Find and sort log files by modification time
        log_files = []
        for root, _, files in os.walk(working_directory):
            for file in files:
                if file.startswith("log"):
                    log_path = os.path.join(root, file)
                    log_files.append(log_path)

        log_files.sort(key=lambda x: os.path.getmtime(x))

        # Process sorted log files
        for log_path in log_files:
            with open(log_path, "r") as log_file:
                lines = log_file.readlines()
                for line_number, line in enumerate(lines, 1):
                    if error_regex.search(line):
                        print(f"[bold red]{log_path} (line {line_number}):[/bold red]")
                        context_start = max(0, line_number - 1)
                        context_end = min(len(lines), line_number + 3)
                        for i in range(context_start, context_end):
                            print(f"{i+1}: {lines[i].strip()}")
                        if context_end < len(lines):
                            print("......")
                        print()  # Add a blank line for readability between errors

    except Exception as e:
        print(f"[bold red]Error:[/bold red] {str(e)}")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
