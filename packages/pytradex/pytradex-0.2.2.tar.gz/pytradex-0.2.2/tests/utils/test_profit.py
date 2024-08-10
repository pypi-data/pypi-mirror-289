import pytest

from tradex.models.order import OrderProfitFormSimple
from tradex.models.take_profit import TakeProfit
from tradex.utils.profit import take_profit_list, take_profit_total

cases = [
    # long
    (
        # OrderProfitFormSimple
        OrderProfitFormSimple(0.1, 1000, 0, 1),
        # TakeProfit list
        [
            TakeProfit(volume=150.0, price=1.382, percentage=0.15),
            TakeProfit(volume=250.0, price=1.618, percentage=0.25),
            TakeProfit(volume=450.0, price=2, percentage=0.45),
            TakeProfit(volume=150.0, price=2.618, percentage=0.15),
            TakeProfit(volume=0, price=3, percentage=0),
        ],
        # total profit
        18045.0,
    ),
    # short
    (
        OrderProfitFormSimple(1, 1000, 1, 0),
        [
            TakeProfit(volume=150.0, price=-0.382, percentage=0.15),
            TakeProfit(volume=250.0, price=-0.618, percentage=0.25),
            TakeProfit(volume=450.0, price=-1, percentage=0.45),
            TakeProfit(volume=150.0, price=-1.618, percentage=0.15),
            TakeProfit(volume=0, price=-2, percentage=0),
        ],
        # total profit
        1904.5,
    ),
    # long normal
    (
        OrderProfitFormSimple(1.784, 665, 1.67, 1.89),
        [
            TakeProfit(volume=99.75, price=1.974, percentage=0.15),
            TakeProfit(volume=166.25, price=2.026, percentage=0.25),
            TakeProfit(volume=299.25, price=2.11, percentage=0.45),
            TakeProfit(volume=99.75, price=2.246, percentage=0.15),
            TakeProfit(volume=0, price=2.33, percentage=0),
        ],
        # total profit
        113.69,
    ),
    # short normal
    (
        OrderProfitFormSimple(1.89, 665, 1.931, 1.784),
        [
            TakeProfit(volume=99.75, price=1.728, percentage=0.15),
            TakeProfit(volume=166.25, price=1.693, percentage=0.25),
            TakeProfit(volume=299.25, price=1.637, percentage=0.45),
            TakeProfit(volume=99.75, price=1.546, percentage=0.15),
            TakeProfit(volume=0, price=1.49, percentage=0),
        ],
        # total profit
        84.09,
    ),
    (
        OrderProfitFormSimple(2636.0, 411.88, 2742.0, 2646.0),
        [
            TakeProfit(volume=61.782, price=2609.328, percentage=0.15),
            TakeProfit(volume=102.97, price=2586.672, percentage=0.25),
            TakeProfit(volume=185.346, price=2550.0, percentage=0.45),
            TakeProfit(volume=61.782, price=2490.672, percentage=0.15),
            TakeProfit(volume=0.0, price=2454.0, percentage=0),
        ],
        # total profit
        12.01,
    ),
]


@pytest.mark.parametrize(("order_profit", "take_profits"), [(case[0], case[1]) for case in cases])
def test_take_profit_list(order_profit, take_profits):
    tp_fib = take_profit_list(order=order_profit)
    assert tp_fib == take_profits


@pytest.mark.parametrize(("order_profit", "take_profits", "total_profit"), cases)
def test_take_profit_total(order_profit, take_profits, total_profit):
    total = take_profit_total(order=order_profit, take_profits=take_profits)
    assert total == total_profit
