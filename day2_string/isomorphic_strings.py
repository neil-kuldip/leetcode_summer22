# 205. Isomorphic Strings
# Difficulty: Easy

# Prompt
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.

# Thought Process
# TBD 

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