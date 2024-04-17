def main ():
    nums1 = [1,2,3,4,0,0,0]
    nums2 = [1,5,6]
    nums1_m = 3
    nums2_n = 2
    
    
    answer = merge_sorted_array(nums1, nums2, nums1_m, nums2_n)
    print(answer)
    print(mergedlist)



def merge_sorted_array(nums1: [int] , nums2, nums1_m, nums2_n):
    
    #shrinking if necessary
    while len(nums1) > nums1_m:
        nums1.remove(nums1[-1])
    while len(nums2) > nums2_n:
        nums2.remove(nums2[-1])
    
    #mergin the lists 
    nums1.extend(nums2)
    nums1.sort()
    


    



main()
