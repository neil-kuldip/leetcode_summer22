# 62. Unique Paths
# Difficulty: Medium

# Prompt
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
# The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# Thought Process 
# This problem is very familar in that it was the topic of discussion for 2D array dynamic programming
# Easily can do DFS for each path and update a counter to be returned
# Used neetcode video for this solution since I was stubborn for this one --> https://www.youtube.com/watch?v=IlEsdxuD4lY
# Idea is to basically create a matrix with one more row and column than the inputs provided and traverse 
# the matrix backwards updating the values with number of paths to get to the target since each succeeding value contains how many ways from there
# to get to the end
import typing as *

def uniquePaths(self, m: int, n: int) -> int:
    paths = [[0 for x in range(n+1)] for y in range(m+1)]
    paths[m-1][n-1] = 1
    
    for row in range(m-1, -1, -1):
        for col in range(n-1, -1, -1):
            if row == m-1 and col == n-1:
                continue
            paths[row][col] = paths[row+1][col] + paths[row][col+1]
    
    return paths[0][0]

# Time complexity is O(mn) to create the matrix and then iterate through it
# Space complexity is O(mn) to make the matrix in memory