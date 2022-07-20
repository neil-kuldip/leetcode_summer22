# 392. Is Subsequence
# Difficulty: Easy

# Prompt
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Thought Process
# TBD 

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