# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

str_in = input("Введите последовательность чисел ")
num_in = list(map(int,str_in.split()))
num_out = []
print(num_in)

num_out.append(num_in[0])
for i in range(1,len(num_in)):
    flag = 1
    for j in range(0,len(num_out)):
        if (num_out[j] == num_in[i]):
            flag = 0
            break
    if flag > 0:
        num_out.append(num_in[i])

print(num_out)
        