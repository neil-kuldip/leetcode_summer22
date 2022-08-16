# 21. Merge Two Sorted Lists
# Difficulty: Easy

# Prompt
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Thought Process
# Original attempted idea was to still use dummy head but manipulate the lists so they can be pointed to each other in sorted order instead of appending them one by one to the sorted list
# While the first idea works on lists of the same length, it makes it harder to do the comparisons after the inital while loop
# Referred to geeskforgeeks to double check on the implementation, where this solution easily check the values at each list itr to determine which the order to append
import typing as *

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    
    # Create iterators for each of the linked lists
    currList1, currList2 = list1, list2
    
    # Initialize the start of the combined sorted list
    dummyHead = ListNode("dummy")
    sortedPtr = dummyHead

    # Iterating through both lists and realigning the nodes at the current end of the sorted list
    while currList1 and currList2:
        if currList1.val < currList2.val:
            sortedPtr.next = currList1
            currList1 = currList1.next
        else:
            sortedPtr.next = currList2
            currList2 = currList2.next
        sortedPtr = sortedPtr.next
    
    # Getting every node, especially when the list lengths differ
    while currList1:
        sortedPtr.next = currList1
        currList1 = currList1.next
        sortedPtr = sortedPtr.next
    
    while currList2:
        sortedPtr.next = currList2
        currList2 = currList2.next
        sortedPtr = sortedPtr.next
    
    return dummyHead.next

# Time complexity is O(max(m, n)) where m is the length of list1 and n is the length of list2 since we need to still iterate the longer list in the second while loop to make the full sorted list
# Space is O(1) since we mainly rearrange the existing input list nodes to make the combined list in this algo 