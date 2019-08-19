C:\Users\abhay\Desktop\third sem# import random
# import urllib.request
#
# def download_web_image(url):
#     name=random.randrange(1,1000)
#     full_name=str(name)+".jpg"
#     urllib.request.urlretrieve(url, full_name)
#
# download_web_image("https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fen%2Fthumb%2F7%2F7a%2FSpider-Man_3%252C_International_Poster.jpg%2F220px-Spider-Man_3%252C_International_Poster.jpg&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FSpider-Man_3&docid=Y_T5-dQRGJJXjM&tbnid=ZpTVX6icu8ehkM%3A&vet=10ahUKEwiX1sjzk4fkAhWGbisKHQq9C1MQMwh8KAAwAA..i&w=220&h=327&bih=743&biw=1536&q=spider%20man%203&ved=0ahUKEwiX1sjzk4fkAhWGbisKHQq9C1MQMwh8KAAwAA&iact=mrc&uact=8")
# import os
#
#
# fileSizeTupleList = []
# largestSize = 0
#
# for i in os.listdir(os.curdir):
#     if os.path.isfile(i):
#         fileSizeTupleList.append((i, os.path.getsize(i)))
#
# for fileName, fileSize in fileSizeTupleList:
#     if fileSize > largestSize:
#         largestSize = fileSize
#         largestFile = fileName
#
# print(largestFile, largestSize)
#
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

# abhay=[]
# abhay.append(("a","z"))
# abhay.append(("b","y"))
# for x, v in abhay:
#     print(x + v)