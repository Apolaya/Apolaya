arry: [] = ["flower", "flow", "flight", "flex"]

array_length = len(arry)
initial_prefix = arry[0]


for i in range(1,len(arry)):
    print(" i is: " , i )
    print(initial_prefix , " i is : " , i )
    while arry[i].find(initial_prefix) != 0 :
        print("array at i is : ", arry[i], "the find method is " , arry[i].find(initial_prefix), )
        initial_prefix = initial_prefix[:-1]
        print(initial_prefix, " initial prefix after the check ")
        print(arry[i], 'checking index word ')
        if initial_prefix == False:
            print(" empty ")
 
