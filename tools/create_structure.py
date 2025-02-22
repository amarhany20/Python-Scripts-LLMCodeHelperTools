import os
import json


def create_structure_from_json(structure_json, base_path):
    """
    Create a folder and file structure from a given JSON representation.
    Only creates new files and folders that don't exist yet.

    :param structure_json: JSON data representing the folder structure.
    :param base_path: The root directory where the structure should be created.
    """
    # Create base directory if it doesn't exist
    os.makedirs(base_path, exist_ok=True)

    created_items = []
    existing_items = []

    for path in structure_json:
        full_path = os.path.join(base_path, path.strip("/"))

        if path.endswith("/"):
            # Handle directory creation
            if not os.path.exists(full_path):
                os.makedirs(full_path, exist_ok=True)
                created_items.append(full_path)
            else:
                existing_items.append(full_path)
        else:
            # Handle file creation
            if not os.path.exists(full_path):
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                with open(full_path, "w", encoding="utf-8") as f:
                    f.write("")  # Create an empty file
                created_items.append(full_path)
            else:
                existing_items.append(full_path)

    return created_items, existing_items


def load_json_from_file(json_path):
    """
    Load folder structure from a JSON file.

    :param json_path: Path to the JSON file containing the structure.
    :return: List of paths from the JSON.
    """
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    # Example JSON file path (change this if needed)
    json_file = "structure.json"  # This should contain the list of paths
    base_directory = "output_directory"  # Change this to your target directory

    # Load JSON data
    structure_data = load_json_from_file(json_file)

    # Create the folder and file structure
    new_items, skip_items = create_structure_from_json(structure_data, base_directory)

    # Print results
    if new_items:
        print("\nCreated new items:")
        for item in new_items:
            print(f"+ {item}")

    if skip_items:
        print("\nSkipped existing items:")
        for item in skip_items:
            print(f"- {item}")

    if not new_items:
        print("\nNo new items were created. All files and folders already exist.")