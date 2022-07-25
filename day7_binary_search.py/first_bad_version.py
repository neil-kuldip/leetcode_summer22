# 278. First Bad Version
# Difficulty: Easy

# Prompt
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. 
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. 
# You should minimize the number of calls to the API.

# Thought Process 
# If I didn't know the topic was binary search I probably would've thought about this last
# Find first something in a sorted array --> Search in a list --> Sorted so use binary search
# Modified binary search so if the middle val is bad but not the left val of the middle, middle is the first bad so return middle, otherwise check right of middle
# If middle isn't bad but the right of middle is bad, return the right of middle, else check the left of middle
# Could optimize further by checking both the left and right of middle for the if statement, considering it now
import typing as *

def firstBadVersionHelper(start, end, n):
    if end == start + 1:
        return start
    
    mid = (start + end)//2
    if isBadVersion(mid):
        if mid - 1 >= 1:
            if isBadVersion(mid-1):
                return self.firstBadVersionHelper(start, mid, n)
            else:
                return mid
    else:
        if mid + 1 <= n:
            if isBadVersion(mid+1):
                return mid + 1
            else:
                return self.firstBadVersionHelper(mid+1, end, n)
                
            
                
def firstBadVersion(n: int) -> int:
    start, end = 1, n+1
    return self.firstBadVersionHelper(start, end, n)

# Time complexity is O(log n) since we are implementing a sligthly modified binary search algo
# Space is O(1) since we are using literal values to be compared in our algo, not taking any extra memory