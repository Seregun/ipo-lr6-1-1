# Написать программу, которая:
# - Создаёт список из 6 строк (*строки определяются в коде, на ваш вкус*).
# - Подсчитывает количество строк, содержащих букву `a`.
# - Использует циклы для подсчета.

list = ["Яблоко", "Егор", "Меч", "Банан", "Обезьяна", "Змея"] # Создание списка из 6 строк
count = 0 # Начало подсчета слов с буквой "а"
for string in list: # Цикл for
    if "а" in string.lower(): # Если буква "а" в строке (перевод в нижний регистр)
        count+=1 # Добавить 1 при нахождении буквы "а" в строке
print("Кол-во строк с буквой а: ", count) # Вывод кол-ва строк с буквой "а"