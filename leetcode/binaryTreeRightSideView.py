class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([root])
        res = []

        while q:
            rightMost = None # track at each level
            n = len(q) # number of nodes at the current level
            print(n, 'length')

            for i in range(n):
                node = q.popleft()
                if node:
                    rightMost = node
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            if rightMost:
                res.append(rightMost.val)

        return res