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
bank_account: int = 0
count_operations: int = 0
history = []


def start_menu():
    while True:
        choice = input_validation('ВЫБЕРИТЕ MЕНЮ:\n1. Пополнить\n'
                                  '2. Снять\n3. Посмотреть историю\n0. Выйти\n')
        match choice:
            case 0:
                exit('Пока!')
            case 1:
                amount = input_validation('Введите сумму пополнения: ')
                valid_amount = multiplicity_check(amount)
                refill(valid_amount)
            case 2:
                withdrawing_money()
            case 3:
                read_history()
            case _:
                print('Команда не найдена.')


def refill(amount):
    global bank_account
    global count_operations

    # if bank_account >= MAX_AMOUNT:
    #     wealth_tax = amount * 0.1
    #     bank_account -= bank_account + amount - wealth_tax
    #     record = f'Внесено: {amount}, Налог на богатство: -{wealth_tax}, ИТОГО на счете: {bank_account}'
    # if count_operations % 3 == 0:
    #     record = f'Внесено: {chacked_amount}, Бонус: {chacked_amount * 0.03}, ИТОГО на счете: {bank_account}'
    #     chacked_amount += chacked_amount * 0.03
    # else:
    #     record = f'Внесено: {chacked_amount}, Бонус: 0, ИТОГО на счете: {bank_account}'

    bank_account += amount
    count_operations += 1
    # history.append(record)
    # print(record)
    start_menu()


def withdrawing_money():
    global count_operations
    user_input = input_validation(f'Введите сумму снятия: ')
    amount = multiplicity_check(user_input)
    tax_payment = amount * WITHDRAWAL_FEE
    if LOWER_LIMIT < tax_payment:
        count_operations -= LOWER_LIMIT + amount
    elif UPPER_LIMIT > tax_payment:
        count_operations -= UPPER_LIMIT + amount
    else:
        count_operations -= tax_payment + amount
    start_menu()


def input_validation(mes):
    try:
        number = int(input(mes))
        return number
    except:
        input_validation('Ошибка. Попробуйте еще раз: ')


def multiplicity_check(num):
    while True:
        if num % STEP == 0:
            return num
        print('Сумма должна быть кратна 50. Повторите ввод: ')


def read_history():
    for i in history:
        print(i)


def wealth_tax(payment):
    global bank_account
    if bank_account > 5_000_000:
        payment -= payment * 0.1
    return payment


start_menu()
