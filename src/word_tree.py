from src.avl_tree import AVLNode, AVLTree

# TODO: Add docstrings

class Word:
    """
    Word data class.
    """
    def __init__(self, spelling):
        self.spelling: str = spelling
        self.neighbours: list[str] = []
        self.frequency: int = 1
        self.pointer: int = 0 # Used for inserting words alphabetically into self.neighbours
    
    # Operator overloading not used as it had significant impact on runtime

    def __str__(self) -> str:
        return f"{self.spelling} {self.frequency} {self.neighbours}\n"

class WordTree(AVLTree):
    """
    Subclass of AVLTree containing specialised methods relating to the Word class.
    i.e. WordTree is used when AVLNode data is a Word object.
    """

    def __init__(self):
        super().__init__()

    def insert_element(self, data: str):
        """
        Inserts Word data into WordTree. Increments data frequency if data already in tree.
        """
        if self.root is None:
            self.root = AVLNode(Word(data))
            return

        p: AVLNode = self.root

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
    def g(c: str): return ord(c[0]) - ord('a')

    @staticmethod
    def traverse_inorder(
        local_root: AVLNode,
        sorted_list: list[Word],
        one_char_words: list[Word],
        nested_word_lists: list
    ):
        """
        Traverses tree inorder and:
            1. Appends word to alphabetically sorted list
            2. Appends word to nested_word_lists nested by: word length, then char 1, then char 0
            3. Appends one char words to one_char_words
        """

        if local_root is not None:
            WordTree.traverse_inorder(local_root.left, sorted_list, one_char_words, nested_word_lists)
            
            word = local_root.data
            spelling = word.spelling
            length = len(spelling) - 1
            idx_0 = WordTree.g(spelling[0])

            # Add word to sorted_list
            sorted_list.append(word)

            try:
                # Add word to nested_word_lists
                idx_1 = WordTree.g(spelling[1])
                WordTree.add_to_inner(word, nested_word_lists, length, idx_1, idx_0)
            
            except IndexError:
                # If word is one char, add word to one_char_words
                if len(spelling) == 1: # Should always be true
                    one_char_words.append(word)

            WordTree.traverse_inorder(local_root.right, sorted_list, one_char_words, nested_word_lists)

    @staticmethod
    def add_to_inner(word: Word, lst: list, *n: int):
        """Iteratively nests lists at each index in n, then appends word to deepest list."""
        for i in n:
            try:
                lst = lst[i]

            except IndexError:
                for _ in range(len(lst), i+1):
                    lst.append([])
                lst = lst[i]

        lst.append(word)