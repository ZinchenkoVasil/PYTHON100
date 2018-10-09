def Game_001():
    import random
    N = random.randint(1, 100)

    while True:
        n = int(input("Введите число от 1 до 100: "))
        if N > n:
            print("Наше число больше!")
        elif N < n:
            print("Наше число меньше!")
        else:
            print("Да, это оно!")
            break
        repeat = int(input("Будете продолжать игру? (Да - нажмите клавишу [1], Нет - [0]): "))
        if not repeat:
            break

#лимит в 50 ходов на все партии
def Game_002():
    import random
    N = random.randint(1, 100)
    win = 0
    for i in range(50):
        n = int(input("Введите число от 1 до 100: "))
        if N > n:
            print("Наше число больше!")
        elif N < n:
            print("Наше число меньше!")
        else:
            print("Да, это оно!")
            N = random.randint(1, 100)
            print("Следующая партия!")
            win +=1
    print("Выигранных партий: ", win)


#Game_002()


