def write_array(array, file_name):
    with open(file_name, 'w') as file:
        file.write('\n'.join(array))

line = input('Введите строку: ')
array = []
while line != '#':
    array.append(line)
    line = input('Введите строку: ')

file_name = input('Введите название файла: ')
write_array(array, file_name)

with open(file_name, 'r') as file:
    print(file.read())
