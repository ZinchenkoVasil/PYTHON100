#Получение монет
#получение кол-ва монет
def get_A1_B1(Z, X, Y, A, B):
    A1 = Z // X  #вычислем кол-во требуемых монет 1 типа
    if A < A1:   #кол-во трубыемых монет превышает кол-во монет в наличии
        A1 = A   #
    C = Z - A1*X #вычисляем остаток
    if C % Y == 0: #проверка можно ли разбить остаток на монеты 2 типа
        B1 = C // Y #вычислем кол-во требуемых монет 2 типа
        if B1 > B:  #кол-во трубыемых монет превышает кол-во монет в наличии
            return []
        else:
            return [A1, B1]#выводим получившееся кол-во монет обоих типов
    else:
        return [] #нельзя разбить остаток на монеты 2 типа

#слайд 11 задача1
def Task_001():
    X = 5
    Y = 10
    A = int(input("введите количество 5-рублевых монет: "))
    B = int(input("введите количество 10-рублевых монет: "))
    Z = int(input("введите сумму: "))
    if X*A + B*Y >= Z:
        lst = get_A1_B1(Z, X, Y, A, B)
        if lst:
            print("5-рублевых монет: ", lst[0])
            print("10-рублевых монет: ", lst[1])
        else:
            lst = get_A1_B1(Z, Y, X, B, A)
            if lst:
                print("5-рублевых монет: ", lst[1])
                print("10-рублевых монет: ", lst[0])
            else:
                print("получить введеную сумму нельзя")
    else:
        print("получить введеную сумму нельзя")

def Task_002():
    a = input("введите число: ")
    print("кол-во разрядов: ", len(a))

    # проверка на полиандром
def Task_003():
    str = input("строка: ")
    i = len(str)
    str2 = str[::-1]
    if str == str2:
        print("полиандром")
    else:
        print('не полиандром')

#замена подстроки в строке
def Task_004():
    Str = input("строка: ")
    subStrDelete = input("подстрока в строке, которую надо заменить: ")
    subStrInsert = input("подстрока, на которую надо заменить: ")
    Len = len(subStrDelete)
    lst = list(Str)
    n = 0
    Exists = False
    while True:
        n = Str.find(subStrDelete, n)
        if n == -1:
            break
        else:
            Exists = True
            lst[n:n+Len] = subStrInsert
            n += 1

    if Exists:
        s = '';
        for i in lst:
            s = s + i
        print("Измененная строка: ", s)
    else:
        print("данной подсторки в строке не существует!")

#Task_002()