'''linear time complexity'''


def linear_search(arr, x):
    for i in range(len(arr)): 
        if arr[i] == x:
            return i
    return -1

'''
Analysis:

The basic operation here is the comparison arr[i] == x.
In the worst case (where the element is not in the list or is the last element), this comparison is made "n" times.
Therefore, the time complexity is directly proportional to "n", and we express this as O(n).
notes:
1 - it do not matter the factor will added or divided or multipied by a constant
    for examples:
    5n => O(n)
    n/2 =>  O(n)
    n/5 + 10000 + 2n =>  O(n)
    n * 5 => O(n)
'''


def sum_2_list(arr1: list, arr2: list):
    result = 0 
    
    for i in arr1[:int(len(arr1)/2)]: # O(a/2)
        result += i 
    for i in arr2: # O(b)
        result += i

# O(a + b)


def my_func(arr: list):
    
    first_half = arr[: int(len(arr)/2) ] # O(1)
    
    for  i in first_half:
        print(i) # O(n/2)
    
    for x in range(100):
        print(x) # 100 * O(1)
    
    return 'done' # O(1)
    
# results => 1 + n/2 + 100 + 1 = 101 + n/2 => BIG O(101 +n/2) => BIG(n/2) => BIG(n)



## every important############################

def my_func2(arr: list, arr2):
    
    first_half = arr[: int(len(arr)/2) ] # O(1)
    
    for  i in first_half:
        print(i) # O(a/2)
    
    for x in range(len(arr2)):
        print(arr2[x]) # O(b)
    
    return 'done' # O(1)

# results => 1 + a/2 + b + 1  =>  BIG(a + b)