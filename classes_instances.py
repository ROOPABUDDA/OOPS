class Employee:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = first + '.' + last + '@myfirm.com'
		self.pay = pay

	def fullname(self):
		return "{} {}".format(self.first, self.last)

emp1 = Employee('Roopa', 'Budda', 60000)
emp2 = Employee('Test', 'User', 50000)

print(emp1.fullname())
print(emp2.fullname())
print(Employee.fullname(emp2))
