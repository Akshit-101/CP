class StockSpanner:
    def __init__(self):
        # Stack to store pairs of (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1  # Initial span for the current day
        # Pop prices that are less than or equal to the current price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        
        # Push the current price and its span onto the stack
        self.stack.append((price, span))
        return span
stockSpanner = StockSpanner()
print(stockSpanner.next(100))