'''
Author: Nam Than
Problem 4
'''

mRNA_string = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
protein_string = ''
codon_table = {'UUU':'F',
               'UUC':'F',
               'UUA':'L',
               'UUG':'L',
               'UCU':'S',
               'UCC':'S',
               'UCA':'S',
               'UCG':'S',
               'UAU':'Y',
               'UAC':'Y',
               'UAA':'Stop',
               'UAG':'Stop',
               'UGU':'C',
               'UGC':'C',
               'UGA':'Stop',
               'UGG':'W',
               'CUU':'L',
               'CUC':'L',
               'CUA':'L',
               'CUG':'L',
               'CCU':'P',
               'CCC':'P',
               'CCA':'P',
               'CCG':'P',
               'CAU':'H',
               'CAC':'H',
               'CAA':'Q',
               'CAG':'Q',
               'CGU':'R',
               'CGC':'R',
               'CGA':'R',
               'CGG':'R',
               'AUU':'I',
               'AUC':'I',
               'AUA':'I',
               'AUG':'M',
               'ACU':'T',
               'ACC':'T',
               'ACA':'T',
               'ACG':'T',
               'AAU':'N',
               'AAC':'N',
               'AAA':'K',
               'AAG':'K',
               'AGU':'S',
               'AGC':'S',
               'AGA':'R',
               'AGG':'R',
               'GUU':'V',
               'GUC':'V',
               'GUA':'V',
               'GUG':'V',
               'GCU':'A',
               'GCC':'A',
               'GCA':'A',
               'GCG':'A',
               'GAU':'D',
               'GAC':'D',
               'GAA':'E',
               'GAG':'E',
               'GGU':'G',
               'GGC':'G',
               'GGA':'G',
               'GGG':'G'}

next_codon_index = 0
for i in range(len(mRNA_string)-2):
    if i >= next_codon_index:
        codon = mRNA_string[i] + mRNA_string[i+1] + mRNA_string[i+2]
        next_codon_index = i+3
        if codon_table[codon] == 'Stop':
            break
        else:
            protein_string += codon_table[codon]

print(protein_string)