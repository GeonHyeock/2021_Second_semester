def gen_matrix(row,col):
    output = []
    str1 = "X,"+"+,"*(col-2)+"X"+"\n"
    output.append(("X,"*(col-1)+"X"+"\n"))
    for i in range(col-2):    
        output.append(str1)
    output.append("X,"*(col-1)+"X")
    open("matrix.txt","w").writelines(output)
n = int(input("rows = "))
m = int(input("columns = "))
gen_matrix(n,m)