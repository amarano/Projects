from collections import defaultdict

__author__ = 'angelo'


class InvertedIndex:

    def __init__(self, file_list):
        self.file_list = file_list
        self.index = defaultdict(list)

    def build_index(self, search_terms):
        for term in search_terms:
            for file in self.file_list:
                with open(file) as f:
                    if any(map(lambda x : x == term, self._words(f))):
                        self.index[term].append(file)

    @staticmethod
    def _words(text_file):
        return (word for line in text_file for word in line.split())

    def get_index(self):
        return self.index

inverted_index = InvertedIndex(["textfile1.txt", "textfile2.txt"])

inverted_index.build_index(["is", "stuff", "Abby"])

print inverted_index.get_index()