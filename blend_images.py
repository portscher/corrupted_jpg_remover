import argparse
import os

import cv2


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
    parser.add_argument('-src', '--source', required=True)
    parser.add_argument('-trg', '--target', required=True)
    parser.add_argument('-size', '--size', type=int, required=True)

    args = parser.parse_args()

    src_folder = args.source
    trgt_folder = args.target
    size = args.size

    imgs = os.listdir(src_folder)

    for name1 in imgs:
        for name2 in imgs:
            # make sure every class is only blended with other classes, not its own
            if get_class_from_filename(name1) not in name2:
                img1 = cv2.imread(f"{src_folder}{name1}")
                img2 = cv2.imread(f"{src_folder}{name2}")
                blended = blend_image(img1, img2, size)
                cv2.imwrite(f"{trgt_folder}{remove_file_extension(name1)}_{name2}", blended)


if __name__ == '__main__':
    main()
