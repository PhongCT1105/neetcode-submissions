# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    

    def merge(self, list1, list2):
        dummy = ListNode()
        curr1, curr2 = list1, list2
        curr_merge = dummy

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                curr_merge.next = curr1
                curr_merge = curr_merge.next
                curr1 = curr1.next
            else:
                curr_merge.next = curr2
                curr_merge = curr_merge.next
                curr2 = curr2.next
        while curr1:
            curr_merge.next = curr1
            curr_merge = curr_merge.next
            curr1 = curr1.next
        while curr2:
            curr_merge.next = curr2
            curr_merge = curr_merge.next
            curr2 = curr2.next

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr_merge_list = []
        if not lists:
            return
            
        while len(lists) > 1:
            for i in range(0,len(lists),2):
                if i+1 < len(lists):
                    curr_merge = self.merge(lists[i], lists[i+1])
                    curr_merge_list.append(curr_merge)
                else:
                    curr_merge_list.append(lists[i])

            lists = curr_merge_list
            curr_merge_list = []
        

        return lists[0]