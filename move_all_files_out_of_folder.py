import os
import shutil
import sys

[
    [
        shutil.move(
            os.path.join(root, file), sys.argv[1]
        )
        for file in files
    ]
    for root, dirs, files in os.walk(sys.argv[1], topdown=False)
]
