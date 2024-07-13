# Solution for Copying directories 

import shutil
import os

src = input ("Enter the Source Directory" )
top_directory = src
for dirpath, dirnames, filenames in os.walk(top_directory):
    for filename in filenames:
        full_path = os.path.join(dirpath, filename)
        print(full_path)

#src = 'D:/Python/Src_dir/*'
# print (path)
#file_names = os.listdir(src)
#st = 'D:/Python/target_dir'
#file_names = os.listdir(dst)
# shutil.copy2(src, dst)  # Copies with additional metadata