class QueueNode:

    """ Node: Class for single node of LinkedQueue """

    def __init__(self, elem, nextnode):
        self.value = elem
        self.next = nextnode


class QueueIterator:

    """ QueueIterator: Iterator for LinkedQueue """

    def __init__(self, node, emptynode):

        """ Initializes new Iterator """

        self.start_iter = node
        self.stop_iter = emptynode

    def __next__(self):

        """ Returns next element of queue: next(iter) """

        if self.start_iter == self.stop_iter:
            raise StopIteration
        else:
            current_value = self.start_iter.value
            self.start_iter = self.start_iter.next
            return current_value


class LinkedQueue:

    """ LinkedQueue """

    def __init__(self):

        """ Initializes new queue """

        self.emptynode = QueueNode(None, None)
        self.head = self.emptynode
        self.tail = self.head
        self.size = 0

    def push(self, elem):

        """ Pushes 'elem' to queue """

        if not self.size:
            self.tail = QueueNode(elem, self.emptynode)
            self.head = self.tail
            self.size = 1
        else:
            new_node = QueueNode(elem, self.emptynode)
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def pop(self):

        """ Removes front of queue and returns it """

        out = self.head.value
        self.head = self.head.next
        self.size -= 1
        return out

    def front(self):

        """ Returns front of queue """

        return self.head.value

    def empty(self):

        """ Checks whether queue is empty """

        if self.size:
            return False
        else:
            return True

    def __iter__(self):

        """ Returns Iterator for queue: iter(queue) """

        return QueueIterator(self.head, self.emptynode)

    def __len__(self):

        """ Returns size of queue: len(queue) """

        return self.size

    def clear(self):

        """ Makes queue empty """

        self.tail = self.emptynode
        self.head = self.tail
        self.size = 0
