# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

coefMaxIndex = 10

def makeCoefArray(str):
    # Erase the end of equation " = 0"
    str = str[:-4]
    # print(str)

    s1 = list(map(lambda s: s.strip(), str.split('+')))
    # print(s1)

    s2 = list(map(lambda str1: str1.split('*x^'), s1))
    # print(s2)

    lst = [0 for i in range(coefMaxIndex)]
    for i in range(len(s1)):
        lst[int(s2[i][1])] = int(s2[i][0])
    # print(lst)
    return lst

data1 = open('./04_HomeWork/file04_05_01.txt','r',encoding="UTF-8")
str1 = data1.read()
data1.close
print(str1)
lst1 = makeCoefArray(str1)

data2 = open('./04_HomeWork/file04_05_02.txt','r',encoding="UTF-8")
str2 = data2.read()
data2.close
print(str2)
lst2 = makeCoefArray(str2)

lst3 = list(map(sum,zip(lst1,lst2)))
# print(lst3)

data3 = open('./04_HomeWork/file04_05_03.txt','w',encoding="UTF-8")
printed_flag = 0
power_max = len(lst3)-1
for i in range(power_max,-1,-1):
    if lst3[i] == 0:
        continue
    
    if printed_flag > 0:
        print(" + ", end = "")
        data3.write(" + ")
    else:
       printed_flag = 1 
        
    print(f"{lst3[i]}",end='')
    data3.write(f"{lst3[i]}")
    
    print(f"*x^{i}",end="")
    data3.write(f"*x^{i}")
    
print(" = 0")
data3.write(" = 0")
data3.close
