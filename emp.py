"""
    @Author: Deven Gupta
    @Date: 1-08-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 1-08-2024
    @Title : UC-6 Python program to Calculate Monthly Wage (day=20,hour=100)
"""   

print("Welcome to Employee Wage Computation Program\n")

import random

WAGE_PER_HOUR = 20
FULL_TIME_HOUR = 8
PART_TIME_HOUR = 4
MAX_HOURS = 100
MAX_DAYS = 20

def check_attendance():
    """
    Description:
        This function is used to check the attendance of the employee.
    Parameters:
        None
    Returns:
        int: 0 (Absent), 1 (Full Time), 2 (Part Time)
    """
    return random.choice([0, 1, 2])

def cal_daily_wage():
    """
    Description:
        This function is used to calculate the daily wage based on attendance.
    Parameters:
        None
    Returns:
        int: Daily wage after calculation
    """
    status = check_attendance()
    
    if status == 1:
        return WAGE_PER_HOUR * FULL_TIME_HOUR
    elif status == 2:
        return WAGE_PER_HOUR * PART_TIME_HOUR
    else:
        return 0

def monthly_wage():
    """
    Description:
        This function calculates the monthly wage until a total of 100 working hours or 20 days is reached.
    Parameters:
        None
    Returns:
        tuple: (total monthly wage, total working hours, total working days)
    """
    total_wage = 0
    total_hours = 0
    total_days = 0
    
    while total_hours < MAX_HOURS and total_days < MAX_DAYS:
        daily_wage = cal_daily_wage()
        total_wage += daily_wage
        if daily_wage > 0:
            if daily_wage == WAGE_PER_HOUR * FULL_TIME_HOUR:
                total_hours += FULL_TIME_HOUR
            else:
                total_hours += PART_TIME_HOUR
            total_days += 1

    return total_wage, total_hours, total_days

def main():
    wage, hours, days = monthly_wage()
    print(f"The Monthly wage of Employee is {wage}")
    print(f"Total Working Hours: {hours}")
    print(f"Total Working Days: {days}")

if __name__ == "__main__":
    main()
