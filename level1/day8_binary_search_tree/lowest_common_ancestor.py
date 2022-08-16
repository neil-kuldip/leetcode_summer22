# 235. Lowest Common Ancestor of a Binary Search Tree
# Difficulty: Easy

# Prompt
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that 
# has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Thought Process 
# Every two nodes has a path from the root, so there exists a common ancestor
# Ancestor --> find direct path, was thinking of doing inorder traversal but that seems like a higher time complexity than storing the path for a
# a search for each p and q
# Originally thought of using lists but thinking lookup for membership, better to use sets to see where they diff and update ancestor accordingly 
import typing as *

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    pPath, qPath = set(), set()
    
    def search(root, path, path2, target):
        curr = root
        ancestor = None
        path.add(curr)
        if curr in path2:
            ancestor = curr
            
        while curr.val != target.val:
            if curr.val > target.val:
                curr = curr.left
            else:
                curr = curr.right
            path.add(curr)
            if curr in path2:
                ancestor = curr
        return ancestor
        
    search(root, qPath, pPath, q)
    return search(root, pPath, qPath, p)

# Time complexity is O(n) since worst case is if the BST has a structure of a linked list, although average is O(log n)
# Space complexity is O(n) where in the worst case there would be two sets, pPath and qPath, of size n