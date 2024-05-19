class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(word)

    def match(self, candidates):
        return [candidate for candidate in candidates if sorted(candidate) == self.sorted_word and candidate.lower() != self.word.lower()]