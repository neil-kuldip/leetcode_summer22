# 274. H-Index
# Difficulty: Medium

# Prompt
# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return compute the researcher's h-index.
# According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n papers have at least h citations each, and the other n − h papers have no more than h citations each.
# If there are several possible values for h, the maximum one is taken as the h-index.

# Thought Process
# This problem relies on being able to determine if there are h elements that each has h properties and the rest doesn't, but since we don't rely on the original index 
# of each element it would be better to sort the array and keep count as we iterate the sorted array
# Since h needs to be papers that have at LEAST h citations and the rest is AT MOST, we need to decrement downwards to compare with the itr value
# Took me time to understand this but writing it down in this fashion helped understand incrementing forwards wouldn't get the max h value
# Sorting in-place or sorting to a copy of the input is the trade off

def hIndex(self, citations: List[int]) -> int:
    citations.sort()
    h = len(citations)
    count = 0
    while h > 0 and citations[h-1] >= len(citations) - h + 1:
        count += 1
        h -= 1
    return count

# Time complexity is O(n^2) since we are using in=place sorting
# Space complexity is O(1) since we modified the argument array for this algo

# Alternative using O(nlogn) time and O(n) space for using the python's sorting implementation to a new copy of the input array

# Further optimization was hinted at in the sucessor question to this problem about using a modified bianry search since the array will be sorted in the algorithm
# Will consider fixing this implementation, but in this problem since the input isn't guaranteed to be sorted this doesn't affect the overall amortized time complexity