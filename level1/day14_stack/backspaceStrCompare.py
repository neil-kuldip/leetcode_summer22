# 844. Backspace String Compare
# Difficulty: Easy

# Prompt
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

# Thought Process 
# Backspace for a string --> Stack implementation
# There's a possible solution in constant but I wasn't able to figure it out in the time frame
# Making two stacks and comparing each after iterating through each string and building each respective stack seemed like the most straightforward idea
# Since we need to remove the previous char before the '#', using stacks help, but now after seeing the relevant topics, it makes sense that two pointers would work
# Comparing two strings --> Two pointers are a viable solution, probably pointing to the ends of each string
import typing as *

def backspaceCompare(s: str, t: str) -> bool:
    sStack, tStack = [], []
    for idx, val in enumerate(s):
        if val != "#":
            sStack.append(val)
        elif sStack:
            sStack.pop()
    for idx, val in enumerate(t):
        if val != "#":
            tStack.append(val)
        elif tStack:
            tStack.pop()
            
    return sStack == tStack

# Time complexity is O(n) if n is the arbitrary sum of the length of s and t strings. Iterating through each string and iterating each stack for the final comparison
# Space complexity is O(n) since we are making two stacks of collective size n in memory for this algorithm