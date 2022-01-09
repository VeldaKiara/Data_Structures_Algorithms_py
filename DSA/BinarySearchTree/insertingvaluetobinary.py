#Create a class to hold the node in a BST
class Node:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None

#utility function to insert a new node into the BST

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right,key)
        else:
            root.left = insert(root.left, key)
    return root


#utility function to do inorder tree traversal 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
    
inorder(r)