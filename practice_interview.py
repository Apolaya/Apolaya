arr = [4,7,6,9,5,4,7,7,45,7,56,7,6,2,23,6,7,4]
expectation = [[4,10], [9,5]]

lowest = expectation[0][0]
highest = expectation [0][1]

indicies = [lowest, highest]

reverse_elements = []
for i in range(lowest, highest): 
    print(i , " value of i ")
    reverse_elements.append(arr[i])


print(reverse_elements , " elements in seperate list ")
reversed_elements_complete = reverse_elements[::-1]

print(reversed_elements_complete, " reversal complete ")

for i in range(len(indicies)):
    arr[indicies[i]] = reversed_elements_complete[i]

print(arr, " final array " )
