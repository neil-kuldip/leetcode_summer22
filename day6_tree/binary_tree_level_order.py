# 102. Binary Tree Level Order Traversal
# Difficulty: Medium

# Prompt
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Thought Process 
# Level order --> BST with a queue for iterative apporach
# Since the output requires a sublist for each element in the same order, we need to keep track the level of each element we traverse to
# Keep more information in a data structure --> Tuples (first val is the node, second val is the level val)
# When appending to the queue, just +1 on the current node's level to its children
import typing as *

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []
    
    queue = [(root, 0)]
    traversal = dict()
    
    while queue:
        currNode, level = queue.pop(0)
        if currNode is None:
            continue
        if level not in traversal:
            traversal[level] = [currNode.val]
        else:
            traversal[level].append(currNode.val)
        queue.append((currNode.left, level+1))
        queue.append((currNode.right, level+1))
    
    return list(traversal.values())

# Time complexity is O(n) for the number of nodes in the tree and converting the traversal dictionary values into a list
# Space complexity is O(n) since we are creating a hastable and queue in memory to do level order traversal and get elements in sublists by level