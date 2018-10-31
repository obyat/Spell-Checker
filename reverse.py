import stdio
from linkedstack import Stack


# Reads in strings from standard input and writes them in reverse order to
# standard output.
def main():
    # Build a stack.
    sk = Stack()

    # Read strings from standard input and push them into the stack.
    ss = stdio.readAllStrings()
    for x in ss:
        sk.push(x)
    # Pop each element of the stack and write it to standard output.
    while not sk.isEmpty():
        stdio.writeln(sk.pop())

if __name__ == '__main__':
    main()


