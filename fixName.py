import exiftool
import sys
import os

myFile = sys.argv[1]

with exiftool.ExifTool() as et:
    metadata = et.get_metadata(myFile)


if "Matroska:Title" in metadata:
    newName = metadata["Matroska:Title"].replace(" ", "_") + ".mkv"
    os.rename(myFile, newName)
    print("Renamed to " + newName)
else:
    print("ERROR: Given file does not have 'Matroska:Title' in it's metadata")