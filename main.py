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
}

def sort_by():
    #types['Images'].append(".pixel")
    print("Default Catagories:")
    for type in types:
        print(type)
        print(types.get(type))
    print("(By Default Folders and Others each get their own catagories)\n")
    while True:
        response = input("\nHow would you like to sort your files? \n 1. Default \n 2. By Extention\n\n")
        if response == "1":
              print("Default\n")
              return 1
        if response == "2":
              print("By Extention\n")
              return 2
        #if response == "3":
              #print("Custom\n")
              #return 1
        

def sort_to():
    p = Path.cwd()
    sort_to = input(f'Where do you want to sort to? (leave blank for default location "{p.name}")\n').strip()
    if sort_to != p and sort_to != '':
          p = sort_to
    return Path(p)

def sort_from():
    f = Path.home()/"Downloads"
    sort_to = input(f'\nWhere do you want to sort? (leave blank for default location "{f.name}")\n').strip()
    if sort_to != f and sort_to != '':
        f = sort_to
    return Path(f)

def sort_1(f,p):
    p = p/"Sorted"
    if not p.is_dir():
        p.mkdir()
        print("Sorted Folder created")
    for file in f.iterdir():
        if file.is_dir():
            shutil.move(file, p/"Folders")
            continue
        fs = file.suffix
        found = False
        for type in types:
            if fs in types[type]:
                path = p / type
                if not path.is_dir():
                    path.mkdir()
                    print(type, "Folder created")
                shutil.move(file, p/type)
                print(file.name, "sorted into", type)
                found = True
                break
        if found == False:
            path = p / "Others"
            if not path.is_dir():
                    path.mkdir()
                    print("Others Folder created")
            shutil.move(file, p/"Others")
            print(file.name, "sorted into Others")
    print("Files Sorted!")

def sort_2(f,p):
    p = p/"Sorted"
    if not p.is_dir():
        p.mkdir()
        print("Sorted Folder created")
    for file in f.iterdir():
        if file.is_dir():
            shutil.move(file, p/"Folders")
            continue
        fs = file.suffix
        path = p / fs
        if not path.is_dir():
                    path.mkdir()
                    print(fs, "Folder created")
        shutil.move(file, p/fs)
        print(file.name, "sorted into", fs)
    print("Files Sorted!")
     
f = sort_from()
p = sort_to()
sm = sort_by()
if sm == 1:
     sort_1(f,p)
elif sm == 2:
     sort_2(f,p)
     print("WIP")
