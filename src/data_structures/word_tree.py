from src.data_structures.avl_node import AVLNode
from src.data_structures.avl_tree import AVLTree
from src.shared.word import Word
from src.utils.neighbours_utils import add_word_to_nested_list

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
    def traverse_inorder(
        local_root: AVLNode,
        sorted_list: list[Word],
        one_char_words: list[Word],
        nested_word_list: list
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
            WordTree.traverse_inorder(local_root.left, sorted_list, one_char_words, nested_word_list)
            
            word = local_root.data

            # Add word to sorted_list
            sorted_list.append(word)

            # Add word to nested_word_lists
            add_word_to_nested_list(word, nested_word_list, one_char_words)

            WordTree.traverse_inorder(local_root.right, sorted_list, one_char_words, nested_word_list)
