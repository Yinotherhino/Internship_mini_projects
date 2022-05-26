# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True



def find_anagram(word, anagram):
    # [assignment] Add your code here
    #checkif length is equal
    if len(word) == len(anagram):
        word,anagram = list(word),list(anagram)
        #         sort both words 
        word.sort(),anagram.sort()
        #   check if both words are the same
        if word == anagram:
            return True
        else:
            return False
    else:
        return False

word_1= input("Enter a word: ")
word_2= input("Enter another word: ")
print (find_anagram(word_1,word_2))
