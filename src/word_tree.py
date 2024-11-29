from src.avl_tree import AVLNode, AVLTree

class Word:
    """
    Represents a word and its associated data.

    Attributes:
        spelling (str): The word's spelling.
        neighbours (list[str]): A list of neighboring words (e.g. words that
            differ by one character).
        frequency (int): The frequency of the word's occurrence.
        pointer (int): Used for inserting words alphabetically into the 
            `neighbours` list.
    """
    def __init__(self, spelling):
        self.spelling: str = spelling
        self.neighbours: list[str] = []
        self.frequency: int = 1
        self.pointer: int = 0
    
    # NOTE: Operator overloading not used as it has significant impact 
    # on runtime.

    def __str__(self) -> str:
        """
        Returns a string representation of a Word.

        Returns:
            A string representation of the word, including its spelling, 
            frequency, and list of neighbors. e.g. "cat 6 ['bat', 'cab', 'cut']"
        """
        return f"{self.spelling} {self.frequency} {self.neighbours}\n"

class WordTree(AVLTree):
    """
    Specialized AVLTree subclass for storing and managing Word objects.

    A WordTree is used when AVLNode data is a Word object.
    """

    def __init__(self):
        super().__init__()

    def insert_element(self, data: str):
        """
        Inserts Word data into WordTree. Increments frequency if already in tree.

        Args:
            data (str): The word to insert.

        Behavior:
            - If the tree is empty, creates the root node with the word.
            - If the word already exists in the tree, its frequency is 
                incremented.
            - Otherwise, adds the word as a new node in the correct position and
                rebalances the tree.
        """
        if self.root is None:
            self.root = AVLNode(Word(data))
            return

        p: AVLNode = self.root

        while True:
            if data == p.data.spelling:
                # Increment data frequencey if data already in tree
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

    @staticmethod
    def g(c: str):
        """
        Calculates the alphabetical index of a character relative to 'a'

        Args:
            c (str): A single character.

        Returns:
            int: The index of the character (0 for 'a', 1 for 'b', etc.)
        """
        return ord(c[0]) - ord('a')

    @staticmethod
    def traverse_inorder(
        local_root: AVLNode,
        sorted_list: list[Word],
        one_char_words: list[Word],
        nested_word_lists: list
    ):
        """
        Performs an inorder traversal of the WordTree.

        During traversal, it:
            1. Appends each word to an alphabetically sorted list.
            2. Appends word to nested_word_lists nested by: word length, 
            then char 1, then char 0
            3. Appends one char words to one_char_words

        Args:
            local_root (AVLNode): The current node in the traversal.
            sorted_list (list[Word]): A list to hold all words in alphabetical 
                order.
            one_char_words (list[Word]): A list to hold single-character words.
            nested_word_lists (list): A nested list to organize words by length 
                and characters.
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
        """
        Iteratively nests lists at each index in n, appending word to deepest list.

        Args:
            word (Word): The Word object to add.
            lst (list): The outermost list to which the word will be added.
            *n (int): A sequence of indices specifying the nested structure.

        Behavior:
            - Navigates the nested structure according to the indices in `n`.
            - Creates intermediate lists as needed if they do not exist.
            - Appends the word to the deepest list specified by `n`.
        """
        for i in n:
            try:
                lst = lst[i]

            except IndexError:
                for _ in range(len(lst), i+1):
                    lst.append([])
                lst = lst[i]

        lst.append(word)