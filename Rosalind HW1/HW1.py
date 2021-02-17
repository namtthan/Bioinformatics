directory = 'C:/Users/marti/Downloads/'
read_name = 'rosalind_ini5.txt'
write_name = 'rosalind_ini5_write.txt'

new_file = []

read_file = open(directory+read_name, 'r')
for line in read_file:
    new_file.append(line.strip('\r'))
read_file.close()

length = len(new_file)

write_file = open(directory+write_name, 'w')
for i in range(length):
    write_file.write(new_file[i]) if i%2==1 else None
write_file.close()
