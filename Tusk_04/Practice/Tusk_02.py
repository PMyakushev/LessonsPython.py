# class Huker():
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def marksBook(self, index = 0):
#         min_mark = min(self.marks)
#         max_mark = max(self.marks)
#         if index == len(self.marks):
#             return self.marks
#         else:
#             if __name__ == '__main__':
#                 if self.marks[index] == max_mark:
#                     self.marks[index] = min_mark
#                 return self.marksBook(index + 1)



# vasiliy = Huker("Василий", [1, 3, 3, 3, 4])

# print(vasiliy.marksBook())

marks = [1, 3, 3, 3, 4]

def marksBook(marks):
    min_mark = min(marks)
    max_mark = max(marks)
    for i in range(len(marks)):
        if marks[i] == max_mark:
            marks[i] = min_mark
    return marks

print(marksBook(marks))