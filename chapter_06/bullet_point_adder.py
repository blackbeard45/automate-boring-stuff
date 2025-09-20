#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pyperclip
# bullet_point_adder.py - adds Wikipedia bullet points to the start of each line of text on the clipboard

text = pyperclip.paste()  # get text from clipboard
lines = text.split('\n')  # split text into a list of lines
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]  # add star to each line
text = '\n'.join(lines)  # join the modified lines back into a single string
pyperclip.copy(text)  # copy the modified text to the clipboard

