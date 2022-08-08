# 394. Decode String
# Difficulty: Medium

# Prompt
# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
# Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. 
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 

# Thought Process 
# This was a challenging problem, which means I should focus more on stack problems since after reviewing the accepted solutions I 
# never considered having only a single stack throughout the string iteration
# I thought that since we need to multiply each sequence by a factor k, split the factors and sequences into two seperate stacks 
# and append backwards using recursion on everything in-between brackets so we can evaluate them first and multiply by the factor in the parent
# I used recursion after getting stuck and noticing recursion as a relevant topic, so if repeated work in a single string --> recursion is an option
import typing as *

def decodeString(s: str) -> str:
    multi = []
    seqs = []
    lvls = 0
    subSeq = ""
    subMulti = ""
    result = ""
    for idx, val in enumerate(s):
        if val == "]":
            lvls -= 1
            if lvls == 0:
                seqs.append(decodeString(subSeq))
                if len(multi) < len(seqs):
                    multi.append(1)
                subSeq = ""
            else:
                subSeq += val
        elif val == "[":
            if len(subMulti) > 0:
                multi.append(int(subMulti))
                subMulti = ""
            if lvls > 0:
                subSeq += val
            lvls += 1
        elif lvls == 0:
            if val.isdigit():
                subMulti += val
            else:
                if len(subMulti) > 0:
                    multi.append(int(subMulti))
                    subMulti = ""
                seqs.append(val)
                if len(multi) < len(seqs):
                    multi.append(1)
        else:
            subSeq += val

    while multi:
        currMulti = multi.pop()
        currSeq = seqs.pop()
        newStr = ""
        for i in range(currMulti):
            newStr += currSeq
        result = newStr + result

    return result

# Time complexity is O(n^2) since althugh we are iterating through the s string, popping from each stack will take at most n times 
# and in each pop, we are creating a new string for the result O(n) each
# Space complexity is O(n) since in the woorst case we have n recursive stack calls with a max of n values in both stacks throughout the whole algorithm's duration
