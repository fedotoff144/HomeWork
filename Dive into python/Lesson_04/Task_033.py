"""
Задача №6
Напишите программу банкомат.
Начальная сумма равна нулю
Допустимые действия: пополнить, снять, выйти
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третей операции пополнения или снятия начисляются проценты - 3%
Нельзя снять больше, чем на счёте
При превышении суммы в 5 млн, вычитать налог на богатство
10% перед каждой операцией, даже ошибочной
Любое действие выводит сумму денег
Разбейте задачу на отдельные операции — функции. Дополнительно сохраняйте
все операции поступления и снятия средств в список.
"""

STEP = 50
WITHDRAWAL_FEE = 0.015
BONUS = 0.03
UPPER_LIMIT = 600
LOWER_LIMIT = 30
MAX_AMOUNT = 5_000_000
WEALTH_TAX = 0.1
bank_account = 0
count_operations: int = 0
history = []


def input_validation(mes):
    while True:
        try:
            number = int(input(mes))
            return number
        except:
            print('Ошибка. Попробуйте еще раз.')


def refill():
    global bank_account
    global count_operations
    amount = input_validation(f'Введите сумму пополнения кратную {STEP}у.е.: ')
    if amount % STEP != 0:
        refill()
    else:
        bank_account += amount
        count_operations += 1


def withdrawing_money():
    amount = input_validation(f'Введите сумму снятия: ')


def log_history(**kwargs):
    global history
    return history.append(kwargs)


def read_history():
    global history
    for i in history:
        print(i)


def start_menu():
    choice = input_validation('ВЫБЕРИТЕ MЕНЮ:\n1. Пополнить\n2. Снять\n3. Посмотреть историю\n0. Выйти\n')
    match choice:
        case 0:
            exit('Пока!')
        case 1:
            refill()
        case 2:
            withdrawing_money()
        case 3:
            read_history()
        case _:
            print('Команда не найдена.')
            start_menu()

start_menu()
