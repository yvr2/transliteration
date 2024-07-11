import os
import shutil

def combine_files_to_main_directory(main_directory):
    # Walk through all files in the directory and subdirectories
    for root, _, files in os.walk(main_directory):
        # Skip the main directory itself
        if root == main_directory:
            continue

        for filename in files:
            file_path = os.path.join(root, filename)
            dest_path = os.path.join(main_directory, filename)
            
            # Move file to the main directory
            shutil.move(file_path, dest_path)

            print(f"Moved {file_path} to {dest_path}")

    # Remove empty subdirectories
    for root, dirs, _ in os.walk(main_directory, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                print(f"Removed empty directory {dir_path}")

# Example usage
combine_files_to_main_directory(r'C:\Users\yvr2\Documents\ACO\marcxml')
