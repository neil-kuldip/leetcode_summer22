# 274. Word Break
# Difficulty: Medium

# Prompt
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Thought Process
# Honestly this problem gave a lot me many issues since my mind was focusing on a DFS approach to check each susbtring of the input string 
# This problem had me thinking of word search and using tries to quickly find the words, although this wasn't better than using sets but I wanted to try it for practice
# My solution was time exceeded so I later decided to find the more efficient solution
import typing as *

class TrieNode:
    def __init__(self, char='', isEnd=True):
        self.char = char
        self.children = {}
        self.isEnd = isEnd
    
    def insert(self, word):
        curr = self
        for ch in word:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                curr.children[ch] = TrieNode(ch, False)
                curr = curr.children[ch]
        curr.isEnd = True
    
    def search(self, word):
        curr = self
        for ch in word:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return False
        return True if curr.isEnd else False

def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    if len(wordDict) == 1:
        return True if wordDict[0] == s else False
    
    root = TrieNode()
    for word in wordDict: # O(n) for length of the wordDict
        root.insert(word) # 0(k) for average length of each word
    
    def checkString(s):
        if len(s) == 0:
            return True
        for idx in range(len(s)): # O(s) where s is the length of the string
            if root.search(s[:idx+1]): # O(s)
                if checkString(s[idx+1:]): # O(s^2) call stack space 
                    return True
        return False
    
    return checkString(s)

# Time complexity is O(nk + s^2) for inserting each word in the trie and doing the for loop where we check if the word exists
# Space complexity is O(s) for the recursive call stack made by the for loop 

# Better solution --> https://www.youtube.com/watch?v=Sx9NNgInc3A
# Thoughts
# I knew after the recursive solution I came up had redundant steps that could have been clarified with a dynamic programming but I wasn't sure how to proceed
# There is probably a better utilization for the trie but I was thinking sets made more sense in this context
# This solution fixes the problem of recursive calls by storing the previous recursive call results to be referenced later in determining if the current substring fits the description
# Reminds me of jump game and frog jump solution, trend: recursion to dynamic programming if possible (space tradeoff to reduce time)

def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    dp = [False for _ in range(len(s)+1)]
    dp[0] = True
    wordSet = set(wordDict)
    for start in range(len(s)):
        if not dp[start]: continue
        for i in range(start+1, len(s)+1):
            if s[start:i] in wordSet:
                dp[i] = True
    return dp[-1]

# Time complexity is O(s^2), where we are checking if each substring exists in the set, which takes constant time within the double for loop
# Space complexity is O(s + n) for the length of the wordDict being converted to a set and the length of the string for the dp list


