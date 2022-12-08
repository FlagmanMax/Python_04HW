# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
data = open('./04_HomeWork/file04_04.txt','w',encoding="UTF-8")
k = int(input("Введите степень k : "))
coef = []
str = []
printed_flag = 0

for i in range(k+1):
    coef.append(random.randint(0,100))
    if coef[i] == 0:
        continue
    if printed_flag > 0:
        print(" + ", end = "")
        data.write(" + ")
    else:
       printed_flag = 1  
    print(f"{coef[i]}",end='')
    data.write(f"{coef[i]}")
    
    power = k-i
    if power==0:
        print(" ",end = '')
        data.write(" ")
    elif power == 1:
        print("*x",end = '')
        data.write("*x")
    # elif power == 2:
    #      print("*x\u00B2",end = '')
    #      data.write("*x\u00B2")
    # elif power == 3:
    #     print("*x\u00B3",end = '')
    #     data.write("*x\u00B3")
    # elif power == 4:
    #     print("*x\u2074",end = '')
    #     data.write("*x\u00B4")
    # elif power == 5:
    #     print("*x\u2075",end = '')
    #     data.write("*x\u00B5")
    # elif power == 6:
    #     print("*x\u2076",end = '')
    #     data.write("*x\u00B6")
    # elif power == 7:
    #     print("*x\u2077",end = '')
    #     data.write("*x\u00B7")
    # elif power == 8:
    #     print("*x\u2078",end = '')
    #     data.write("*x\u00B8")
    # elif power == 9:
    #     print("*x\u2079",end = '')
    #     data.write("*x\u00B9")
    else:
        print(f"*x^{power}",end="")
        data.write(f"*x^{power}")
print(" = 0")
data.write(" = 0")
data.close



