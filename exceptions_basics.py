# Обработка исключений
# Исключения - это извещения интерпретатора, возбуждаемые в случае возникновения ошибки в
# программном коде или при наступлении какого-либо события. Если в коде не предусмотрена
# обработка исключения, выполнение программы прерывается, и выводится сообщение об ошибке

# Существует три типа ошибок:
# СИНТАКСИЧЕСКИЕ - ошибки имени оператора или функции, отсутсвие закрывающей
# или открывающей ковычек, ошибки в синтаксисе языка
# print("Нет завершающей кавычки!)
# SyntaxError: EOL while scanning string literal

# ЛОГИЧЕСКИЕ - ошибки в логике программы, которые можно выявить только по результатам работы.
# Как правило, интерпретатор не предупреждает о наличии такой ошибки. Выявить и исправить
# такие ошибки весьма трудно!

# ОШИБКИ, ВРЕМЕНИ ВЫПОЛНЕНИЯ - ошибки, которые возникают во время работы программы.
# Причиной являются события, не предусмотренные программистом.
def test(x, y): return x / y


test(4, 2)  # 2.0
# test(4, 0) Приведет к ошибке, ZeroDivisionError: division by zero
# Деление на ноль

# Необходимо заметить, что в Python исключения возбуждаются не только при возникновении ошибки,
# но и как уведомление о наступлении каких-либо событий. Например, метод index()
# возбуждает исключение ValueError, если искомый фрагмент не входит в строку
# 'Строка'.index('текст')
# ValueError: substring not found

# Инструкция try...except...else...finally
# Для обработки исключений предназначена инструкция try.

# try:
#     <Блок, в котором перехватываются исключения>
# [except [<Исключение1> as <Объект исключения>]]:
#     <Блок, выполняемый при возникновении исключения>
# [...
# except [<ИсключениеN>[ as <Объект исключения>]]:
#     <Блок, выполняемый при возникновении исключения>]]
# [else:
#     <Блок, выполняемый, если исключение не возникло>]
# [finally:
#     <Блок, выполняемый в любом случае>]

try:  # Перехватываем исключение
    x = 1 / 0  # Ошибка: деление на 0
except ZeroDivisionError:  # Указываем класс исключения
    print('Обработали деление на 0')
    x = 0
print(x)  # >> 0

# В случае если исключение не соотвествует указанному классу, управление передается
# следующему блоку except

try:
    try:
        x = 1 / 0
    except NameError:
        print('Неопределенный идентификатор')
    except IndexError:
        print('Несуществующий индекс')
    print('Выражение после вложенного обработчика')
except ZeroDivisionError:
    print('Обработка деления на 0')
    x = 0
print(x)
# В этом примере во вложенном обработчике не указано исключение ZeroDivisionError,
# поэтому исключение всплывает к обработчику более высокого уровня.

# В конструкции except можно указать сразу несколько исключений, записав их через запятую
# внутри круглых скобок

try:
    x = 1 / 0
except (NameError, IndexError, ZeroDivisionError):
    # обработка сразу нескольких исключений
    x = 0
print(x)  # >> 0

# Получить информацию об обрабатываемом исключении можно через второй параметр в инструкции except

try:
    x = 1 / 0
except (NameError, IndexError, ZeroDivisionError) as err:
    print(err.__class__.__name__)  # Название класса исключения
    print(err)  # Текст сообщения об ошибке

# Если в инструкции except не указан класс исключения, то такой блок будет перехватывать
# все исключения. На практике следует избегать пустых инструкций except, т.к. можно
# перехватить исключение, которое является лишь сигналом системе, а не ошибкой

try:
    x = 1 / 0  # Ошибка деления на 0
except:  # Обработка всех исключений
    x = 0
print(x)  # >> 0

# Если в обработчике присутствует блок else, то инструкции внутри этого блока будут
# выполнены только ПРИ ОТСУТСВИИ ОШИБОК, если ошибки есть блок не будет выполнен.
# Если необходимо выполнить какие-либо действия вне зависимости от того, возникло
# исключение или нет, следует воспользоваться блоком finally.

try:
    x = 10 / 2
    # x = 10 / 0
except ZeroDivisionError:
    print('Деление на 0')
else:
    print('Блок else')
finally:
    print('Блок finally')
# Так как ошибки при обработке не случилось результатом будет
# >> Блок else
# >> Блок finally

# Последовательность выполнения блока при наличии исключения будет другой
# >> Деление на 0
# >> Блок finally

# Переделаем программу суммирования целых чисел, введеных пользователем, таким образом,
# чтобы при вводе строки вместо числа программа не завершалась с фатальной ошибкой
print('Введите слово "stop" для получения результата')
summa = 0
while True:
    x = input('Введите число: ')
    if x == 'stop':
        break  # Выход и цикла
    try:
        x = int(x)  # Преобразуем строку в число
    except ValueError:
        print('Необходимо ввести целое число')
    else:
        summa += x
print('Сумма чисел равна:', summa)

# Инструкция with...as
# Язык Python поддерживает протокол менеджеров контекста. Этот протокол гарантирует
# выполнение завершающих действий (например, закрытие файла) вне зависимост от того,
# произошло исключение внутри блока кода или нет.

# Для работы с протоколом предназначена инструкция with...as.

# with <Выражение1>[ as <Переменная>][, ...,
#     <ВыражениеN>[ as <Переменная>]]:
#     <Блок, в котором перехватываем исключения>

# Пользовательские исключения
# Для возбуждения пользовательских исключений предназначены две функции
# raise и assert
# Инструкция raise возбуждает заданное исключение

# raise <Экземпляр класса>
# raise <Название класса>
# raise <Экземпляр или название класса> from <Объект исключения>
# raise
try:
    raise ValueError('WrongNumberOfPlayersError')
except ValueError as msg:
    print(msg)


class MyError(Exception):
    def __init__(self, value):
        self.msg = value

    def __str__(self):
        return self.msg


try:

    raise MyError('Описание исключения')
except MyError as err:
    print(err)
    print(err.msg)
raise MyError('Описание исключения')