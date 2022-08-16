# 70. Climbing Stairs
# Difficulty: Easy

# Prompt
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Thought Process 
# Almost identical to the fibonacci problem solved earlier --> sequence that requires knowing previous values
# Previous values that would be recalculated can be stored somewhere --> DP Problem
# Considering iteration like before and just storing the previous two values into variables
import typing as *
def climbStairs(n: int) -> int:
    prev = 1
    current = 2
    if n == 1:
        return prev
    if n == 2:
        return current
    
    for itr in range(2, n):
        prev, current = current, prev + current
    
    return current

# Time complexity is O(n) since we're iterating to n and using the previous two steps paths to calculate the next
# Space complexity is O(1) since we require only two variables to store the previous two steps paths to calculate the next