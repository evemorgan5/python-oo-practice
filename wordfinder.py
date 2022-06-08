from ast import While
import random


class WordFinder:
    """ Word Finder: finds random words from a dictionary."""

    def __init__(self, words):
        self.words = self.read_file(words)

    # def __repr__(self):
    #     return f"<WordFinder words={self.words}"

    def read_file(self, words):
        """ Docestring needed"""
        file = open(f"{words}", "r")
        read_words = file.readlines()
        read_words_modified = []
        for word in read_words:
            if(word[0] != '#'):
                read_words_modified.append(word[:-1])

        while ("" in read_words_modified):
            read_words_modified.remove("")

        file.close()
        print(f"{len(read_words_modified)} words read")
        return read_words_modified

    def random(self):
        return random.choice(self.words)
