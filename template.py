import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "template"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/data/__init__.py",
    f"src/{project_name}/features/feature.py/__init__.py/",
    f"src/{project_name}/models/__init__.py",
    f"src/{project_name}/visualization/visualize.py/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    "references/.gitkeep",
    "models/.gitkeep",
    "notebooks/notebook.ipynb",
    "reports/figures",
    "config/config.yaml",
    #"dvc.yaml",
    #"params.yaml",
    "requirements.txt",
    "setup.py",

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")