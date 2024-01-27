class Employee:
    # Class variable to count the number of Employees
    no_of_employees = 0

    def __init__(self, name, family, salary, department):
        # Instance variables
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department

        # Increment the employee count
        Employee.no_of_employees += 1

    def average_salary(self, *salaries):
        # Calculate and return the average salary
        total_salary = sum(salaries) + self.salary
        num_employees = len(salaries) + 1
        return total_salary / num_employees


class FullTimeEmployee(Employee):
    # FullTimeEmployee class inheriting from Employee class
    def __init__(self, name, family, salary, department, bonus):
        # Call the constructor of the parent class
        super().__init__(name, family, salary, department)
        self.bonus = bonus


# Creating instances of Employee and FullTimeEmployee
employee1 = Employee("Deepthi Deshpande", "Family1", 50000, "HR")
employee2 = Employee("Gayathri Pandey", "Family2", 60000, "Finance")

full_time_employee = FullTimeEmployee("Anuhya Ane", "Family3", 70000, "IT", 10000)

# Calling member functions
average_salary_employee = employee1.average_salary(employee2.salary)
average_salary_fulltime = full_time_employee.average_salary()

print(f"Total number of employees: {Employee.no_of_employees}")
print(f"Average salary for all employees: {average_salary_employee}")
print(f"Average salary for FullTimeEmployee: {average_salary_fulltime}")




