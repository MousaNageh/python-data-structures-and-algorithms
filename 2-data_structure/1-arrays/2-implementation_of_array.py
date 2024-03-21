class MyArray:

    def __init__(self) -> None:
        self.data = {}
        self.len = 0

    def push(self, value):
        self.data[self.len] = value
        self.len += 1

    def pop(self):
        if self.len == 0:
            raise IndexError("pop from empty array")
        self.len -= 1
        value = self.data[self.len]
        del self.data[self.len]
        return value

    def remove(self, index):
        self.__check_index(index)
        value = self.data[index]

        # Shift items to the left and decrease len
        for i in range(index, self.len - 1):
            self.data[i] = self.data[i + 1]

        del self.data[self.len - 1]

        self.len -= 1
        return value

    def insert(self, index, value):
        self.__check_index(index)
        self.data[self.len] = None
        self.len += 1
        # Shift items to the right
        for i in range(self.len - 1, index, -1):
            self.data[i] = self.data[i - 1]
            i -= 1
        self.data[index] = value

    def __str__(self) -> str:
        return str(list(self.data.values()))

    def __getitem__(self, index):
        self.__check_index(index)
        return self.data[index]

    def __setitem__(self, index, value):
        self.__check_index(index)
        self.data[index] = value

    def __check_index(self, index):
        if index < 0:
            raise ValueError("index can not be negative")
        if index > self.len or not self.data:
            raise IndexError("index out of range")

    def __len__(self):
        return self.len

    def __iter__(self):
        self.start_index = -1

        return self

    def __next__(self):
        if self.start_index < self.len - 1:
            self.start_index += 1
            return self.data[self.start_index]
        else:
            raise StopIteration


l = MyArray()
l.push(1)
l.push(2)
l.insert(1, "mousa")
print(l)
for val in l:
    print(val)
