from PIL import Image
import os, sys
from pathlib import Path

def are_same_path(p1, p2):
    return Path(p1).resolve(strict=False) == Path(p2).resolve(strict=False)

def get_src_dest():
    try:
        src = sys.argv[1]
        dest = sys.argv[2]
    except IndexError as err:
        print(f"Error: {err}")
        print(f"Usage: python {sys.argv[0]} <src-dir> <dest-dir>")
        sys.exit(1)
    else:
        return src, dest

def validate_src_dest():

    src, dest = get_src_dest()

    if are_same_path(src, dest):
        print(f"Error: source and destination dirs can't be the same!")
        sys.exit(1)

    if not os.path.isdir(src):
        print(f"Error: source dir '{src}' doesn't exist!")
        sys.exit(1)

    ls = os.listdir(src)

    for file in ls:
        if file.lower().endswith((".jpg", ".jpeg")):
            break
    else:
        print(f"Error: file '{src}' doesn't contain a .jpg or .jpeg file!")
        sys.exit(1)

    if not os.path.isdir(dest):
        os.mkdir(dest)
    else:
        while True:
            choice = input(f"'{dest}' dir already exists! Do you want to overwrite it? (y/n): ")
            if choice.lower() == 'n':
                sys.exit(1)
            elif choice.lower() == 'y':
                break
            else:
                print(f"Error: invalid choice: '{choice}'!")

    return True

def main():
    if validate_src_dest():
        src, dest = get_src_dest()
        ls = os.listdir(src)
        for file in ls:
            if file.lower().endswith('.jpg'):
                img = Image.open(f'{src}/{file}')
                base_name = file.removesuffix('.jpg')
                img.save(f"{dest}/{base_name}.png", 'PNG')
            elif file.lower().endswith('.jpeg'):
                img = Image.open(f'{src}/{file}')
                base_name = file.removesuffix('.jpeg')
                img.save(f"{dest}/{base_name}.png", 'PNG')
        print(f"Successfully converted all .jpg or .jpeg files present in '{src}' dir to .png and saved to '{dest}' dir!")


if __name__ == "__main__":
    main()