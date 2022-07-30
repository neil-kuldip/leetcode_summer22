# 509. Fibonacci Number
# Difficulty: Easy

# Prompt
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
# such that each number is the sum of the two 
# preceding ones, starting from 0 and 1.

# Thought Process 
# Fibbonacci sequence --> Sequence can work with both iteration and recursion
# Recursion requires O(2^n) on the call stack since we are getting the the values for the previous 
# two and the previous two for each one and so forth
# Prime example of dynamic programming since we can save on space by putting the previously calculated values in an array
# However this is the best optimization since we are iterating forwards like we would hand write it with just two variables
import typing as *
def fib(n: int) -> int:
    prev = 0
    current = 1
    if n == 0:
        return prev
    if n == 1:
        return current
    
    for itr in range(1, n):
        prev, current = current, prev + current
    
    return current

# Time complexity is O(n) since we are iterating to n to get the n-2 and n-1 value in the sequence
# Space complexity is O(1) since we only need two variables to store the values of the previous two numbers,
# which is constant memory