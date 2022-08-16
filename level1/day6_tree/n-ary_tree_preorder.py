# 589. N-ary Tree Preorder Traversal
# Difficulty: Easy

# Prompt
# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value

# Thought Process 
# Preorder --> Visit root then the children (left to right) using DFS
# Try to go for an iterative approach to avoid memory usage on the call stack
# Create a stack and append the root, from there append the root's children in reverse order so the top of the stack is always the leftmost child
import typing as *

def preorder(root: 'Node') -> List[int]:
    if root is None:
        return []
    
    traversal = []
    stack = []
    stack.append(root)
    
    while stack:
        currNode = stack.pop()
        if currNode is None:
            continue
        traversal.append(currNode.val)
        for child in range(len(currNode.children)-1, -1, -1):
            stack.append(currNode.children[child])
    
    return traversal

# Time complexity is O(n) for the number of nodes in the n-ary tree
# Space complexity is O(n) since even at the worst cases we are pushing all n elements in tree traversal before popping