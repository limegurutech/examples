import xlrd

loc = ("input.xls")
 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

#print(sheet.cell_value(0,0))


row_count = sheet.nrows
col_count = sheet.ncols 

for i in range(0, row_count):
    row = []
    for j in range(0, col_count):
        row.append(sheet.cell_value(i,j))
    print(row)
