class Node:
    def __init__(self, data = 0, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
root = Node(1)
root.left = Node(-50)
root.right = Node(50)
print(root.left.data , root.data, root.right.data)