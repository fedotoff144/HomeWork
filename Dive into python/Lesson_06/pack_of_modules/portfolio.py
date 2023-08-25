__all__ = ['calculate_portfolio_value', 'calculate_portfolio_return', 'get_most_profitable_stock']

_start_prices: dict = {}


def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    _start_prices.update(prices)
    result: float = sum(stocks[key] * prices[key] for key in stocks.keys() if key in prices)
    return result


def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    result: float = current_value / (initial_value / 100) - 100
    return result


def get_most_profitable_stock(stocks: dict, prices: dict) -> str:
    tempo_dict: dict = {}
    for key in stocks.keys():
        if key in prices.keys():
            tempo_dict[key] = stocks[key] * prices[key]
    return f'{max(tempo_dict, key=tempo_dict.get)}'


