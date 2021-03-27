#!/usr/bin/python3

import os
import sys

import cv2


def remove_corrupted_img(img_file):
    if cv2.imread(img_file) is None:
        print(f"deleting {img_file}")
        try:
            os.remove(img_file)
        except OSError:
            print("Something went wrong.")


[
    [
        remove_corrupted_img(os.path.join(root, file))
        for file in files if file.endswith(".jpg")
    ]
    for root, dirs, files in os.walk(sys.argv[1])
]
