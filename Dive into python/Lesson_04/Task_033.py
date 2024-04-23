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
count_operations: int = 1
transaction_history = ['ИСТОРИЯ ОПЕРАЦИЙ:']


def start_menu():
    while True:
        choice = input_validation('ВЫБЕРИТЕ MЕНЮ:\n1. Пополнить\n'
                                  '2. Снять\n3. Посмотреть историю\n0. Выйти\n')
        match choice:
            case 0:
                exit('До свидания!')
            case 1:
                print(f'На вашем счету: {bank_account}')
                amount = check_step('Введите сумму пополнения: ')
                refill(amount)
            case 2:
                print(f'На вашем счету: {bank_account}')
                amount = check_step('Введите сумму снятия: ')
                withdrawing_money(amount)
            case 3:
                read_history()
            case _:
                print('Команда не найдена.')


def input_validation(mes):
    """Prompts the user to input a number and validates the input
    to ensure it is an integer.
    """

    while True:
        try:
            number = int(input(mes))
            break
        except ValueError:
            mes = 'Ошибка. Попробуйте еще раз: '
    return number


def check_step(mes):
    """Checks whether a number is a multiple of the specified step."""
    while True:
        num = input_validation(mes)
        if num % STEP == 0:
            return num
        mes = 'Сумма должна быть кратна 50. Повторите ввод: '


def refill(amount):
    global bank_account
    global count_operations

    increased_tax = wealth_tax(amount)
    fee_for_rich(increased_tax)
    additional_bonus = bonus(amount)

    bank_account += amount + additional_bonus
    count_operations += 1

    record = f'Сумма пополнения: {amount}, \t' \
             f'Дополнительный бонус: {additional_bonus}, \t' \
             f'ИТОГО на счете: {bank_account}'
    write_history(record)


def withdrawing_money(amount):
    global bank_account
    global count_operations

    increased_tax = wealth_tax(amount)
    fee_for_rich(increased_tax)

    additional_bonus = bonus(amount)
    commission = set_commission(amount)
    if bank_account < (amount + commission) + additional_bonus:
        print('На счете недостаточно средств')
        return None

    bank_account -= (amount + commission) - additional_bonus
    count_operations += 1

    record = f'Сумма снятия: {amount}, \t' \
             f'Комиссия за снятие: -{commission}, \t' \
             f'Дополнительный бонус: {additional_bonus}, \t' \
             f'ИТОГО на счете: {bank_account}'
    write_history(record)


def fee_for_rich(increased_tax):
    global bank_account
    if increased_tax:
        bank_account -= increased_tax
        record = f'Налог на богатство: -{increased_tax}, \t' \
                 f'Остаток на счете: {bank_account}'
        write_history(record)


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


def write_history(record):
    print(record)
    transaction_history.append(record)


def read_history():
    for i in transaction_history:
        print(i)


start_menu()
