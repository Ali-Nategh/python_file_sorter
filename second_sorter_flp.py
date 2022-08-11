import os
import sys
import time

"""
This is a File sorter that sorts flp (FL studio project) files by extentions.
You can use it in a command line like this:
sorter.py SourcePath DestinationPath
If the file matches the written extentions, then it looks up the file creation and modification dates,
creates a folder with the files creation or modification year (picks the one that is lower than the other),
and it will copy the file to that path using read and write (not using any libraries like shutil or ... was intentional and intended as a challenge) 
You can change this a bit and use it for your own sorting purposes if you want lol.
"""

command = sys.argv
srcPath = command[1]
dstPath = command[2]
for files in os.walk(srcPath):
    for file in files[2]:
        filePath = files[0]
        if "." in file and file.split(".")[-1].lower() == "flp":
            folder = "flProjs"
            timem = time.ctime(os.path.getmtime(f"{filePath}{os.sep}{file}"))
            timec = time.ctime(os.path.getctime(f"{filePath}{os.sep}{file}"))
            year = timem.split()[-1]
            year2 = timec.split()[-1]
            if year2 < year:
                year = year2
            f = open(f"{filePath}{os.sep}{file}", "rb")
            x = f.read()
            f.close()
            if not os.path.exists(f"{dstPath}"):
                os.mkdir(f"{dstPath}")
            if os.path.exists(f"{dstPath}{os.sep}{year}"):
                    g = open(f"{dstPath}{os.sep}{year}{os.sep}{file}", "wb")
                    g.write(x)
                    g.close()
            else:
                os.mkdir(f"{dstPath}{os.sep}{year}")
                g = open(f"{dstPath}{os.sep}{year}{os.sep}{file}", "wb")
                g.write(x)
                g.close()
