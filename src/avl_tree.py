# TODO: Remove lexicon specific methods from AVL tree. Create a subclass that handles lexicons.
# Alternatively make it more specific to lexicons (e.g., instead of data attribute, just have word attributs in AVLNode)
# Add type hints for all args.
# Make code more DRY.

class Word:
    def __init__(self, spelling):
        self.spelling = spelling
        self.neighbours = []
        self.frequency = 1
        self.here = 0 # Used in neighbours_same_1()

    def __str__(self):
        return f"{self.spelling} {self.frequency} {self.neighbours}\n"

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

class AVLTree:
    def __init__(self):
        self.root = None

    # Modified to increment data frequencyuency if data already in tree.
    def insert_element(self, data):
        if self.root is None:
            self.root = AVLNode(Word(data))
            return
            
        p = self.root
        while True:
            if data == p.data.spelling:
                p.data.frequency += 1
                break
            elif p.left != None and data <= p.data.spelling:
                p = p.left
                continue
            elif p.right != None and data > p.data.spelling:
                p = p.right
                continue
            elif data <= p.data.spelling:
                p.left = AVLNode(Word(data))
                new_local_root = self.rebalance(p.left)
                self.set_node_height(new_local_root)
                break
            else:
                p.right = AVLNode(Word(data))
                new_local_root = self.rebalance(p.right)
                self.set_node_height(new_local_root)
                break

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

    # Traverses tree inorder and:
    # 1. Appends word to alphabetically 1 list
    # 2. Appends word to nested list in same_0 by word length, then char 0
    # 3. Appends word to nested list in same_1 by word length, then char 1, then char 0
    def inorder_list(self, local_root, sorted_lst, same_0, same_1):

        g = lambda c: ord(c) - ord('a')

        if local_root is not None:
            self.inorder_list(local_root.left, sorted_lst, same_0, same_1)
            
            word = local_root.data
            spelling = word.spelling
            length = len(spelling) - 1
            idx_0 = g(spelling[0])

            sorted_lst.append(word)    

            self.add_to_inner(word, same_0, length, idx_0)

            if length > 0:
                idx_1 = g(spelling[1])
                self.add_to_inner(word, same_1, length, idx_1, idx_0)

            self.inorder_list(local_root.right, sorted_lst, same_0, same_1)

    # Iteratively nests lists at each index in n, then appends word to deepest list.
    def add_to_inner(word, lst, *n):
        for i in n:
            try:
                lst = lst[i]
            except:
                for _ in range(len(lst), i+1):
                    lst.append([])
                lst = lst[i]
        lst.append(word)