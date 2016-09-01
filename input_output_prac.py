"""
word_list = []
word_file = open("output.txt", "r")
word_count = 0


while True:
    if word_count < 3:
        new_word = word_file.readline()
        new_word = new_word[:len(new_word) - 1]
        word_list.append(new_word)
        word_count += 1
    else:
        word_file.close()
        break

print (word_list)


print (type(word_file.readline()))
print (word_file.readline())
word_file.close()
"""

from hangman_data import word_list

print (word_list)
