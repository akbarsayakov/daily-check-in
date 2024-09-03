class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = collections.deque([root])
        res = []

        while q:
            total = 0
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node:
                    total = total + node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            res.append(total / n)
        return res