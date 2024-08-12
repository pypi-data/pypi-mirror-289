import os
import json
import yaml
import shutil
import pandas as pd
import pyarrow as pa
from typing import Any
from pathlib import Path
import pyarrow.parquet as pq
from .text import current_time
from .fast_types import valid_path, is_string, is_array, is_dict
from typing import Any, Literal, Optional, Union, List, Tuple, Dict


def get_folders(
    path: str | Path,
    pattern: str | None = None,
    pattern_position: Literal["before", "after"] = "after",
) -> list[Path] | list:
    if not valid_path(path, "path"):
        return []
    text_patern = "*"
    if is_string(pattern):
        if pattern_position == "after":
            text_patern = f"*{pattern}"
        else:
            text_patern = f"{pattern}*"
    return [x for x in Path(path).glob(text_patern) if x.is_dir()]


def get_files(
    path: str | Path,
    extensions: str | list[str] | tuple[str, ...] | None = None,
    pattern: str | None = None,
    pattern_position: Literal["before", "after"] = "before",
) -> list[Path] | list:
    if not valid_path(path):
        return []

    text_pattern = "*.{extension}"
    if is_string(pattern):
        if pattern_position == "after":
            text_pattern = f"*{pattern}." + "{extension}"
        else:
            text_pattern = f"{pattern}*." + "{extension}"

    if is_string(extensions):
        return [
            x
            for x in Path(path).rglob(text_pattern.format(extension=extensions))
            if x.is_file()
        ]
    elif is_array(extensions):
        response = []
        [
            response.extend(get_files(path, x, pattern, pattern_position))
            for x in extensions
            if is_string(x, True)
        ]
        return response
    return [x for x in Path(path).rglob("*") if x.is_file()]


def create_path(path: str | Path):
    Path(path).mkdir(parents=True, exist_ok=True)


def load_json(path: str | Path) -> list | dict | None:
    """
    Load JSON/JSONL data from a file.

    Args:
        path (Union[str, Path]): The path to the JSON file.

    Returns:
        Union[list, dict, None]: The loaded JSON data as a list, dictionary, or None if any error occurs.
    """

    if not valid_path(path, expected_dir="file"):
        return None
    path = Path(path)
    if not path.name.endswith((".json", ".jsonl")):
        return None

    if path.name.endswith(".jsonl"):
        results = []
        for line in path.read_bytes().splitlines():
            try:
                results.append(json.loads(line))
            except:
                pass
        return results
    try:
        return json.loads(path.read_bytes())
    except:
        return None


def save_json(
    path: str | Path,
    content: list | dict,
    encoding: str = "utf-8",
    indent: int = 4,
    mode: Literal["w", "a"] = "a",
) -> None:
    """
    Save JSON data to a file.

    Args:
        path (Union[str, Path]): The path to save the JSON file.
        content (Union[list, dict]): The content to be saved as JSON.
        encoding (str, optional): The encoding of the file. Defaults to "utf-8".
        indent (int, optional): The indentation level in the saved JSON file. Defaults to 4.
    """

    if not is_string(path):
        path = current_time() + ".json"
    path = Path(path)
    if not path.name.endswith((".json", ".jsonl")):
        path = f"{path}.json"
    create_path(Path(path).parent)
    if path.name.endswith(".jsonl"):
        content = content + "\n"
    with open(path, mode, encoding=encoding) as file:
        json.dump(content, file, indent=indent)


def _load_parquet(content: Any):
    if not is_dict(content):
        return content
    return {key: list(value) for key, value in content.items()}


def load_parquet(path: str):
    """Load a Parquet file."""
    table = pq.read_table(path).to_pandas().to_dict(orient="records")
    return [_load_parquet(x) for x in table]


def save_parquet(path: str, data: list | dict) -> None:
    """Save a list to a Parquet file."""
    create_path(Path(path).parent)
    table = pa.Table.from_pandas(pd.DataFrame(data))
    pq.write_table(table, path)


def load_text(
    path: Path | str,
    encoding: str = "utf-8",
) -> str:
    """Load text content from a file. If not exists it returns a empty string."""
    if not valid_path(path):
        return ""
    return Path(path).read_text(encoding, errors="ignore")


def save_text(
    path: Path | str, content: str, encoding: str = "utf-8", append: bool = True
) -> None:
    """Save a text file to the provided path."""
    path = Path(path)
    create_path(Path(path).parent)
    text = content
    if append and valid_path(path, "file"):
        text = load_text(path, encoding) + content
    path.write_text(text, encoding=encoding, errors="ignore")


def load_yaml(
    path: Union[Path, str],
    encoding: str = "utf-8",
    unsafe_loader: bool = True,
) -> Optional[Union[List[Any], Dict[str, Any]]]:
    """
    Loads YAML content from a file.

    Args:
        path (Union[Path, str]): The path to the file.
        encoding (str): The encoding of the file. Default is 'utf-8'.
        unsafe_loader (bool): If False, it will use the safe_load instead.

    Returns:
        Optional[Union[List[Any], Dict[str, Any]]]: The loaded YAML data.
    """
    if not valid_path(path):
        return None
    loader = yaml.safe_load if not unsafe_loader else yaml.unsafe_load
    try:
        return loader(Path(path).read_bytes())
    except Exception as e:
        print(f"YAML load error: {e}")
    return None


def save_yaml(
    path: Union[Path, str],
    content: Union[List[Any], Tuple[Any, Any], Dict[Any, Any]],
    encoding: str = "utf-8",
    safe_dump: bool = False,
) -> None:
    """Saves a YAML file to the provided path.

    Args:
        path (Union[Path, str]): The path where the file will be saved.
        content (Union[List[Any], Tuple[Any, Any], Dict[Any, Any]]): The data that will be written into the file.
        encoding (str, optional): The encoding of the output. Default is 'utf-8'. Defaults to "utf-8".
        safe_dump (bool, optional): If True, it uses the safe_dump method instead. Defaults to False.
    """
    create_path(Path(path).parent)
    save_func = yaml.safe_dump if safe_dump else yaml.dump
    try:
        with open(path, "w", encoding=encoding) as file:
            save_func(data=content, stream=file, encoding=encoding)
    except Exception as e:
        print(f"An exception occurred while saving {path}. Exception: {e}")


def move_to(
    source_path: Union[str, Path],
    destination_path: Union[str, Path]
):
    """
    Moves a file or directory from one location to another.

    Args:
        source_path (Union[str, Path]): The path of the file/directory to be moved.
        destination_path (Union[str, Path]): The new location for the file/directory.

    Raises:
        AssertionError: If the source path does not exist or is invalid
    """
    assert (
        str(source_path).strip() and Path(source_path).exists()
    ), "Source path does not exists!"
    source_path = Path(source_path)
    assert valid_path(source_path), "Source path does not exists!"
    destination_path = Path(destination_path)
    create_path(destination_path)
    try:
        shutil.move(source_path, destination_path)
    except Exception as e:
        print(f"Failed to move the destination path! {e}")


def delete_path(
    files: str | Path | list[str | Path] | tuple[str | Path, ...], verbose=False
):
    if is_string(files) and Path(files).exists():
        try:
            shutil.rmtree(files)
            if verbose:
                print("'{files}' deleted")
        except Exception as e:
            if verbose:
                print(f"Failed to delete {files}, Exception: {e}")
    elif is_array(files):
        [delete_path(path) for path in files if is_string(path) or is_array(path)]


__all__ = [
    "get_folders",
    "get_files",
    "create_path",
    "load_json",
    "save_json",
    "load_parquet",
    "save_parquet",
    "load_text",
    "save_text",
    "load_yaml",
    "save_yaml",
    "move_to",
    "delete_path",
]
