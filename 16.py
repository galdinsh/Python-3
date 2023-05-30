from random import randint
lis = list()
lens = int(input('Введите длину списка: '))
for i in range(lens):
    lis.append(randint(0, 20))
print(lis)
count = 0
number = int(input('Введите искомое число: '))
for j in range(len(lis)):
    if lis[j] == number:
        count += 1
print(count)