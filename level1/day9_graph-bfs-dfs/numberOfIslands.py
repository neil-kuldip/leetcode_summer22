# 200. Number of Islands
# Difficulty: Medium

# Prompt
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# Thought Process
# This was a refresher from a previous time when I did this problem, but interesting since we only count islands once and find connectiong neighbor land of each island 
# DFS since islands can be in weird shapes so finding abnormal long paths makes sense for this type of algo
# Must have a visited array to not process through the same cells again
import typing as *

def numIslands(self, grid: List[List[str]]) -> int:
    visited = [[False for _ in range(len(grid[0]))] for __ in range(len(grid))]
    stack = []
    islandCounter = 0
    
    def landValid(grid, row, col, visited):
        if row < 0 or row >= len(grid):
            return False
        if col < 0 or col >= len(grid[0]):
            return False
        return not visited[row][col]
        
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if not landValid(grid, row, col, visited) or grid[row][col] == "0":
                continue
            stack.append((row, col))
            while stack:
                currRow, currCol = stack.pop()
                if not landValid(grid, currRow, currCol, visited):
                    continue
                visited[currRow][currCol] = True
                if grid[currRow][currCol] == "0":
                    continue
                stack.append((currRow-1, currCol)) # Top
                stack.append((currRow+1, currCol)) # Bottom
                stack.append((currRow, currCol-1)) # Left
                stack.append((currRow, currCol+1)) # Right
            islandCounter += 1
    
    return islandCounter
                
# Time complexity is O(mn) since with the double for loop we are getting to every cell in the grid either through this iteration or through DFS
# Space complexity is O(mn) for the visiting matrix to keep track of cells we have visited