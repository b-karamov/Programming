import csv

arr = []
with open('table.csv', 'r') as table, open('table_new.csv', 'w') as new:
    table = csv.reader(table, delimiter=';')
    arr = list(table)
    writer = csv.writer(new)
    arr[0].insert(3, 'Grades')
    for i in range(1, len(arr)):
        arr[i].insert(3, 0)
    arr.insert(3, [0]*len(arr[0]))
    writer.writerows(arr)
    
