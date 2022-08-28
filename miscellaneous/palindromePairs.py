# 336. Palindrome Pairs
# Difficulty: Hard

# Prompt
# Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

# Thought Process
# This feels like a another application of a hash table just like in the two sum question, but what would be the keys and values of the dictionary?
# The words in the provided words argument list would work as the keys but I'm not sure how to proceed considering I need the rest of the algo to check the dictionary at some point
# This is where after some time, I implemented the brute force solution of using a double for loop and reversing the concatenated string to check if it's a palindrome 
# Needing to practice on working my way up to larger cases and edge cases are the thing since I was so focused on cases like: "abc" and "cba", but not "abc" and "" or "abcddd" and "cba"
import typing as *

def palindromePairs(self, words: List[str]) -> List[List[int]]:
    results = []
    for idx in range(len(words)): # O(n) where n is length of the list
        for idx2 in range(idx + 1, len(words)): # O(n) 
            if idx == idx2: continue # O(1)
            combine1 = words[idx] + words[idx2] # O(k^2) where k is the average number of chars in both words[idx] and words[idx2]
            combine2 = words[idx2] + words[idx] # O(k^2)
            if combine1 == combine1[::-1]: # O(k)
                results.append([idx, idx2])
            if combine2 == combine2[::-1]: # O(k)
                results.append([idx2, idx])
    return results

# Time complexity is O(k^2n^2) since we're using a double for loop to check each pair combination of words, but inside the nested for loop we are creating concatenated strings to be compared
# Space complexity is O(1) if not counting the results array, otherwise no additional memory used

# Better Solution Idea found here: --> https://dev.to/seanpgallivan/solution-palindrome-pairs-23j6

# Thoughts
# The part that was getting me as mentioned before was how to use the hash table idea, since I wasn't thinking of how the different cases vary for palindromes
# For cases where the word is an empty string, both "" + the second word and vise versa would be palindromes so a nested loop to account for that satisfies that case
# To check if the full reversed string is a palindrome was something I accounted for, but the partial string surprised me:
    # It didn't occur to me that for partial strings that makes a palindrome with another in the list, the remaining of the string should be itself a palindrome
# Biggest takeaway was that I should break down cases more to recognize the pattern and then proceed to address them
# It seems I am making progress since I recognized I can use a table, but by following the highlighted step above, I would've gotten to this solution
def palindromePairs(self, words: List[str]) -> List[List[int]]:
    results = []
    def isPalindrome(word):
        start, end = 0, len(word)-1
        while start < end:
            if word[start] != word[end]: return False
            start += 1
            end -= 1
        return True
    
    wordMap = { word : idx for idx, word in enumerate(words) }
    
    for idx, word in enumerate(words):
        if word == "":
            for idx2, val2 in enumerate(words):
                if idx2 == idx or not isPalindrome(val2): continue
                results.append([idx, idx2])
                results.append([idx2, idx])
            continue
        backwardWord = word[::-1]
        if backwardWord in wordMap and wordMap[backwardWord] != idx:
            results.append([idx, wordMap[backwardWord]])
        
        for idx2 in range(1, len(backwardWord)):
            backward1 = backwardWord[:idx2]
            backward2 = backwardWord[idx2:]
            if backward1 in wordMap and isPalindrome(backward2):
                results.append([wordMap[backward1], idx])
            if backward2 in wordMap and isPalindrome(backward1):
                results.append([idx, wordMap[backward2]])
    
    return results

# Time complexity is O(nk^2) where n is the length of the words list and k is the average length of the words in the list
# Space complexity is O(n) for the wordMap dictionary

