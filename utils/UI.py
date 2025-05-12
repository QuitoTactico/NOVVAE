import re
from typing import Optional

import tkinter as tk
from tkinter import filedialog, messagebox


def input_file_selector(language: str = None) -> str:
    """
    Opens a file dialog to select a file and returns the selected file path.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title=(
            f"Select the {language.upper()} JSON file"
            if language
            else "Select a JSON file"
        ),
        filetypes=(("JSON files", "*.json"), ("All files", "*.*")),
    )
    return file_path


def output_file_namer(
    input_file_path_en: str, input_file_path_ja: str
) -> Optional[str]:
    """
    Generates the output file name based on the input file names.
    If the input files are from the same scene, in `'pm<scene_id>.txt.scn.m.json'` format, the output file name will be `'extracted<scene_id>.json'`.
    - It can recognize if the input files are from different scenes to say ERROR.
    - Otherwise, if the input files don't match the filename format, it will open a file dialog to save the file with a custom title.
    """
    pattern = r"pm(\d{2}_\d{2})\.txt\.scn\.m\.json"
    match_en = re.search(pattern, input_file_path_en)
    match_ja = re.search(pattern, input_file_path_ja)

    if match_en and match_ja:
        if match_en.group(1) == match_ja.group(1):
            default_filename = f"extracted{match_en.group(1)}.json"
        else:
            raise Exception("The selected files are from different scenes.")
    elif match_en:
        default_filename = f"extracted{match_en.group(1)}.json"
    elif match_ja:
        default_filename = f"extracted{match_ja.group(1)}.json"
    else:
        default_filename = "extracted.json"

    return filedialog.asksaveasfilename(
        title="Save file as",
        defaultextension=".json",
        initialfile=default_filename,
        filetypes=(("JSON files", "*.json"), ("All files", "*.*")),
    )


# ============================== UTIL ====================================


def folder_selector(message: str = None) -> str:
    """
    Opens a folder dialog to select a folder and returns the selected folder path.
    """
    print(f"Selecting {(message or 'a').upper()} folder...")
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    folder_path = filedialog.askdirectory(
        title=(f"Select an {message.upper()} folder" if message else "Select a folder")
    )
    print(folder_path)
    return folder_path


def UI_error(e: Exception):
    messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    a = folder_selector()
    print(a)
