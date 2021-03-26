import os
import sys
import shutil


def main():
    folder = sys.argv[1]  # must include the final '/'

    subfolders = os.listdir(folder)
    print(subfolders)

    for sub in subfolders:
        files = os.listdir(f"{folder}{sub}")
        for file in files:
            shutil.move(f"{folder}{sub}/{file}", f"{folder}/{file}")
        print(f"Moved all files from {sub}.")


if __name__ == '__main__':
    main()
