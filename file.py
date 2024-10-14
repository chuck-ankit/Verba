import os

def create_project_structure(base_path):
    dirs = [
        "data/raw",
        "data/processed",
        "models",
        "scripts",
        "results"
    ]

    for dir in dirs:
        path = os.path.join(base_path, dir)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Created directory: {path}")
        else:
            print(f"Directory already exists: {path}")

if __name__ == "__main__":
    base_path = os.path.dirname(os.path.abspath(__file__))
    create_project_structure(base_path)
