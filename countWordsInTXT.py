# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as f:
        text = f.read()
    text= [v for v in text if (v.isalpha() or v == " ")]
    text= ("").join(text)
    text = text.split()
    return text
    



def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    wordCount={}
    eachWord = sorted(list(set(text)))
    for n in range(len(eachWord)):
        wordCount[eachWord[n]] = text.count(eachWord[n])
    return wordCount

# read_file_content("./story.txt")
count_words()
