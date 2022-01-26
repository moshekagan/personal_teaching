class ByteNode:
    def __init__(self, byte):
        if not isinstance(byte, str):
            raise TypeError("Byte must a string!")

        if len(byte) != 8:
            raise ValueError("Length must be 8")

        for i in range(len(byte)):
            current_bit = byte[i]
            if not (current_bit == "0" or current_bit == "1"):
                raise ValueError("Bits must be 0 or 1")

        self.byte = byte
        self.next = None

    def get_byte(self):
        return self.byte

    def get_next(self):
        return self.next 

    def __repr__(self):
        return "[" + self.byte +"]=>"


class LinkedListBinaryNum:
    def __init__(self, num=0):
        if not isinstance(num, int):
            raise TypeError("The number must be an int!")
        elif num < 0:
            raise ValueError('The number must be a positive int!')

        self.size = 0
        self.head = None

        BYTE_SIZE = 8
        bin_num = bin(num).replace("0b", "")

        for i in range(len(bin_num), 0, -BYTE_SIZE):
            min = i - BYTE_SIZE if i - BYTE_SIZE >= 0 else 0
            byte = bin_num[min:i]
            byte = byte.zfill(BYTE_SIZE)
            self.add_MSB(byte)

    def add_MSB(self, byte):
        new_head = ByteNode(byte)
        old_head = self.head
        new_head.next = old_head
        self.head = new_head
        self.size += 1

    def __len__(self):
        return self.size

    def __str__(self):#end user
        pass

    def __repr__(self):#developer
        byte_msg = "Byte" if len(self) == 1 else "Bytes"
        msg = f"LinkedListBinaryNum with {self.size} {byte_msg}, Bytes map: "

        current_node = self.head
        while current_node is not None:
            msg += str(current_node)
            current_node = current_node.get_next()

        msg += str(current_node)

        return msg

    def __getitem__(self, item):
        if item <= -1*self.size - 1 or self.size <= item:
            raise IndexError

        if item < 0:
            item += self.size

        i = 0
        curr = self.head
        while i < item:
            curr = curr.get_next()
            i += 1

        return curr.get_byte()

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

if __name__ == '__main__':
    # n1 = ByteNode("111")
    # n2 = ByteNode("222")
    #
    # n1.next = n2
    #
    # bl = LinkedListBinaryNum(123)
    # bl.head = n1
    # bl.size = 2
    #
    # for i in bl:
    #     print(i)

    LinkedListBinaryNum(10)
    print()
    LinkedListBinaryNum(255)
    print()
    LinkedListBinaryNum(256)
    print()
    LinkedListBinaryNum(2047)
    print()
    LinkedListBinaryNum(4294967296)