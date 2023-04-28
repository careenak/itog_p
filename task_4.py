"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
string_list = ['разработка', 'администрирование', 'protocol', 'standard']

byte_list = []

for word in string_list:
    word_bytes = word.encode('utf-8')  # получили байты
    byte_list.append(word_bytes)
    print(word_bytes, type(word_bytes))

for byte in byte_list:
    string = byte.decode('utf-8')  # получили строку
    print(string, type(string))