with open('HW2_task1.txt', 'w') as file:
    file.write('У лукоморья дуб зелёный; \nЗлатая цепь на дубе том: \nИ днём и ночью кот учёный \nВсё ходит по цепи кругом.\n')
with open('HW2_task1.txt', 'r') as file:
    for line in file:
        print(line.strip())

