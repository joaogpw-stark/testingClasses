import datetime
from employee import Employee, Developer, Manager

emp1 = Employee('Vitoria', 'Caroline', 'Head of People', 90000)
emp2 = Employee('Luca', 'Zarpelon', 'Advogado', 60000)
dev1 = Developer('Joao', 'Poletto', 'Developer', 50000, 'Python')

man1 = Manager('Matheus','Stark', 'lead of development', 200000, [])
print(man1.__dict__)
man1.add_employee(emp1)
man1.add_employee(emp2)
man1.add_employee(dev1)
man1.print_employees()

print(emp1)
print(emp1.personal_email)
emp1.fullname = 'Edward Sizorhands'
print(emp1)
print(emp1.personal_email)


# You can access all the information on an instance using:
#   print(f'Whole instance: {emp1.__dict__}')

# You can access all the information on an class using:
#   print(f'Whole instance: {Employee.__dict__}')

# -----------------------------------------------------------------------------------
# CLASS VARIABLES:
# -----------------------------------------------------------------------------------

# You can change class variables using:
#   Employee.raise_percentage = 1.05

# If you want to change a class variable use this, but it actually 
# creates a instance variable that is searched first than a class variable:
#   emp1.raise_percentage = 1.05

# But if you access the class variable with the following command, it 
# did not change even after the previous command, since it created an instance var:
#   Employee.raise_persentage 

# -----------------------------------------------------------------------------------
# CLASS METHODS:
# -----------------------------------------------------------------------------------

# To change the class variable we can use the class method:
# Employee.set_raise_percentage(1.05)

# You can also use class methods as an alternative constructor, 
# we created from_string_init():
# emp = Employee.from_string_init('Tereza-Poletto-CEO-200000')

# -----------------------------------------------------------------------------------
# STATIC METHODS:
# -----------------------------------------------------------------------------------

# Static methods are ran using the same sintax as the other ones:
# print(Employee.is_work_day(datetime.date(2016, 7, 10)))

