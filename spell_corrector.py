import sys
import stdio
from instream import InStream


# Takes as a command-line argument the name of a file that contains common
# misspellings and corrections, and suggests replacements for the misspelled
# words on standard input, by writing them to standard output.
def main():
    # Read all lines from the misspellings file specified as command-line
    # argument, into a list.
    ll = InStream(sys.argv[1]).readAllLines()

    # From the list above, build a dictionary whose keys are the common
    # misspellings and values are their corrections.
    dd = dict()
    for line in ll:
        a,b = line.split(' ',1)
        dd[a] = b[1:-1]


    # Read strings from standard input, check if it is in the dictionary,
    # ie, it is misspelled, and in that case write the word along with its
    # correction to standard output.
    for word in stdio.readAllStrings():
        if word in dd:
            stdio.write(word)
            stdio.write(" -> ")
            stdio.writeln(dd[word])

if __name__ == '__main__':
    main()


