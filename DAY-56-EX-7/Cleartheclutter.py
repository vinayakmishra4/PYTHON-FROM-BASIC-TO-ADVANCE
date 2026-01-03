# write the program to clear the clutter with the help of os module

import os

def clear_clutter(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Filter out only the PNG files
    png_files = [file for file in files if file.lower().endswith('.png')]

    # Sort the files alphabetically (optional, to ensure a consistent order)
    png_files.sort()

    # Loop through the PNG files and rename them
    for index, file in enumerate(png_files, 1):
        old_path = os.path.join(folder_path, file)
        new_name = f"{index}.png"
        new_path = os.path.join(folder_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)

    print(f"Renamed {len(png_files)} PNG files.")

# Example usage
folder_path = r"C:\path\to\your\folder"  # Replace this with the path to your folder
clear_clutter(folder_path)
