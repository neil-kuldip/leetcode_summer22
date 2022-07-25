# 704. Binary Search
# Difficulty: Easy

# Prompt
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Thought Process 
# This is straightforward in that it the problem is asking for the algorithm and not a scenario problem utilizing that algorithm
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

# Time complexity is O(log n) by the nature of searching the middle value of each half partition of the input array for binary search
# Space is O(1) since we are using solely the input array values for this algorithm
        
