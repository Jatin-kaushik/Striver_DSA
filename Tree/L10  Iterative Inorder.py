# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.list = []
        self.stc = []
        # def inorder(root):
        #     if root == None: return
        #     inorder(root.left)
        #     self.list.append(root.val)
        #     inorder(root.right)
        # inorder(root)
        node = root
        while True:
            if node != None:
                self.stc.insert(0, node)
                node = node.left
            else:
                if len(self.stc) == 0: break
                node = self.stc.pop(0)
                self.list.append(node.val)
                node = node.right
        return self.list
    