x=""
z=0
kovi=0
import os
y=[[" "," "," "],[" "," "," "],[" "," "," "]]

def ellenorzes():
    for i in range(3):
        if y[i][0] == y[i][1] == y[i][2] and y[i][0] != " ":
            return y[i][0] 
        if y[0][i] == y[1][i] == y[2][i] and y[0][i] != " ":
            return y[0][i]

    if y[0][0] == y[1][1] == y[2][2] and y[0][0] != " ":
        return y[0][0]
    if y[0][2] == y[1][1] == y[2][0] and y[0][2] != " ":
        return y[0][2]
    
    for sor in y:
        if " " in sor:
            return None 
            
    return "Döntetlen"

while True:
    os.system('cls')
    print(f'''
    |-----------|-----------|-----------|
    |     {y[0][0]}     |     {y[0][1]}     |     {y[0][2]}     |
    |-----------|-----------|-----------|
    |     {y[1][0]}     |     {y[1][1]}     |     {y[1][2]}     |
    |-----------|-----------|-----------|
    |     {y[2][0]}     |     {y[2][1]}     |     {y[2][2]}     |
    |-----------|-----------|-----------|
    ''')
    
    eredmeny = ellenorzes()
    if eredmeny:
        print("Játék vége, nyertes: ", eredmeny)
        break

    if kovi == 0:
        a = input("X-játékos (sor,oszlop): ").split(",")
        if 1 <= int(a[0]) <= 3 and 1 <= int(a[1]) <= 3 and y[int(a[0])-1][int(a[1])-1] == " ":            
            y[int(a[0])-1][int(a[1])-1] = "X" 
            kovi = 1
        else:
            print("iden em tudsz rakni")
            input()
    else:
        a = input("O-játékos (sor,oszlop): ").split(",")
        if 1 <= int(a[0]) <= 3 and 1 <= int(a[1]) <= 3 and y[int(a[0])-1][int(a[1])-1] == " ":            
            y[int(a[0])-1][int(a[1])-1] = "O" 
            kovi = 0
        else:
            print("iden em tudsz rakni")
            input()