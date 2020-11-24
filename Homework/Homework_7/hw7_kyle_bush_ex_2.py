'''
Homework 7, Exercise 2
Kyle Bush
11/23/2020
This program
1. Walks through a directory tree (os.walk()) and searches for files with an extension of .pdf.
2. Print these files with their absolute path and file size to the screen.
3. Copy these files from whatever location they are into a new folder
'''
import os, shutil
from pathlib import Path

def main():
    pathRoot = Path.cwd()
    copyDirPath = pathRoot / 'copied_pdfs'

    # If the target copy directory does not exist then create it.
    if not copyDirPath.exists():
        os.mkdir(copyDirPath)

    # Walks through the directory tree
    for folderName, subfolder, fileNames in os.walk(pathRoot):
        for filename in fileNames:
            if filename.endswith('.pdf'):
                # change directory to the current folder and get the file path.
                os.chdir(folderName)
                filePath = os.path.abspath(filename)

                # print absolute path of the file.
                print(filePath)

                # print the file size in bytes.
                fileSize = os.path.getsize(filePath) / 8
                print('File size: ' + str(fileSize) + ' bytes')

                # copy the file to the new target location.
                copyFilePath = copyDirPath / filename
                if not copyFilePath.exists():
                    shutil.copy(filePath, copyDirPath)
                    print('File copied successfully to ' + str(copyFilePath))
                else:
                    print('File already exists at ' + str(copyFilePath))


if __name__ == '__main__':
    main()