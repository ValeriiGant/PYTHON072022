# Напишите программу, удаляющую из текста все слова, содержащие "абв".
my_text = 'абв Ура, питон круто, очеагбвнь инетресные семинарабвы! абв'
def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(my_text)


# word = 'абв Ура, питон круто, очеагбвнь инетресные семинарабвы! абв'
# col = word.split()
# print(col)
# new_col = []
# search = 'абв'
# for item in col:
#     if search not in item:
#         new_col.append(item)

# print(new_col)

# new_col = [item for item in col if 'абв' not in item]
# print(new_col)













# word = 'абв Ура, питон круто, очеагбвнь инетресные семинарабвы! абв'
# find = 'абв'

# word = word.split()
# print(word)

# f = lambda x: not x.count(find) > 0 
# lst = list(filter(f, word))
# print('lst = ',lst)

# str_new = ' '.join(lst)
