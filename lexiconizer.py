import os, timeit

class Word:
    def __init__(self, spelling):
        self.spelling = spelling
        self.neighbours = []
        self.frequency = 1
        self.pointer = 0 # Used in neighbours_same_1()

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

    #         Modified to increment data frequencyuency if data already in tree.
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

    def right_rot(self, g):
        p = g.left
        rcp = p.right
        p.right = g
        g.left = rcp
        self.set_node_height(g)
        return p

    def left_rot(self, g):
        p = g.right
        lcp = p.left
        p.left = g
        g.right = lcp
        self.set_node_height(g)
        return p

    def right_left_rot(self, g):
        p = g.right
        g.right = self.right_rot(p)
        return self.left_rot(g)

    def left_right_rot(self, g):
        p = g.left
        g.left = self.left_rot(p)
        return self.right_rot(g)

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
                local_root = self.left_right_rot(local_root)
            else:
                local_root = self.right_rot(local_root)
        elif difference == -2:
            if self.get_height_diff(local_root.right) == 1:
                local_root = self.right_left_rot(local_root)
            else:
                local_root = self.left_rot(local_root)
        return local_root

    #         Traverses tree inorder and:
    #         1. Appends word to alphabetically 1 list
    #         2. Appends word to nested list in same_0 by word length, then char 0
    #         3. Appends word to nested list in same_1 by word length, then char 1, then char 0
    def traverse_inorder(self, local_root, sorted_lst, same_0, same_1):
        if local_root is not None:
            self.traverse_inorder(local_root.left, sorted_lst, same_0, same_1)
            
            word = local_root.data
            spelling = word.spelling
            length = len(spelling) - 1
            idx_0 = g(spelling[0])

            sorted_lst.append(word)    

            add_to_inner(word, same_0, length, idx_0)

            if length > 0:
                idx_1 = g(spelling[1])
                add_to_inner(word, same_1, length, idx_1, idx_0)

            self.traverse_inorder(local_root.right, sorted_lst, same_0, same_1)

def g(c):
    return ord(c) - ord('a')

#         Iteratively nests lists at each index in n, then appends word to deepest list.
#         Quite psychedelic.
def add_to_inner(word, lst, *n):
    for i in n:
        try: lst = lst[i]
        except:
            for _ in range(len(lst), i+1):
                lst.append([])
            lst = lst[i]
    lst.append(word)

#         Reads data and inserts into AVLTree, or increments frequencyuency if data already present.
def read_data(lexicon, filename):
    with open(filename, "r") as infile:
        for line in infile:
            tokens = line.strip().split()
            for token in tokens:
                token = "".join([ch for ch in token if ch.isalpha()]).lower()
                if token != "":
                    lexicon.insert_element(token)

#         Returns True if words are neighbours, otherwise False.
#         Only checks indices between start and end.
def check_neighbours(word_1, word_2, start, end, diffs=0):
    for i in range(start, end):
        if word_1[i] != word_2[i]:
            diffs += 1
            if diffs > 1:
                return False
    return True

#         Adds neighbours for words with only one char.
#         check_neighbours() not required as all one-char words are neighbours (other than self).
def neighbours_one_char(one_char):
    len_one_char = len(one_char)

    for i in range (len_one_char):
        for a in one_char[i]: # Word 1
            spelling_1 = a.spelling
            neighbours_1 = a.neighbours

            for j in range(i+1, len_one_char):
                for b in one_char[j]: # Word 2
                    spelling_2 = b.spelling
                    neighbours_2 = b.neighbours

                    neighbours_1.append(spelling_2)
                    neighbours_2.append(spelling_1)

#         Adds neighbours for words of same length and with same first letter.
#         check_neighbours() begins after first letter, as it is always the same.
def neighbours_same_0(same_0):
    for same_len in range(len(same_0)): # Words of same length

        for inner in same_0[same_len]: # Words with same char at idx 0
            len_inner = len(inner)
            if len_inner > 1:

                for i in range(len_inner): # Word 1
                    spelling_1 = inner[i].spelling
                    neighbours_1 = inner[i].neighbours

                    for j in range(i+1, len_inner): # Word 2
                        spelling_2 = inner[j].spelling
                        neighbours_2 = inner[j].neighbours

                        if check_neighbours(spelling_1, spelling_2, 1, same_len+1):
                            neighbours_1.append(spelling_2)
                            neighbours_2.append(spelling_1)

# Adds neighbours for words of same length and with same second letter.
# SKIPS words with same first letter (checked previously).

# check_neighbours() begins after second letter, with 1 difference already counted.
# (First letter always different, second letter always same.)

# spelling_1 inserted to neighbours_2 BEFORE all neighbours previously added in neighbours_same_0(),
# and AFTER all neighbours previously added in neighbours_same_1(). Word.pointer keeps count of this
# index for each Word object.
def neighbours_same_1(same_1):
    for same_len in range(len(same_1)): # Words of same length

        for lst in same_1[same_len]: # Words with same char at idx 1
            len_lst = len(lst)

            for a in range(len_lst): # Words with same char at idx 0

                for b in range(len(lst[a])): # Word 1
                    word_1 = lst[a][b]
                    spelling_1 = word_1.spelling
                    neighbours_1 = word_1.neighbours

                    for c in range(a+1, len_lst): # Words with same char at idx 0, starting AFTER Word 1

                        for d in range(len(lst[c])): # Word 2
                            word_2 = lst[c][d]
                            spelling_2 = word_2.spelling
                            neighbours_2 = word_2.neighbours

                            if check_neighbours(spelling_1, spelling_2, 2, same_len+1, 1):
                                neighbours_1.append(spelling_2)
                                neighbours_2.insert(word_2.pointer, spelling_1)
                                word_2.pointer += 1

def write_to_file(sorted_lst, filename):
    with open(filename, "w") as outfile:
        for i in sorted_lst:
            outfile.write(str(i))

def build_lexicon(input_filename, output_filename):
    lexicon = AVLTree()
    sorted_lst, same_0, same_1 = [], [], []

    # Generate AVL Tree
    read_data(lexicon, input_filename)

    # Populate lists
    lexicon.traverse_inorder(lexicon.root, sorted_lst, same_0, same_1)

    # Add neighbours
    neighbours_one_char(same_0[0])
    neighbours_same_0(same_0)
    neighbours_same_1(same_1)

    # print(f'Number of words: {len(sorted_lst)}')
    # print(f'Avg same 0: {get_average_same_0_len(same_0)}')
    # print(f'Avg same 1: {get_average_same_1_len(same_1)}')
    # print()

    # Write to file
    write_to_file(sorted_lst, output_filename)

def get_average_same_0_len(same_0):
    sum_total = 0
    divisor = 0
    for a in same_0:
        for b in a:
            sum_total += len(b)
            divisor += 1

    return sum_total / divisor

def get_average_same_1_len(same_0):
    sum_total = 0
    divisor = 0
    for a in same_0:
        for b in a:
            for c in b:
                sum_total += len(b)
                divisor += 1

    return sum_total / divisor

def time_build_lexicon(input_filename, output_filename, N_REPEATS=1):
    print("\nRunning...")
    total_execution_time = timeit.timeit(lambda: build_lexicon(input_filename, output_filename), globals=globals(), number=N_REPEATS)
    average_time = total_execution_time / N_REPEATS
    print("COMPLETE.")
    print(f'\nAverage execution time: {average_time:.2f}s across {N_REPEATS} runs')

if __name__ == '__main__':

    def input_int():
        while True:
            num = input(">>> ").strip()
            if num.isdigit() and int(num) > 0:
                return int(num)
            else:
                print("INVALID (Must be integer greater than 0)")

    def input_y_n():
        while True:
            y_n = input(">>> ").lower().strip()
            if y_n == "y":
                return True
            elif y_n == "n":
                return False
            else:
                print("INVALID (Must be Y/n)")

    def run_test():
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        input_filename = os.path.join(__location__, "in.txt")
        output_filename = os.path.join(__location__, "out.txt")

        print("Input number of repeats\n(Higher number = longer total runtime, but more accurate results)")
        N_REPEATS = input_int()
        time_build_lexicon(input_filename, output_filename, N_REPEATS)

        print("Again? [Y/n]")
        if input_y_n():
            print()
        else:
            quit()

    while True:
        run_test()