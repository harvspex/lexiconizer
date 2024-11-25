from abc import ABC, abstractmethod

# TODO: Add type hints
# TODO: Make most methods static

class AVLNode:
    def __init__(self, data):
        self.data: object = data
        self.left: AVLNode = None
        self.right: AVLNode = None
        self.height: int = 0

class AVLTree(ABC):
    """An AVL tree. Contains methods to balance nodes."""
    def __init__(self):
        self.root: AVLNode = None

    # TODO: add args
    # NOTE: Plausibly slightly slower. Could get rid of the abstract methods
    @abstractmethod
    def insert_element(self, data): pass

    @abstractmethod
    def traverse_inorder(self, local_root, sorted_lst, same_char_0, same_char_1): pass

    def set_node_height(self, local_root: AVLNode):
        left = local_root.left
        right = local_root.right
        left_height = -1 if left is None else left.height
        right_height = -1 if right is None else right.height

        if left_height >= right_height:
            local_root.height = left_height + 1
        else:
            local_root.height = right_height + 1

    def right_rotation(self, g: AVLNode):
        p = g.left
        rcp = p.right
        p.right = g
        g.left = rcp
        self.set_node_height(g)
        return p

    def left_rotation(self, g: AVLNode):
        p = g.right
        lcp = p.left
        p.left = g
        g.right = lcp
        self.set_node_height(g)
        return p

    def right_left_rotation(self, g: AVLNode):
        p = g.right
        g.right = self.right_rotation(p)
        return self.left_rotation(g)

    def left_right_rotation(self, g: AVLNode):
        p = g.left
        g.left = self.left_rotation(p)
        return self.right_rotation(g)

    def get_height_diff(self, node: AVLNode):
        if node.left == None:
            left_height = -1
        else:
            left_height = node.left.height
        
        if node.right == None:
            right_height = -1
        else:
            right_height = node.right.height
        
        return left_height - right_height

    def rebalance(self, local_root):
        difference = self.get_height_diff(local_root)

        if difference == 2:
            if self.get_height_diff(local_root.left) == -1:
                local_root = self.left_right_rotation(local_root)
            else:
                local_root = self.right_rotation(local_root)

        elif difference == -2:
            if self.get_height_diff(local_root.right) == 1:
                local_root = self.right_left_rotation(local_root)
            else:
                local_root = self.left_rotation(local_root)

        return local_root
