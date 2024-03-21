"""constant time complexity"""


def find_element_by_index(arr, index):
    return arr[index]


"""
whatevery the input size is, the operation time will be constant time  ,
"""


def find_element_by_index_and_next_one(arr, index):
    res = []
    if index < len(arr) - 2:
        res.append(arr[index])
        res.append(arr[index + 1])


# still o(1), as the number of operations is constant , whatever the  input size is


# What is the Big O of the below function?


def anotherFunction(i):
    print(i)  # o(1)


def funChallenge(input):
    a = 10  # o(1)
    a = 50 + 3  # o(1)

    for i in range(input):  # o(n)
        anotherFunction(i)  # o(1) * n = o(n)
        stranger = True  # o(1) * n = o(n)
        print(stranger)  # o(1) * n = o(n)
        a += 1  # o(1) * n = o(n)
    return a  # o(1)


# result => 3 * o(1) +  5 * o(n) => 3 + 5n => BIG O(3+5n) => BIG(n)


# What is the Big O of the below function?


def funChallenge2(input):
    for i in range(input):
        pass
    for i in range(input):
        pass


# result => 2 * o(n) => 2n => BIG O(2n) => BIG(n)
