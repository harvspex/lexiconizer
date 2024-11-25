from avl_tree import AVLNode, AVLTree
from dataclasses import dataclass

@dataclass
class Word:
    spelling: str
    neighbours = []
    frequency = 1
    pointer = 0 # Used in neighbours_same_1()

    def __eq__(self, other):
        if isinstance(other, str):
            return self.spelling == other

        if isinstance(other, Word):
            return self.spelling == other.spelling

        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, str):
            return self.spelling < other

        if isinstance(other, Word):
            return self.spelling < other.spelling

        return NotImplemented

    def __str__(self):
        return f"{self.spelling} {self.frequency} {self.neighbours}\n"

class LexiconTree(AVLTree):
    def insert_element(self, data):
        word_data = Word(data)

        if self.root is None:
            self.root = AVLNode(word_data)
            return
            
        p = self.root
        while True:
            if word_data == p.data:
                p.data.frequency += 1 # Increment data frequencey if data already in tree
                break
            elif p.left != None and word_data <= p.data:
                p = p.left
                continue
            elif p.right != None and word_data > p.data:
                p = p.right
                continue
            elif word_data <= p.data:
                p.left = AVLNode(word_data)
                new_local_root = self.rebalance(p.left)
                self.set_node_height(new_local_root)
                break
            else:
                p.right = AVLNode(word_data)
                new_local_root = self.rebalance(p.right)
                self.set_node_height(new_local_root)
                break


    # Traverses tree inorder and:
    # 1. Appends word to alphabetically 1 list
    # 2. Appends word to nested list in same_0 by word length, then char 0
    # 3. Appends word to nested list in same_1 by word length, then char 1, then char 0
    def traverse_inorder(self, local_root, sorted_lst, same_0, same_1):

        g = lambda c: ord(c) - ord('a')

        if local_root is not None:
            self.traverse_inorder(local_root.left, sorted_lst, same_0, same_1)
            
            word = local_root.data
            spelling = word
            length = len(spelling) - 1
            idx_0 = g(spelling[0])

            sorted_lst.append(word)    

            self.add_to_inner(word, same_0, length, idx_0)

            if length > 0:
                idx_1 = g(spelling[1])
                self.add_to_inner(word, same_1, length, idx_1, idx_0)

            self.traverse_inorder(local_root.right, sorted_lst, same_0, same_1)

    # Iteratively nests lists at each index in n, then appends word to deepest list.
    def add_to_inner(word, lst, *n):
        for i in n:
            try:
                lst = lst[i]
            except IndexError:
                for _ in range(len(lst), i+1):
                    lst.append([])
                lst = lst[i]
        lst.append(word)