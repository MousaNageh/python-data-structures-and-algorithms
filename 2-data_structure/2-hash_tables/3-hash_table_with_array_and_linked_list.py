from typing import List


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.size = 0
        self.table: List[Node] = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def __setitem__(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = Node(key=key, value=value)
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key=key, value=value)
            new_node.next = self.table[index]
            self.table[index] = new_node
        self.size += 1

    def __getitem__(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next

    def __delitem__(self, key):
        index = self._hash(key)
        current = self.table[index]
        previous: Node = None
        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                    return
                else:
                    self.table[index] = current.next

            previous = current
            current = current.next
        self.size -= 1

    def __contains__(self, key):
        return self.__getitem__(key)

    def __len__(self):
        return self.size

    def __str__(self) -> str:
        text = ""
        for node in self.table:
            if node:
                current = node
                while current:
                    text += f"{current.key!r} : {current.value!r} , "
                    current = current.next
        return "{ " + text + " } "


my_dict = HashTable()

my_dict["key1"] = 1
my_dict[1] = 1
my_dict["key2"] = "mousa nageh"
my_dict["1"] = 32
del my_dict["1"]
print(my_dict)
print(len(my_dict))
print("key2" in my_dict)
