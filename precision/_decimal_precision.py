import decimal as d

# brief: implements logic for round numbers
class Round:
    def __init__(self, precision):
        self._precision = self.ComputePrecision(precision)

    # brief: round the value up
    # param: value - target value
    # return: rounded value
    def Up(self, value):
        return float(d.Decimal(value).quantize(self._precision, d.ROUND_CEILING))

    # brief: round the value down
    # param: value - target value
    # return: rounded value
    def Down(self, value):
        return float(d.Decimal(value).quantize(self._precision, d.ROUND_FLOOR))

    # brief: compute precision
    # param: precision - new value of a precision (must be positive integer number)
    # return: decimal-number like 1.0...<precision>...0
    @staticmethod
    def ComputePrecision(precision):
        result = "1." + "".join(["0" for _ in range(precision)])
        return d.Decimal(result)