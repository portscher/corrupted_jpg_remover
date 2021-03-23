#!/usr/bin/python3

# find corrupted images and delete them
import cv2
import os
import sys

folder = sys.argv[1]
print(f"checking images in folder {folder}")


def verify_image(img_file):
    img = cv2.imread(img_file)
    return True if img is None else False


for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith(".jpg"):
            currentFile = os.path.join(root, file)
            if not verify_image(currentFile):
                print(f"deleting {currentFile}")
                try:
                    os.remove(currentFile)
                except OSError:
                    print("Something went wrong.")
