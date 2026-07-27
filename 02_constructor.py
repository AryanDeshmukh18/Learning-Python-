class Employee:
    def __init__(self,name,salary,bond):
        self.name = name
        self.salary = salary
        self.bond = bond
    def get_salary(self):
        return self.salary
    
e1 = Employee("Aryan",35000,2)
e1.getinfo()