"""
### 2. Словарь частот слов

Пользователь вводит текст.
Программа должна:

1. Привести текст к нижнему регистру.
2. Удалить знаки пунктуации.
3. Подсчитать, сколько раз встречается каждое слово.
4. Отсортировать результат по убыванию частоты.
"""

sentence = input("Введите педложение \n")
l_sentence = sentence.strip().lower()
print(f"Текст в нижнем регистре \n{l_sentence}")
i = 0
while i < len(l_sentence):
    if l_sentence[i] in ("/",".",",",'"'):
        l_sentence = l_sentence.replace(l_sentence[i], "")
        i -= 1
    i += 1
print(f"Текст без знаков пунктуации \n{l_sentence}")
s_sentence = l_sentence.split()

dictionary = {}
for j in s_sentence:
    if j in dictionary:
        dictionary[j] += 1
    else:
        dictionary[j] = 1

sort_dict = {}
while dictionary:
    max_key = max(dictionary, key = dictionary.get)
    sort_dict[max_key] = dictionary[max_key]
    del dictionary[max_key]
print(f"Отсортированный текст \n{sort_dict}")