import os
import sys


def main():
    folder = sys.argv[1]  # must include the final '/'

    files = os.listdir(folder)

    for file in files:
        if "jpg" not in file:
            os.rename(f"{folder}{file}", f"{folder}{file}.jpg")


if __name__ == '__main__':
    main()
