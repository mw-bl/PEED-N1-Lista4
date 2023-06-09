class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def display(self):
        if self.is_empty():
            print("A lista está vazia.")
            return

        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def create_reverse_linked_list(numbers):
    linked_list = LinkedList()
    for num in reversed(numbers):
        linked_list.insert_at_end(num)
    return linked_list


numbers = input("Digite os números separados por espaço: ").split()
numbers = [int(num) for num in numbers]

reverse_list = create_reverse_linked_list(numbers)

reverse_list.display()
