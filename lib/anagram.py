class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, word_list):
        matches = []
        for words in word_list:
            lower_words = words.lower()
            if lower_words!= self.word and sorted(lower_words) == self.sorted_word:
                matches.append(words)
        return matches

anagram = Anagram("enlist")
print(anagram.match(["listen", "silent", "hippopotamus"]))  
