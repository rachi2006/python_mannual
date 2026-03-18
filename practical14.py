import csv
with open('marks.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    total = 0
    count = 0
    for column in reader:
        total += float(column[1])
        count += 1
    average = total / count
    print("Average:", average)