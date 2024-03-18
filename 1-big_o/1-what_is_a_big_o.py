# why big o 

from typing import List
import time


def find_element(arr: List[int], target: int) -> int:
    indexes_found = [] 
    for indx, val in enumerate(arr):
        if val == target:
            indexes_found.append(indx) 
    return indexes_found 

arr = [i for i in range(1000)]

start_time = time.time()
print(find_element(arr, 500)) 
end_time = time.time()
print(end_time - start_time , "ms")

# increase the array size 
arr = [i for i in range(10000000)]

start_time = time.time()
print(find_element(arr, 9999999)) 
end_time = time.time()
print(end_time - start_time , "ms")

'''
as we can see the more input size increases the more execution time increases.
but the calculations depends on the computer itself. like cpu, ram..etc 
!!!!!!!!!!!!!!!!!!! so how i measure the time and space of an operation, that's what big o can do !!!!!!!!!!!
'''


'''
Big O notation in programming is a mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity.
It's a way to express the upper bound of an algorithm's running time or space requirements in terms of the size of the input data set. B
ig O notation is used in computer science to classify algorithms according to how their run time or space requirements grow as the input size grows.

Here's a quick overview of some common Big O notations and what they signify:

O(1): Constant time. The algorithm takes the same amount of time to execute, regardless of the size of the input data set.
O(log n): Logarithmic time. The execution time of the algorithm increases logarithmically as the input size increases. Binary search is a classic example of an algorithm that runs in logarithmic time.
O(n): Linear time. The execution time of the algorithm increases linearly with the increase in input size. For example, a loop that goes through each element of an array once exhibits linear time complexity.
O(n log n): Linearithmic time. This time complexity is common in algorithms that break the problem into smaller subproblems, solve them independently, and then combine their solutions, such as in merge sort and quick sort.
O(n^2): Quadratic time. The execution time of the algorithm is proportional to the square of the input size. Algorithms with nested loops over the input data often have quadratic time complexity, like the bubble sort algorithm.
O(2^n): Exponential time. The execution time of the algorithm doubles with each addition to the input data set. An example would be certain naive solutions to the travelling salesman problem.
O(n!): Factorial time. The execution time of the algorithm grows factorialy with the increase in input size. Algorithms that generate all possible permutations of a set fall into this category.


Big O notation gives a high-level understanding of the algorithm's efficiency in terms of time and space and helps in comparing different algorithms
'''


'''
Calculating the Big O notation (O(n)) of an algorithm involves analyzing its time complexity with respect to the size of its input, denoted as "n". The goal is to understand how the execution time or the number of operations required by the algorithm scales as the input size increases. Here's a simplified process for calculating Big O notation:

1 - Identify the Basic Operations: First, determine what basic operation the algorithm's performance depends on. This could be a key computation, comparison, or assignment that occurs within the algorithm.

2 - Count the Operations: Next, count how many times the basic operation is executed in terms of "n". This often involves looking at loops, recursive calls, and other structures that cause repeated execution.

3 - Find the Dominant Term: As "n" grows, some terms in your operation count will grow faster than others. Identify the term that grows the fastest, as this will dominate the execution time for large "n".

4 - Express in Big O Notation: Finally, express the dominant term in Big O notation, which is the standard way of describing the upper limit of an algorithm's growth rate.

'''
