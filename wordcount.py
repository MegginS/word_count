"""Count words in file."""

def word_count (path):

    word_count_dict = {}
    punc = '''!()-[];:'"\,<>./?@#$%^&*_~'''

    for line in open(path):
        words = line.split(' ')
        for word in words:
            for ele in word:
                word = word.replace("\n", "")
                if ele in punc:
                    word = word.replace(ele, "")
                word = word.title()
            word_count_dict[word] = word_count_dict.get(word,0) + 1

    print(word_count_dict)
    return word_count_dict

word_count("twain.txt")

    
# put your code here.
