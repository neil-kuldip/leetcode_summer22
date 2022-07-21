# 205. Isomorphic Strings
# Difficulty: Easy

# Prompt
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.

# Thought Process
# Keyword: Characters focused in strings --> Hashtable
# Utilizing the fact that hashtables are key-value pairs, it's a great use for one thing as a key to be mapped or translated to another character
# Only case that originally came to mind to look for was if a key was mapped to different character later in the string
# Tried implementing it one way where the mapping goes both ways to improve time complexity (i.e. 'a' -> 'b' and 'b' -> 'a') but that doesn't account for many test cases

from typing import *

def isIsomorphic(s: str, t: str) -> bool:
    # If both strings are not the same size, they cannot be isomorphic
    if (len(s) != len(t)):
        return False
    
    # Two conditions:
    # If two keys map to the same character 
    # If one key maps to two or more different characters
    
    mapping = {}
    for idx, ch in enumerate(s):
        if ch not in mapping:
            if t[idx] in mapping.values():
                return False
            mapping[ch] = t[idx]
        else:
            if mapping[ch] != t[idx]:
                return False
    return True

# Time complexity is O(n^2) since although we are iterating through the s and t strings to build the hash table, in the worst case if all characters are unique, 
# we are checking for exisiting value membership in the dictionary values. This takes O(n) time alone
# Space complexity is O(n) for that we build a hash table in memory to keep track of the mapping and see if any character mapping violates the two conditions identified  
