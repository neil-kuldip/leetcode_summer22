# 1. Two Sum
# Difficulty: Easy

# Prompt
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Thought Process 
# Out of all interview questions, this is the one that comes up most frequently and similar other problems I've encountered uses concepts applied to this problem
# Need to find two numbers in an array to satisfy condition --> Checking through iteration --> Storing possible combinations to optimize repetitive work
# Ideal solution uses a hash table with the index of the first number as the value with the complement being the key
# Reduces O(n^2) time complexity with a double for loop with an O(n) solution with a single linear search
import typing as *

def twoSum(nums: List[int], target: int) -> List[int]:
    # Hashtable --> dictionary store the index of one of the sum elements and the complement is the key
    
    complement = dict()
    for itr in range(len(nums)):
        if nums[itr] in complement:
            return [complement[nums[itr]], itr]
        else:
            diff = target - nums[itr]
            complement[diff] = itr

# Time complexity is O(n) for the iteration through the array and updating the hash table
# Space complexity is O(n) since we are creating a hash table in memory to store the indicies and complements 
