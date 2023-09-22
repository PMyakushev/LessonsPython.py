class Sorted():
    def __init__(self, arrayOne, arrayTwo):
        self.arrayOne = arrayOne
        self.arrayTwo = arrayTwo

    def sortedArray(self):
        arrayUnion = list(self.arrayOne | self.arrayTwo)
        arrayUnion.sort()
        return arrayUnion

n = int(input("Введите количество элементов в первом наборе: "))
arrayOne = set()
for i in range(n):
  ele = int(input())
  arrayOne.add(ele)

m = int(input("Введите количество элементов во втором наборе: "))
arrayTwo = set()
for i in range(m):
  ele = int(input())
  arrayTwo.add(ele)
print(arrayTwo)
print(arrayOne)

sets_obj = Sorted(arrayTwo, arrayOne)
result = sets_obj.sortedArray()
print(result)