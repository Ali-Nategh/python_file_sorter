import os
import sys
import time

"""
This is a File sorter that sorts image and video files by extentions.
You can use it in a command line like this:
sorter.py SourcePath DestinationPath
If the file matches the written extentions, then it looks up the file creation and modification dates,
creates a folder with the files creation or modification year (picks the one that is lower than the other),
and it will copy the file to that path using read and write (not using any libraries like shutil or ... was intentional and intended as a challenge) 
You can change this a bit and use it for your own sorting purposes if you want lol.
"""


# gets the command line arguments
command = sys.argv
# stores the path
srcPath = command[1]
# stores the source
dstPath = command[2]
# goes through the source folder and subfolders and their files
for files in os.walk(srcPath):
    # files[0] is the path and files[2] is all the files in that path
    for file in files[2]:
        filePath = files[0]
        # standard constants
        picExt = ["jpg", "jpeg", "png"]
        vidExt = ["mp4", "avi", "3gp", "mpeg", "mkv", "wmv", "mov"]

        # a function that gets the folder name as an argument and does all the sorting accordingly
        def filecreation(folder):
            # this gets the file modification date
            times = time.ctime(os.path.getmtime(f"{filePath}{os.sep}{file}"))
            # this gets the creation date
            times2 = time.ctime(os.path.getctime(f"{filePath}{os.sep}{file}"))
            year = times.split()[-1]
            year2 = times2.split()[-1]
            # we want to sort it with the year that is sooner than the other so we do a simple comparison
            if year2 < year:
                year = year2
            # we open that file as bites and with read only mode
            f = open(f"{filePath}{os.sep}{file}", "rb")
            # store it's value
            x = f.read()
            # and close it
            f.close()
            # creating the destination path if it doesn't exist already
            if not os.path.exists(f"{dstPath}"):
                os.mkdir(f"{dstPath}")
            # now we want to copy files in our year folder, so we check if it exists or not
            if os.path.exists(f"{dstPath}{os.sep}{year}"):
                # it exists, now we just copy our file into our folder if the folder exists
                if os.path.exists(f"{dstPath}{os.sep}{year}{os.sep}{folder}"):
                    g = open(
                        f"{dstPath}{os.sep}{year}{os.sep}{folder}{os.sep}{file}", "wb")
                    g.write(x)
                    g.close()
                # the folder doesnt exist so we create one and copy the files into it
                else:
                    os.mkdir(f"{dstPath}{os.sep}{year}{os.sep}{folder}")
                    g = open(
                        f"{dstPath}{os.sep}{year}{os.sep}{folder}{os.sep}{file}", "wb")
                    g.write(x)
                    g.close()
            # the year folder didn't exist so we create it and all the subfolders needed, and we copy the files into it
            else:
                os.mkdir(f"{dstPath}{os.sep}{year}")
                os.mkdir(f"{dstPath}{os.sep}{year}{os.sep}{folder}")
                g = open(
                    f"{dstPath}{os.sep}{year}{os.sep}{folder}{os.sep}{file}", "wb")
                g.write(x)
                g.close()
        # for all the extentions, we check if the file matches them or not
        # if it does we call the function, if it doesnt we go to the next file
        for pic in picExt:
            if "." in file and file.split(".")[-1].lower() == pic.lower():
                filecreation("photos")
        for vid in vidExt:
            if "." in file and file.split(".")[-1].lower() == vid.lower():
                filecreation("videos")
