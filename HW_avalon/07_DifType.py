def Dubl_001():
    n = int(input("введите число n: "))
    s = input("введите строку s: ")
    s = s * n
    print(s)

def Steps_002():
    n = int(input("введите число n: "))
    for i in range(1, n+1):
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
            if len(word) in dict_words:
                dict_words[len(word)] += 1
            else:
                dict_words[len(word)] = 1
    for item in dict_words.items():
        print("длины - ", item[0] ," ", item[1], " слова")

#Dubl_001()
#Steps_002()
UseDict_004()


