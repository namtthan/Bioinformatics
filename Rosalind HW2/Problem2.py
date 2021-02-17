'''
Author: Nam Than
Problem 2
'''

RNA_nuc = {'A', 'C', 'G', 'U'}  # define a set of RNA nucleotides

DNA_string = 'GATGGAACTTGACTACGTAAATT'

RNA_string = ''

for i in DNA_string:
    if i != 'T':
        RNA_string += i
    else:
        RNA_string += 'U'

print(RNA_string)