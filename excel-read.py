import openpyxl

filename = "ba.xlsx"
book = openpyxl.load_workbook(filename)

sheet = book.worksheets[0]

data = []
for row in sheet.rows:
    data.append([
        row[0].value,
        row[9].value
    ])

del data[0]
del data[0]
del data[0]
del data[0]

del data[17]
del data[17]

print(data)


data = sorted(data, key=lambda x: int(x[1]))

for i, a in enumerate(data): #요소
    if i >= 5:
        break
    print(i+1, a[0], int(a[1]))