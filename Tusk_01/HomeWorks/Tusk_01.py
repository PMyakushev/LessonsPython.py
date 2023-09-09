class NumberManipulator:
    def __init__(self, n):
        self.n = n

    def calculate_result(self):
        res = 0
        for digit in str(self.n):
            res += int(digit)
        return res


n = 123
manipulator = NumberManipulator(n)
result = manipulator.calculate_result()
print(result)
