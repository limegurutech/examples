import xlwt
  
workbook = xlwt.Workbook() 
sheet = workbook.add_sheet("limeguru")


# sheet.write(0, 0, 'SAMPLE')
# workbook.save("output.xls")

data = [["python", 20], ["java", 30], ["cloud", 10]]
for i in range(0,3):
    for j in range(0,2):
        sheet.write(i, j, data[i][j])
workbook.save("output.xls")