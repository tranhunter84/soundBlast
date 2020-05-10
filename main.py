import time
import os
import glob, os

list = []
FOLDER_PATH = r"C:\\Users\\USERNAME\\Desktop\\Soundblast"
print("Current files in directory:")

def listDir(dir):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        list.append(fileName)
if __name__ == '__main__':
    listDir(FOLDER_PATH)

item = 0
trashcan = []
length1 = len(list)

for i in range(length1):
    if 'wav' in list[i]:
        item+=1
    if 'wav' not in list[i]:
        trashcan.append(list[item])
        item+=1

item = 0
length2 = len(trashcan)

for i in range(length2):
    if trashcan[item] in list:
        list.remove(trashcan[item])
        item+=1
    else:
        item+=1

final_length = len(list)
print(final_length)
print(list)
print("")

def play_mp3():
    import winsound
    winsound.PlaySound(filename, winsound.SND_FILENAME)

print("Select a .wav file and provide name only. (EXAMPLE: im still standing)")
select = input("Enter the desired file's name. ")
data = select.casefold()
filename = str(data) + ".wav"

if filename not in list:
    print("Not an appropriate choice.")
else:
    play_mp3()
