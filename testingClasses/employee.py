# This is the employee class:

class Employee:

    # Here we define class variables that are the same across every instance:
    raise_percentage = 1.04     
    number_of_employees = 0

    def __init__(self, first_name, last_name, role, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.pay = pay
        self.personal_email = f'{self.first_name}.{self.last_name}@hotmail.com'
        # Every time a new instance is created number of employees increases by 1:
        Employee.number_of_employees += 1


    # If we defined the email instance variable in the constructor (like the personal email), by changing 
    # the first/last name the email would not change. By using the property decorator email will be 
    # treated as a varaible (no need of parenthesis) but updated once the first/last name changes:
    ## Note that when using the property atribute you need to return the value, it stores as a var.
    @property
    def email(self):
        return f'{self.first_name}.{self.last_name}@starkbank.com'

    @ property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    # Here we are using a setter decorator, this is here because if we want to change directly 
    # the full name of an instance (that means changing its first and last name, since when the 
    # full name method is called it regenerates the full name) this was not here it would not work.
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last


    def apply_raise(self):
        # This will change the pay of the employee after called
        self.pay = int(self.pay * self.raise_percentage)

    # Now we will define a class method, the previous ones are instance methods,
    # a class method will change class variables, in this case the raise_percentage
    @classmethod
    def set_raise_percentage(cls, percentage):
        cls.raise_percentage = percentage

    # We can also use class methods as alternative constructors, lets say that the
    # initilization variables come in the following string: 'first_name-last_name-role-pay':
    @classmethod
    def from_string_init(cls, str):
        # First you need to split the string:
        first_name, last_name, role, pay = str.split('-')
        return cls(first_name, last_name, role, pay)

    # We can also define static methods that do not need any class or instance varaibles:
    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    # We can also change the special methods, methods that are already built in:
    # repr is a method to return data in code format to repeat that object:
    def __repr__(self):
        return f'Employee({self.first_name},{self.last_name},{self.role},{self.pay})'

    # This is the representation of the object, when print(object) is called this is tha format it will appear:
    def __str__(self):
        return f'Full Name: {self.fullname}, Email: {self.email}, Role: {self.role}, Pay: {self.pay}'

# -----------------------------------
# INHERIT CLASSES (SUBCLASSES):
# -----------------------------------

class Developer(Employee):

    # Now we can redefine class variables only for this subclass:
    raise_percentage = 1.08

    # If we want more information than the parent class, just add to the arg:
    def __init__(self, first_name, last_name, role, pay, programing_language):
        # Then let super.__init__() use the parent class to initialize the parent arg
        super().__init__(first_name, last_name, role, pay)
        self.programing_language = programing_language

# Lets create a manager class that takes a list of employee objects that he/she manages:
class Manager(Employee):

    def __init__(self, first_name, last_name, role, pay, employees_list=None):
        super().__init__(first_name, last_name, role, pay)
        if employees_list is None:
            self.employees_list = []
        else:
            self.employees_list = employees_list
        
    # Add employee to the list:
    def add_employee(self,employee):
        if employee not in self.employees_list:
            self.employees_list.append(employee)

    # Remoce employee to the list:
    def remove_employee(self,employee):
        if employee in self.employees_list:
            self.employees_list.remove(employee)

    # Print the full name of the employees that the manager manages:
    def print_employees(self):
        for employee in self.employees_list:
            print(f'--> {employee.fullname}')