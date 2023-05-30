from random import randint
lis = list()
lens = int(input('Введите длину списка: '))
for i in range(lens):
    lis.append(randint(0, 20))
print(lis)
number = int(input('Введите число с которым необходимо сравнивать элементы списка: '))
min = abs(number - lis[0])
index = 0
for i in range(len(lis)):
    count = abs(number - lis[i])
    if count < min:
        min = count
        index = i
print(lis[index])