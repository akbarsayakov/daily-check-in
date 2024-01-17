class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        myMap = {None: None}
        curr = head
        
        while curr:
            copyNode = Node(curr.val)
            myMap[curr] = copyNode
            curr = curr.next
        
        curr = head
        while curr:
            copyNode = myMap[curr]
            copyNode.next = myMap[curr.next]
            copyNode.random = myMap[curr.random]
            curr = curr.next
        
        return myMap[head]
        