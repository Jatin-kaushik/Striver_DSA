#Basically for loops se baar baar level pakad rhe hain

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        if root:
            queue.insert(0, root)
        res = []
        while queue:
            sz = len(queue)
            lorder = []
            for i in range(sz):
                e = queue.pop(-1)
                lorder.append(e.val)
                if e.left: queue.insert(0, e.left)
                if e.right: queue.insert(0, e.right)
            res.append(lorder)
        return res