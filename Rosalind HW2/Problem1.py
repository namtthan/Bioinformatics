'''
Author: Nam Than
Problem 1
'''

data = 'We tried list and we tried dicts also we tried Zen'
splitted_words =  data.split(' ')
word_dict = {}

for word in splitted_words:
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1

print (word_dict)