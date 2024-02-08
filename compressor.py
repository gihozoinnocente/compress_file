#!/usr/bin/python3
import os
import tarfile
import zipfile
from datetime import datetime


def compress_folder(folder_path, compress_type):
    try:
        folder_name = os.path.basename(folder_path)
        current_date = datetime.now().strftime("%Y_%m_%d")
        compressed_filename = f"{folder_name}_{current_date}.{compress_type}"

        if compress_type == "zip":
            with zipfile.ZipFile(compressed_filename, "w") as zip_file:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        zip_file.write(
                            os.path.join(root, file),
                            os.path.relpath(os.path.join(root, file), folder_path),
                        )

        elif compress_type == "tar":
            with tarfile.open(compressed_filename, "w") as tar_file:
                tar_file.add(folder_path, arcname=os.path.basename(folder_path))

        elif compress_type == "tgz":
            with tarfile.open(f"{compressed_filename}.tar.gz", "w:gz") as tar_gz_file:
                tar_gz_file.add(folder_path, arcname=os.path.basename(folder_path))

        print(
            f"Compression successful. Compressed file saved as: {compressed_filename}"
        )

    except Exception as e:
        print(f"Compression failed. Error: {e}")


def main():
    folder_path = input("Enter the path of the folder to compress: ")
    if not os.path.isdir(folder_path):
        print("Error: Invalid folder path.")
        return

    compress_types = ["zip", "tar", "tgz"]
    print("Available compress types:")
    for i, compress_type in enumerate(compress_types, 1):
        print(f"{i}. {compress_type}")

    compress_choice = input(
        "Select the desired compress type (enter the corresponding number): "
    )

    if isinstance(compress_choice, str):
        try:
            compress_choice = int(compress_choice)
        except ValueError:  # Handle non-integer input
            print(
                "Error: Invalid compress type choice. Please Enter a number from 1 to 3."
            )
            return
    if compress_choice not in range(1, len(compress_types) + 1):
        print("Error: Invalid compress type choice.")
        return

    compress_type = compress_types[compress_choice - 1]
    compress_folder(folder_path, compress_type)


if __name__ == "__main__":
    main()
