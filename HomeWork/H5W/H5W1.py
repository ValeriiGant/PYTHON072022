#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text_del = 'Абв szf свмао ысвкмчипрабв аб в Яуксмаритнь бав лячыыц чычвувчабв'

print(' '.join(list(filter(lambda word: not word.__contains__('абв'), text_del.split()))))