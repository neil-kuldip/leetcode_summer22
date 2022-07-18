# 1480. Running Sum of 1d Array
# Difficulty: Easy

# Prompt
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# Thought Process
# Keywords/Concepts: Sum --> some form of iteration
# Sum can be put in place during calculation since it requires the prev sum val + curr index val
from typing import *

def runningSum(nums: List[int]) -> List[int]:
    for itr in range(1, len(nums)):
        nums[itr] += nums[itr-1]
    return nums

