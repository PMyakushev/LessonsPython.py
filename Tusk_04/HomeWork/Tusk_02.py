class BlueberryFarm:
    def __init__(self, crops):
        if len(crops) < 3:
            crops += [0] * (3 - len(crops))
        self.crops = crops * 2

    def max_harvest(self):
        max_harvest = 0
        for i in range(len(self.crops) // 2): # пройдем по каждому растению на ферме
             max_harvest = max(max_harvest, sum(self.crops[i:i+3]))
        return max_harvest


# rсчитывание входных данных
N = int(input("Введите количество кустов: "))
crops = []
for i in range(N):
    ai = int(input(f"Введите количество ягод на кусте {i+1}: "))
    crops.append(ai)

farm = BlueberryFarm(crops)
print(f"Максимальное количество ягод, которое можно собрать за один прием, составляет {farm.max_harvest()}."