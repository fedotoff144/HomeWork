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
        choice = int(input('ВЫБЕРИТЕ MЕНЮ:\n1. Пополнить\n'
                           '2. Снять\n3. Посмотреть историю\n0. Выйти\n'))
        match choice:
            case 0:
                exit('Пока!')
            case 1:
                print(f'На вашем счету: {bank_account}')
                amount = int(input('Введите сумму пополнения: '))
                refill(amount)
            case 2:
                print(f'На вашем счету: {bank_account}')
                amount = int(input('Введите сумму снятия: '))
                withdrawing_money(amount)
            case 3:
                read_history()
            case _:
                print('Команда не найдена.')


def refill(amount):
    global bank_account
    global count_operations

    increased_tax = wealth_tax(amount)
    if increased_tax:
        record = f'Налог на богатство: -{increased_tax}'
        history.append(record)
        bank_account -= increased_tax
        print(f'{record}, \tОстаток на счете: {bank_account}')

    additional_bonus = bonus(amount)
    bank_account += amount + additional_bonus
    count_operations += 1

    record = f'Сумма пополнения: {amount}, \t' \
             f'Дополнительный бонус: {additional_bonus}, \t' \
             f'ИТОГО на счете: {bank_account}'
    history.append(record)
    print(record)


def withdrawing_money(amount):
    global bank_account
    global count_operations

    increased_tax = wealth_tax(amount)
    if increased_tax:
        record = f'Налог на богатство: -{increased_tax}'
        history.append(record)
        bank_account -= increased_tax
        print(f'{record}, Остаток на счете: {bank_account}')

    additional_bonus = bonus(amount)
    commission = set_commission(amount)
    if bank_account < (amount + commission) + additional_bonus:
        print('На счете недостаточно средств')
        return None
    bank_account -= (amount + commission) + additional_bonus

    count_operations += 1

    record = f'Сумма снятия: {amount}, \t' \
             f'Комиссия за снятие: -{commission}, \t' \
             f'Дополнительный бонус: {additional_bonus}, \t' \
             f'ИТОГО на счете: {bank_account}'
    history.append(record)
    print(record)


def input_validation(mes):
    while True:
        try:
            number = int(input(mes))
            break
        except:
            print('Ошибка. Попробуйте еще раз: ')

    return number


def multiplicity_check(mes):
    num = input_validation(mes)
    if num % STEP != 0:
        multiplicity_check('Сумма должна быть кратна 50. Повторите ввод: ')
    return num


def wealth_tax(amnt):
    fee = 0
    if bank_account >= MAX_AMOUNT:
        fee = amnt * WEALTH_TAX
        return fee
    return fee


def bonus(amnt):
    additional_bonus = 0
    if count_operations != 0 and count_operations % 3 == 0:
        additional_bonus = amnt * BONUS
        return additional_bonus
    return additional_bonus


def set_commission(amnt):
    percent_mnt = amnt * WITHDRAWAL_FEE
    if percent_mnt < LOWER_LIMIT:
        return LOWER_LIMIT
    elif percent_mnt > UPPER_LIMIT:
        return UPPER_LIMIT
    return percent_mnt


def read_history():
    for i in history:
        print(i)


start_menu()
