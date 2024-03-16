import os
import logging
from pathlib import Path


logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : %(message)s:')

def create_project_files(project_name):
    """
    Creates necessary project files and directories.

    Parameters:
    - project_name (str): The name of the project.

    Returns:
    - None
    """

    # List of file paths to create
    list_of_file_paths = [
        ".github/workflows/.gitkeep",
        f"src/{project_name}/__init__.py",
        f"src/{project_name}/components/__init__.py",
        f"src/{project_name}/utils/__init__.py",
        f"src/{project_name}/utils/common.py",
        f"src/{project_name}/logging/__init__.py",
        f"src/{project_name}/config/__init__.py",
        f"src/{project_name}/config/configuration.py",
        f"src/{project_name}/pipeline/__init__.py",
        f"src/{project_name}/entity/__init__.py",
        f"src/{project_name}/constants/__init__.py",
        "config/config.yaml",
        "params.yaml",
        "app.py",
        "main.py",
        "Dockerfile",
        "requirements.txt",
        "setup.py",
        "research/trials.ipynb"
    ]

    # Iterate through file paths
    for file_path in list_of_file_paths:
        file_path = Path(file_path)
        file_dir, file_name = file_path.parent, file_path.name

        # Create directory if it doesn't exist
        if file_dir != "":
            file_dir.mkdir(parents=True, exist_ok=True)
            logging.info(f"Creating directory: {file_dir} for the file {file_name}")

        # Create empty file if it doesn't exist or is empty
        if not file_path.exists() or file_path.stat().st_size == 0:
            file_path.touch()
            logging.info(f"Creating empty file: {file_path}")
        else:
            logging.info(f"{file_name} already exists")

# Usage example
if __name__ == "__main__":
    project_name = "TextSummarizer"
    create_project_files(project_name)
