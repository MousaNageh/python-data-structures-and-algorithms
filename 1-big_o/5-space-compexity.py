

def fun(arr: list): 
    for i in arr: # O(1)
        print(i)
#result => O(1)



def fun(arr: list): 
    val = None
    for i in arr: # O(1)
        val = i # O(1) reused
        print(val)
#result => O(1)



def fun(arr: list): 
    val = [] # create data structure
    for i in arr: # O(1)
        val.append(i) # O(1) allocation
        print(val)
#result => O(n)



def fun(arr: list): 
    val = []
    for i in arr: # O(1)
        val.append(i) # O(n) allocation
        var2 = i  # O(1)
        print(val)
        print(var2)
#result => O(n) + O(n) = O(n)