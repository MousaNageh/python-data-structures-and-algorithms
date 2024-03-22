class Node:

    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self.value)


class SingleLinkedList:

    def __init__(self, head_value) -> None:
        # at the init the head is the same as the tail
        self.head: Node = Node(value=head_value)
        self.tail: Node = self.head
        self.size = 1

    # add value to the end of linked linked list --- O(1)
    def append(self, value):
        # 1 - create new node
        new_node = Node(value)
        # 2 - make the next of th tail points to the new node
        self.tail.next = new_node
        # 3 - make the new node became the tail
        self.tail = new_node
        # 4 - increase size of linked list
        self.size += 1

        return self

    # add value to the first of linked linked list --- O(1)
    def prepend(self, value):
        # 1 - create new node
        new_node = Node(value)
        # 2 - make the next of the new node points to the head
        new_node.next = self.head
        # 3 - make the new node become the head
        self.head = new_node
        # 4 - increase size of linked list
        self.size += 1

    # add value to the nth posistion of linked linked list --- O(n)
    def insert(self, value, position):
        # node1 --> node2 -->  ...
        #      \      /
        # step3 \    / step 2
        #      new_node
        #       (step1)
        self.__check_position(position)
        if position == 0:
            self.prepend(value)
        elif position >= self.size:
            self.append(value)
        else:
            current = self.head
            current_index = 1
            while current:
                if current_index == position:
                    # 1 - create new node
                    new_node = Node(value)
                    # 2 - make the next of new node points to the next of current node
                    new_node.next = current.next
                    # 3 - make the next of current node points to the new node
                    current.next = new_node
                    # 4 - increase size of linked list
                    self.size += 1
                    break
                current = current.next
                current_index += 1

    # O(1)
    def remove_first(self):
        if self.size > 1:
            current_head = self.head
            self.head = self.head.next
            del current_head
            self.size -= 1

    # O(n)
    def remove_last(self):
        if self.size <= 2:
            self.head.next = None
            current = self.tail
            self.tail = self.head
            del current
        else:
            current_idx = 0
            current = self.head
            while current_idx < self.size - 2:
                current = current.next
                current_idx += 1
            self.tail = current.next
            self.tail.next = None
            del current
        self.size -= 1

    # remove value to the nth position of linked linked list --- O(n)
    def remove(self, position):
        self.__check_position(position)
        if position == 0:
            self.remove_first()
        elif position >= self.size:
            self.remove_last()
        else:
            current_index = 1
            current = self.head
            prev = None
            while current_index <= position:
                prev = current
                current = current.next
                current_index += 1
            prev.next = current.next
            del current
            self.size -= 1

    # O(n)
    def search_by_position(self, position):
        self.__check_position(position, for_search=1)
        current = self.head
        current_index = 0
        while current_index != position:
            current = current.next
            current_index += 1
        if current:
            return current.value

    # O(n)
    def first_matched_value(self, value):
        current = self.head
        index = -1
        current_index = 0
        while current:
            if current.value == value:
                index = current_index
                break
            current_index += 1
            current = current.next
        return index

    # O(n)
    def all_matched_value(self, value):
        current = self.head
        indexes = []
        current_index = 0
        while current:
            if current.value == value:
                indexes.append(current_index)
            current_index += 1
            current = current.next
        return indexes

    def __check_position(self, index, for_search=0):
        if index < 0:
            raise IndexError("index can not be less than 0")
        if index + for_search > self.size:
            raise IndexError("out of range")

    def __iter__(self):
        self.current = 1
        return self

    # O(n)
    def __next__(self):
        if self.current == 1:
            self.current = self.head
        else:
            self.current = self.current.next
        if not self.current:
            raise StopIteration
        return self.current

    def __contains__(self, key):
        return self.first_matched_value(key)

    def __str__(self) -> str:
        text = ""
        current = self.head
        while current:
            text += str(current) + " --> "
            current = current.next
        return text.strip(" --> ")

    def __len__(self):
        return self.size


single_linked = SingleLinkedList(1)
single_linked.append(2)
single_linked.append(3)
single_linked.append(4)
single_linked.append(5)
single_linked.append(6)
single_linked.append(6)
single_linked.append(2)
single_linked.append(3)
single_linked.append(5)
