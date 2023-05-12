def num2():
    print("Введите трехзначное число")
    Number = input()
    Sum = int(Number[0]) + int(Number[1]) + int(Number[2])
    print(Sum)


def num4():
    print("Введите имя ребенка (Петя, Катя или Сережа)")
    name = input()
    if name == "Катя":
        print("Введите количество ")
        Number = int(input())
        Peter = int(Number / 4)
        if Peter == 0:
            Peter = 1
        Sum = Peter * 2 + Number
        print(Sum)
    else:
        print("Введите количество ")
        Number = int(input())
        Sum = Number * 2 + Number * 4
        print(Sum)


def num6():
    print("Введите шестизначное число")
    Number = input()
    Sum1 = int(Number[0]) + int(Number[1]) + int(Number[2])
    Sum2 = int(Number[3]) + int(Number[4]) + int(Number[5])
    if Sum1 == Sum2:
        print("Счастливый")
    else:
        print("Обычный")


def num8():
    print("Введите первую сторону")
    n = int(input())
    print("Введите вторую сторону")
    m = int(input())
    print("Введите число долек")
    k = int(input())
    if n * m > k:
        if (k % n == 0) or (k % m == 0):
            print('Можно')
        else:
            print('Нельзя')
    else:
        print('Невыполнимое условие')


def num10():
    n = int(input())
    count_zero = 0
    count_one = 0
    for i in range(n):
        x = int(input())
    if x == 0:
        count_zero += 1
    else:
        count_one += 1
    if count_one > count_zero:
        print(count_zero)
    else:
        print(count_one)


def num12():
    x = int(input())
    y = int(input())
    for i in range(x):
        for j in range(y):
            if x == i + j and y == i * j:
                print(i, j)


def num14():
    n = int(input())
    i = 0
    while 2 ** i <= n:
        print(2 ** i)
    i += 1


def num16():
    N = abs(int(input('Введите количество элементов списка А: ')))
    A_entered = input("Введите через пробел элементы списка: ").split()
    A_num = list(map(int, A_entered))
    if len(A_num) != N:
        print('Введенные элементы не соответствуют заявленному количеству!')
    else:
        X = int(input('Введите число X, которое необходимо найти в списке: '))
        count = 0
        for i in range(N):
            if A_num[i] == X:
                count += 1
        print(f'Число {X} встречается в списке A {count} раз')


def num18():
    N = abs(int(input('Введите количество элементов списка А: ')))
    A_entered = input("Введите через пробел элементы списка: ").split()
    A_num = list(map(int, A_entered))
    if len(A_num) != N or N == 0:
        print('Введенные элементы не соответствуют заявленному количеству!')
    else:
        X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
        min = abs(X - A_num[0])
        index = 0
        for i in range(1, N):
            count = abs(X - A_num[i])
            if count < min:
                min = count
                index = i
        print(
            f'Число {A_num[index]} в списке A наиболее близко по величине к числу {X},'
            f' их разница составляет {abs(X - A_num[index])}')


def num20():
    eng = {1: 'AEIOULNSTR',
           2: 'DG',
           3: 'BCMP',
           4: 'FHVWY',
           5: 'K',
           8: 'JZ',
           10: 'QZ'}
    rus = {1: 'АВЕИНОРСТ',
           2: 'ДКЛМПУ',
           3: 'БГЁЬЯ',
           4: 'ЙЫ',
           5: 'ЖЗХЦЧ',
           8: 'ШЭЮ',
           10: 'ФЩЪ'}
    N = abs(int(input('Введите 1, если играем в английской раскладке, либо 0, если в русской: ')))
    word = input('Введите слово: ').upper()
    if N == 1:
        print('За это слово вы получаете', sum([k for i in word for k, v in eng.items() if i in v]), 'очков')
    elif N == 0:
        print('За это слово вы получаете', sum([k for i in word for k, v in rus.items() if i in v]), 'очков')
    else:
        print('Вы мухлюете и играете не по правилам!')


def num22():
    print("Введите первый список")
    a = input()
    print("Введите второй список")
    b = input()
    print(*sorted(set(a.split()) & set(b.split()), key=int))


def num24():
    n_bushes = int(input('Введите количество кустов черники: '))
    arr = list()
    for i in range(n_bushes):
        a = int(input(f'Введите количество ягод на кусте {i + 1}: '))
        arr.append(a)

    arr_count = list()
    for i in range(len(arr)):
        arr_count.append(arr[i - 2] + arr[i - 1] + arr[i])
    print(max(arr_count))


def num26():
    def recApowB(a, b):
        if b == 0:
            return 1
        return a * recApowB(a, b - 1)

    a = int(input('Введите число: '))
    b = int(input('Введите степень: '))
    print(recApowB(a, b))


def num28():
    def recsum(a, b):
        if b == 0:
            return a
        return 1 + recsum(a, b - 1)
    a = int(input('Введите число a:  '))
    b = int(input('Введите число b:  '))
    print(recsum(a, b))


print("Введите номер задачи (2/4/6/8/10/12/14/16/18/20/22/24/26/28)")
x = int(input())
if x == 2:
    num2()
elif x == 4:
    num4()
elif x == 6:
    num6()
elif x == 8:
    num8()
elif x == 10:
    num10()
elif x == 12:
    num12()
elif x == 14:
    num14()
elif x == 16:
    num16()
elif x == 18:
    num18()
elif x == 20:
    num20()
elif x == 22:
    num22()
elif x == 24:
    num24()
elif x == 26:
    num26()
elif x == 28:
    num28()
else:
    print("Задача не найдена")
