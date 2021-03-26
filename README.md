# Image preprocessing scripts for machine learning

## Prerequisites
```
pip3 install opencv-python
``` 

## delete_corrupted_imgs.py
A simple script which iterates through a folder and removes all corrupted jpg files.
What does corrupted mean in this context? An image that cannot be opened by OpenCV. 

### Usage:
```
python3 delete_corrupted_imgs.py <directory>
```

## move_all_files_out_of_folder.py
Parameter: A directory which contains a number of sub-directories. This script moves all files withing these sub-directories into the main directory. The script is non-recursive and only works for one layer of sub-directories, which currently fits my use case. I might change that soon to generalize the script.

### Usage:
```
python3 move_all_files_out_of_folder.py <directory>
```

# rename_all_files_in_folder.py
All files in the given directory will have their current names changes to the input to <name>_0.jpg, <name>_1.jpg, <name>_2.jpg, etc.

### Usage:
```
python3 rename_all_files_in_folder.py <directory> <new_name>
```
