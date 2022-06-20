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
        self.post = []
        if root:
            curr = root
        while curr != None or self.stc:
            if curr != None:
                self.stc.append(curr)
                curr = curr.left
            else:
                temp = self.stc[-1].right
                if temp == None:
                    temp = self.stc.pop(-1)
                    self.post.append(temp.val)
                    while self.stc and temp == self.stc[-1].right:
                        temp = self.stc.pop(-1)
                        self.post.append(temp.val)             
                else:
                    curr = temp
        return self.post       
res =  Solution()
ans = res.postorderTraversal(a)
print(ans)