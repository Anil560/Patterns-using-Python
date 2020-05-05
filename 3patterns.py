#Output
#    enter the size:4
#     1             1
#     1 2         2 1 
#     1 2 3     3 2 1
#     1 2 3 4 4 3 2 1





n=int(input("enter the size:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
        x=(2*n)-(2*i)
    for j in range(x):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

