class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        temp = res

        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                temp = list1
                list1 = list1.next
            
            else: 
                temp.next = list2
                temp = list2
                list2 = list2.next
            
        if list1:
                temp.next = list1
        else:
                temp.next = list2
        return res.next