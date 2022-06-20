# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        self.stc = []
        self.dfsres = []
        self.que = []
        self.bfsres = []
        def dfs(root):
            if root:
                self.stc.append(root)
            while self.stc:
                ele = self.stc.pop(-1)
                if ele.left:
                    self.stc.append(ele.left)
                # print(ele.val)
                self.dfsres.append(ele.val)
                if ele.right:
                    self.stc.append(ele.right)
        def bfs(root):
            if root:
                self.que.append(root)
            while self.que:
                ele = self.que.pop(0)
                if ele.left:
                    self.que.append(ele.left)
                self.bfsres.append(ele.val)
                if ele.right:
                    self.que.append(ele.right)
        dfs(root)
        bfs(root)
        return self.dfsres, self.bfsres
    
a = TreeNode(1)
a.left = TreeNode(2)    
a.left.left = TreeNode(3)
a.left.left.right = TreeNode(4)
a.left.left.right.right = TreeNode(5)
a.left.left.right.right.right = TreeNode(6)

a.right = TreeNode(7)
a.right.left = TreeNode(8)
# print(a.val, a.left.val, a.right.val)
res =  Solution()
ans = res.inorderTraversal(a)
print(ans)
