from typing import Optional


class Node:

    def __init__(self, value, next=None, prev=None) -> None:
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return self.value


class DoubleLinkedList:

    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size = 0

    # O(1)
    def append(self, value):
        # 1 - create new node
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            # 2 - make prev of new node points to the tail
            new_node.prev = self.tail
            # 3 - make next of  tail points to the new node
            self.tail.next = new_node
            # 4 - make new node become the tail
            self.tail = new_node
        # 5 - increase size
        self.size += 1

    # O(1)
    def prepend(self, value):
        # 1 - create new node
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            # 2 - make next of new node points to the head
            new_node.next = self.head
            # 3 - make prev of head points to the new node
            self.head.prev = new_node
            # 4 - make new node become the head
            self.head = new_node

        # 5 - increase size
        self.size += 1

    def insert(self, value, position):
        self.__check_position(position)
        if position == 0:
            self.prepend(value)
        elif position >= self.size:
            self.append(value)
        else:
            new_node = Node(value)
            target_node = self.__get_node_of_index(position)
            new_node.next = target_node
            new_node.prev = target_node.prev
            target_node.prev.next = new_node
            target_node.prev = new_node
            self.size += 1

    # O(1)
    def remove_first(self):
        if not self.head:
            raise ValueError("list already empty")
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1

    # O(1)
    def remove_last(self):
        if not self.tail:
            raise ValueError("list already empty")
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1

    # O(n)
    def remove(self, position):
        self.__check_position(position)
        if position == 0:
            self.remove_first()
        elif position == self.size - 1:
            self.remove_last()
        else:
            target_node = self.__get_node_of_index(position)
            prev_next = target_node.prev
            next_node = target_node.next
            prev_next.next = next_node
            next_node.prev = prev_next
            self.size -= 1

    # O(n)
    def find_first_match(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    # O(n/2)
    def all_first_match(self, value):
        current = self.head
        matches = []
        start_node = self.head
        end_node = self.tail
        start = 0
        end = self.size - 1
        while start < end:
            if start_node.value == value:
                matches.append(start)
            if end_node.value == value:
                matches.append(end)
            end_node = end_node.prev
            start_node = start_node.next
            end -= 1
            start += 1
        return matches

    def __get_node_of_index(self, target_index):
        # Decide the traversal direction based on the target index
        if target_index <= (self.size // 2):
            # Start from the head for the first half of the list
            current = self.head
            index = 0
            while current:
                if index == target_index:
                    return current
                index += 1
                current = current.next
        else:
            # Start from the tail for the second half of the list
            current = self.tail
            index = self.size - 1
            while current:
                if index == target_index:
                    return current
                index -= 1
                current = current.prev

    def __str__(self) -> str:
        text: str = ""
        current = self.head
        while current:
            text += str(current) + " --> "
            current = current.next
        return text.strip(" --> ")

    def __check_position(self, index, for_search=0):
        if index < 0:
            raise IndexError("index can not be less than 0")
        if index + for_search > self.size:
            raise IndexError("out of range")


double = DoubleLinkedList()
double.append(1)
double.append(2)
double.append(6)
double.append(3)
double.append(4)
double.append(5)
double.append(6)
double.append(3)
print(double.all_first_match(23))
