def FromNumber10ToNumber16(number10):
    lst16 = '0123456789ABCDEF'
    buf = ''
    while number10 > 0:
        buf = buf + lst16[number10 % 16]
        number10 = number10 // 16
    i = len(buf)
    return buf[::-1]

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

#перевод из 10-чной в 8-чную
def FromNumber10ToNumber8(number10):
    buf = ''
    while number10 > 0:
        buf = buf + str(number10 % 8)
        number10 = number10 // 8
    return buf[::-1]

#перевод из 8-чной в 10-чную
def FromNumber8ToNumber10(strNumber8):
    strNumber8 = strNumber8[::-1]
    j = 0
    buf = 0
    for s in strNumber8:
        buf = buf + int(s) * 8 ** j
        j +=1
    return buf


#8 -> 16
def Task_001():
    #8 -> 10
    strNumber8 = input("введите число в 8-ичном формате: ")
    number10 = FromNumber8ToNumber10(strNumber8)
    #10 -> 16
    Number16 = FromNumber10ToNumber16(number10)
    print("число в 16-ричном формате: ", Number16)

#16 -> 8
def Task_002():
    #16 -> 10
    strNumber16 = input("введите число в 16-ичном формате: ")
    number10 = FromNumber16ToNumber10(strNumber16)
    #10 -> 8
    Number8 = FromNumber10ToNumber8(number10)
    print("число в 8-ричном формате: ", Number8)

#Task_002()



