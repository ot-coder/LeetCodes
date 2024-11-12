# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
            slow, fast = head, head
            while  fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                 #The equivalent of nesting tortoise and hare in another tortoise and hare. or should i say tortoise and tortoise hahaha   
                    slow2 = head
                    while slow2 != slow:
                        slow = slow.next
                        slow2 = slow2.next
                    return slow
            return None