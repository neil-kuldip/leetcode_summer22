# 724. Find Pivot Index
# Difficulty: Easy

# Prompt
# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.

# Thought Process
# Keywords/Concepts: changing SUBARRAY sums --> Sliding windows on both side
# Interpreted the question wrong before, NOTE to read the definition thoroughly
# Can't sort it since we need the index at the value
# Probably better to treat as two sliding windows to update the sum rather than recalculate every time
from typing import *

def pivotIndex(nums: List[int]) -> int:
    if len(nums) == 1:
        return 0
    
    leftSum = 0
    rightSum = sum(nums)
    
    for itr, val in enumerate(nums):
        if itr > 0:
            leftSum += nums[itr - 1]
        rightSum -= val
        
        if leftSum == rightSum:
            return itr
        
    return -1

# Analysis
# Time complexity: O(n) since we iterated once to get the total sum, and another to update the left and right sum to find the pivot
# Space complexity: O(1) since we are only using two variables to be compared to find the pivot