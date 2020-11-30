'''
Homework 7, Exercise 1
Kyle Bush
11/23/2020
Here’s what the program should do:
- Search all filenames in the current working directory for American-style dates in the names.
- When one is found, rename the file to make the date portion Asian style (the rest of the filename doesn’t change).
'''
import shutil, os, re

def main():
    # Regex that matches files with the American date format.
    americanDatePattern = re.compile(r"""^(.*?) # all text before the date
       ((0|1)?\d)-                              # one or two digits for the month
       ((0|1|2|3)?\d)-                          # one or two digits for the day
       ((19|20)\d\d)                            # four digits for the year
       (.*?)$                                   # all text after the date
       """, re.VERBOSE)

    # Loop over the files in the working directory.
    for americanFilename in os.listdir('.'):
        match = americanDatePattern.search(americanFilename)
        # Skip files without a date.
        if match == None:
            continue

        # Get the different parts of the filename.
        beginningFileName = match.group(1)
        month  = match.group(2)
        day    = match.group(4)
        year   = match.group(6)
        endFileName  = match.group(8)

        # Create the Asian style filename.
        asianFilename = beginningFileName + year + '-' + month + '-' + day + endFileName

        # Get the full, absolute file paths.
        absWorkingDir = os.path.abspath('.')
        amerFilename = os.path.join(absWorkingDir, americanFilename)
        asianFilename = os.path.join(absWorkingDir, asianFilename)

        # Rename the files.
        print(f'Renaming "{amerFilename}" to "{asianFilename}"...')
        shutil.move(amerFilename, asianFilename)

if __name__ == '__main__':
    main()