import os
import sys


def main():
    folder = sys.argv[1]  # must include the final '/'
    name = sys.argv[2]

    files = os.listdir(folder)

    counter = 0
    for file in files:
        new_name = f"{name}_{counter}"
        os.rename(f"{folder}{file}", f"{folder}{new_name}.jpg")
        counter += 1


if __name__ == '__main__':
    main()
