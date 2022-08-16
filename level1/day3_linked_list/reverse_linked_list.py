# 206. Reverse Linked List
# Difficulty: Easy

# Prompt
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Thought Process
# Reverse --> Iteration or Stack
# Reversing a data stucture by elements can either be done by creating another data structure in memory and iterating 
# backwards or using another structure to aid in the reversal. 
# Since we have a singly linked list, we can't iterate backwards but we can use a stack to push each ListNode into the stack
# And then keep popping and changing it's next to the new list
import typing as *

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return head
    
    # Stack implementation
    # Start with a var to the head and iterating through the list and pushing the nodes into the stack
    # Remove next pointer for recently inserted node in the stack to avoid cycles
    # Make dummyhead for reversed list
    # While the stack isn't empty, pop the top of the stack and append to the reversed list
    # Return the next node of dummyhead
    
    stack = []
    currPtr = head
    while currPtr:
        stack.append(currPtr)
        currPtr = currPtr.next
        stack[-1].next = None
    
    dummyHead = ListNode("dummy")
    reverseItr = dummyHead
    
    while stack:
        currNode = stack.pop()
        reverseItr.next = currNode
        reverseItr = reverseItr.next
    
    return dummyHead.next

# Time complexity is O(n) for n being the length of the list and we are iterating through the list twice, 
# once for appending to stack and the next for emptying the stack to make the new list
# Space complexity is O(1) since we are only making a dummyHead pointer in memory and the rest is rearranging 
# the nodes from the input 