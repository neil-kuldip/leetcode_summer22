# 98. Validate Binary Search Tree
# Difficulty: Medium

# Prompt
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Thought Process 
# What are ways to validate a BST? We are given the rules for the BST and they're emphasizing the values of the nodes rather than the stucture. 
# General knowledge --> Have to traverse the tree but in which way? --> Inorder traversal should be in sorted order
# Can easily make an array of the inorder traversal and then iterate the array to check if the prev is smaller than current
import typing as *
def isValidBST(root: Optional[TreeNode]) -> bool:
    if root is None:
        return True
    stack = []
    traversal = []
    temp = root
    
    while temp or stack:
        while temp:
            stack.append(temp)
            temp = temp.left
        temp = stack.pop()
        traversal.append(temp.val)
        temp = temp.right
    
    if len(traversal) == 1:
        return True
    
    for itr in range(1, len(traversal)):
        if traversal[itr] <= traversal[itr-1]:
            return False
    
    return True

# Time complexity O(n) to get through all nodes in the tree and then iterate the list to check sorted order
# Space complexity O(n) since using extra memory to make traversal array
# Consideration for optimization
    # Since when we iterate we only care about the prev and the current value, we don't need an array just a variable
    # to store the prev value
    # Space would be less since we won't have two arrays with size n

    def isValidBST(root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        stack = []
        prevVal = None
        temp = root
        
        while temp or stack:
            while temp:
                stack.append(temp)
                temp = temp.left
            temp = stack.pop()
            if prevVal is None:
                prevVal = temp.val
            else:
                if prevVal >= temp.val:
                    return False
                prevVal = temp.val
            temp = temp.right
        
        return True  