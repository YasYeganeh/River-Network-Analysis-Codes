import openpyxl as pxl


book=pxl.load_workbook("Network 2425.xlsx") # ba taghire name file shabake in code baraye har do shabake kar mikonad
sheet1=book["Sheet1"]

orders=sheet1['F']
# list orderha
a=[]
for cell in orders:
    a.append(cell.value)
a.remove('Order')
# print("a:",a)
# print(len(a))

b=set(a)
# print(b)

cnt=0
for i in b:
    cnt=a.count(i)
    print('order:',i,'count:',cnt)


