while True:
    print(" 1_Add\n","2_subtract\n","3_multiply\n","4_divergance\n")
    Operation = int(input("Enter the Operation Code (1: Add, 2: Subtract, 3: Multiply, 4: Divide), press Enter to confirm: "))
    
        
    
    Operation_int=[1,2,3,4]
    
    if  Operation in Operation_int   :
        print("valid")
        try:
            First=float(input("Enter num_1"))
            second=float(input("Enter num_2"))   
        except ValueError:
            print(" Invalid input! Please enter a numeric value for num_1.")
           
        if Operation == 1 :
            sum_result = First+second
            print (sum_result)
        elif Operation == 2 :
            sub_result = First-second
            print(sub_result)
        elif Operation == 3 :
            multi_result = First*second
            print(multi_result)
        elif Operation == 4 :
           if second != 0 :
             div_result = (First/second)
             print(div_result)
           else:
               print("Error (second) can not have (0) value")
            
        else:
             print("Error in the Program,enter numerical number only")
                
        
    else:
        print("invalid,Error Enter the Operation code  ")
        
        
    repeat= input("do you want to perform another Operation")
    if repeat not in ["yes","y"]:
           print("Thank you for using our program")
           break
        