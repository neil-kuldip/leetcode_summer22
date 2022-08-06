# 299. Bulls and Cows
# Difficulty: Medium

# Prompt
# You are playing the Bulls and Cows game with your friend.
# You write down a secret number and ask your friend to guess what the number is. 
# When your friend makes a guess, you provide a hint with the following info:
# The number of "bulls", which are digits in the guess that are in the correct position.
# The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.
# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

# Thought Process 
# OH SNAP IS THIS THE ORIGINAL WORDLE OR DID WORDLE COME FIRST?? Similar concept to Wordle, which helps understanding the problem's context
# Occurences and positioning matter --> Occurences think of hashtable, positioning --> probably set the values of the table to be a set for easy membership lookup
# Original idea --> Set up hash table and check for bulls as we go but reconsidered since that would mean checking the idx value for guess string and not including the idx value in the table if bull
# Prompted to first iterate through secret and make the table and then iterate through guess to check if the char is even in the guess and then search in the char's hash table value to find the index
# to add to cows
# Not optimized solution but using python's dictionary is better average space than using a set 26 character hash table for space in memory
import typing as *

def getHint(secret: str, guess: str) -> str:
    secretHash = {}
    guessHash = {}
    for itr, val in enumerate(secret):
        if val in secretHash:
            secretHash[val].add(itr)
        else:
            secretHash[val] = set()
            secretHash[val].add(itr)
            
    bulls, cows = 0, 0
    for itr, val in enumerate(guess):
        if val in secretHash:
            if val not in guessHash:
                guessHash[val] = 1
            else:
                guessHash[val] += 1
            if itr in secretHash[val]:
                bulls += 1
                secretHash[val].remove(itr)
                guessHash[val] -= 1
    
    for key in guessHash:
        if guessHash[key] < len(secretHash[key]):
            cows += guessHash[key]
        else:
            cows += len(secretHash[key])
        
    return f'{bulls}A{cows}B'
                
# Time complexity is O(n^2) if we consider the size of secret and guess to be n size, where we're iterating both secret and guess in linear time but Python's set add and remove functions in the worst case 
# takes O(n) time in case of collisions when there's a high load factor. Thus these functions are called on each value in the string, resilting in possible quadratic time but average linear time
# Space complexity is O(n) since we are using space in memory for both hash tables in memory
# Note: possible optimization thorugh the use of one less hash table and storing counts easier in the first hash table

# Optimization
# I had honestly overthough this problem since I was thinking it was important to store to position since position mattered but we only need to know position for the bulls
# Also creating a guessCopy skipped my mind since I was thinking an array would be horrible for lookup space but realized lookup given index is always constant time and the other lookup is from the dictionary
def getHint(secret: str, guess: str) -> str:
    secretHash = {}
    guessCopy = [x for x in guess]
    bulls, cows = 0, 0
    for idx, val in enumerate(secret):
        if guess[idx] == val:
            bulls += 1
            guessCopy[idx] = None
        else:
            if val in secretHash:
                secretHash[val] += 1
            else:
                secretHash[val] = 1
    
    for idx, val in enumerate(guessCopy):
        if not val:
            continue
        if val in secretHash and secretHash[val] > 0:
            cows += 1
            secretHash[val] -= 1
        
    return f'{bulls}A{cows}B'

# Time complexity is O(n) since we are just iterating over both strings of size n and updating the hash table and variables along with creating the array for guess
# Space complexity is O(n) since even though we are using one less hash table, we are using an array for the guess string to skip in interating if we had a match in the secret string iteration

