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
    
    # NOTE: Operator overloading not used for comparison, as it has 
    # significant impact on runtime.

    def __str__(self) -> str:
        """
        Returns a string representation of a Word.

        Returns:
            A string representation of the word, including its spelling, 
            frequency, and list of neighbors. e.g. "cat 6 ['bat', 'cab', 'cut']"
        """
        return f"{self.spelling} {self.frequency} {self.neighbours}\n"