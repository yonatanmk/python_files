pyg = 'ay'

print ('Enter a word and I will convert it into Pig Latin:')
print ('Please enter only a single word and do not use numbers or symbols')
original = input('-->')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word[1:len(word)] + first + pyg
    new_word = new_word[0].upper() + new_word[1:len(new_word)]
    print (new_word)
else:
    print ('empty')
