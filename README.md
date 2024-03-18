# python data structures and algorithms

## 1. BIG O:

  ![Big o](./1-big_o/1-big_o.jpeg)

  * `O(1):` Constant time. The algorithm takes the same amount of time to execute, regardless of the size of the input data set.
  ![O(1) constant time](./1-big_o/3-constant-o(1).png)

  * `O(log n):` Logarithmic time. The execution time of the algorithm increases logarithmically as the input size increases. Binary search is a classic example of an algorithm that runs in logarithmic time.

  * `O(n):` Linear time. The execution time of the algorithm increases linearly with the increase in input size. For example, a loop that goes through each element of an array once exhibits linear time complexity.
  ![O(n) linear time](./1-big_o/2-linear-o(n).png)
  
  * `O(n log n):` Linearithmic time. This time complexity is common in algorithms that break the problem into smaller subproblems, solve them independently, and then combine their solutions, such as in merge sort and quick sort.

  * `O(n^2):` Quadratic time. The execution time of the algorithm is proportional to the square of the input size. Algorithms with nested loops over the input data often have quadratic time complexity, like the bubble sort algorithm.
  ![O(n^2) quadratic](./1-big_o/4-quadratic.png)

  * `O(2^n):` Exponential time. The execution time of the algorithm doubles with each addition to the input data set. An example would be certain * naive solutions to the travelling salesman problem.

  * `O(n!):` Factorial time. The execution time of the algorithm grows factorialy with the increase in input size. Algorithms that generate all possible permutations of a set fall into this category.

  ### rules of Calculating BIG 0
    1. Worst case 
    2. Remove constants 
    3. Different terms of input
    4. remove Drop None Dominant

  