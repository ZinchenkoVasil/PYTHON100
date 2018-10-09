def Dubl_001():
    n = int(input("введите число n: "))
    s = input("введите строку s: ")
    s = s * n
    print(s)

def Steps_002():
    n = int(input("введите число n: "))
    for i in range(n):
        print('=' * i)

def UseDict_003():
    String = input("введите строку: ")
    dict_literas = {}
    for litera in String:
        if litera in dict_literas:
            dict_literas[litera] += 1
        else:
            dict_literas[litera] = 1

    print(dict_literas)


def UseDict_004():
    String = input("введите предложение: ")
    words = String.split(' ')
    dict_words = {}
    for word in words:
        if not (word in dict_words):
            dict_words[word] = len(word)

    print(dict_words)

#Dubl_001()
#Steps_002()
#UseDict_004()


