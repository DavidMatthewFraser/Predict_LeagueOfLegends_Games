f = open('sample1.csv')
l = f.readlines()
for line in l:
    words = line.split(' ')
    if words[3] == 'True\n':
        words[3] = '1\n'
    else:
        words[3] = '0\n'
    print(words[1], end=' ')
    print(words[2], end=' ')
    print(words[3], end='')
