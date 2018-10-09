#перевод из 1 с-мы в другую
#перевод из 10-чной в 2-чную
def FromNumber10ToNumber2(number10):
    buf = ''
    while number10 > 0:
        buf = buf + str(number10 % 2)
        number10 = number10 // 2
    i = len(buf)
    return buf[::-1]

def FromNumber10ToNumber16(number10):
    lst16 = '0123456789ABCDEF'
    buf = ''
    while number10 > 0:
        buf = buf + lst16[number10 % 16]
        number10 = number10 // 16
    i = len(buf)
    return buf[::-1]

#перевод из 2-чной в 10-чную
def FromNumber2ToNumber10(strNumber2):
    strNumber2 = strNumber2[::-1]
    j = 0
    buf = 0
    for s in strNumber2:
        buf = buf + int(s) * 2 ** j
        j +=1
    return buf

#перевод из 16-чной в 10-чную
def FromNumber16ToNumber10(strNumber16):
    lst16 = '0123456789ABCDEF'
    strNumber16 = strNumber16[::-1]
    j = 0
    buf = 0
    for s in strNumber16:
        buf = buf + lst16.find(s) * 16 ** j
        j +=1
    return buf

#Слайд 12
def Task_001():
    number10 = int(input("введите число в 10-чном формате: "))
    strNumber2 = FromNumber10ToNumber2(number10)
    print("число в двоичном формате: ", strNumber2)

def Task_002():
    strNumber2 = input("введите число в 2-ичном формате: ")
    number10 = FromNumber2ToNumber10(strNumber2)
    print("число в десятичном формате: ", number10)

#16->10
def Task_003():
    strNumber16 = input("введите число в 16-ичном формате: ")
    number10 = FromNumber16ToNumber10(strNumber16)
    print("число в десятичном формате: ", number10)

#10 -> 16
def Task_004():
    number10 = int(input("введите число в 10-чном формате: "))
    strNumber16 = FromNumber10ToNumber16(number10)
    print("число в 16-чном формате: ", strNumber16)

#16 -> 2
def Task_005():
    strNumber16 = input("введите число в 16-ичном формате: ")
    #каждая буква - 4 двоичные цифры
    dict16 = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
              '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    strNumber2 = ''
    for c in strNumber16:
        strNumber2 += dict16[c]
    print("число в 2-ичном формате: ", strNumber2)

#2 -> 16
def Task_006():
    lst16 = '0123456789ABCDEF'
    strNumber2 = input("введите число в 2-ичном формате в виде xxxx.xxxx.xxxx (ставьте '.' между каждыми 4 двоичными цифрами): ")
    lstNumber2 = strNumber2.split('.')
    strNumber16 = ''
    for number2 in lstNumber2:
#2->10
        number10 = FromNumber2ToNumber10(number2)
        strNumber16 += lst16[number10]
    print("число в 16-чном формате: ", strNumber16)

#Task_003()
#Task_006()
