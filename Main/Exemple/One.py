import cmath

input_t = input("Введите температуру и размерность через пробел ")
split_t = input_t.split(" ")
if len(split_t) == 2:

    try:float_t = float(split_t[0])
    except ValueError: split_t[0], split_t[1] = split_t[1], split_t[0]

    try:float_t = float(split_t[0])
    except ValueError: print("Не введена температура")
    else:
        if split_t[1].upper() == "C" or split_t[1].upper() == "С":
            other_t = float_t * 9 / 5 + 32
            print(other_t)
        elif split_t[1].upper() == "F":
            other_t = (float_t - 32) * 5 / 9
            print(other_t)
        else:
            print("Единица измерения указанна некорректно")

elif len(split_t) > 2:
    print("Введен лишний аргумент")
elif len(split_t) < 2:
    print("Введен лишний аргумент")

