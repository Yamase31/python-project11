"""
File: concordance.py

Prints a table of the unique words in a text file and their frequencies,
as well as the number of lines, words, unique words, and running time
in seconds.
"""

from arraydict import ArrayDict
from treesorteddict import TreeSortedDict
from hashdict import HashDict
import time

def main(table = dict(), fileName = None):
    if fileName is None: return
    file = open(fileName, 'r')
    t1 = time.time()
    wordCount = 0
    uniqueWordCount = 0
    lineCount = 0
    for line in file:
        lineCount += 1
        line = line.upper()
        for word in line.split():
            wordCount += 1
            if word[-1] in "!.,:;": word = word[:-1]
            freq = table.get(word, None)
            if freq:
                table[word] = freq + 1
            else:
                uniqueWordCount += 1
                table[word] = 1
    file.close()
    t2 = time.time()
##    print("                     Word                                        Frequency")
##    for key in table:
##        print("%65s%6d" % (key, table[key]))
    print(lineCount, "lines.")
    print(wordCount, "words.")
    print(uniqueWordCount, "unique words.")
    print("Running time was", t2 - t1, "seconds.")

if __name__ == "__main__":
    main(fileName = "command.txt")
