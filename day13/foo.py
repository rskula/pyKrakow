class Person:
    def __init__(self, c_fn, c_ln):
        self.__fn = c_fn
        self.__ln = c_ln

    @property
    def fn(self):
        return self.__fn.capitalize()

    @fn.setter
    def fn(self, val):
        self.__fn = val.capitalize()

    @property
    def ln(self):
        return self.__ln.capitalize()

    @ln.setter
    def ln(self, val):
        self.__ln = val.capitalize()


p = Person("jan", "kowalski")
p.fn = "adam"
p.ln = "nowak"
print(p.fn + " " + p.ln)
