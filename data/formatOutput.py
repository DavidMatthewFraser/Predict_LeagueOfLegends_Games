f = open('sample3/sample3.csv')
l = f.readlines()
print('mastery,rank,result')
for line in l:
    words = line.split(' ')
    print(words[1], end='')
    print(words[2], end='')
    print(words[3], end='')
f.close()
