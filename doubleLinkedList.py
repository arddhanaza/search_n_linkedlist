# Double Linked List

class Node:
    def __init__(self, data=None):
        self.next = None
        self.prev = None
        self.data = data


class DoubleLinked:
    def __init__(self):
        self.head = None

    # push in front
    def push(self, data):
        new_node = Node(data)

        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        tail = self.head
        while tail.next:
            tail = tail.next

        tail.next = new_node
        new_node.prev = tail

        return

    def insertAfter(self, prev_node, data):

        if prev_node is None:
            print("there is no previous node")
            return

        new_node = Node(data)
        new_node.next = prev_node.next

        prev_node.next = new_node

        new_node.prev = prev_node

        if new_node.next:
            new_node.next.prev = new_node

    def pop(self):
        temp = self.head
        while (temp):
            print("\nPop Data -->")
            print(temp.data)
            self.head = temp.next
            temp = None

    def print_list(self):
        temp = self.head
        last = None
        print("Cetak dari Depan -->")
        while (temp):
            print(temp.data, end=" ")
            last = temp
            temp = temp.next

        print("\nCetak dari Belakang -->")
        while (last):
            print(last.data, end=" ")
            last = last.prev


data = DoubleLinked()
data.push(2)
data.push(3)
data.push(6)
data.append(0)
data.push(1)
data.append(15)
data.print_list()
