#! /usr/bin/python3
# -*- coding: utf-8 -*-

# selective_copy.py - Copies files with a specific extension from one
# directory to another.

import shutil, os
import re

# Function to copy files with a specific extension
def selective_copy(src_dir, dest_dir, file_extension):
    # Ensure the destination directory exists
    os.makedirs(dest_dir, exist_ok=True)

    # Loop over files in the source directory
    for filename in os.listdir(src_dir):
        if filename.endswith(file_extension):
            src_file = os.path.join(src_dir, filename)
            dest_file = os.path.join(dest_dir, filename)
            print(f"Copying '{src_file}' to '{dest_file}'...")
            shutil.copy2(src_file, dest_file)  # Copy file with metadata
        else:
            print(f"Skipping '{filename}', does not match extension '{file_extension}'.")

# Example usage
selective_copy("source_directory", "destination_directory", ".txt")
