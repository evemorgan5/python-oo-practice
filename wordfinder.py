class WordFinder:
    """ Word Finder: finds random words from a dictionary."""
    def __init__(self,words):
        self.words = self.read_file(words)

    # def __repr__(self):
    #     return f"<WordFinder words={self.words}"

    def read_file(self):
        file = open(self.words)
        count = 0
        for line in file:
            print("line =", line)
            count += 1
        file.close()
        return (f"{count} words read")

    def random(self):



