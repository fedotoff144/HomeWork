"""
    1. Решить задачи, которые не успели решить на семинаре.
    2. В модуль с проверкой даты добавьте возможность запуска в терминале
       с передачей даты на проверку.

Основная задача:
Задача: Расчет финансовых показателей портфеля акций

Описание задачи:
Вы являетесь инвестором и хотите создать программу для расчета нескольких
финансовых показателей вашего портфеля акций. Создайте модуль Python
под названием "portfolio.py", который будет содержать функции
для выполнения следующих операций:

    1. Расчет общей стоимости портфеля акций:
       Функция calculate_portfolio_value(stocks: dict, prices: dict) -> float
       принимает два аргумента: stocks - словарь,
       где ключами являются символы акций (например, "AAPL" для Apple Inc.),
       и значениями - количество акций каждого символа. prices - словарь,
       где ключами являются символы акций, а значениями -
       текущая цена каждой акции. Функция должна вернуть
       общую стоимость портфеля акций на основе количества акций
       и их текущих цен. Пример: Пришло

stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}

Вышло:
16410,25

    1. Расчет доходности портфеля:
    Функция calculate_portfolio_return(initial_value: float, current_value: float) -> float
    принимает два аргумента: initial_value - начальная стоимость портфеля акций.
    current_value - текущая стоимость портфеля акций.
    Функция должна вернуть процентную доходность портфеля. Пример:

Пришло:
10000.0
15000.0
Вышло:
50%

    1. Определение наиболее прибыльной акции:
    Функция get_most_profitable_stock(stocks: dict, prices: dict) -> str
    принимает два аргумента: stocks - словарь с акциями и их количеством.
    prices - словарь с акциями и их текущими ценами.
    Функция должна вернуть символ акции (ключ), которая имеет наибольшую прибыль
    по сравнению с ее начальной стоимостью. Начальная стоимость -
    первый вызов calculate_portfolio_value, данные из этого вызова
    следует сохранить в защищенную переменную на уровне модуля.

Пример:
Пришло:
stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
prices = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
Вышло:
MSFT


Тестирование модуля:

Напишите небольшую программу, которая импортирует модуль "portfolio.py"
и демонстрирует использование всех трех функций.

Создайте словари для акций и цен, запустите функции и выведите результаты.
Примечание:
В реальном мире вы можете использовать API для получения актуальных данных
о ценах акций. В данной задаче можно использовать фиктивные данные
для тестирования и обучения.
"""
from pack_of_modules import portfolio

stocks = {"GAZP ": 18, "VTBR": 1013, "SBPR": 63, "AFLT": 113}
prices = {"GAZP ": 174.64, "VTBR": 0.02766, "SBPR": 258.34, "AFLT": 44.17}
current_prices = {"GAZP ": 154.64, "VTBR": 1.02766, "SBPR": 358.34, "AFLT": 34.17}


def different_prices(initial_praces: dict, current_prices: dict) -> dict:
    result: dict = {}
    for key in initial_praces.keys():
        result[key] = portfolio.calculate_portfolio_return(initial_value=initial_praces[key],
                                                           current_value=current_prices[key])
    return result


total_portfolio_value: float = portfolio.calculate_portfolio_value(stocks, prices)
diff_prices: dict = different_prices(prices, current_prices)
most_profit: str = portfolio.get_most_profitable_stock(diff_prices)


print(total_portfolio_value)
print(diff_prices)
print(most_profit)
