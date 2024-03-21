"""
without hash collision
Insertion: O(1) 
Update: O(1) 
Search: O(1) 
Retrieve: O(1) 
Delete: O(1) 
Traverse: O(n)
"""
"""
When collisions occur in a hash table, 
the efficiency of operations such as insertion, search, update, retrieve, and delete can be affected, 
leading to a potential degradation from their average-case time complexities. 
The extent of this impact depends largely on the collision resolution strategy employed by the hash table. 
Two common strategies are chaining and open addressing (which includes linear probing, quadratic probing, and double hashing as its variants).


1 - Insertion: In the worst case, all keys hash to the same slot, making the time complexity O(n), where n is the number of keys. However, if the hash function is well-designed and distributes keys uniformly, the lengths of the chains remain small, and the average insertion time remains close to O(1).
2 - Search/Retrieve: Similarly, the worst-case time complexity is O(n) when all keys collide into the same slot. The average case remains close to O(1) if collisions are minimal and well-managed.
3 -Delete: Deleting an element also requires searching for it first in its chain, 
so it shares the same time complexity as search and retrieve operations.
"""
my_dict = {}  # Create an empty dictionary
my_dict["apple"] = "green"  # Insert a new key-value pairs
my_dict["apple"] = "red"  # Update the value for the key "apple"
apple_color = my_dict.get("apple", "not found")  # Retrieve the value for "apple"
# "apple_color" will be "red" if "apple" exists, otherwise "not found"
del my_dict["apple"]  # Delete the key-value pair with key "apple"
for key, value in my_dict.items():  # Traverse the dictionary
    print(f"Key: {key}, Value: {value}")


