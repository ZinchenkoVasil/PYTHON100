def while_001():
    dist = 0
    day = 1
    while dist < 1000:
        dist += 2**day
        day += 1
    print(day - 1)

#Слайд 8 задача 2
def while_002():
    d = 3
    simple = 2
    listSimple = [2]
    i = 2
    while d < 1000:
        simple += 1
        for n in listSimple:
            if simple % n == 0:
                break
        else:
            d = d + simple
            listSimple.append(simple)
            print(simple)
            i += 1
    print("дней = ",i)


def while_003():
    d = 1
    dist = 10
    while d <= 30:
        dist = dist + dist * 0.15
        d += 1
    print(dist)

def while_004():
    d = 1
    dist = 10
    while dist < 100:
        dist = dist + dist * 0.1
        d += 1

    print("спортсмен пробежал 100 км за: ", d - 1, "дней")
    d = 1
    dist = 10
    step = 10
    while step < 20:
        step = dist * 0.1
        dist = dist + step
        d += 1
    print("спортсмен пробежал 20 км в день через: ", d - 1, "дней")
#while_004()