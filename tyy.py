rows=30 
columns=2*rows-1
for row in range(rows):
    for column in range(1,columns+1):
        if(rows-row)<=column<=(rows+row):
            print("*",end="")
        else:
            print(" ",end="") 
    print("")            
 