from dataclasses import dataclass

from tradex.constants.enuming import Direction


@dataclass
class OrderProfitFormSimple:
    price: float
    size: float

    # fib mark to calculate fibonacci retracement
    zero_mark: float
    middle_mark: float

    @property
    def order_type(self) -> Direction:
        return Direction.LONG if self.middle_mark > self.price else Direction.SHORT

    @property
    def order_price(self) -> float:
        return self.price * self.size
