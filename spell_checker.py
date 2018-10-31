import binarysearch
import sys
import stdio
from instream import InStream


# Takes as a command-line argument the name of a file containing a list of
# words, and then reads strings from standard input and writes any string
# that is not in the list.
def main():
    # Read the words from the file specified as command-line argument into
    # a list, and sort the list.
    file = sys.argv[1]
    ist = InStream(file)
    l = []
    for word in ist.readAllStrings():
        l.append(word)
    l.sort()

    # Read strings from standard input, efficiently search for each one in the
    # list of words, and write the string to standard output if it is not
    # found, ie, it is misspelled.
    for word in stdio.readAllStrings():
        if binarysearch.search(word,l) == -1:
            stdio.writeln(word)


if __name__ == '__main__':
    main()


