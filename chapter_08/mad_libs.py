#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# mad_libs.py - A simple Mad Libs game that prompts the user for words to
# fill in the blanks in a story template.

import re

def mad_libs(input_file, output_file):
    # Read the input file
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Regex to find placeholders (ADJECTIVE, NOUN, ADVERB, VERB)
    placeholders = re.findall(r'\b(ADJECTIVE|NOUN|ADVERB|VERB)\b', text)

    # Replace each placeholder with user input
    for placeholder in placeholders:
        article = "an" if placeholder[0] in "AEIOU" else "a"  # handle "a" vs "an"
        user_input = input(f"Enter {article} {placeholder.lower()}: ")
        text = text.replace(placeholder, user_input, 1)  # replace one at a time

    # Save the modified text to output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

    # Print the final result
    print("\n--- Final Mad Libs ---\n")
    print(text)


mad_libs("madlibs.txt", "madlibs_completed.txt")
