"""
    @Author: Deven Gupta
    @Date: 1-08-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 1-08-2024
    @Title : UC-7 Python program to Calculate Monthly Wage (day=20,hour=100) (refactor using class)
"""
import random

class EmployeeWage:
   
    WAGE_PER_HOUR = 20
    FULL_TIME_HOUR = 8
    PART_TIME_HOUR = 4
    MAX_HOURS = 100
    MAX_DAYS = 20

    def __init__(self):
        self.total_wage = 0
        self.total_hours = 0
        self.total_days = 0
        self.lst_hour = []

   
    def check_attendance(self):
        """
        Description:
            This function is used to check the attendance of the employee.
        Parameters:
            None
        Returns:
            int: 0 (Absent), 1 (Full Time), 2 (Part Time)
        """

        return random.choice([0, 1, 2])

    def cal_daily_wage(self):
        """
        Description:
            This function is used to Calculate the daily wage based on attendance.
        Parameters:
            None
        Returns:
            int: Daily wage after calculation
        """

        status = self.check_attendance()
        
        if status == 1:
            return self.WAGE_PER_HOUR * self.FULL_TIME_HOUR
        elif status == 2:
            return self.WAGE_PER_HOUR * self.PART_TIME_HOUR
        else:
            return 0

    def compute_monthly_wage(self):
        """
        Description:
            This function calculates the monthly wage until a total of 100 working hours or 20 days is reached.
        Parameters:
            None
        Returns:
            tuple: (total monthly wage, total working hours, total working days ,list containing hours)
        """
        while self.total_hours < self.MAX_HOURS and self.total_days < self.MAX_DAYS:
            daily_wage = self.cal_daily_wage()
            self.total_wage += daily_wage
            if daily_wage > 0:
                if daily_wage == self.WAGE_PER_HOUR * self.FULL_TIME_HOUR:
                    self.total_hours += self.FULL_TIME_HOUR
                    self.lst_hour.append(self.FULL_TIME_HOUR)
                else:
                    self.total_hours += self.PART_TIME_HOUR
                    self.lst_hour.append(self.PART_TIME_HOUR)
                self.total_days += 1
            
            if self.total_hours >= 104:
                self.total_wage = 2000
                break

        return self.total_wage, self.total_hours, self.total_days, self.lst_hour

def main():
    emp_wage = EmployeeWage()
    wage, hours, days, lst = emp_wage.compute_monthly_wage()
    print(f"The Monthly wage of Employee is {wage}")
    print(f"Total Working Hours: {hours}")
    print(f"Total Working Days: {days}")
    print(f"Hours worked per day: {lst}")

if __name__ == "__main__":
    main()
