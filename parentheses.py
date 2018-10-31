import sys
import stdio
from linkedstack import Stack


# Reads in a string as command-line argument and writes True if its
# parentheses are properly balanced and False otherwise.
def main():
    # Read a string s as command-line argument.
    s = sys.argv[1]

    # Build a stack.
    sk = Stack()

    # Define a variable balanced and set it to True.
    balanced = True

    # Enumerate the characters c in s. If c is any of the opening parenthesis,
    # push it onto the stack. Otherwise, set balanced to False and break
    # the loop if either the stack is empty or if the value atop the stack
    # doesn't open c.
    for c in s:
        if c in "[{(":
            sk.push(c)
        else:
            if sk.isEmpty():
                balanced = False
                break
            prev = sk.pop()
            if (c == ')' and prev == '(') \
                or (c == ']' and prev == '[') \
                or (c == '}' and prev == '{'):
                pass
            else:
                balanced = False
                break

    # The parentheses in s are balanced if balanced is True and the stack
    # is empty.
    if balanced and sk.isEmpty():
        stdio.writeln('True')
    else:
        stdio.writeln('False')

if __name__ == '__main__':
    main()


