import os
import sys


def main():
    folder = sys.argv[1]  # must include the final '/'

    [
        os.rename(f"{folder}{file}", f"{folder}{file}.jpg")
        for file in os.listdir(folder)
        if "jpg" not in file
    ]


if __name__ == '__main__':
    main()
