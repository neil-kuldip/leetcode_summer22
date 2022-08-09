# 692. Top K Frequent Words
# Difficulty: Medium

# Prompt
# Given an array of strings words and an integer k, return the k most frequent strings.
# Return the answer sorted by the frequency from highest to lowest. 
# Sort the words with the same frequency by their lexicographical order.

# Thought Process 
# Sorted by frequency --> Frequency can be calculated through a hashtable and sorted can either be done via sorted function w/ lambda expression or with a heap
# Since this is a great heap example question, I'm going to implement with heap since I need heap practice
# Although just sorting with the sorted function in reverse and getting the first k indicies would be faster 
import typing as *
import heapq as hq

def topKFrequent(words: List[str], k: int) -> List[str]:
    freq = {}
    for x in words:
        if x not in freq:
            freq[x] = (-1, x)
        else:
            freq[x] = (freq[x][0]-1, x)
            
    freq = list(freq.values())
    hq.heapify(freq)
    return [hq.heappop(freq)[1] for _ in range(k) ]

# Time complexity is O(klogn) since although we are iterating through the input array to create the frequency table, taking linear time to create a list from the table values and heapifying it, 
# the resulting array continues for k times and performing heappop which takes log(n) time for each iteration
# Space is O(n) since in the worst case every word in the list is unique so the size of the table would be 2n and the heap would be of size n
