class WatermelonSelector:
    def __init__(self, weights):
        self.weights = weights

    def select(self):
        min_weight = self.weights[0]
        max_weight = self.weights[0]

        for weight in self.weights:
            if weight < min_weight:
                min_weight = weight
            if weight > max_weight:
                max_weight = weight

        return min_weight, max_weight



selector = WatermelonSelector([5, 1, 6, 5, 9])
lightest, heaviest = selector.select()

print(f'Самый легккий арбуз весит {lightest}кг')
print(f'Самый тяжелый арбуз весит {heaviest}кг')