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


print("Введите номер задачи (2/4/6/8)")
x = int(input())
if x == 2:
    num2()
elif x == 4:
    num4()
elif x == 6:
    num6()
elif x == 8:
    num8()
else:
    print("Задача не найдена")
