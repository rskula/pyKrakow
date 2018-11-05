class Employee:
    def __init__(self, c_first=None, c_last=None, c_rate=None):
        self.first = c_first
        self.last = c_last
        self.rate = c_rate


class EmployeeMonthly(Employee):
    # def __init__(self, c_first, c_last, c_salary):
    #     super().__init__(c_first, c_last)
    def salary(self, h):
        return int(self.rate * h / 160)


class EmployeeHourly(Employee):
    # def __init__(self, c_rate):
    def wages(self, h):
        return self.rate * h


e1 = EmployeeMonthly("Jan", "Kowalski", 1600)
print(e1.first, e1.last, e1.rate)
print(e1.salary(80))

e2 = EmployeeHourly()
e2.first, e2.last, e2.rate = "Jan", "Nowak", 10
print(e2.first, e2.last, e2.rate)
print(e2.wages(80))

print(isinstance(e1, Employee))
print(issubclass(EmployeeMonthly, Employee))