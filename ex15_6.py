def Pascal(num):

    num_list = []

    for i in range(num):
        num_list.append([1]*(i+1))
        
    for i in range(2,num):  
        for j in range(1,i)  :
            num_list[i][j] = num_list[i-1][j-1] + num_list[i-1][j]

    for r in num_list:
        for c in r:
            print(c,end = " ")
        print()
    
    print()
            
        
number = int(input("""How many steps do you want Khayyam Pascal's triangle to show?
                                            Enter a number: """))

Pascal(number)
