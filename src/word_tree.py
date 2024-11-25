from avl_tree import AVLNode, AVLTree

class Word:
    """Word data class.
    Comparison operator overloading not used as it had significant impact on runtime."""
    def __init__(self, spelling):
        self.spelling: str = spelling
        self.neighbours: list[str] = []
        self.frequency: int = 1
        self.pointer: int = 0 # Used in neighbours_same_1()

    def __str__(self) -> str:
        return f"{self.spelling} {self.frequency} {self.neighbours}\n"

class WordTree(AVLTree):
    """Subclass of AVLTree containing specialised methods relating to the Word class.
    i.e. WordTree is used when AVLNode data is a Word object."""

    def __init__(self):
        super().__init__()

    def insert_element(self, data):
        """Inserts Word data into WordTree. Increments data frequency if data already in tree."""
        # NOTE: Before extracting Word(data) to a common attribute, check impact on performance
        # TODO: Could init WordTree with root note. This would remove the below comparison,
        # and could make insert_element a static method (maybe faster?)

        if self.root is None:
            self.root = AVLNode(Word(data))
            return
            
        p = self.root
        while True:
            if data == p.data.spelling:
                p.data.frequency += 1 # Increment data frequencey if data already in tree
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

    @staticmethod
    def traverse_inorder(local_root, sorted_lst, same_char_0, same_char_1):
        """Traverses tree inorder and:
            1. Appends word to alphabetically sorted list
            2. Appends word to list in same_char_0 nested by word length, then char 0
            3. Appends word to list in same_char_1 nested by word length, then char 1, then char 0"""

        g = lambda c: ord(c) - ord('a')

        if local_root is not None:
            WordTree.traverse_inorder(local_root.left, sorted_lst, same_char_0, same_char_1)
            
            word = local_root.data
            spelling = word.spelling
            length = len(spelling) - 1
            idx_0 = g(spelling[0])

            sorted_lst.append(word)    

            WordTree.add_to_inner(word, same_char_0, length, idx_0)

            if length > 0:
                idx_1 = g(spelling[1])
                WordTree.add_to_inner(word, same_char_1, length, idx_1, idx_0)

            WordTree.traverse_inorder(local_root.right, sorted_lst, same_char_0, same_char_1)

    @staticmethod
    def add_to_inner(word, lst, *n):
        """Iteratively nests lists at each index in n, then appends word to deepest list."""
        for i in n:
            try:
                lst = lst[i]
            except IndexError:
                for _ in range(len(lst), i+1):
                    lst.append([])
                lst = lst[i]
        lst.append(word)