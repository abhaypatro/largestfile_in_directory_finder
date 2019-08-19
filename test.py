
import os

fileSizeList = []
largestSize = 0
val=input("Enter the directory ")
for root, dirs, files in os.walk(val):
    for file in files:
        fileSizeList.append((file, os.path.getsize(os.path.join(root, file))))

for fileName, fileSize in fileSizeList:
    if fileSize > largestSize:
        largestSize = fileSize
        largestFile = fileName

print(largestFile, "is the largest file with a size of ", largestSize,"bytes")

