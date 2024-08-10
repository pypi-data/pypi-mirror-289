import os
import uuid
from digifoam.types import FileTree, FileNode, FolderNode


def get_file_size(file_list) -> list[dict]:
    """Get the size of each file in the list."""
    return [{"path": file, "size": os.path.getsize(file)} for file in file_list]


def if_obj(path: str) -> bool:
    """Check if the file has a supported OpenFOAM 3D extension."""
    openfoam_3d_extensions = {
        # Mesh formats
        ".msh",
        ".unv",
        ".cgns",
        ".foam",
        ".vtk",
        ".vtu",
        ".vtp",
        ".ply",
        ".fluent",
        ".ans",
        ".neu",
        # CAD formats
        ".stl",
        ".obj",
        ".step",
        ".stp",
        ".iges",
        ".igs",
        ".brep",
        ".sat",
        ".prt",
        ".sldprt",
        ".sldasm",
        ".dwg",
        ".dxf",
        # OpenFOAM specific formats
        ".blockMesh",
        ".snappyHexMesh",
        ".polyMesh",
        ".triSurface",
        ".eMesh",
        ".gz",
        # Other 3D formats
        ".3ds",
        ".fbx",
        ".dae",
        ".blend",
        ".x3d",
        ".wrl",
        ".gltf",
        ".glb",
        # Point cloud formats
        ".xyz",
        ".pts",
        ".las",
        ".e57",
        # Paraview formats
        ".pvd",
        ".pvsm",
        # Simulation result formats
        ".case",
        ".foam",
        ".dat",
        ".csv",
        ".tec",
        ".h5",
        ".hdf5",
    }
    return os.path.splitext(path)[1].lower() in openfoam_3d_extensions


def is_text_file(file_path, sample_size=8192):
    try:
        with open(file_path, "rb") as f:
            sample = f.read(sample_size)
        return not any(
            c for c in sample if c < 9 and c not in (10, 13, 8, 9)
        )  # Allow newline, carriage return, backspace, and tab
    except IOError:
        return False


def create_file_tree(paths: list[str]) -> FileTree:
    """Create a file tree from the list of paths."""
    tree: FileTree = []
    for path in paths:
        parts = path.split(os.sep)
        current = tree
        for i, part in enumerate(parts):
            abs_path = os.path.join(*parts[: i + 1])  # Construct the absolute path
            existing_node = next(
                (node for node in current if node["name"] == part), None
            )

            if i == len(parts) - 1:
                # It's a file
                if not existing_node:
                    is_editable = (
                        not if_obj(abs_path)
                        and is_text_file(abs_path)
                        and os.path.getsize(abs_path) <= 100 * 1024
                    )
                    file_node: FileNode = {
                        "type": "file",
                        "name": part,
                        "path": abs_path,
                        "id": str(uuid.uuid4()),
                        "is_editable": is_editable,
                    }
                    current.append(file_node)
            else:
                # It's a directory
                if not existing_node:
                    folder_node: FolderNode = {
                        "type": "folder",
                        "name": part,
                        "path": abs_path,
                        "id": str(uuid.uuid4()),
                        "children": [],
                    }
                    current.append(folder_node)
                    current = folder_node["children"]
                else:
                    current = existing_node["children"]
    return tree
