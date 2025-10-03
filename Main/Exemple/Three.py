"""### 3. Банкомат

Сделай консольное приложение:

* У пользователя есть баланс (например, 10 000).
* Он может вводить команды: `пополнить`, `снять`, `баланс`, `выход`.
* Снятие наличных возможно только, если хватает денег.
* Все операции логируются в список (или словарь с временем)."""
from datetime import datetime, timedelta
money = 10000
ex = 1
log = {}
while ex:
    oper = input("Введите действие \n")
    oper = oper.lower().strip()
    if oper == "выход":
        ex = 0
    elif oper == "пополнить":
        replenish = input("Введите сумму пополнения \n")
        try:
            replenish = int(replenish)
            log[datetime.now().strftime("%d.%m.%y %H:%M:%S")] = str(f"{oper} - {replenish}")
            if replenish > 0:
                money = money + replenish
            elif replenish == 0:
                print("Круто придумал, баланс - 0")
                money = 0
            else:
                print("Сумма пополнения не может быть отрицательной")
        except ValueError:
            log[datetime.now().strftime("%d.%m.%y %H:%M:%S")] = str(f"Ошибка:{oper} - {replenish}")
            print("Некорректная сумма")
    elif oper == "снять":
        replenish = input("Введите сумму снятия \n")
        try:
            replenish = int(replenish)
            log[datetime.now().strftime("%d.%m.%y %H:%M:%S")] = str(f"{oper} - {replenish}")
            if replenish != 0 and replenish<money:
                money = money - abs(replenish)
            elif replenish > money:
                print("Недостаточно средств")
            elif replenish == 0:
                print("Круто придумал, баланс - 0")
                money = 0
        except ValueError:
            log[datetime.now().strftime("%d.%m.%y %H:%M:%S")] = str(f"Ошибка:{oper} - {replenish}")
            print("Некорректная сумма")
    elif oper == "баланс":
        log[datetime.now().strftime("%d.%m.%y %H:%M:%S")] = str(f"{oper} - {money}")
        print(f"Текущий баланс - {money}")
    elif oper == "лог":
        print(log)
    else:
        log[datetime.now().strftime("%d.%m.%y %H:%M:%S")] = str(f"Ошибка:{oper}")
        print("Неизвестная операция")


