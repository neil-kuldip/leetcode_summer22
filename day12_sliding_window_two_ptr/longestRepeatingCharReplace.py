# 424. Longest Repeating Character Replacement
# Difficulty: Medium

# Prompt
# You are given a string s and an integer k. 
# You can choose any character of the string and change it to any other uppercase English character. 
# You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Thought Process 
# This is a problem I need to revisit later on, as I didn't come up to an answer on my own and had to reference Neetcode for it (https://www.youtube.com/watch?v=gqXU1UyA8pk)
# Original idea was to find the longest substring with a sliding window and then proceed to check the left and right if we can flip characters
# This was hard especially if there equally long substrings in the main string
# My modified thought process would be to use sliding window but check the conditions to the window's hash table and length
# That way we can find the longest substring that satisfies the condition as we're using the window without additional parts
import typing as *

def characterReplacement(s: str, k: int) -> int:
    if len(s) == 1:
        return len(s)
    
    longest = 0
    left, right = 0, 0
    freq = {}
    while right < len(s):
        if s[right] in freq:
            freq[s[right]] +=1
        else:
            freq[s[right]] = 1
        while (right - left + 1) - max(freq.values()) > k:    
            left += 1
            freq[s[left-1]] -= 1
        if (right - left + 1) > longest:
            longest = (right - left + 1)
        right += 1
    
    return longest

# Time complexity is O(n) since as we're iterating through the string, we are looking for the max of the dictionary values,
# where it would usually be take O(n) time but the set of characters that may be keys in the dictionary are all uppercase English letters
# which there are only 26 of them, thus O(26*n) which is amortized O(n)
# Space complexity is O(1) since for the same reason there can at most only be 26 key-value pairs, which is amortized constant time 