import sys
eq = input("Введите температуру и размерность через пробел ")
eq_split = eq.strip().split()

try:
    float(eq_split[-1])
    float(eq_split[0])
except ValueError:
    print(f"Выражение начинается или заканчивается знаком")
    sys.exit(1)

i = 0
while i < len(eq_split)-1:
    if eq_split[i] in ("*", "/"):
        try:
            left = float(eq_split[i-1])
            right = float(eq_split[i+1])
        except ValueError:
            print(f"Ошибка синтаксиса в {eq_split[i-1]} {eq_split[i]} {eq_split[i+1]}")
            sys.exit(1)
        if eq_split[i] == "/":
            if right == 0:
                print ("Деление на ноль")
                sys.exit(1)
            else:
                result = left/right
        else:
            result = left*right
        eq_split[i - 1:i + 2] = [str(result)]
        i = 0
    i += 1

j = 0
while j < len(eq_split)-1:
    if eq_split[j] == "+" or eq_split[j] == "-":
        if eq_split[j] == "+":
            result = float(eq_split[j-1]) + float(eq_split[j+1])
        else:
            result = float(eq_split[j-1]) - float(eq_split[j+1])
        eq_split[j - 1:j + 2] = [str(result)]
        j = 0
    j += 1
print(f"{eq} = {float(eq_split[0])}")

"""
Напиши программу, которая принимает на вход строку вида:
```
12 + 7 * 3 - 4 / 2
```
и вычисляет результат (без использования `eval`).

думаю скобки лучше не добавлять))00
"""