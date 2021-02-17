# Author: Nam Than
# Date: 02/07/2021
# Problem 1, 2, 3, 4, 5
'''
Write a short Python program to calculate the frequencies of nucleotides in a DNA sequence. This
can be the program from the Python primer or a program of your own construction. Run it on the H.
influenza genome and the T. aquaticus genome (get the nucleotide sequence files directly from the
course web page). Turn in the nucleotide frequencies of the two genomes & your program.
'''
known_nuc = {'A', 'G', 'T', 'C'}  # Define a non-duplicated set of nuc

def nuc_freq_cal(name):
    nuc_dict = {}
    file = open(name, 'r')
    for line in file:
        line = line.strip('\r\n')
        for let in line:
            if let not in known_nuc:
                pass
            else:
                if let not in nuc_dict:
                    nuc_dict[let] = 1
                else:
                    nuc_dict[let] += 1
    file.close()
    seq_len = sum(nuc_dict.values())  # Sum of all counts in the dict
    nuc_freq = {}
    for nuc in known_nuc:
        nuc_freq[nuc] = nuc_dict[nuc]/seq_len
    file = open('Nuc_freq_'+name, 'w')
    for nuc in nuc_freq:
        file.write('The nucleotide {0} appears {1} times or {2} %.\n'.
                   format(nuc, nuc_dict[nuc], 100.0 * nuc_freq[nuc]))
    file.close()
    print(nuc_dict)  # Quick check
    print(nuc_freq)  # Quick check


def main():
    file_dir = ['Hinfluenzae.txt',
                'Taquaticus.txt']
    for name in file_dir:
        nuc_freq_cal(name)


if __name__ == '__main__':
    main()
