class AVLNode:
    """
    A node for an AVL tree.

    Attributes:
        data (object): The data stored in the node, such as a Word object.
        left (AVLNode or None): The left child node.
        right (AVLNode or None): The right child node.
        height (int): The height of the node within the AVL tree.
    """
    def __init__(self, data: object):
        self.data: object = data
        self.left: AVLNode = None
        self.right: AVLNode = None
        self.height: int = 0