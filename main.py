import os
import shutil
from pathlib import Path

types = {
    "Images": [".dwg", ".xcf", ".jpg", ".jpx", ".png", ".apng", ".gif", ".webp", ".cr2",
        ".tif", ".bmp", ".jxr", ".psd", ".ico", ".heic", ".avif"],
    "Video": [".3gp", ".mp4", ".m4v", ".mkv", ".webm", ".mov", ".avi", ".wmv", ".mpg", ".flv"],
    "Audio": [".aac", ".mid", ".mp3", ".m4a", ".ogg", ".flac", ".wav", ".amr", ".aiff"],
    "Archive": [".br", ".rpm", ".dcm", ".epub", ".zip", ".tar", ".rar", "gz", ".bz2", ".7z",
        ".xz", ".pdf", ".swf", ".rtf", ".eot", ".ps", ".sqlite", ".nes", ".crx",
        ".cab", ".deb", ".ar", ".Z", ".lzo", ".lz", ".lz4", "zstd"],
    "Documents": [".doc", ".docx", ".odt", ".xls", ".xlsx", ".ods", ".ppt", ".pptx", ".odp"],
    "Font": [".woff", ".woff2", ".ttf", ".otf"],
    "Application": [".wasm", ".exe"],
    "Folders": []
}

def sort_to():
    p = Path.cwd()
    sort_to = input(f'Where do you want to sort to? (leave blank for default location "{p.name}") ').strip()
    if sort_to != p and sort_to != '':
          p = sort_to
    return Path(p)

def make_dirs(p):
    path = p / "Sorted"
    if not path.is_dir():
        path.mkdir()
    for type in types:
        path = p / "Sorted" / type
        if not path.is_dir():
            path.mkdir()
    path = p / "Sorted/Others"
    if not path.is_dir():
            path.mkdir()
    path = p / "Sorted/Folders"
    if not path.is_dir():
            path.mkdir()
    print("Directories created!")

    
def sort_from():
    f = Path.home()/"Downloads"
    sort_to = input(f'Where do you want to sort? (leave blank for default location "{f.name}") ').strip()
    if sort_to != f and sort_to != '':
        f = sort_to
    return Path(f)

def sort(f,p):
    p = p/"Sorted"
    for file in f.iterdir():
        if file.is_dir():
            shutil.move(file, p/"Folders")
            continue
        fs = file.suffix
        found = False
        for type in types:
            if fs in types[type]:
                 shutil.move(file, p/type)
                 found = True
                 break
        if found == False:
            shutil.move(file, p/"Others")
    print("Files Sorted!")

     
f = sort_from()
print(f)
p = sort_to()
print(p)
make_dirs(p)
sort(f,p)
