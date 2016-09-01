def listmaker(word_list_file, listnum):
    word_list_2 = []
    count = 0
    while True:
        word_addition = word_list_file.readline()
        word_addition = word_addition[:len(word_addition) - 1]
        word_list_2.append(word_addition)
        count += 1
        if count == listnum:
            break
    return word_list_2

def list_edit(list):
    new_list = []
    new_list2 = []
    print ('The original list was:\n %s' % (list))
    print()
    for item in list:
        if '-' in item:
            print ('%s removed because contained hyphen' % (item))
        elif ' ' in item:
            print ('%s removed because contained space' % (item))
        else:
            item = item.lower()
            new_list.append(item)
    print()
    print('The halfway edited list is:\n %s' % (new_list))
    print()
    for item in new_list:
        if item not in new_list2:
            new_list2.append(item)
        else:
            print ('%s removed because contained it was a duplicate' % (item))
    return (new_list2)

def list_combine(listA, listB):
    new_list = listA
    for item in listB:
        if item in new_list:
            print ('%s removed because contained it was a duplicate' % (item))
        else:
            new_list.append(item)
    return new_list


word_list_file = open("hangman_data2.py", "r")
new_words = listmaker(word_list_file, 230)

word_list_file.close()

new_words2 = list_edit(new_words)
print (new_words2)

my_file = open("hangman_data3.py", "w")
for item in new_words2:
    my_file.writelines('%s\n' % (item))
my_file.close()
