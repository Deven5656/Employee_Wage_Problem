"""
    @Author: Deven Gupta
    @Date: 4-08-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 4-08-2024
    @Title : UC-10-14 Python program to Calculate Monthly Wage (Manage employee and company)
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
        self.hours_per_day = []

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
            This function is used to calculate daily wage
        Parameters:
            None
        Returns:
            int: Daily wage
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
            This function is used to calculate monthly wage until a total working hours or days is reached
        Parameters:
            None
        Returns:
            tuple: (total monthly wage, total working hours, total working days, list of hours worked per day)
        """

        while self.total_hours < self.MAX_HOURS and self.total_days < self.MAX_DAYS:
            daily_wage = self.cal_daily_wage()
            self.total_wage += daily_wage
            
            if daily_wage > 0:
                if daily_wage == self.WAGE_PER_HOUR * self.FULL_TIME_HOUR:
                    self.total_hours += self.FULL_TIME_HOUR
                    self.hours_per_day.append(self.FULL_TIME_HOUR)
                else:
                    self.total_hours += self.PART_TIME_HOUR
                    self.hours_per_day.append(self.PART_TIME_HOUR)
                self.total_days += 1
            
            # Cap wage calculation at MAX_HOURS
            if self.total_hours >= self.MAX_HOURS:
                self.total_wage = min(self.total_wage, self.WAGE_PER_HOUR * self.MAX_HOURS)
                break

        return self.total_wage, self.total_hours, self.total_days, self.hours_per_day

class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name
        self.wage_calculator = EmployeeWage()

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}"

class Company:
    def __init__(self, company_name, wage_per_hour, total_working_days, total_monthly_hours):
        self.company_name = company_name
        self.employees = {}
        self.wage_per_hour = wage_per_hour
        self.total_working_days = total_working_days
        self.total_monthly_hours = total_monthly_hours

    def add_employee(self, emp_id, name):
        """
        Description:
            This function is used to add employee
        Parameters:
            emp_id: Numeric value
            name : employee name
        Returns:
            none
        """
        if emp_id in self.employees:
            print(f"Employee with ID {emp_id} already exists.")
        else:
            self.employees[emp_id] = Employee(emp_id, name)
            print(f"Employee {name} added successfully.")

    def get_employee(self, emp_id):
        """
        Description:
            This function is used to get id of employee
        Parameters:
            emp_id: Numeric value
        Returns:
            key of dict
        """
        return self.employees.get(emp_id, "Employee not found.")

    def remove_employee(self, emp_id):
        """
        Description:
            This function is used to remove employee
        Parameters:
            emp_id: Numeric value
        Returns:
            none
        """
        if emp_id in self.employees:
            del self.employees[emp_id]
            print(f"Employee {emp_id} removed successfully.")
        else:
            print("Employee not found.")

    def list_employees(self):
        """
        Description:
            This function is used to display the employee 
        Parameters:
            none
        Returns:
            none
        """
        if not self.employees:
            print("No employees in the company.")
        else:
            for emp in self.employees.values():
                print(emp)

    def calculate_monthly_wages(self):
        """
        Description:
            This function is used to calculate monthly wage
        Parameters:
            none
        Returns:
            dict : employee id and  monthly wage
        """
        wages = {}
        for emp in self.employees.values():
            wage_calculator = emp.wage_calculator
            wage, hours, days, _ = wage_calculator.compute_monthly_wage()
            wages[emp.emp_id] = wage
        
        return wages

    def __str__(self):
        return f"Company: {self.company_name}, Wage Per Hour: {self.wage_per_hour}, Total Working Days: {self.total_working_days}, Total Monthly Hours: {self.total_monthly_hours}"

class CompanyManager:
    def __init__(self):
        self.companies = {}    # company name ,wage per hr,total days,total hr

    def add_company(self, company_name, wage_per_hour, total_working_days, total_monthly_hours):
        """
        Description:
            This function is used to add company
        Parameters:
            company_name : company name
            wage_per_hour : amount per hr
            total_working_days : total days in month
            total_monthly_hours : total hr 
        Returns:
            none
        """
        if company_name in self.companies:
            print(f"Company {company_name} already exists.")
        else:
            self.companies[company_name] = Company(company_name, wage_per_hour, total_working_days, total_monthly_hours)
            print(f"Company {company_name} added successfully.")

    def remove_company(self, company_name):
        """
        Description:
            This function is used to remove company
        Parameters:
            company_name : company name 
        Returns:
            none
        """
        if company_name in self.companies:
            del self.companies[company_name]
            print(f"Company {company_name} removed successfully.")
        else:
            print("Company not found.")

    def get_company(self, company_name):
        """
        Description:
            This function is used to get the name of company
        Parameters:
            company_name : company name
        Returns:
            key of dict
        """
        return self.companies.get(company_name, "Company not found.")

    def list_companies(self):
        """
        Description:
            This function is used to display company info
        Parameters:
            none
        Returns:
            none
        """
        if not self.companies:
            print("No companies in the system.")
        else:
            for company in self.companies.values():
                print(company)

def main():
    manager = CompanyManager()

    while True:
        print("\n--- Company and Employee Management System ---")
        print("1. Add Company")
        print("2. Remove Company")
        print("3. List Companies")
        print("4. Manage Employees in a Company")
        print("5. Calculate Monthly Wages for a Company")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            company_name = input("Enter company name: ")
            wage_per_hour = float(input("Enter wage per hour: "))
            total_working_days = int(input("Enter total working days in a month: "))
            total_monthly_hours = int(input("Enter total monthly hours: "))
            manager.add_company(company_name, wage_per_hour, total_working_days, total_monthly_hours)
        
        elif choice == '2':
            company_name = input("Enter company name to remove: ")
            manager.remove_company(company_name)

        elif choice == '3':
            manager.list_companies()

        elif choice == '4':
            company_name = input("Enter company name: ")
            company = manager.get_company(company_name)
            if company == "Company not found.":
                print(company)
            else:
                while True:
                    print(f"\nManaging employees for {company_name}")
                    print("1. Add Employee")
                    print("2. Remove Employee")
                    print("3. List Employees")
                    print("4. Go Back")
                    
                    emp_choice = input("Enter your choice: ")

                    if emp_choice == '1':
                        emp_id = int(input("Enter employee ID: "))
                        name = input("Enter employee name: ")
                        company.add_employee(emp_id, name)

                    elif emp_choice == '2':
                        emp_id = int(input("Enter employee ID to remove: "))
                        company.remove_employee(emp_id)

                    elif emp_choice == '3':
                        company.list_employees()

                    elif emp_choice == '4':
                        break

                    else:
                        print("Invalid choice. Please try again.")

        elif choice == '5':
            company_name = input("Enter company name to calculate wages for: ")
            company = manager.get_company(company_name)
            if company == "Company not found.":
                print(company)
            else:
                wages = company.calculate_monthly_wages()
                print(f"\nMonthly Wages for {company_name}:")
                for emp_id, wage in wages.items():
                    print(f"Employee ID: {emp_id}, Monthly Wage: {wage:.2f}")

        elif choice == '6':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
