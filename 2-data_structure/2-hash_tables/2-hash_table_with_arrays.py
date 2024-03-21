


class HashTable:
    
    def __init__(self, capacity = 1000) -> None:
        self.table = [None] * capacity
        self.capacity = capacity
        self.size = 0
    
    def _hash(self, key) -> int:
        return hash(key) % self.capacity
        
    
    def __setitem__(self, key, value):
        index = self._hash(key)
        current = self.table[index]
        if current == None:
            self.table[index] = [[ key, value] ] 
        else:
            exists= False
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

    def __len__(self):
        return self.size

    def __str__(self) -> str:
        text = ""
        for collision in self.table:
            if  collision:
                for item in collision:
                    text += f"{item[0]!r} : {item[1]!r} , "
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
    
    