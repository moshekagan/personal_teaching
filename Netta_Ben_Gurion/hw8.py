class ByteNode:
    def __init__(self, byte):
        self.byte = byte
        self.next = None
        # if not isinstance(self.byte, str):
        #     raise TypeError
        # elif len(self.byte) != 8:
        #     raise ValueError
        # for i in range(8):
        #     if int(i) != 0 and int(i) != 1:
        #         raise ValueError

    def get_byte(self):
        return self.byte

    def get_next(self):
        return self.next 

    def __repr__(self):
        return "[" + self.byte +"]=>"


class LinkedListBinaryNum:
    def __init__(self, num=0):
        self.num = num
        self.head = None
        self.size = 0
        if not isinstance(self.num, int):
            raise TypeError("The number must be an int!")
        elif self.num < 0:
            raise ValueError('The number must be a positive int!')

    def add_MSB(self, byte):
        temp = byte
        temp.next = self.head
        self.head = temp
        self.len += 1

    def __len__(self):
        return len(self.size)

    def __str__(self):#end user
        pass

    def __repr__(self):#developer
        if len == 1:
            return 'LinkedListBinaryNum with' + str(self.size) + "Byte, " + "Bytes map: " + str(self.num)
        else:
            return "LinkedListBinaryNum with" + str(self.size) + "Bytes, " + "Bytes map: " + str(self.num)

    def __getitem__(self, item):
        pass

    #Order relations:

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __radd__(self, other):
        pass


class DoublyLinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

    def set_next(self, next):
        return self.next

    def get_next(self):
        return self.prev

    def get_prev(self):
        pass

    def set_prev(self, prev):
        pass

    def __repr__(self):
        pass


class DoublyLinkedList:
    def __init__(self):
        pass

    def __len__(self):
        pass

    def add_at_start(self, data):
        pass

    def remove_from_end(self):
        pass

    def get_tail(self):
        pass

    def get_head(self):
        pass

    def __repr__(self):
        pass

    def is_empty(self):
        pass


class DoublyLinkedListQueue:
    def __init__(self):
        self.data = DoublyLinkedList()

    def enqueue(self, val):
        pass

    def dequeue(self):
        pass

    def __len__(self):
        pass

    def is_empty(self):
        pass

    def __repr__(self):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass
