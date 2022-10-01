"""The idea is set up a dictionary for the last char
for all words in words.
then add up string and if we see a letter in the dic (key by default)
and the length of string is greater than the word,
reverse query the string and see if it matches the words
"""

class StreamChecker:
    def __init__(self, words) -> None:
        self.words=words
        self.d={}
        for w in words:
            if w[-1] not in self.d:
                self.d[w[-1]]=[w[:-1]]
            else:
                self.d[w[-1]].append(w[:-1])
        self.s=""
        # print(self.d)

    def query(self, letter: str) -> bool:
        self.s+=letter # adding up streams to form queries

        if letter in self.d:
            # by default checks in keys
            for word in self.d[letter]:
                # for all the words that start with letter are stored in list in dict
                complete_word_formed=word+letter
                length_of_word_formed=len(complete_word_formed)
                # check if the complete word formed here
                # is the suffix of the stream
                if complete_word_formed == self.s[-length_of_word_formed:]:
                    return True
        return False
        

obj=StreamChecker(["cd", "f", "kl" "cdef"])
obj=StreamChecker(["abc", "xyz"])
print(obj.query('a'))
print(obj.query('x'))
print(obj.query('y'))
print(obj.query('z'))


print(obj.query('f'))
print(obj.query('kl'))
print(obj.query('a'))
print(obj.query('b'))
print(obj.query('c'))
print(obj.query('d'))
print(obj.query('e'))
print(obj.query('f'))
print(obj.query('g'))
print(obj.query('h'))
print(obj.query('i'))
print(obj.query('j'))
print(obj.query('k'))
print(obj.query('l'))
