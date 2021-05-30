import argparse
import random

import cv2
import pandas as pd

random.seed(1337)


def blend_image(src1, src2, size, alpha=0.5):
    src1 = cv2.resize(src1, (size, size))
    src2 = cv2.resize(src2, (size, size))
    return cv2.addWeighted(src1, alpha, src2, 1 - alpha, 0.0)


def remove_file_extension(filename):
    return filename[:len(filename) - 4]


def get_class_from_filename(filename):
    return filename.split('_', 1)[0]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-csv', '--csv', required=True)
    parser.add_argument('-src', '--source', required=True)
    parser.add_argument('-trg', '--target', required=True)
    parser.add_argument('-size', '--size', type=int, required=True)

    args = parser.parse_args()

    csv = args.csv
    src_folder = args.source
    trgt_folder = args.target
    size = args.size

    csv_df = pd.read_csv(csv)
    imgs = csv_df['image'].tolist()

    ctr = 0
    for name1 in imgs:
        img1 = cv2.imread(f"{src_folder}{name1}")
        same_class = True
        while same_class:
            name2 = random.choice(imgs)
            if get_class_from_filename(name1) not in name2:
                same_class = False
        img2 = cv2.imread(f"{src_folder}{name2}")
        print(f"Reading {src_folder}{name2}")
        cv2.imwrite(f"{trgt_folder}{remove_file_extension(name1)}_{name2}", blend_image(img1, img2, size))
        ctr += 1

        if ctr % 100 == 0:
            print(ctr)


if __name__ == '__main__':
    main()
