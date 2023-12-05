'''

'''

def check(x1, y1, x2, y2):
    if x1 < 1 or x1 > 8 or y1 < 1 or y1 > 8 or x2 < 1 or x2 > 8 or y2 < 1 or y2 > 8:
        return "Координаты поля должны быть в диапазоне от 1 до 8!!!"

    c1 = (x1 + y1) % 2 == 0  
    c2 = (x2 + y2) % 2 == 0  

    if c1 == c2:
        return "Поля ({}, {}) и ({}, {}) одного цвета.".format(x1, y1, x2, y2)
    else:
        return "Поля ({}, {}) и ({}, {}) разного цвета.".format(x1, y1, x2, y2)

x1 = int(input("Значение x первого поля: "))
y1 = int(input("Значение y первого поля: "))
x2 = int(input("Значение x второго поля: "))
y2 = int(input("Значение y второго поля: "))

r = check(x1, y1, x2, y2)
print(r)