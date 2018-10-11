def FillList_001(N):
    lst = list(range((N + 2) * N))
    print(lst)


def Duplicate_002(N):
    lst1 = list(range((N + 2) * N))
    lst2 = [number + 1 for number in range((N + 2) * N)]
    lst = lst1 + lst2
    print(lst)
    return lst

def SelectList_003():
    lst = Duplicate_002()
    lst2 = lst[-2:0:-1]
    print(lst2)


def Filter_004():
    lst_out = []
    lst_in = Duplicate_002()
    i = 0
    while i < len(lst_in):
        if i % 3 == 1:
            lst_out.append(lst_in[i])
        i += 1
    print(lst_out)

def Filter_005():
    lst_out = []
    lst_in = Duplicate_002()
    i = 0
    while i < len(lst_in):
        if i % 3 == 1:
            lst_out.append(lst_in[i])
        i += 1
    print(lst_out)
    print("Длина получившейся последовательности: ", len(lst_out))



#FillList_001()
#Duplicate_002()
#SelectList_003()
#Filter_005()

