class Clinic:
    schedule = {}
    @classmethod
    def input_schedule(cls):
        pass

    @classmethod
    def get_daily_schedule(cls):
        pass

    @classmethod
    def get_doctors_schedule(cls):
        pass


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


class Doctor(Person):
    def __init__(self, c_fn, c_ln):
        super(Doctor, self).__init__(c_fn, c_ln)


class Patient(Person):
    def __init__(self, c_fn, c_ln):
        super(Patient, self).__init__(c_fn, c_ln)


def main():
    d1 = Doctor("jan", "nowak")
    p1 = Patient("adam", "kowal")
    p2 = Patient("ewa", "nowicka")
    p3 = Patient("piotr", "pawlowski")
    p4 = Patient("anna", "kowalska")
    p5 = Patient("janina", "pawlowska")


if __name__ == '__main__':
    main()
