#Google Question
#Given an array = [2,5,1,2,3,5,1,2,4]:
#It should return 2

#Given an array = [2,1,1,2,3,5,1,2,4]:
#It should return 1

#Given an array = [2,3,4,5]:
#It should return None 

from typing import List

# O(n^2)

def find_first_occurence(arr: List[int]):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]

#O(n)
def find_first_occurence(arr: List[int]):
    
    if not arr or len(arr) < 2:
        return None
    occurence = set() # can be dict 
    for value in arr:
        if value in occurence:
            return value 
        else:
            occurence.add(value)


print(find_first_occurence([2,5,1,2,3,5,1,2,4]))
print(find_first_occurence([2,1,1,2,3,5,1,2,4]))
print(find_first_occurence([2,3,4,5]))