print('')
print('Задача "Однокоренные"')
print('')

def single_root_words (root_word, *other_word):
    same_words = []
    a = root_word.lower()
    b=[]
    flag_1 = False
    flag_2 = False
    for i in range(len(other_word)):
        b = other_word[i].lower()
        flag_1 = a in b
        flag_2 = b in a
        if flag_1 == True or flag_2 == True:
            same_words.append(other_word[i])
    print('Проверочное слово:', root_word)
    print('Заданный список слов:', other_word)
    print(same_words)


single_root_words('Час', 'часы', 'Часовня', 'часто', 'чисто')

print('')
print('Задание выполнено')