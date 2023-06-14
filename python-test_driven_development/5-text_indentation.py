#!/usr/bin/python3
"""shebang"""


def text_indentation(text):
    """text indentation"""
    newtext = ""
    spacecheck = False
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in range(len(text)):
        if text[char - 1] in [".", "?", ":"]:
            newtext += text[char] + "\n\n"
            spacecheck = True
        if spacecheck:
            if char < len(text) - 1 and text[char + 1] == " ":
                continue
            spacecheck = False
        else:
            newtext += text[char]
    print(newtext, end='')
