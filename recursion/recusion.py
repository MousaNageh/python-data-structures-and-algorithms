
def make_list_flat(arr: list, res: list=[]):
    for element in arr:
        if isinstance(element, list): # recursive case 
            make_list_flat(element, res) 
        else: # base case 
            res.append(element)
    return res 


print(make_list_flat([[1,2,3,4], 5,6,7 , [8,9,10]]))



         

def factorial(val: int):
    if val > 1: # recursive case 
        return val * factorial(val -1)
    else: # base case 
        return 1

print(factorial(5))

# fibonacci :  0,1,1,2,3,5,8,13,21,34,55,....

# O(n^2)
def fibonacci(n: int):
    if n > 2: # recursive case  
        return fibonacci(n-1) + fibonacci(n-2)
    else: # recursive case 
        if n <= 0 :
            return 0 
        else:
            return 1 
        
print(fibonacci(10))      

# O(n)
def fibonacci2(n: int):
    if n <= 2: 
        if n == 0:
            return 0 
        return 1
    res1 = 1
    res2 = 1
    counter = 2
    while counter < n:
        temp = res2 
        res2 = res2 + res1
        res1 = temp
        counter += 1  
    
    return res2

print(fibonacci2(10))      



def reverse_string(text: str):
    counter = len(text) -1 
    def reverser(counter):
        if counter == 0:
            return text[counter]
        else:
            return text[counter] + reverser(counter -1)
    return reverser(counter)

print(reverse_string('mousa'))
        
    
    