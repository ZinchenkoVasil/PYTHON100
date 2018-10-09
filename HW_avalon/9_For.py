#Задача 1 Слайд 9
def For_001():
    N = 10
    a = [1, 1]
    for i in range(2, N):
        a.append(a[i - 1] + a[i - 2])
    print(a[N - 1])


def For_002():
    N = int(input("введите число N:"))
    a = [1, 1 , 1]
    for i in range(3, N):
        a.append(a[i - 1] + a[i - 2] + a[i - 3])
    print(a[N - 1])

def For_003():
    N = int(input("введите число N:"))
    a = []
    for i in range(1,N,2):
        a.append(i*i)
    print(a)

def For_004():
    A = 10
    B = 5
    print('*'*A)
    for i in range(1,B):
        print('*' + ' ' * (A - 2) + '*')
    print('*'*A)

def For_005():
    A = 1
    B = 10
    sum = 0
    p = 1
    for i in range(A, B + 1):
        sum += i
        p *= i
    print('сумма: ',sum)
    print('произведение: ', p)

def For_006():
    A = 1
    B = 10
    lst1 = []
    lst2 = []
    for i in range(A + 1, B):
        if i % 2 == 0:
            lst1.append(i)
        else:
            lst2.append(i)

    print("Список четных: ", lst1)
    print("Список нечетных: ", lst2)

def For_007():
    lst = [-2, -1, 0, 1, 2]
    lst1 = []
    lst2 = []
    for i in lst:
        if i >= 0:
            lst1.append(i)
        else:
            lst2.append(i)

    print("Список положительных: ", lst1)
    print("Список отрицательных: ", lst2)


#For_007()