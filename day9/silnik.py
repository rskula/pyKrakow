class Silnik(object):
    def __init__(self, c_pojemnosc, c_moc):
        self.pojemnosc = c_pojemnosc
        self.moc = c_moc
        self.odpalony = False

    def odpal(self):
        self.odpalony = True
