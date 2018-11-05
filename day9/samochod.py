class Samochod(object):
    def __init__(self, c_marka, c_model, c_silnik):
        self.marka = c_marka
        self.model = c_model
        self.silnik = c_silnik
        self.odpalony = False

    def otworz(self):
        self.otwarty = True
