# 876. Middle of the Linked List
# Difficulty: Easy

# Prompt
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Thought Process
# Lists --> Pointers for iteration 
# This question was one that was in my mind when I learned of Floyd's Cycle Detection Algorithm
# Concept goes that since the fast pointer travels 2x fast the speed of the slow pointer, once the fast pointer reaches the end of the list, 
# the slow pointer has only reached the middle of said list
import typing as *

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    # Floyd's Cycle Detection Algorithm
    # Fast pointer will always be iterating the list twice as fast as the slow pointer
    # That means when the fast pointer gets to the end, the slow pointer will only have reached the middle
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Time complexity is O(n) for the fast pointer to get to the end of the list
# Space complexity is O(1) since we are only making two pointers in memory
