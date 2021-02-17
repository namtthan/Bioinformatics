'''
Author: Nam Than
Problem 3
'''

DNA_string = 'AAAACCCGGT'
complemented_DNA = ''
reversed_DNA = ''

for i in DNA_string:
    if i == 'A':
        complemented_DNA += 'T'
    elif i == 'T':
        complemented_DNA += 'A'
    elif i == 'C':
        complemented_DNA += 'G'
    else:
        complemented_DNA += 'C'

for i in range(len(complemented_DNA)):
    reversed_DNA += complemented_DNA[-(i+1)]

print(complemented_DNA)
print(reversed_DNA)