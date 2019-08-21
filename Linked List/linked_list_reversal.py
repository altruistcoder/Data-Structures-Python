class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()


llist = LinkedList()
n = int(input('Enter the number of elements to be added in Linked List: '))
for i in range(n):
    data = int(input('Enter the data item: '))
    llist.push(data)
print('The Linked List: ')
llist.display()
print('The Reversed Linked List: ')
llist.reverse()
llist.display()
