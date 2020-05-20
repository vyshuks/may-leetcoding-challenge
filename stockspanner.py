"""
Write a class StockSpanner which collects daily price quotes
for some stock, and returns the span of that stock's price for
the current day.

The span of the stock's price today is defined as the maximum number
of consecutive days (starting from today and going backwards) for which
the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were
[100, 80, 60, 70, 60, 75, 85], then the stock spans would be
[1, 1, 1, 2, 1, 4, 6].
"""


class StockSpanner:

    def __init__(self):
        self.stock_stack = []

    def next(self, price: int) -> int:
        cnt = 1
        while len(self.stock_stack)>0 and self[-1][0] <= price:
            cnt+=self.stock_stack[-1][1]
            self.stock_stack.pop()
        self.stock_stack.append((price, cnt))
        return cnt

