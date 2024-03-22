class HashTable:

    def __init__(self, capacity=1000) -> None:
        self.table = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def _hash(self, key) -> int:
        # return hash(key) % self.capacity
        # or let us build our hash
        hash = 0
        key = str(key)
        for i in range(len(key)):
            hash += ord(key[i]) * i
        return hash % self.capacity

    def __setitem__(self, key, value):
        index = self._hash(key)
        current = self.table[index]
        if current == None:
            self.table[index] = [[key, value]]
        else:
            exists = False
            for item in current:
                if item[0] == key:
                    item[1] = value
                    exists = True
                    break
            if not exists:
                current.append([key, value])
        self.size += 1

    def __getitem__(self, key):
        index = self._hash(key)
        current = self.table[index]
        for item in current:
            if item[0] == key:
                return item[1]

    def __delitem__(self, key):
        index = self._hash(key)
        current = self.table[index]
        for item in current:
            if item[0] == key:
                del item
                break
        self.size -= 1

    def __contains__(self, key):
        return self.__getitem__(key)

    def keys(self):
        keys = []
        for collision in self.table:
            if collision:
                for item in collision:
                    keys.append(item[0])
        return keys

    def values(self):
        keys = []
        for collision in self.table:
            if collision:
                for item in collision:
                    keys.append(item[0])
        return keys

    def values(self):
        values = []
        for collision in self.table:
            if collision:
                for item in collision:
                    values.append(item[1])
        return values

    def items(self):
        items = []
        for collision in self.table:
            if collision:
                for item in collision:
                    items.append(item)
        return items

    def __iter__(self):
        self.current_index = -1
        self.exist_item = []
        for collision in self.table:
            if collision:
                for item in collision:
                    self.exist_item.append(item[0])
        return self

    def __next__(self):
        if self.current_index >= len(self.exist_item) - 1:
            raise StopIteration
        self.current_index += 1
        return self.exist_item[self.current_index]

    def __len__(self):
        return self.size

    def __str__(self) -> str:
        text = ""
        for collision in self.table:
            if collision:
                for item in collision:
                    text += f"{item[0]!r} : {item[1]!r} , "
        return "{ " + text + " } "


my_dict = HashTable()

my_dict["key1"] = 1
my_dict["key1"] = 2
my_dict["key2"] = "mousa nageh"
my_dict["key3"] = 32
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# print("key2" in my_dict)

for key in my_dict:
    print(key)
