import openpyxl

book = openpyxl.load_workbook(r'C:\Users\Combuter\Desktop\workbook.xlsx')
sheet = book["paper"]

print(sheet["A1"].value)


sheet["A2"] =  "HOW ARE YOU "

book.save(r'C:\Users\Combuter\Desktop\workbook.xlsx')