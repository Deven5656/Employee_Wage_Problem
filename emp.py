"""
    @Author: Deven Gupta
    @Date: 2-08-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 2-08-2024
    @Title : UC-9 Python program to Calculate Monthly Wage (Multiple Companies)
"""
import random

class EmployeeWage:
    FULL_TIME_HOUR = 8
    PART_TIME_HOUR = 4

    def __init__(self, wage_per_hour, max_hours, max_days):
        self.wage_per_hour = wage_per_hour
        self.max_hours = max_hours
        self.max_days = max_days

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
            return self.wage_per_hour * self.FULL_TIME_HOUR
        elif status == 2:
            return self.wage_per_hour * self.PART_TIME_HOUR
        else:
            return 0

    def compute_monthly_wage(self):
        """
        Description:
            This function calculates the monthly wage until a total of maximum working hours or maximum days is reached.
        Parameters:
            None
        Returns:
            tuple: (total monthly wage, total working hours, total working days, list containing hours worked per day)
        """
        total_wage = 0
        total_hours = 0
        total_days = 0
        hours_worked_per_day = []
        
        while total_hours < self.max_hours and total_days < self.max_days:
            daily_wage = self.cal_daily_wage()
            total_wage += daily_wage
            if daily_wage > 0:
                if daily_wage == self.wage_per_hour * self.FULL_TIME_HOUR:
                    total_hours += self.FULL_TIME_HOUR
                    hours_worked_per_day.append(self.FULL_TIME_HOUR)
                else:
                    total_hours += self.PART_TIME_HOUR
                    hours_worked_per_day.append(self.PART_TIME_HOUR)
                total_days += 1

        return total_wage, total_hours, total_days, hours_worked_per_day

class EmpWageBuilder:
    def __init__(self):
        self.companies = []

    def add_company(self, company_name, wage_per_hour, max_hours, max_days):
        self.companies.append({
            'name': company_name,
            'wage_per_hour': wage_per_hour,
            'max_hours': max_hours,
            'max_days': max_days
        })

    def compute_wages(self):
        for company in self.companies:
            employee_wage = EmployeeWage(company['wage_per_hour'],company['max_hours'],company['max_days'])
            wage, hours, days, hours_per_day = employee_wage.compute_monthly_wage()
            print(f"THE COMPANY NAME IS {company['name']}")
            print(f"The Monthly wage of Employee is {wage}")
            print(f"Total Working Hours: {hours}")
            print(f"Total Working Days: {days}")
            print(f"Hours worked per day: {hours_per_day}\n")

def main():
    builder = EmpWageBuilder()

    number_of_companies = int(input("Total companies: "))
    
    for _ in range(number_of_companies):
        company_name = input("Company name: ")
        wage_per_hour = int(input("Wage per hour: "))
        hours_per_month = int(input("Hours per month: "))
        days_per_month = int(input("Number of days per month: "))
        builder.add_company(company_name, wage_per_hour, hours_per_month, days_per_month)
    
    builder.compute_wages()

if __name__ == "__main__":
    main()
