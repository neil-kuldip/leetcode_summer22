# 733. Flood Fill
# Difficulty: Easy

# Prompt
# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. 
# Replace the color of all of the aforementioned pixels with color.
# Return the modified image after performing the flood fill.

# Thought Process
# Adjacent nodes --> Some matrix cell traversal (BFS or DFS)
# This problem I have solved before twice and it was during practice of BFS and DFS
# Here either works but I prefer solving BFS for this problem since I believe it mimicks the behavior of a flood after a spill the most
# Getting to every valid neighbor will still take the same amount of time as DFS but this solution seems more intuitive to grasp
import typing as *

def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    # Storing original val of starting cell to be used for comparison
    pixelVal = image[sr][sc]
    
    # Tuples to store pixel properties accessed through BFS
    queue = [(sr, sc)]
    
    def inBounds(image, row, col):
        if row < 0 or row >= len(image):
            return False
        if col < 0 or col >= len(image[0]):
            return False
        return True
    
    # Implementing BFS
    while queue:
        curr = queue.pop(0)
        if not inBounds(image, curr[0], curr[1]) or image[curr[0]][curr[1]] == color or image[curr[0]][curr[1]] != pixelVal:
            continue
        image[curr[0]][curr[1]] = color
        queue.append((curr[0], curr[1]-1)) # Top
        queue.append((curr[0], curr[1]+1)) # Down
        queue.append((curr[0]-1, curr[1])) # Left
        queue.append((curr[0]+1, curr[1])) # Right
    
    return image

# Time complexity is O(mn) since in the worst case we would traverse to every cell given there are enough 4-directional valid neighbors to traverse every cell
# Space complexity is O(mn) for that we require a queue in memory to utilize BFS and in worst case hold at most n cells