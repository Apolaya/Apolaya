#leet code question Kids with candies. 
import random

def main():
    mystery = random.Random()
    random_int = mystery.randint(1,9)
    
    
    student_candies = [None] * random_int

    for index in range(len(student_candies)):
        random_candy = mystery.randint(1,5)
        student_candies[index] = random_candy
        
    print(student_candies , "student candies list")

    extra_candies = mystery.randint(1,4)
    
    print(extra_candies, " :Extra candies") 
    max_value = 0 
    for index in range(len(student_candies)):
        if student_candies[index] > max_value:
                max_value = student_candies[index]
        student_candies[index] = student_candies[index] + extra_candies
        
    answer_list = [None] * len(student_candies)
    for index in range(len(student_candies)):
            
        
        if student_candies[index] >= max_value:
            answer_list[index] = True
        else:
            answer_list[index] = False
        
    
           

    
    print("the max value is " , max_value)
    
                
        
        #if student_candies[index] > student_candies[index-1]:
         #   answer_list[index] = True
        #lse: 
        #    answer_list[index] = False
        
        

    print (student_candies)
    print (answer_list)



main()