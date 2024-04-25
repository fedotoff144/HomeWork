__all__ = ['calculate_portfolio_value', 'get_most_profitable_stock',
           'clear_stock_original']

_primary_values: dict = {}


def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    sum_dict = {key: value * prices[key] for key, value in stocks.items()}

    global _primary_values
    if not _primary_values:
        _primary_values = sum_dict

    return sum(sum_dict.values())


def calculate_portfolio_return(initial_value: float,
                               current_value: float) -> float:
    result = current_value / initial_value * 100 - 100
    return result


def get_most_profitable_stock(stocks: dict, prices: dict) -> str:
    """Compares stock values with the original ones
    and returns the name of the most profitable stock
    """
    second_values = {key: value * prices[key] for key, value in stocks.items()}
    total_dict: dict = {}

    for key, value in second_values.items():
        temp_value = calculate_portfolio_return(_primary_values[key], value)
        total_dict[key] = temp_value

    max_total_value = max(total_dict.values())
    most_profit_stock = [key for key, value in total_dict.items() if
                         value == max_total_value]
    return most_profit_stock[0]


def clear_stock_original():
    """Clears the original dictionary"""
    global _primary_values
    return _primary_values.clear()


if __name__ == '__main__':
    st = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
    pric = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}

    val_1 = 1000.00
    val_2 = 1500.00

    print(calculate_portfolio_value(st, pric))
    print(calculate_portfolio_return(val_1, val_2))
    print(_primary_values)
    pric = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}

    print(*get_most_profitable_stock(st, pric))
