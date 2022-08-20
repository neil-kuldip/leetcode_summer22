# 403. Frog Jump
# Difficulty: Hard

# Prompt
# A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. 
# The frog can jump on a stone, but it must not jump into the water.
# Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. 
# Initially, the frog is on the first stone and assumes the first jump must be 1 unit.
# If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. 
# The frog can only jump in the forward direction.

# Thought Process
# Keywords/Concepts: Stones can skip other stones, check to see if there is a path --> Dynamic Programming
# Similar to Jump Game, but greedy approach won't work since the value of k from one stone to the next will be different
# from another previous stone to the same next stone
# Decided to make a dp array to store the highest k but ran into this test case: [0,1,3,6,10,13,15,18]
# The problem is although we can collect the highest k for any index, the highest may not be the best way to proceed
# Thought about how to store the best one to proceed, but landed on making a sets for the values of each dict key
from typing import *

def canCross(self, stones: List[int]) -> bool:
    dp = [{-1} for _ in range(len(stones))]
    dp[0] = {0, 1}

    for idx in range(len(stones)):
        if -1 in dp[idx]: continue
        idx2 = idx + 1
        while idx2 < len(stones):
            if stones[idx2] - stones[idx] in dp[idx]:
                k = stones[idx2] - stones[idx]
                if -1 in dp[idx2]:
                    dp[idx2] = {k-1, k, k+1}
                else:
                    dp[idx2].add(k)
                    dp[idx2].add(k-1)
                    dp[idx2].add(k+1)
            idx2 += 1
    return False if -1 in dp[-1] else True

# Analysis
# Time complexity: TBD
# Space complexity: TBD