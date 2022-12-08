# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
data = open('./04_HomeWork/file04_04b.txt','w',encoding="UTF-8")
k = int(input("Введите степень k : "))
coef = []
str = []
printed_flag = 0

for i in range(k+1):
    coef.append(random.randint(0,100))

    if printed_flag > 0:
        print(" + ", end = "")
        data.write(" + ")
    else:
       printed_flag = 1 
        
    print(f"{coef[i]}",end='')
    data.write(f"{coef[i]}")
    
    power = k-i

    print(f"*x^{power}",end="")
    data.write(f"*x^{power}")
    
print(" = 0")
data.write(" = 0")
data.close



