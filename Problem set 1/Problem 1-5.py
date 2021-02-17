'''
Author: Nam Than
Date: 02/07/2021
UT Austin
Bioinformatics

Problems 1-5
'''
import numpy as np
import matplotlib.pyplot as plt

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
    return nuc_dict, nuc_freq

def dinuc_freq_cal(name):
    dinuc_dict = {}
    long_line = ''
    file = open(name, 'r')
    # Make a long line of all nuc
    for line in file:
        long_line += line.strip('\r\n')
    # Remove unwanted nuc
    all_nuc = set(long_line)
    unwanted_nuc = all_nuc.difference(known_nuc)  # Find the wrong nuc
    for i in unwanted_nuc:
        long_line = long_line.replace(i,'')
    # Check for dinucleotides
    for i in range(len(long_line)-1):
        dinuc = long_line[i] + long_line[i+1]
        if dinuc not in dinuc_dict:
            dinuc_dict[dinuc] = 1
        else:
            dinuc_dict[dinuc] += 1
    file.close()
    seq_len = sum(dinuc_dict.values())
    dinuc_freq = {}
    for nuc in dinuc_dict:
        dinuc_freq[nuc] = dinuc_dict[nuc]/seq_len
    file = open('Dinuc_freq_'+name, 'w')
    for dinuc in dinuc_freq:
        file.write('The dinucleotide {0} appears {1} times or {2} %.\n'.
                   format(dinuc, dinuc_dict[dinuc], 100.0 * dinuc_freq[dinuc]))
    file.close()
    return dinuc_dict, dinuc_freq


def expected_freq_cal(nuc_freq: dict):
    expected_freq = {}
    for first_nuc in nuc_freq.keys():
        for second_nuc in nuc_freq:
            dinuc = first_nuc + second_nuc
            probability = nuc_freq[first_nuc] * nuc_freq[second_nuc]
            expected_freq[dinuc] = probability
    return expected_freq


def plot_freq(freq_1: dict, freq_2: dict, label_1: str, label_2: str):
    # Rearrange so keys line up
    sorted_key_list = sorted(freq_1.keys())
    sorted_freq_1 = {}
    sorted_freq_2 = {}
    for key in sorted_key_list:
        sorted_freq_1[key] = freq_1[key]
        sorted_freq_2[key] = freq_2[key]
    # Plot
    x_axis = np.arange(len(sorted_key_list))
    fig = plt.subplot(111)
    fig.bar(x_axis, sorted_freq_1.values(), width=0.2, color='g',
            align='center')
    fig.bar(x_axis+0.2, sorted_freq_2.values(), width=0.2, color='b',
            align='center')
    fig.legend((label_1, label_2))  # arg is a tuple
    plt.title('Frequency comparison', fontsize=15)
    plt.xticks(x_axis, sorted_key_list)
    plt.savefig('{0}_{1}_freq_barplot'.format(label_1, label_2))
    plt.close()

def main():
    file_dir = ['Hinfluenzae.txt',
                'Taquaticus.txt',
                'MysteryGene1.txt',
                'MysteryGene2.txt',
                'MysteryGene3.txt']
    # Problem 1:
    print('Problem 1')
    HF_nuc_freq = nuc_freq_cal(file_dir[0])[1]
    TA_nuc_freq = nuc_freq_cal(file_dir[1])[1]

    # Problem 2:
    print('Problem 2')
    HF_dinuc_freq = dinuc_freq_cal(file_dir[0])[1]

    # Problem 3:
    print('Problem 3')
    TA_dinuc_freq = dinuc_freq_cal(file_dir[1])[1]

    # Problem 4:
    print('Problem 4')
    expected_dinuc_freq = expected_freq_cal(HF_nuc_freq)
    plot_freq(HF_dinuc_freq, expected_dinuc_freq, 'observed', 'expected')

    # Problem 5
    print('Problem 5')
    myst_1 = dinuc_freq_cal(file_dir[2])[1]
    plot_freq(myst_1, HF_dinuc_freq, 'myst_1', 'HF')
    plot_freq(myst_1, TA_dinuc_freq, 'myst_1', 'TA')

    myst_2 = dinuc_freq_cal(file_dir[3])[1]
    plot_freq(myst_2, HF_dinuc_freq, 'myst_2', 'HF')
    plot_freq(myst_2, TA_dinuc_freq, 'myst_2', 'TA')

    myst_3 = dinuc_freq_cal(file_dir[4])[1]
    plot_freq(myst_3, HF_dinuc_freq, 'myst_3', 'HF')
    plot_freq(myst_3, TA_dinuc_freq, 'myst_3', 'TA')


if __name__ == '__main__':
    main()