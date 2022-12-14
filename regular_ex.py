# Синтаксис регулярных выражений (Stepik курс)

common_string = 'C:\file\file.txt'  # Обычная строка
raw_string = r'C:\file\file.txt'  # Сырая строка

a = 1
b = 2
# Добавляем выражения в строку с полмощью специального синтаксиса {}
print(f"{a} + {b} = {a + b}")
print(f"5! = {1 * 2 * 3 * 4 * 5}")

# Использование 2 префиксов одновременно:
raw_f_string = rf'C:\file.txt'
f_raw_string = fr'C:\file.txt'

# task 1
s = r"Последовательность \n используется для переноса строк"
print(s)

# task 2
a = 5
print(f'{a} * {a} = {a * a}')

# Экранирование строк
# Вместо символа \n мы получим переход на новую строку
print("Переносим\nстроку")

# Вместо \\' получаем вывод \'
# Первый \ экранирует второй \, и он исчезает из вывода
print("\\'")

# task 3
print(r"\\\'")  # recommended!
# or
print("\\\\\\'")

# task 4
a, b = 2, 3
print(rf"{a}\n+\n{b}\n=\n{a + b}")

range_list = list(range(1, 4))
print(range_list)

# Использование квадратных скобок
# r'[cr1]' - Найдет c, r, 1
# r'[cr]at' - Найдет слова cat или rat
# r'[12]7[56]' - Найдет 175, 176, 275, 276

# Последовательность символов не влияет на конечный результат поиска
# r'[rc]at' - Все также находит слова cat и rat

# Для исключения символов использутеся ^

# r'[^12]' - Найдет все, кроме 1 и 2
# r'[^12]7' - Найдет все последовательности, что заканчиваются на 7, и не начинаются на 1 или 2

# Если необходим диапазон, то регулярное выражение можно сократить так

# r'[0-9]' - Тоже самое, что и [0123456789] - все числа от 0 до 9
# r'[a-z]' - Тоже самое, что и [abcdefghijklmnopqrstuvwxyz] - английский алфавит от a до z
# регистр символов влияет на поиск, то есть регулярное выражение r'[a-z]' не найдет заглавные символы,
# а будет искать только среди строчных (в нижнем регистре) букв
# r'[A-Z]' - ищет заглавные буквы английского алфавита от A до Z

# Также стоит учесть, что r'[21-47]' не найдет числа от 21 до 47,
# а будет равносильна выражению r'[212347]'
# В выражении r'[21-47]', к диапазону, относятся только числа от 1 до 4,
# 2 и 7 находятся вне диапазона

# Также можно совмещать регулярные выражения в одних квадратных скобках
# r'[a-zA-z0-9]' - будет искать буквы английского алфавита (в верхнем и нижнем регистре) и цифры от 0 до 9

# r'[а-яА-я]' - не захватывает буквы ё и Ё, для этого их придется дописать отдельно
# r'[а-яА-яёЁ]' - данное выражение ищет все буквы от А до я, а также буквы ё и Ё

