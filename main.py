import time
import test
import os
import glob, os

# Variable 'list' - list that will be used to
## store names of all files in 'Soundblast' folder
list = []

# Variable 'FOLDER_PATH' - path of 'Soundblast' folder
FOLDER_PATH = r"C:\\Users\\***INSERT USERNAME HERE***\\Desktop\\Soundblast"

print("Soundblast is a tool that lets you listen to any .wav file!")
print("")
print("Current files in directory:")

# listDir navigates through Soundblast folder and appends
## the names of all the files in the folder to the empty list created earlier
def listDir(dir):

    # Variable 'fileNames' - uses os module to set the variables's value equal
    ## to a list of everything in the directory
    fileNames = os.listdir(dir)

    # For loop iterates until every file in fileName is evalutaed
    for fileName in fileNames:

        # Every iteration - file name is added to variable 'list'
        list.append(fileName)

# Call function 'listDir' taking variable 'FOLDER_PATH' in as an argument
if __name__ == '__main__':
    listDir(FOLDER_PATH)

# Variable 'item' - the list item number for which the loop will evalutate
## Initial value is 0, the first item in the list
item = 0

# Variable 'trashcan' - list that will be used to store names of files that
## are not .wav file type
trashcan = []

# Variable 'length' - Integer value equal to the length of the original list
length1 = len(list)

# For loop iterates for length of the original list
for i in range(length1):

    # Does nothing for .wav files in the list
    if 'wav' in list[i]:
        item+=1

    # Adds names of files that aren't .wav to 'trashcan' list
    if 'wav' not in list[item]:
        trashcan.append(list[item])

# Variable 'item' - the list item number for which the loop will evalutate
## Initial value is 0, the first item in the list
item = 0

# Variable 'length2' - Integer value equal to the length of the 'trashcan' list
length2 = len(trashcan)

# For loop iterates for length of the 'trashcan' list
for i in range(length2):

    # Removes all non-.wav files from the orignal list by iterating through all
    ## the items that exist in trashcan
    if trashcan[item] in list:
        list.remove(trashcan[item])
        item+=1

    # Does nothing if the evaluated item from the original list doesn't exist in trashcan
    else:
        item+=1

# Variable 'final_length' - the length of the list after all non-.wav files have
## been removed
final_length = len(list)

# Print the new length
print(final_length)

# Print our newly created list of .wav files available to choose from
print(list)
print("")


# Fetches song file and plays it
def play_mp3():
    import winsound
    winsound.PlaySound(filename, winsound.SND_FILENAME)

print("Select a .wav file and provide name only. (EXAMPLE: im still standing)")
select = input("Enter the desired file's name. ")

# Use .casefold() function to remove capitalization
data = select.casefold()

# Variable 'filename' - equal to the user's input for desired file's name
## plus .wav file type specified at the end
filename = str(data) + ".wav"

# If the user's desired file's name isn't in the list, reject user's request
if filename not in list:
    print("Not an appropriate choice.")

# If the user's desired file name is valid and in the list, play
## corresponding .wav file
else:
    play_mp3()


            
