# 409. Longest Palindrome
# Difficulty: Easy

# Prompt
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

# Thought Process 
# Palindrome --> composed only of even sets of characters and/or one odd set of characters
# Had a bit of struggle since I originally thought to just find the maxOdd character set and add it to the number of even sets to get the longest length
# Later came to mind to just subtract one from each of the smaller odd sets to be used in the length
# Hashtable to just focus on character frequency since we don't have to generate the longest palindrome
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

# Time complexity is O(n) since we are iterating through the string to make the dictionary and then through the dictionary values of length n to make the total sum
# Space complexity is O(n) since we created a hashtable with extra memory to calculate the longest possible palindrome length