list = {1: "AEIOULNSTRАВЕИНОРСТ",
        2: "DGДКЛМПУ",
        3: "BCMPБГЁЬЯ",
        4: "FHVWYЙЫ",
        5: "KЖЗХЦЧ",
        8: "JXШЭЮ",
        10: "QZФЩЪ"}

slovo = input('Введите слово:').upper()
sum = 0
for i in slovo:
    for n, m in list.items():
        if i in m:
                sum += n
print(f'Стоимость слова = {sum}')
