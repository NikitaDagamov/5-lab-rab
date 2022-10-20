I = int(input("Введите число от 0 до 255: "))
Z = int(input("Введите целевую систему счисления(2 или 8): "))
s = ""
if Z == 2:
    while I > 0:
        s = str(I % Z) + s
        I //= Z
print(s)
if Z == 8:
    while I > 0:
        s = str(I % Z) + s
        I //= Z
print(s)
if I < 0 or I > 255 and Z != 2 and 8:
    print("Ошибка, перечитайте условия для ввода")
