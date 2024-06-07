#pyramid

n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range (n-i-1):
        print(" " ,end=" ")
   
    for j in range(2*i+1):
        print("*", end=" ")
    
    print()


#uppertriangle
#n = int(input("Enter the number of rows:"))

for i in range(n):
    for j in range(i):
        print(" ", end=" ")

    for j in range(n-i):
        print("*", end=" ")
    print()



#lowertriangle

#n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range (i+1):
        print("*", end=" ")
    
    print()