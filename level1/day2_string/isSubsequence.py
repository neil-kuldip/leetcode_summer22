# 392. Is Subsequence
# Difficulty: Easy

# Prompt
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Thought Process
# This is the second time I'm approaching this problem, where the first time I wasn't able to think of a viable solution
# First time around I was too focused on finding the occurences of a string with a hash table along it's index but that logic didn't make sense in implementation
# This approach uses two pointers to compare characters and using a conditional if to both 1) skip all characters not in the subsequence and 
# 2) check if membership and order of the characters in the subsquence is present in the original string (retuning true or false if we got to all strings in the subsequence) 

from typing import *

def isSubsequence(s: str, t: str) -> bool:
    # Original string must be longer or equal to size of subsequence
    if len(s) > len(t):
        return False
    
    # Two pointer on each of the strings
    # If the subsequence exists then the algo iterates through the whole subsequence as the main string idx reaches the end
    subIdx, idx = 0, 0
    
    while idx < len(t) and subIdx < len(s):
        if s[subIdx] == t[idx]:
            subIdx += 1
        idx += 1
    
    return subIdx == len(s)

# Time complexity is O(n) since in the worst case scenario if we consider n to be the length of t, s and t are exactly the same string so it'll be the same length. 
# Average case iterates through most of t
# Space complexity is O(1) since we are using two variables to iterate through both lists in the while loop