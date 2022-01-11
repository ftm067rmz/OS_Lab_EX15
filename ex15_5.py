arry = input("\nPlease enter a list of numbers(format: 1,3,0,...) = ")
arry = (arry.split(","))

n = len(arry)

for i in range(n):
    if arry[i] == arry[n-1-i]:
        flag = 1
    else:
        flag = 0
        break

if flag == 1:
    print("The array is symmetric")
else:
    print("The array is not symmetric")

