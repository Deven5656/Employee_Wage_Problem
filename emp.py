"""
    @Author: Deven Gupta
    @Date: 1-08-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 1-08-2024
    @Title : UC-8 Python program to Calculate Monthly Wage (Multiple Companies)
"""
import random

class EmployeeWage:

    FULL_TIME_HOUR = 8
    PART_TIME_HOUR = 4
   
    def __init__(self,wph,max_hours,max_days):
        self.WAGE_PER_HOUR = wph
        self.MAX_HOURS = max_hours
        self.MAX_DAYS = max_days
       

   
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
        total_wage = 0
        total_hours = 0
        total_days = 0
        lst_hour = []
        while total_hours < self.MAX_HOURS and total_days < self.MAX_DAYS:
            daily_wage = self.cal_daily_wage()
            total_wage += daily_wage
            if daily_wage > 0:
                if daily_wage == self.WAGE_PER_HOUR * self.FULL_TIME_HOUR:
                    total_hours += self.FULL_TIME_HOUR
                    lst_hour.append(self.FULL_TIME_HOUR)
                else:
                    total_hours += self.PART_TIME_HOUR
                    lst_hour.append(self.PART_TIME_HOUR)
                total_days += 1

        return total_wage, total_hours, total_days, lst_hour

def main():

    number_of_company =int(input("Total company : "))

    for _ in range(number_of_company):
        company_name =input("company name : ")
        wage_per_hour =int(input("wage per hour : "))
        hours_no =int(input("hours per month : "))
        day_no =int(input("Number of days : "))
        company = EmployeeWage(wage_per_hour,hours_no,day_no)
        wage, hours, days, lst = company.compute_monthly_wage()
        print(f"THE COMPANY NAME IS {company_name}")
        print(f"The Monthly wage of Employee is {wage}")
        print(f"Total Working Hours: {hours}")
        print(f"Total Working Days: {days}")
        print(f"Hours worked per day: {lst}\n")

        
    # tata = EmployeeWage(20,100,20)
    # wage, hours, days, lst = tata.compute_monthly_wage()
    # print(f"The Monthly wage of Employee is {wage}")
    # print(f"Total Working Hours: {hours}")
    # print(f"Total Working Days: {days}")
    # print(f"Hours worked per day: {lst}\n")


    # infosys = EmployeeWage(30,150,30)
    # wage, hours, days, lst = infosys.compute_monthly_wage()
    # print(f"The Monthly wage of Employee is {wage}")
    # print(f"Total Working Hours: {hours}")
    # print(f"Total Working Days: {days}")
    # print(f"Hours worked per day: {lst}\n")

if __name__ == "__main__":
    main()
