import os
import shutil
import argparse


def copy_and_sort_files(src_dir, dest_dir="dist"):
    """
    Recursively copies files from the source folder to the target folder,
    organizing them into subfolders based on file extensions.
    """
    # Ensure the target folder exists
    os.makedirs(dest_dir, exist_ok=True)

    # Process each item in the current folder
    for item in os.listdir(src_dir):
        item_path = os.path.join(src_dir, item)

        # If item is a folder, apply the function recursively
        if os.path.isdir(item_path):
            try:
                copy_and_sort_files(item_path, dest_dir)
            except Exception as e:
                print(f"Error accessing folder {item_path}: {e}")

        # If item is a file, sort and copy based on its extension
        elif os.path.isfile(item_path):
            file_extension = os.path.splitext(item)[1][1:]  # Extract file extension without the dot

            # Define target folder based on file type
            if file_extension:
                target_dir = os.path.join(dest_dir, file_extension)
            else:
                target_dir = os.path.join(dest_dir, "no_extension")

            os.makedirs(target_dir, exist_ok=True)  # Create subfolder if it doesn’t exist yet

            try:
                # Copy the file into the corresponding subfolder
                shutil.copy2(item_path, target_dir)
                print(f"Copied {item} to {target_dir}")
            except Exception as e:
                print(f"Error copying file {item}: {e}")


def main():
    # Set up command-line arguments
    parser = argparse.ArgumentParser(description="Recursively copy files and organize them by extension.")
    parser.add_argument("source", type=str, help="Path to the source folder")
    parser.add_argument("destination", type=str, nargs="?", default="dist",
                        help="Path to the target folder (default: dist)")

    args = parser.parse_args()

    # Execute the function to copy and organize files
    try:
        copy_and_sort_files(args.source, args.destination)
        print("Files copied and organized successfully.")
    except Exception as e:
        print(f"Error during file processing: {e}")


if __name__ == "__main__":
    main()
