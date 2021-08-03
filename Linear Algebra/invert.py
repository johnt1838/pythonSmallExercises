def inverting():
    print("Inverting matrix")
    m = int(input("[ROW] m= "))
    n = int(input("[COLUMN] n= "))
    print("Matrix : {} x {}".format(m,n))
    matrix = []
    print("[!] Inputting the data")
    for i in range(m):
        column = []
        for j in range(n):
            x= int(input("enter : "))
            column.append(x)
        matrix.append(column)
    print(matrix)

    #printing
    for i in range(m):
        print("\n")
        for j in range(n):
            print("A_{}{}={} ".format(i,j,matrix[i][j]), end = '')
    #--------------

    matrix_Inv = []
    if m ==n:
        for i in range(m):
            print("\n")
            column2 = []
            for j in range(n):
                #print("[!]Inverted matrix")
                column2.append(matrix[j][i])
            matrix_Inv.append(column2)
            print(matrix_Inv)
        for i in range(m):
            print("\n")
            for j in range(n):
                print("A_{}{}={} ".format(i, j, matrix_Inv[i][j]), end='')
    else:
        for i in range(n):
            print("\n")
            column2 = []
            for j in range(m):
                # print("[!]Inverted matrix")
                column2.append(matrix[j][i])
            matrix_Inv.append(column2)
            print(matrix_Inv)
        for i in range(n):
            print("\n")
            for j in range(m):
                print("A_{}{}={} ".format(i, j, matrix_Inv[i][j]), end='')