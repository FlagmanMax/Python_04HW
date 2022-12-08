# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("Введите натуральное число "))

def primary(n):
   i = 2
   lst = []
   while i * i <= n:
       while n % i == 0:
           lst.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       lst.append(int(n))
   return lst

lst = primary(n)
print(lst)