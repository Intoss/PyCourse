"""### 4. Генератор паролей

Программа запрашивает у пользователя:

* длину пароля
* нужно ли использовать цифры, буквы, спецсимволы
  и возвращает сгенерированный пароль.

---"""
import random

while True:
    length = input("Введите длину пароля ")
    try:
        length = int(length)
        if length > 7 and length < 31:
            break
        if length > 30:
            print("Пароль слишком длинный")
        else:
            print("Пароль должен быть больше 8 символов")
    except:
        print("Неверная длина пароля, введите еще раз")

while True:
    while True:
        let = input("Использовать буквы? y/n ")
        if let in ("y", "n"):
            break
        else:
            print("Неверный знак, попробуйте еще раз")
    while True:
        numb = input("Использовать цифры? y/n ")
        if numb in ("y", "n"):
            break
        else:
            print("Неверный знак, попробуйте еще раз")
    while True:
        character = input("Использовать специальные символы? y/n ")
        if character in ("y", "n"):
            break
        else:
            print("Неверный знак, попробуйте еще раз")

    if "y" in (let, numb, character):
        break
    else:
        print("Пароль не может быть без знаков")

l_symbol = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "—", "_", "+", "=",
";", ":", ",", ".", "/", "?", "|", "`", "~", "[", "]", "{", "}"]
l_char = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
          "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
password = []

if character == "y":
    t = random.choice(l_symbol)
    password += str(t)
if numb == "y":
    t = random.randint(0, 9)
    password += str(t)
if let == "y":
    t = random.choice(l_char)
    password += str(t)

i=0
while i < length:
    t_t = random.randint(1, 6)
    if t_t == 1:
        if character == "y":
            t = random.choice(l_symbol)
            password += str(t)
            i += 1
    elif t_t > 1 and t_t < 3:
        if numb == "y":
            t = random.randint(0, 9)
            password += str(t)
            i += 1
    else:
        if let == "y":
            t = random.choice(l_char)
            password += str(t)
            i += 1
random.shuffle(password)
password = ''.join(password)
print(password)






