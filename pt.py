"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def inOrder(root):

    if root!=None:
        inOrder(root.left, end=' ')
        print(root.info),
        inOrder(root.right)

def preOrder(root):
    if root != None:
        print(root.info, end=' '),
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root !=None:
        postOrder(root.left)
        postOrder(root.right)
        print(root.info, end=' ')
