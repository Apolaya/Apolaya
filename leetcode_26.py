

nums = [-3,-1,-1,0,0,0,0,0,2]

    
i = 0
while i < len(nums):

    while nums.count(nums[i]) > 1: 
        print(nums.remove(nums[i]), "removed number is ", nums[i] )
            
        print(nums)
    i +=1
        