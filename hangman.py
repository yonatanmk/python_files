word_list = [
'acres', 'adult', 'advice', 'arrangement', 'attempt', 'border', 'constantly', 'contrast', 'cookies',
'customs', 'damage', 'deeply', 'depth', 'discussion', 'doll', 'donkey', 'fireplace', 'floating', 'folks', 'fort', 'garage', 'grabbed', 'grandmother', 'habit',
'happily', 'heading', 'hunter', 'image', 'independent', 'instant', 'kids', 'label', 'lungs', 'manufacturing', 'mathematics', 'melted', 'memory', 'mill', 'mission', 'monkey', 'mysterious', 'neighborhood',
'nuts', 'occasionally', 'official', 'ourselves', 'palace', 'plates', 'poetry', 'policeman', 'positive', 'possibly',
'practical', 'pride', 'promised', 'recall', 'relationship', 'remarkable', 'require', 'rhyme', 'rocky', 'rubbed', 'rush', 'sale', 'satellites', 'satisfied', 'scared', 'selection',
'shake', 'shaking', 'shallow', 'shout', 'silly', 'simplest', 'slight', 'slip', 'slope', 'soap', 'solar', 'species', 'spin', 'stiff', 'swung', 'tales', 'thumb', 'tobacco', 'toy', 'trap'
]

from random import randint

wordnumber = randint(0,88)
word_to_guess = word_list[wordnumber]
word_length = len(word_to_guess)

print ('Welcome to Hangman')
print ('The word is %s letters long' % (word_length))
#print (word_to_guess)
print ('_ ' * word_length)
guess = input("Please guess a letter. No capitals, numbers, or symbols please.")
