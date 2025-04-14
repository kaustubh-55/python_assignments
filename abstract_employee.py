from abc import ABC , abstractmethod

class Employee(ABC):

    @abstractmethod
    def salary(self):
        pass

    @abstractmethod
    def strict_salary(self):
        pass

class EMP_Salary(Employee):

    def __init__(self, name , emp_salary , bonus , leaves , dept):
        self.name = name
        self.emp_salary = emp_salary
        self.bonus = bonus
        self.leaves = leaves
        self.dept = dept

    def salary(self):
        print(f"salary of employee before bonus :{self.emp_salary}")
        new_salary = self.emp_salary + self.bonus
        print(f"updated salary of employee after bonus is : {new_salary}")
    
    def strict_salary(self):
        salary_per_day = 1000
        strict_salary = self.emp_salary - (salary_per_day * self.leaves)
        print(f"Employee has taken leaves for {self.leaves} days , so strict salary will be {strict_salary}")
        #Print()        

    def employee_details(self):
        print(f"Employee name : {self.name} , Salary of employee : {self.emp_salary} , Bonus is :{self.bonus} , Leaves taken by employee :{self.leaves} , department of employee : {self.dept}")
        

emp1= EMP_Salary("Ram" , 45000 , 10000 , 5 , "IT")

emp1.salary()
emp1.strict_salary()
emp1.employee_details()