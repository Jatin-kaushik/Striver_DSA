# use pair 1,2,3 to track the visitng nodes


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
a = TreeNode(1)
a.left = TreeNode(2)   
a.right = TreeNode(3) 
a.left.left = TreeNode(4)
a.left.right = TreeNode(5)
a.right.left = TreeNode(6)
a.right.left.right = TreeNode(7)
a.right.left.right.right = TreeNode(8)

class Solution:
    def maxdepth(self, root):
        if root == None:
            return 0
        lh = self.maxdepth(root.left)
        rh = self.maxdepth(root.right)
        return 1+ max(lh, rh)

ans = Solution()
res = ans.maxdepth(a)
print(res)