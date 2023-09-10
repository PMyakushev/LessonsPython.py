# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

class Reddli:
    def __init__(self, S, P):
        self.S = S
        self.P = P

    def sum_difference(self):
        for x in range(1, 1001):
            for y in range(x, 1001):

                if x + y == self.S and x * y == self.P:
                    return (x, y)
            return "Нет решений"



game = Reddli(7, 10)
solution = game.sum_difference()
