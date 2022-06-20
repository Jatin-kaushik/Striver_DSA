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
        self.stc = []
        def postorder(root):
            if root:
                postorder(root.left)
                postorder(root.right)
                self.stc.append(root.val)
        postorder(root)
        return self.stc
res =  Solution()
ans = res.postorderTraversal(a)
print(ans)