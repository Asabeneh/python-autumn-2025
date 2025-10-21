'''
note.txt, 
csv, tsv, 

'''
""" f = open('./names.txt')
lines = f.read().splitlines()
print(lines)

words = []
for line in lines:
    line_splited = line.lower().replace('.', '').split()
    words.extend(line_splited)
print(words)
f.close() """


with open('./names.txt') as f:
    lines = f.read().splitlines()
    print(lines)
    words = []
    for line in lines:
        line_splited = line.lower().replace('.', '').split()
        words.extend(line_splited)
    print(words)
    



# readline, readlines, read, write