# 704. Binary Search
# Difficulty: Easy

# Prompt
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Thought Process 
# TBD
import typing as *

def searchHelper(start, end, nums, target):
    if len(nums[start:end]) == 1:
        if nums[start] == target:
            return start
        else:
            return -1
        
    mid = (start + end)//2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return self.searchHelper(mid+1, end, nums, target)
    else:
        return self.searchHelper(start, mid, nums, target)

def search(nums: List[int], target: int) -> int:
    start, end = 0, len(nums)
    if target > nums[-1] or target < nums[0]:
        return -1
    return self.searchHelper(start, end, nums, target)
        
