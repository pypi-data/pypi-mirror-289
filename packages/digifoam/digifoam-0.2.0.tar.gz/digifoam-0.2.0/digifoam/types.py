from typing import TypedDict, Union, List, Literal


class FileNode(TypedDict):
    type: Literal["file"]
    name: str
    path: str
    id: str
    is_editable: bool


class FolderNode(TypedDict):
    type: Literal["folder"]
    name: str
    path: str
    id: str
    children: List[Union["FileNode", "FolderNode"]]


FileTree = List[Union[FileNode, FolderNode]]
