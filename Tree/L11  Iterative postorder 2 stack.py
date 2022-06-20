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
    def postorderTraversal(self, root):
        self.stc1 = []
        self.stc2 = []
        if root:
            self.stc1.append(root)
        while self.stc1:
            ele = self.stc1.pop(-1)
            if ele.left:
                self.stc1.append(ele.left)
            if ele.right:
                self.stc1.append(ele.right)
            self.stc2.append(ele.val)
        return self.stc2[::-1]
res =  Solution()
ans = res.postorderTraversal(a)
print(ans)