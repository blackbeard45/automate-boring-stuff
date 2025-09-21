#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# regex_finder.py - Searches for a regex pattern in all .txt files in a given
# folder and prints the lines containing the pattern along with the filename
# and line number.

import os
import re

def search_in_txt(folder_path, pattern):
    # Compile the regex for faster performance
    regex = re.compile(pattern)

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder_path, filename)

            with open(filepath, "r", encoding="utf-8") as f:
                for line_num, line in enumerate(f, start=1):
                    if regex.search(line):
                        print(f"[{filename}:{line_num}] {line.strip()}")


folder = input("Enter folder path: ")
regex_pattern = input("Enter regex pattern to search: ")
search_in_txt(folder, regex_pattern)
