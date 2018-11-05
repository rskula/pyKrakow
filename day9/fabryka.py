from samochod import Samochod
from silnik import Silnik


def szybszy(f_samochod1, f_samochod2):
    if f_samochod1.silnik.moc >= f_samochod2.silnik.moc:
        return f_samochod1
    else:
        return f_samochod2


samochod1 = Samochod('VW', 'EOS', Silnik(2.0, 130))
samochod2 = Samochod('VW', 'Jetta', Silnik(1.6, 110))

zwyciezca = szybszy(samochod1, samochod2)
print('{} {}'.format(zwyciezca.marka, zwyciezca.model))

zwyciezca.otworz()
zwyciezca.silnik.odpal()
if zwyciezca.otwarty and zwyciezca.silnik.odpalony: print('Brum, brum')
