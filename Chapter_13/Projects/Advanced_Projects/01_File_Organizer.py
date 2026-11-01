"""Advanced project: file organizer.

Definition: A file organizer groups files into folders based on their
extensions. This project practises pathlib, files, loops, and exceptions.
"""

from pathlib import Path
import shutil

folder = Path(input("Folder to organize: ")).expanduser()
if not folder.is_dir():
    print("Folder does not exist.")
else:
    for file in folder.iterdir():
        if not file.is_file() or file.name.startswith("."):
            continue
        extension = file.suffix.lower().lstrip(".") or "no_extension"
        destination = folder / extension
        destination.mkdir(exist_ok=True)
        shutil.move(str(file), str(destination / file.name))
    print("Files organized.")
