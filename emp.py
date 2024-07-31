""" 
    @Author: Deven Gupta
    @Date: 31-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 31-07-2024
    @Title : UC-4 Python program to Calculate Wage using switch case

"""   
print("Welcome to Employee Wage Computation Program\n")

import random
WAGE_PER_HOUR = 20
FULL_TIME_HOUR = 8
PART_TIME_HOUR = 4


def check_attendance():
    """
    Description:
        This function used to Check attendance of employee
    Parameters:
        None
    Returns:
        int : 0, 1, 2
        
    """
    status = random.choice([0,1,2])
    if status == 1 :
        return 1
    elif status == 2 :
        return 2
    elif status == 0:
        return 0


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
    status = check_attendance()

    match status:
        case 1:
            print("Employee Full-time Employee")
            daily_wage = WAGE_PER_HOUR * FULL_TIME_HOUR
            return daily_wage
        case 2:
            print("Employee Part-time Employee")
            daily_wage = WAGE_PER_HOUR * PART_TIME_HOUR
            return daily_wage
        case 0:
             print("Employee Absent")
             return daily_wage


def main():
    print(f"The Daily wage of Employee is {cal_daily_wage()}")


if __name__ == "__main__" :
    main()