num = [2,1,8]
k = 10
def dynamic_windw(num: [], k:int )-> int:
    if k ==0 :
        return -1
    
    minimum = 10000
    current_min = 0  
    window_right = 0 
    window_left = 0 

    for window_right in range(len(num)):
        current_min += num[window_right]
        while(current_min >= k):
            minimum = min(current_min, window_right - window_left +1)
            
            current_min -= num[window_left]
            window_left += 1
    
    if minimum == window_right+1:
        return -1
    return minimum , " size of list"
print(dynamic_windw(num, k))