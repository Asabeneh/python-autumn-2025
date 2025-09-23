'''
String: a text under single, double or triple quote
'''

letter = 'a'
word = 'love'
print(type(letter))
print(type(word), word, len(word))
print(word.upper())
print(word[1:])
print(word[1:3])
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[-4])
print(word[-3])
print(word[-2])
print(word[-1])
print(word[-3:-1])

print(word.startswith('l'))
print(word.startswith('L'))
print(word.endswith('ove'))
print('Fin' in 'Finland')
print('land' in 'Finland')

sentence = 'I love people, if you do not love people what else do you love.'
print(sentence.upper())
print(sentence.lower())
print(sentence.swapcase())
print(sentence.title())
print(sentence.find('I'))
print(sentence.find('i'))
print(sentence.rfind('love'))
print(sentence.rindex('love'))
print(sentence.index('I'))
print(sentence.rindex('love'))
print(sentence.find('z'))
print('What is the number of love in the text: ', sentence.count('love'))
print(sentence.split())


words = sentence.replace('.', '').replace(',', '').lower().split()
print(words)
print(len(words))
print(words,len(words), set(words), len(set(words)))
total_words = len(words)
unique_words = len(set(words))
print(unique_words / total_words * 100)
