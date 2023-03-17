# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
        self.matching_words = []

    def match(self, input_list):
        for each_word in input_list:
            if sorted(list(each_word)) == sorted(list(self.word)):
                self.matching_words.append(each_word)

        return self.matching_words

        # for each_word in input_list:
        #     if set(each_word) in input_list == set(self.word):
        #         print(self.matching_words.append(each_word))
