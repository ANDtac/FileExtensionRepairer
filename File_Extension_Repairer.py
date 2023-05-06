import os
import shutil
import filetype
from pathlib import Path

def process_files_in_directory(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        if os.path.isfile(file_path):
            file_extension = Path(file).suffix

            if not file_extension:
                try:
                    file_type = filetype.guess(file_path)
                    if file_type is not None:
                        new_file_path = file_path + '.' + file_type.extension
                        os.rename(file_path, new_file_path)
                        print(f"File '{file}' has been renamed to '{Path(new_file_path).name}'")
                    else:
                        print(f"Unknown file type for '{file}'")
                except Exception as e:
                    print(f"Error processing file: {file_path}")
                    print(f"Exception: {e}")


def main():
    directory = input("Enter the directory path: ").strip()

    if not os.path.isdir(directory):
        print("The directory does not exist.")
        return

    process_files_in_directory(directory)
    print("Files have been processed successfully.")

if __name__ == "__main__":
    main()
