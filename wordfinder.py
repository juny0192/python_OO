"""Word Finder: finds random words from a dictionary."""
    # for line in f:
    #     line = line.strip()
    #     print(f"- {line}")
import random

class WordFinder:
    """Find random words from the directed file."""

    def __init__(self, path):
        """Read file and print how many words in the file."""
        f = open(path, 'rt')
        self.words = self.strip(f)
        print(f"{len(self.words)} words read")
    
    def strip(self, file):
        """Change words in the file into the list."""
        lst = []
        for word in file:
            lst.append(word.strip())
        return lst
        
    def random(self):
        """Pick random word"""
        return random.choice(self.words)
    
    

        

        



        


