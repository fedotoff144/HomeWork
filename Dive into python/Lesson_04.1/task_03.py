"""
У вас есть банковская карта с начальным балансом равным 0 у.е.
Вы хотите управлять этой картой, выполняя следующие операции,
для выполнения которых необходимо написать следующие функции:

check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
deposit(amount): Пополнение счёта.
withdraw(amount): Снятие денег.
exit(): Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.

Пополнение счета:
Функция deposit(amount) позволяет клиенту пополнять свой счет
на определенную сумму. Пополнение счета возможно только на сумму,
которая кратна MULTIPLICITY.

Снятие средств:
Функция withdraw(amount) позволяет клиенту снимать средства со счета.
Сумма снятия также должна быть кратной MULTIPLICITY.
При снятии средств начисляется комиссия в процентах от снимаемой суммы,
которая может варьироваться от MIN_REMOVAL до MAX_REMOVAL.

Завершение работы:
Функция exit() завершает работу с банковским счетом.
Перед завершением, если на счету больше RICHNESS_SUM,
начисляется налог на богатство в размере RICHNESS_PERCENT процентов.

Проверка кратности суммы:
Функция check_multiplicity(amount) проверяет, кратна ли сумма amount
заданному множителю MULTIPLICITY. Реализуйте программу для управления
банковским счетом, используя библиотеку decimal для точных вычислений.

Пример

На входе:
deposit(10000)
withdraw(4000)
exit()

print(operations)

На выходе:
['Пополнение карты на 10000 у.е. Итого 10000 у.е.', 'Снятие с карты 4000 у.е. Процент за снятие 60 у.е.. Итого 5940 у.е.']

На входе:
deposit(1000)
withdraw(200)
exit()

print(operations)

На выходе:
['Пополнение карты на 1000 у.е. Итого 1000 у.е.', 'Снятие с карты 200 у.е. Процент за снятие 30 у.е.. Итого 770 у.е.', 'Возьмите карту на которой 770 у.е.']

На входе:
deposit(1000)
withdraw(200)
withdraw(300)
deposit(500)
withdraw(3000)
exit()

print(operations)

На выходе:
['Пополнение карты на 1000 у.е. Итого 1000 у.е.', 'Снятие с карты 200 у.е. Процент за снятие 30 у.е.. Итого 770 у.е.', 'Снятие с карты 300 у.е. Процент за снятие 30 у.е.. Итого 440 у.е.', 'Пополнение карты на 500 у.е. Итого 940 у.е.', 'Недостаточно средств. Сумма с комиссией 3045.000 у.е. На карте 940 у.е.', 'Возьмите карту на которой 940 у.е.']
На входе:


deposit(173)
withdraw(21)
exit()

print(operations)

На выходе:
Сумма должна быть кратной 50 у.е.
Сумма должна быть кратной 50 у.е.
['Недостаточно средств. Сумма с комиссией 51 у.е. На карте 0 у.е.', 'Возьмите карту на которой 0 у.е.']

На входе:
deposit(1000000000000000)
withdraw(200)
withdraw(300)
deposit(500)
withdraw(3000)
exit()

print(operations)

На выходе:
['Пополнение карты на 1000000000000000 у.е. Итого 1000000000000000 у.е
"""
import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)  # some explanation
MIN_REMOVAL = 30
MAX_REMOVAL = 600
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(5_000_000)

CMD_REPLENISH = 'r'
CMD_WITHDRAW = 'w'
CMD_EXIT = 'e'

bank_account = decimal.Decimal(0)
count = 0
operations = []


# Проверка кратности суммы при пополнении и снятии.
def check_multiplicity(amount)->bool:
    
    pass


# Пополнение счёта.
def deposit(amount):
    pass


# Снятие денег.
def withdraw(amount):
    pass


# Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.
def exit():
    pass


while True:
    cmd = input(
        f'Enter command ({CMD_REPLENISH} = replenish, {CMD_WITHDRAW} = withdraw, '
        f'{CMD_EXIT} = exit:\n')
    if cmd == CMD_EXIT:
        print(f'Balance: {bank_account}\nBy-by')
        break
    if bank_account > RICHNESS_SUM:
        tax_amount = bank_account * RICHNESS_PERCENT
        bank_account = bank_account - tax_amount
        print(f'The wealth tax has been written off in the amount of '
              f'{tax_amount}. Balance: {bank_account}')
    if cmd in (CMD_REPLENISH, CMD_WITHDRAW):
        amount = decimal.Decimal(
            input(f'Enter amount multimple {MULTIPLICITY} :\n'))
        while amount % MULTIPLICITY:
            amount = decimal.Decimal(
                input(f'Enter amount multimple {MULTIPLICITY} :\n'))
        if cmd == CMD_WITHDRAW:
            withdrawal_fee = amount * PERCENT_REMOVAL
            withdrawal_fee = MIN_REMOVAL if withdrawal_fee < MIN_REMOVAL else \
                MAX_REMOVAL if withdrawal_fee > MAX_REMOVAL else withdrawal_fee
            withdrawal_amount = amount + withdrawal_fee
            if bank_account > withdrawal_amount:
                bank_account = bank_account - withdrawal_amount
                print(
                    f'Transaction amount = {amount}, withdrawal commission = {withdrawal_fee}, balance = {bank_account}')
                count += 1
            else:
                print(
                    f'Insufficient funds. Balance: {bank_account}. Withdrawal amount = {withdrawal_amount}.')
        elif cmd == CMD_REPLENISH:
            bank_account += amount
            print(f'Your balance is {bank_account}')
            count += 1

        if count % COUNTER4PERCENTAGES == 0:
            bonus = bank_account * PERCENT_DEPOSIT
            bank_account = bank_account + bonus
            print(
                f'You have performed three operations. Your bonus is {bonus}. Balance is '
                f'{bank_account}')
