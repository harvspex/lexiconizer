from abc import ABC, abstractmethod

# TODO: Extract AVLNode into separate file
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

class AVLTree(ABC):
    """
    Represents an AVL tree. Contains methods to balance nodes.

    An AVL tree is a self-balancing binary search tree. The tree ensures 
    balance to maintain efficient operations such as insertion, deletion, 
    and search. Balancing is achieved using rotations.

    Attributes:
        root (AVLNode or None): The root node of the AVL Tree.

    Variable Name Shorthand:
        g: Grandparent node
        p: Parent node
        c: Child node
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
        """
        Updates the height of a given node based on the heights of its children.

        Args:
            local_root (AVLNode): The node whose height is to be updated.
        """
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
        """
        Performs a right rotation on a subtree to restore AVL balance.

        Args:
            g (AVLNode): The root node of the subtree requiring rotation.

        Returns:
            AVLNode: The new local root node of the subtree after rotation.
        """
        p = g.left
        rc = p.right
        p.right = g
        g.left = rc
        AVLTree.set_node_height(g)
        return p

    @staticmethod
    def left_rotation(g: AVLNode):
        """
        Performs a left rotation on a subtree to restore AVL balance.

        Args:
            g (AVLNode): The root node of the subtree requiring rotation.

        Returns:
            AVLNode: The new local root node of the subtree after rotation.
        """
        p = g.right
        lc = p.left
        p.left = g
        g.right = lc
        AVLTree.set_node_height(g)
        return p

    @staticmethod
    def right_left_rotation(g: AVLNode):
        """
        Performs a right-left rotation on a subtree to restore AVL balance.

        Args:
            g (AVLNode): The root node of the subtree requiring rotation.

        Returns:
            AVLNode: The new local root node of the subtree after rotation.
        """
        p = g.right
        g.right = AVLTree.right_rot(p)
        return AVLTree.left_rot(g)

    @staticmethod
    def left_right_rotation(g: AVLNode):
        """
        Performs a left-right rotation on a subtree to restore AVL balance.

        Args:
            g (AVLNode): The root node of the subtree requiring rotation.

        Returns:
            AVLNode: The new local root node of the subtree after rotation.
        """
        p = g.left
        g.left = AVLTree.left_rot(p)
        return AVLTree.right_rot(g)

    @staticmethod
    def get_height(subtree: AVLNode):
        """
        Retrieves the height of a subtree.

        Args:
            subtree (AVLNode or None): The root nood of the subtree.

        Returns:
            int: The height of the subtree. Returns -1 if the subtree is None.
        """
        return -1 if subtree == None else subtree.height

    @staticmethod
    def get_height_diff(node: AVLNode):
        """
        Calculates the height difference (balance factor) of a node's children.

        Args:
            node (AVLNode): The node whose children's height difference is to be
                calculated.

        Returns:
            int: The difference between the heights of the left and right 
                children. Positive values indicate left-heavy, negative values 
                indicate right-heavy.
        """
        left_height = AVLTree.get_height(node.left)
        right_height = AVLTree.get_height(node.right)
        return left_height - right_height

    @staticmethod
    def rebalance(local_root: AVLNode):
        """
        Rebalances the subtree rooted at the given node, if necessary.

        Args:
            local_root (AVLNode): The root node of the subtree to rebalance.

        Returns:
            AVLNode: The new root node of the subtree after rebalancing.
        """
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
