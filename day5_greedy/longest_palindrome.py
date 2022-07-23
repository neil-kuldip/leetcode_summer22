# 409. Longest Palindrome
# Difficulty: Easy

# Prompt
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

# Thought Process 
# TBD
import typing as *

def longestPalindrome(self, s: str) -> int:
    freq = {}
    for ch in s:
        if ch not in freq:
            freq[ch] = 1
        else:
            freq[ch] += 1
    maxOdd, totalEven = -1, 0
    maxOddCh = None
    for val in freq.values():
        if val&1:
            if val > maxOdd:
                if maxOdd != -1:
                    totalEven += (maxOdd - 1)
                maxOdd = val 
            else:
                totalEven += (val - 1)
        else:
            totalEven += val
    
    return maxOdd + totalEven if maxOdd != -1 else totalEven