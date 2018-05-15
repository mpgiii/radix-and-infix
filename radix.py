class Queue:
    def __init__(self):
        self.items = []
        self.frontIdx = 0

    def __compress(self):
        newitems = []
        for i in range(self.frontIdx, len(self.items)):
            newitems.append(self.items[i])

        self.items = newitems
        self.frontIdx = 0

    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to dequeue an empty queue")

        # When queue is half full, compress it. This
        # achieves an amortized complexity of O(1) while
        # not letting the list continue to grow unchecked.
        if self.frontIdx * 2 > len(self.items):
            self.__compress()

        item = self.items[self.frontIdx]
        self.frontIdx += 1
        return item

    def enqueue(self, item):
        self.items.append(item)

    def front(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to access front of empty queue")

        return self.items[self.frontIdx]

    def isEmpty(self):
        return self.frontIdx == len(self.items)

    def clear(self):
        self.items = []
        self.frontIdx = 0


def charAt(s, i):
    if len(s) - 1 < i:      # returns blanks if that index doesn't exist
        return " "
    else:
        return s[i]


def longestlength(list):
    length = 0              # determines longest length in list, and returns that length
    for x in list:
        if len(x) > length:
            length = len(x)

    return length


def radixsort(unsortedlist, size):
    mainQueue = Queue()         # initializes queue
    longest = longestlength(unsortedlist)   # finds longest length
    newwordlist = []                # initializes place to store modified words
    queuelist = []                  # initializes list to store our ASCII queues
    finallist = []
    newword = ''

    for x in unsortedlist:      # cycle through list
        for i in range(longest):
            newwordlist.append(charAt(x, i))
        newword = ''.join(newwordlist)  # get the word, with blanks
        mainQueue.enqueue(newword)      # put that with blanks word on the queue
        newwordlist = []

    for j in range(256):
        queuelist.append(Queue())

    for w in range(longest - 1, 0, -1):
        string = mainQueue.dequeue()
        spot = ord(charAt(string, w))
        queuelist[spot].enqueue(string)

    for i in range(256):
        while not queuelist[i].isEmpty():
            mainQueue.enqueue(queuelist[i].dequeue())

    while not mainQueue.isEmpty():
        finallist.append(mainQueue.dequeue().strip())

    return finallist


def main():
    unsortedlst = ['aaa', 'abc', 'aa', 'cc', 'cba', 'zzz']
    sorted = radixsort(unsortedlst, len(unsortedlst))
    print(sorted)


if __name__ == '__main__':
    main()
