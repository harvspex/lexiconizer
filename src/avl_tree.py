# TODO: Remove lexicon specific methods from AVL tree. Create a subclass that handles lexicons.
# Alternatively make it more specific to lexicons (e.g., instead of data attribute, just have word attributs in AVLNode)
# Add type hints for all args.
# Make code more DRY.

from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class AVLNode:
    data: object # TODO: test this
    left = None
    right = None
    height = 0

@dataclass
class AVLTree(ABC):
    root = None

    # TODO: add args
    @abstractmethod
    def insert_element(): pass

    @abstractmethod
    def traverse_inorder(): pass

    def set_node_height(self, local_root):
        left = local_root.left
        right = local_root.right
        left_height = -1 if left is None else left.height
        right_height = -1 if right is None else right.height

        if left_height >= right_height:
            local_root.height = left_height + 1
        else:
            local_root.height = right_height + 1

    def right_rotation(self, g):
        p = g.left
        rcp = p.right
        p.right = g
        g.left = rcp
        self.set_node_height(g)
        return p

    def left_rotation(self, g):
        p = g.right
        lcp = p.left
        p.left = g
        g.right = lcp
        self.set_node_height(g)
        return p

    def right_left_rotation(self, g):
        p = g.right
        g.right = self.right_rotation(p)
        return self.left_rotation(g)

    def left_right_rotation(self, g):
        p = g.left
        g.left = self.left_rotation(p)
        return self.right_rotation(g)

    def get_height_diff(self, node):
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
