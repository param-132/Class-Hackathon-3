#Assignment -
from random import choice
import random
import xlrd

#1
file = open(r"C:\Users\Param Mane\Desktop\DS\paper1.txt","w")
i=0
for i in range(0,6):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column =2
    x = choice(sh1.col(column)).value
    file.write(str(i)+". what is the fullform of "+str(x)+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 2
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 1
    if( z == 1):
        p = sh1.cell(y,1)
        file.write('     1.'+p.value+'   2.'+choice(sh1.col(column)).value+'   3.'+choice(sh1.col(column)).value+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,1)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")

    elif(z==3):
        p = sh1.cell(y,1)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")


    i+=1


i=6
for i in range(6,13):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column =1
    x = choice(sh1.col(column)).value
    file.write(str(i)+ ". what is the shortform of "+x+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 1
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 2
    if( z == 1):
        p = sh1.cell(y,2)
        file.write('     1.'+p.value+'   2.'+choice(sh1.col(column)).value+'   3.'+choice(sh1.col(column)).value+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,2)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")

    elif(z==3):
        p = sh1.cell(y,2)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")


    i+=1

i=13
for i in range(13,19):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column = 1
    x = choice(sh1.col(column)).value
    file.write(str(i)+ ". what is the price of "+x+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 1
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 3
    if( z == 1):
        p = sh1.cell(y,3)
        file.write('     1.'+str(p.value)+'   2.'+str(choice(sh1.col(column)).value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,3)
        file.write('     1.'+str(choice(sh1.col(column)).value)+'   2.'+str(p.value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")

    elif(z==3):
        p = sh1.cell(y,3)
        file.write('    1.'+str(choice(sh1.col(column)).value)+'  2.'+ str(choice(sh1.col(column)).value)+'  3.'+str(p.value)+"\n")
    i+=1


file.close()

#2
file = open(r"C:\Users\Param Mane\Desktop\DS\paper2.txt","w")
i=0
for i in range(0,6):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column =2
    x = choice(sh1.col(column)).value
    file.write(str(i)+". what is the fullform of "+str(x)+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 2
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 1
    if( z == 1):
        p = sh1.cell(y,1)
        file.write('     1.'+p.value+'   2.'+choice(sh1.col(column)).value+'   3.'+choice(sh1.col(column)).value+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,1)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")

    elif(z==3):
        p = sh1.cell(y,1)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")


    i+=1


i=6
for i in range(6,13):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column =1
    x = choice(sh1.col(column)).value
    file.write(str(i)+ ". what is the shortform of "+x+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 1
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 2
    if( z == 1):
        p = sh1.cell(y,2)
        file.write('     1.'+p.value+'   2.'+choice(sh1.col(column)).value+'   3.'+choice(sh1.col(column)).value+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,2)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")

    elif(z==3):
        p = sh1.cell(y,2)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")


    i+=1

i=13
for i in range(13,19):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column = 1
    x = choice(sh1.col(column)).value
    file.write(str(i)+ ". what is the price of "+x+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 1
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 3
    if( z == 1):
        p = sh1.cell(y,3)
        file.write('     1.'+str(p.value)+'   2.'+str(choice(sh1.col(column)).value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,3)
        file.write('     1.'+str(choice(sh1.col(column)).value)+'   2.'+str(p.value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")

    elif(z==3):
        p = sh1.cell(y,3)
        file.write('    1.'+str(choice(sh1.col(column)).value)+'  2.'+ str(choice(sh1.col(column)).value)+'  3.'+str(p.value)+"\n")
    i+=1


file.close()

#3
file = open(r"C:\Users\Param Mane\Desktop\DS\paper3.txt","w")
i=0
for i in range(0,6):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column =2
    x = choice(sh1.col(column)).value
    file.write(str(i)+". what is the fullform of "+str(x)+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 2
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 1
    if( z == 1):
        p = sh1.cell(y,1)
        file.write('     1.'+p.value+'   2.'+choice(sh1.col(column)).value+'   3.'+choice(sh1.col(column)).value+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,1)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")

    elif(z==3):
        p = sh1.cell(y,1)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")


    i+=1


i=6
for i in range(6,13):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column =1
    x = choice(sh1.col(column)).value
    file.write(str(i)+ ". what is the shortform of "+x+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 1
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 2
    if( z == 1):
        p = sh1.cell(y,2)
        file.write('     1.'+p.value+'   2.'+choice(sh1.col(column)).value+'   3.'+choice(sh1.col(column)).value+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,2)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")

    elif(z==3):
        p = sh1.cell(y,2)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")


    i+=1

i=13
for i in range(13,19):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column = 1
    x = choice(sh1.col(column)).value
    file.write(str(i)+ ". what is the price of "+x+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 1
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 3
    if( z == 1):
        p = sh1.cell(y,3)
        file.write('     1.'+str(p.value)+'   2.'+str(choice(sh1.col(column)).value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,3)
        file.write('     1.'+str(choice(sh1.col(column)).value)+'   2.'+str(p.value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")

    elif(z==3):
        p = sh1.cell(y,3)
        file.write('    1.'+str(choice(sh1.col(column)).value)+'  2.'+ str(choice(sh1.col(column)).value)+'  3.'+str(p.value)+"\n")
    i+=1


file.close()

#4
file = open(r"C:\Users\Param Mane\Desktop\DS\paper4.txt","w")
i=0
for i in range(0,6):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column =2
    x = choice(sh1.col(column)).value
    file.write(str(i)+". what is the fullform of "+str(x)+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 2
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 1
    if( z == 1):
        p = sh1.cell(y,1)
        file.write('     1.'+p.value+'   2.'+choice(sh1.col(column)).value+'   3.'+choice(sh1.col(column)).value+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,1)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")

    elif(z==3):
        p = sh1.cell(y,1)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")


    i+=1


i=6
for i in range(6,13):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column =1
    x = choice(sh1.col(column)).value
    file.write(str(i)+ ". what is the shortform of "+x+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 1
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 2
    if( z == 1):
        p = sh1.cell(y,2)
        file.write('     1.'+p.value+'   2.'+choice(sh1.col(column)).value+'   3.'+choice(sh1.col(column)).value+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,2)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")

    elif(z==3):
        p = sh1.cell(y,2)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")


    i+=1

i=13
for i in range(13,19):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column = 1
    x = choice(sh1.col(column)).value
    file.write(str(i)+ ". what is the price of "+x+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 1
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 3
    if( z == 1):
        p = sh1.cell(y,3)
        file.write('     1.'+str(p.value)+'   2.'+str(choice(sh1.col(column)).value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,3)
        file.write('     1.'+str(choice(sh1.col(column)).value)+'   2.'+str(p.value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")

    elif(z==3):
        p = sh1.cell(y,3)
        file.write('    1.'+str(choice(sh1.col(column)).value)+'  2.'+ str(choice(sh1.col(column)).value)+'  3.'+str(p.value)+"\n")
    i+=1


file.close()

#5
file = open(r"C:\Users\Param Mane\Desktop\DS\paper5.txt","w")
i=0
for i in range(0,6):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column =2
    x = choice(sh1.col(column)).value
    file.write(str(i)+". what is the fullform of "+str(x)+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 2
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 1
    if( z == 1):
        p = sh1.cell(y,1)
        file.write('     1.'+p.value+'   2.'+choice(sh1.col(column)).value+'   3.'+choice(sh1.col(column)).value+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,1)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")

    elif(z==3):
        p = sh1.cell(y,1)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")


    i+=1


i=6
for i in range(6,13):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column =1
    x = choice(sh1.col(column)).value
    file.write(str(i)+ ". what is the shortform of "+x+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 1
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 2
    if( z == 1):
        p = sh1.cell(y,2)
        file.write('     1.'+p.value+'   2.'+choice(sh1.col(column)).value+'   3.'+choice(sh1.col(column)).value+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,2)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")

    elif(z==3):
        p = sh1.cell(y,2)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")


    i+=1

i=13
for i in range(13,19):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column = 1
    x = choice(sh1.col(column)).value
    file.write(str(i)+ ". what is the price of "+x+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 1
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 3
    if( z == 1):
        p = sh1.cell(y,3)
        file.write('     1.'+str(p.value)+'   2.'+str(choice(sh1.col(column)).value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,3)
        file.write('     1.'+str(choice(sh1.col(column)).value)+'   2.'+str(p.value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")

    elif(z==3):
        p = sh1.cell(y,3)
        file.write('    1.'+str(choice(sh1.col(column)).value)+'  2.'+ str(choice(sh1.col(column)).value)+'  3.'+str(p.value)+"\n")
    i+=1


file.close()

#6
file = open(r"C:\Users\Param Mane\Desktop\DS\paper6.txt","w")
i=0
for i in range(0,6):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column =2
    x = choice(sh1.col(column)).value
    file.write(str(i)+". what is the fullform of "+str(x)+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 2
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 1
    if( z == 1):
        p = sh1.cell(y,1)
        file.write('     1.'+p.value+'   2.'+choice(sh1.col(column)).value+'   3.'+choice(sh1.col(column)).value+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,1)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")

    elif(z==3):
        p = sh1.cell(y,1)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")


    i+=1


i=6
for i in range(6,13):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column =1
    x = choice(sh1.col(column)).value
    file.write(str(i)+ ". what is the shortform of "+x+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 1
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 2
    if( z == 1):
        p = sh1.cell(y,2)
        file.write('     1.'+p.value+'   2.'+choice(sh1.col(column)).value+'   3.'+choice(sh1.col(column)).value+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,2)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")

    elif(z==3):
        p = sh1.cell(y,2)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")


    i+=1

i=13
for i in range(13,19):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column = 1
    x = choice(sh1.col(column)).value
    file.write(str(i)+ ". what is the price of "+x+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 1
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 3
    if( z == 1):
        p = sh1.cell(y,3)
        file.write('     1.'+str(p.value)+'   2.'+str(choice(sh1.col(column)).value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,3)
        file.write('     1.'+str(choice(sh1.col(column)).value)+'   2.'+str(p.value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")

    elif(z==3):
        p = sh1.cell(y,3)
        file.write('    1.'+str(choice(sh1.col(column)).value)+'  2.'+ str(choice(sh1.col(column)).value)+'  3.'+str(p.value)+"\n")
    i+=1


file.close()
#7
file = open(r"C:\Users\Param Mane\Desktop\DS\paper7.txt","w")
i=0
for i in range(0,6):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column =2
    x = choice(sh1.col(column)).value
    file.write(str(i)+". what is the fullform of "+str(x)+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 2
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 1
    if( z == 1):
        p = sh1.cell(y,1)
        file.write('     1.'+p.value+'   2.'+choice(sh1.col(column)).value+'   3.'+choice(sh1.col(column)).value+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,1)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")

    elif(z==3):
        p = sh1.cell(y,1)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")


    i+=1


i=6
for i in range(6,13):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column =1
    x = choice(sh1.col(column)).value
    file.write(str(i)+ ". what is the shortform of "+x+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 1
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 2
    if( z == 1):
        p = sh1.cell(y,2)
        file.write('     1.'+p.value+'   2.'+choice(sh1.col(column)).value+'   3.'+choice(sh1.col(column)).value+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,2)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")

    elif(z==3):
        p = sh1.cell(y,2)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")


    i+=1

i=13
for i in range(13,19):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column = 1
    x = choice(sh1.col(column)).value
    file.write(str(i)+ ". what is the price of "+x+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 1
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 3
    if( z == 1):
        p = sh1.cell(y,3)
        file.write('     1.'+str(p.value)+'   2.'+str(choice(sh1.col(column)).value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,3)
        file.write('     1.'+str(choice(sh1.col(column)).value)+'   2.'+str(p.value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")

    elif(z==3):
        p = sh1.cell(y,3)
        file.write('    1.'+str(choice(sh1.col(column)).value)+'  2.'+ str(choice(sh1.col(column)).value)+'  3.'+str(p.value)+"\n")
    i+=1


file.close()
#8
file = open(r"C:\Users\Param Mane\Desktop\DS\paper8.txt","w")
i=0
for i in range(0,6):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column =2
    x = choice(sh1.col(column)).value
    file.write(str(i)+". what is the fullform of "+str(x)+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 2
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 1
    if( z == 1):
        p = sh1.cell(y,1)
        file.write('     1.'+p.value+'   2.'+choice(sh1.col(column)).value+'   3.'+choice(sh1.col(column)).value+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,1)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")

    elif(z==3):
        p = sh1.cell(y,1)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")


    i+=1


i=6
for i in range(6,13):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column =1
    x = choice(sh1.col(column)).value
    file.write(str(i)+ ". what is the shortform of "+x+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 1
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 2
    if( z == 1):
        p = sh1.cell(y,2)
        file.write('     1.'+p.value+'   2.'+choice(sh1.col(column)).value+'   3.'+choice(sh1.col(column)).value+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,2)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")

    elif(z==3):
        p = sh1.cell(y,2)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")


    i+=1

i=13
for i in range(13,19):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column = 1
    x = choice(sh1.col(column)).value
    file.write(str(i)+ ". what is the price of "+x+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 1
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 3
    if( z == 1):
        p = sh1.cell(y,3)
        file.write('     1.'+str(p.value)+'   2.'+str(choice(sh1.col(column)).value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,3)
        file.write('     1.'+str(choice(sh1.col(column)).value)+'   2.'+str(p.value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")

    elif(z==3):
        p = sh1.cell(y,3)
        file.write('    1.'+str(choice(sh1.col(column)).value)+'  2.'+ str(choice(sh1.col(column)).value)+'  3.'+str(p.value)+"\n")
    i+=1


file.close()
#9
file = open(r"C:\Users\Param Mane\Desktop\DS\paper9.txt","w")
i=0
for i in range(0,6):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column =2
    x = choice(sh1.col(column)).value
    file.write(str(i)+". what is the fullform of "+str(x)+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 2
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 1
    if( z == 1):
        p = sh1.cell(y,1)
        file.write('     1.'+p.value+'   2.'+choice(sh1.col(column)).value+'   3.'+choice(sh1.col(column)).value+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,1)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")

    elif(z==3):
        p = sh1.cell(y,1)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")


    i+=1


i=6
for i in range(6,13):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column =1
    x = choice(sh1.col(column)).value
    file.write(str(i)+ ". what is the shortform of "+x+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 1
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 2
    if( z == 1):
        p = sh1.cell(y,2)
        file.write('     1.'+p.value+'   2.'+choice(sh1.col(column)).value+'   3.'+choice(sh1.col(column)).value+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,2)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")

    elif(z==3):
        p = sh1.cell(y,2)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")


    i+=1

i=13
for i in range(13,19):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column = 1
    x = choice(sh1.col(column)).value
    file.write(str(i)+ ". what is the price of "+x+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 1
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 3
    if( z == 1):
        p = sh1.cell(y,3)
        file.write('     1.'+str(p.value)+'   2.'+str(choice(sh1.col(column)).value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,3)
        file.write('     1.'+str(choice(sh1.col(column)).value)+'   2.'+str(p.value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")

    elif(z==3):
        p = sh1.cell(y,3)
        file.write('    1.'+str(choice(sh1.col(column)).value)+'  2.'+ str(choice(sh1.col(column)).value)+'  3.'+str(p.value)+"\n")
    i+=1


file.close()
#10
file = open(r"C:\Users\Param Mane\Desktop\DS\paper10.txt","w")
i=0
for i in range(0,6):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column =2
    x = choice(sh1.col(column)).value
    file.write(str(i)+". what is the fullform of "+str(x)+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 2
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 1
    if( z == 1):
        p = sh1.cell(y,1)
        file.write('     1.'+p.value+'   2.'+choice(sh1.col(column)).value+'   3.'+choice(sh1.col(column)).value+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,1)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")

    elif(z==3):
        p = sh1.cell(y,1)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")


    i+=1


i=6
for i in range(6,13):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column =1
    x = choice(sh1.col(column)).value
    file.write(str(i)+ ". what is the shortform of "+x+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 1
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 2
    if( z == 1):
        p = sh1.cell(y,2)
        file.write('     1.'+p.value+'   2.'+choice(sh1.col(column)).value+'   3.'+choice(sh1.col(column)).value+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,2)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")

    elif(z==3):
        p = sh1.cell(y,2)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")


    i+=1

i=13
for i in range(13,19):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column = 1
    x = choice(sh1.col(column)).value
    file.write(str(i)+ ". what is the price of "+x+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 1
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 3
    if( z == 1):
        p = sh1.cell(y,3)
        file.write('     1.'+str(p.value)+'   2.'+str(choice(sh1.col(column)).value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,3)
        file.write('     1.'+str(choice(sh1.col(column)).value)+'   2.'+str(p.value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")

    elif(z==3):
        p = sh1.cell(y,3)
        file.write('    1.'+str(choice(sh1.col(column)).value)+'  2.'+ str(choice(sh1.col(column)).value)+'  3.'+str(p.value)+"\n")
    i+=1


file.close()
#11
file = open(r"C:\Users\Param Mane\Desktop\DS\paper11.txt","w")
i=0
for i in range(0,6):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column =2
    x = choice(sh1.col(column)).value
    file.write(str(i)+". what is the fullform of "+str(x)+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 2
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 1
    if( z == 1):
        p = sh1.cell(y,1)
        file.write('     1.'+p.value+'   2.'+choice(sh1.col(column)).value+'   3.'+choice(sh1.col(column)).value+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,1)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")

    elif(z==3):
        p = sh1.cell(y,1)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")


    i+=1


i=6
for i in range(6,13):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column =1
    x = choice(sh1.col(column)).value
    file.write(str(i)+ ". what is the shortform of "+x+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 1
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 2
    if( z == 1):
        p = sh1.cell(y,2)
        file.write('     1.'+p.value+'   2.'+choice(sh1.col(column)).value+'   3.'+choice(sh1.col(column)).value+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,2)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")

    elif(z==3):
        p = sh1.cell(y,2)
        file.write('     1.'+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")


    i+=1

i=13
for i in range(13,19):
    wb = xlrd.open_workbook(r"C:\Users\Param Mane\Desktop\DS\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column = 1
    x = choice(sh1.col(column)).value
    file.write(str(i)+ ". what is the price of "+x+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 1
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 3
    if( z == 1):
        p = sh1.cell(y,3)
        file.write('     1.'+str(p.value)+'   2.'+str(choice(sh1.col(column)).value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,3)
        file.write('     1.'+str(choice(sh1.col(column)).value)+'   2.'+str(p.value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")

    elif(z==3):
        p = sh1.cell(y,3)
        file.write('    1.'+str(choice(sh1.col(column)).value)+'  2.'+ str(choice(sh1.col(column)).value)+'  3.'+str(p.value)+"\n")
    i+=1


file.close()
