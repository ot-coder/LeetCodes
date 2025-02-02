# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == None: return 

        def flatten_lists(lists):
            flat_list = []
            for head in lists:
                current = head
                while current:
                    flat_list.append(current.val)
                    current = current.next
            return flat_list

        flat_list = flatten_lists(lists)

        #O(n)
        heapq.heapify(flat_list)

        #return flat_list was wrong

        dummy = ListNode(0)
        current = dummy

        
        #O(nlog(n))
        while flat_list:
            minimum = heapq.heappop(flat_list)
            current.next = ListNode(minimum)
            current = current.next

        return dummy.next