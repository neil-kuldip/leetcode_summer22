# 1046. Last Stone Weight
# Difficulty: Easy

# Prompt
# You are given an array of integers stones where stones[i] is the weight of the ith stone.
# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. 
# Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.
# Return the weight of the last remaining stone. If there are no stones left, return 0.

# Thought Process 
# So we are comparing the two largest values in an array and updating the value of the largest if both not equal and adding it back to the array --> Keeping track of the largest 
# The best data structure to keep track of the largest with updating values is a heap --> utilized as a priority queue
# That way each time we pop the two largest values from the top of the heap and append the smallest when not equal in value, we do not have to utilize or keep track of the sorting 
# In terms of time complexity it reduces the sorting and popping to logarithmic time and insertion to logarithmic, space using heapq libary should have the array be heapified in=place
import typing as *
import heapq as hq

def lastStoneWeight(stones: List[int]) -> int:
    for idx in range(len(stones)):
        stones[idx] *= -1
    hq.heapify(stones)
    
    while len(stones) > 1:
        y = hq.heappop(stones)
        x = hq.heappop(stones)
        if x != y:
            x, y = x*-1, y*-1
            y -= x
            y *= -1
            hq.heappush(stones, y)
            
        
    return stones[0]*-1 if stones else 0

# Time complexity is O(nlogn) since after heapifying the array in linear time via heapq library, the while loop keep going until there is 1 or 0 stones left with heappush and heappop taking O(logn) 
# time for each iteration
# Space complexity is O(1) since we heapified and updated the input array

        