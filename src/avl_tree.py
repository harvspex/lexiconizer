from abc import ABC, abstractmethod

# TODO: Could refactor some methods for elegance/readability
# TODO: Add docstrings

class AVLNode:
    def __init__(self, data: object):
        self.data: object = data
        self.left: AVLNode = None
        self.right: AVLNode = None
        self.height: int = 0

class AVLTree(ABC):
    """
    An AVL tree. Contains methods to balance nodes.

    Variable name shorthand:
        g: grandparent node
        p: parent node
        c: child node
    """
    def __init__(self):
        self.root: AVLNode = None

    @abstractmethod
    def insert_element(self, data: str): pass

    @abstractmethod
    def traverse_inorder(
        local_root: AVLNode,
        sorted_list: list,
        one_char_words: list,
        nested_word_lists: list
    ): pass

    @staticmethod
    def set_node_height(local_root: AVLNode):
        left = local_root.left
        right = local_root.right
        left_height = -1 if left is None else left.height
        right_height = -1 if right is None else right.height

        if left_height >= right_height:
            local_root.height = left_height + 1
        else:
            local_root.height = right_height + 1

    @staticmethod
    def right_rotation(g: AVLNode):
        p = g.left
        rc = p.right
        p.right = g
        g.left = rc
        AVLTree.set_node_height(g)
        return p

    @staticmethod
    def left_rotation(g: AVLNode):
        p = g.right
        lc = p.left
        p.left = g
        g.right = lc
        AVLTree.set_node_height(g)
        return p

    @staticmethod
    def right_left_rotation(g: AVLNode):
        p = g.right
        g.right = AVLTree.right_rot(p)
        return AVLTree.left_rot(g)

    @staticmethod
    def left_right_rotation(g: AVLNode):
        p = g.left
        g.left = AVLTree.left_rot(p)
        return AVLTree.right_rot(g)

    @staticmethod
    def get_height(subtree: AVLNode):
        return -1 if subtree == None else subtree.height

    @staticmethod
    def get_height_diff(node: AVLNode):
        left_height = AVLTree.get_height(node.left)
        right_height = AVLTree.get_height(node.right)
        return left_height - right_height

    @staticmethod
    def rebalance(local_root: AVLNode):
        difference = AVLTree.get_height_diff(local_root)

        if difference == 2:
            if AVLTree.get_height_diff(local_root.left) == -1:
                local_root = AVLTree.left_right_rotation(local_root)
            else:
                local_root = AVLTree.right_rotation(local_root)

        elif difference == -2:
            if AVLTree.get_height_diff(local_root.right) == 1:
                local_root = AVLTree.right_left_rotation(local_root)
            else:
                local_root = AVLTree.left_rotation(local_root)

        return local_root
