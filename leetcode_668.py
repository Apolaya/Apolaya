import random

rand = random.Random()

m = rand.randint(1,6)
n = rand.randint(2,6)
k = rand.randint(1,6 )

matrix = []


for i in range(m):
    
    if i == k:
        print(matrix[-1][-1])
        break
    row_list = []
    for j in range(n):
        row_list.append((i+1) * (j+1))
    matrix.append(row_list)
print(m, " row ")
print(n, " Column")

print(min(m,n), " Min function ")
print(max(m,n), " Max funciton")


#Print the matrix in multiplicaple table form 
#for row_list in matrix:
 #   print(row_list)
#print(matrix[-1][-1], " last index of matrix ")


