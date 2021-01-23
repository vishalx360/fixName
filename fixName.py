import exiftool
import sys
import os
import glob


help_page = """---------------------------------
fixName v1.0
author: @vishalx360

A CLI-tool written in python which helps you fix/rename those files with the correct filename (if it exists in the metadata of the file).

usage:
    [FILE_NAME]     file to fix.
    -d              specify a directory to perform fix process on .mkv files.
    -h,--help       to get this help-page.
------------------------------------
"""


def fix(myFile):
    with exiftool.ExifTool() as et:
        metadata = et.get_metadata(myFile)
    # fix title if its available in metadata
    if "Matroska:Title" in metadata:
        newName = metadata["Matroska:Title"].replace(" ", "_") + ".mkv"
        rename(myFile, newName)
    elif "Matroska:TrackName" in metadata:
        newName = metadata["Matroska:TrackName"].replace(" ", "_") + ".mkv"
        rename(myFile, newName)
    else:
        print("ERROR: Given file does not have 'Matroska: Title or TrackName' in it's metadata")


def rename(oldNam, newName):
    print("Do you want to rename this filname from " +
          oldNam+" to " + newName + "?")
    consent = input("y for Yes & n for No: ")
    if consent == 'y':
        os.rename(oldNam, newName)
        print("Renamed " + oldNam+" to " + newName)
    print()


if len(sys.argv) == 1:
    print("ERROR: Invalid Arguments. try --help")
else:
    if sys.argv[1] == "-d" and len(sys.argv) == 3:
        if os.path.exists(sys.argv[2]):
            os.chdir(sys.argv[2])
            files = glob.glob('*.mkv')
            if len(files) == 0:
                print("No '.mkv' files found at specified path.")
            else:
                print("Found " + str(len(files)) + " '.mkv' files")
            for file in files:
                fix(file)
    elif sys.argv[1].endswith(".mkv"):
        fix(sys.argv[1])
    elif sys.argv[1].endswith("-h") or sys.argv[1].endswith("--help"):
        print(help_page)
    else:
        print("ERROR: Invalid Arguments. try running --help")
