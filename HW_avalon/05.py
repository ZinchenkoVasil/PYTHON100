def Calculate_001():
    x = float(input("введите x: "))
    y = float(input("введите y: "))
    z = float(input("введите z: "))
    f = float(input("введите f: "))
    result = (x*(y - x)/z + x + (f + z)/(f ** y) - (z - f)/z)/((z + f)/(z ** y) - f)
    print("Результат: ", result)

