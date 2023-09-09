# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
#
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
#
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
#
# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.
#
# Пример:
#
# n = 385916 -> yes
# n = 123456 -> no


n = input()
if (len(n) % 2) != 0 or not n.isdigit():
    print("Ошибка: номер билета должен содержать нечетное кол-во чисел")
elif sum(map(int, n[:(len(n)//2)])) == sum(map(int, n[(len(n)//2):])):
    print("yes")
else:
    print("no")

