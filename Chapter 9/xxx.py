# Write your code here :-)
import zipfile, os

for folderName, subfolders, filenames in os.walk('C:\\Users\\david\\selective'):
    #print(The current folder is '+ folderName)
    print(folderName)
    for subfolder in subfolders:
        #print(SUBFOLDER OF '+ folderName + ': ' + subfolder)
        print(subfolder)
    for filename in filenames:
        #print(FILE INSIDE '+ folderName+ ': '+ filename)
        print(filename)
    print('')


