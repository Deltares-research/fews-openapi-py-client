import re
from pathlib import Path


def replace_code(file_path: str, values_to_replace: dict) -> str:
    """
    Remove .isoformat() calls from datetime objects in a Python file.

    Args:
        file_path: Path to the Python file to modify

    Returns:
        tuple: (number of replacements made, modified content)
    """
    path = Path(file_path)

    # Read the file
    with open(path, encoding="utf-8") as f:
        content = f.read()

    for pattern, replacement in values_to_replace.items():
        matches = len(re.findall(pattern, content))
        print(f"Modified {file_path}: Replaced {matches} occurrences.")
        content = re.sub(pattern, replacement, content)
    return content


def main():
    package_root = Path(__file__).parent.parent / "fews-openapi-py-client/fews_openapi_py_client"
    files_to_process = ["api/timeseries/timeseries.py"]

    for file in files_to_process:
        file_path = package_root / file
        modified_content = replace_code(
            str(file_path), values_to_replace={r"(\w+)\.isoformat\(\)": r"\1", r"datetime\.datetime": r"str"}
        )
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(modified_content)


if __name__ == "__main__":
    main()
