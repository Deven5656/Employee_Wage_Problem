""" 
    @Author: Deven Gupta
    @Date: 31-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 31-07-2024
    @Title : UC-1 Python program to Check attendance of employee

"""   
print("Welcome to Employee Wage Computation Program\n")

import random

def check_attendance():
    """
    Description:
        This function used to Check attendance of employee
    Parameters:
        None
    Returns:
        None
        
    """
    status = random.choice([0,1])
    if status == 1 :
        print("Employee is Present")
    else:
        print("Employee is Absent")

if __name__ == "__main__" :
    check_attendance()