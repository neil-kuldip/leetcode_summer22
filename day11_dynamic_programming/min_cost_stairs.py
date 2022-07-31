# 746. Min Cost Climbing Stairs
# Difficulty: Easy

# Prompt
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

# Thought Process 
# Choices with paths, minimal cost --> Dynamic Programming
# Since from every point we can either move one or two steps we can take the minimum of the succeeding steps to determine the min val for current
# Thinking of iterating backwards and just return the min of idx 0 or 1's value since we can also start at one
import typing as *

def minCostClimbingStairs(self, cost: List[int]) -> int:
    for itr in range(len(cost)-3, -1, -1):
        cost[itr] += min(cost[itr+1], cost[itr+2])
    return min(cost[0], cost[1])

# Time complexity is O(n) for the iteration through the input array
# Space complexity is O(1) since we are modifying the input array in place
