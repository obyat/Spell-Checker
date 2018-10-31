import sys
import stdio
from linkedqueue import Queue


# Takes a command-line argument k and writes the kth from the last string
# found on standard input.
def main():
    # Read a command-line argument k, as an int.
    k = int(sys.argv[1])

    # Build a queue.
    que = Queue()

    # Read strings from standard input, insert each into the queue, and
    # count the total number of strings inserted into a variable n.
    ss = stdio.readAllStrings()
    n = 0
    for x in ss:
        que.enqueue(x)
        n += 1
    # Dequeue n - k strings from the queue.
    for i in range(n-k):
        que.dequeue()

    # Write the string in front of the queue, which is the kth string from
    # the end.
    stdio.writeln(que.dequeue())

if __name__ == '__main__':
    main()


