# 438. Find All Anagrams in a String
# Difficulty: Medium

# Prompt
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
# You may return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Thought Process 
# Anagrams --> Hash Table probably
# Find something in string --> Iteration with some tool, two pointer or sliding window
# Sliding window since rearrange letters of p into the window in s and compare hash tables
# Can update hash table with iteration and through comparison update output arr with index
import typing as *

def findAnagrams(self, s: str, p: str) -> List[int]:
    if len(p) > len(s):
        return []
    
    anagramIdx = []
    pHash = dict()
    winHash = dict()
    
    for itr in range(len(p)):
        if p[itr] not in pHash:
            pHash[p[itr]] = 1
        else:
            pHash[p[itr]] += 1
        if s[itr] not in winHash:
            winHash[s[itr]] = 1
        else:
            winHash[s[itr]] += 1
    
    if pHash == winHash:
        anagramIdx.append(0)
        if len(p) == len(s):
            return anagramIdx
    
    for itr in range(len(p), len(s)):
        if s[itr] not in winHash:
            winHash[s[itr]] = 1
        else:
            winHash[s[itr]] += 1
            
        winHash[s[itr-len(p)]] -= 1
        if winHash[s[itr-len(p)]] == 0:
            winHash.pop(s[itr-len(p)])
        
        if pHash == winHash:
            anagramIdx.append(itr-len(p)+1)
    
    return anagramIdx

# Time complexity is O(s) for the length of s to be iterated through
# Space complexity is O(s) since the output array in the worst case can nearly all the indicies 