# 142. Linked List Cycle II
# Difficulty: Medium

# Prompt
# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). 
# It is -1 if there is no cycle. Note that pos is not passed as a parameter.
# Do not modify the linked list.

# Thought Process (great resource: https://www.codingninjas.com/codestudio/library/floyds-cycle-finding-algorithm)
# Since we're on the topic of cycles in linked lists again --> Floyd's Cycle Detection Algorithm
# However this problem was hard in that I needed a refresher on how to detect where the cycle began. Here's what I understand:
    # Let's have three arbitary variables: x, y, z, where:
        # x is the number of nodes before the cycle begins
        # y is the number of nodes in the cycle before the pointers meet
        # z is the number of nodes between the meeting point and the start of the cycle
    # The distance traveled by the slow pointer until the meeting point can be described as x + y
    # Distance traveled by fast pointer is (x + y + z) + y = x + 2y + z
    # From the scope of the algo, we know fast pointer travels 2x the speed of slow pointer and time is constant when they both meet so:
        # 2(x + y) = x + 2y + z
        # 2x + 2y = x + 2y + z
        # x = z, therefore the cycle begins when both the slow pointer and fast pointer meet if the slow pointer starts from head and fast pointer starts from the meeting point
    # Since the above explanation doubled the speed of the slow pointer to match the fast pointer this means both needs to travel at the same speed to find the start of the cycle
import typing as *

def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if fast is None or fast.next is None:
        return None

    slow = head
    while (slow != fast):
        slow = slow.next
        fast = fast.next

    return slow

# Time complexity is O(n) since we are making two iterations of the list
# Space complexity is O(1) since are making two pointers in memory for the algorithm 