#Google Question
#Given an array = [2,5,1,2,3,5,1,2,4]:
#It should return 2

#Given an array = [2,1,1,2,3,5,1,2,4]:
#It should return 1

#Given an array = [2,3,4,5]:
#It should return None 

from typing import List

# O(n^2) time complexity
#O(1) for space complexity
def find_first_occurence1(arr: List[int]):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]

#O(n) for time complexity
#O(n) for space complexity
def find_first_occurence2(arr: List[int]):
    
    if not arr or len(arr) < 2:
        return None
    occurence = set() # can be dict 
    for value in arr:
        if value in occurence:
            return value 
        else:
            occurence.add(value)

# O(n^2) time complexity
#O(1) for space complexity
def find_first_occurence3(arr: List[int]):
    small_index_sum = len(arr)
    matches = None
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                if i + j <= small_index_sum:
                    small_index_sum =  i + j 
                    matches = arr[i]
    return matches

print(find_first_occurence1([2,5,1,2,3,5,1,2,4]) == find_first_occurence2([2,5,1,2,3,5,1,2,4]) == find_first_occurence3([2,5,1,2,3,5,1,2,4])) # true
print(find_first_occurence1([2,1,1,2,3,5,1,2,4]) == find_first_occurence2([2,1,1,2,3,5,1,2,4]) ) # false 
print(find_first_occurence1([2,1,1,2,3,5,1,2,4])) # this will return 2 
print(find_first_occurence2([2,1,1,2,3,5,1,2,4])) # this will return 1 
print(find_first_occurence3([2,1,1,2,3,5,1,2,4])) # this will return 1 
print(find_first_occurence1([2,3,4,5]) == find_first_occurence2([2,3,4,5]) == find_first_occurence3([2,3,4,5])) # true


