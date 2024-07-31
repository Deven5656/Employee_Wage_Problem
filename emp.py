""" 
    @Author: Deven Gupta
    @Date: 31-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 31-07-2024
    @Title : UC-2 Python program to Calculate Wage

"""   
print("Welcome to Employee Wage Computation Program\n")

import random
WAGE_PER_HOUR = 20
FULL_TIME_HOUR = 8


def check_attendance():
    """
    Description:
        This function used to Check attendance of employee
    Parameters:
        None
    Returns:
        boolean : True if present else False(absent)
        
    """
    status = random.choice([0,1])
    if status == 1 :
        print("Employee Present")
        return True
    else:
        print("Employee Absent")
        return False


def cal_daily_wage():
    """
    Description:
        This function used to calculate the daily wage
    Parameters:
        None
    Returns:
        int : daily wage after calculation

    """
    daily_wage = 0
    if check_attendance():
        daily_wage = WAGE_PER_HOUR * FULL_TIME_HOUR
        return daily_wage
    return daily_wage

def main():
    print(f"The Daily wage of Employee is {cal_daily_wage()}")


if __name__ == "__main__" :
    main()