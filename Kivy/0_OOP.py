class Auto:
    def __init__(self, barwa, info, rozcznik):
        self.kolor = barwa
        self.ilosc_paliwa = 10
        self.kondycja = info
        self.tryb_eco = False
        self.spalanie_na_100 = 14
        self.wiek = 2023 - rozcznik

    def zasieg(self):
        zasieg = self.ilosc_paliwa / self.spalanie_na_100 * 100 * 0.9
        return round(zasieg)

    def ustaw_tryb(self, tryb):
        if tryb == 'eco':
            self.tryb_eco = True
            self.spalanie_na_100 = 10
            print('ustawiono tryb eco')
        elif tryb == 'normal':
            self.tryb_eco = False
            self.spalanie_na_100 = 14
            print('ustawiono tryb normal')
        else:
            print('bez zmian, komenda nierozpoznana')

moja_toyota = Auto('red', 4, 1970)
print(moja_toyota.wiek)
moja_toyota.wiek += 4
print(moja_toyota.wiek)
print('zasieg ',moja_toyota.zasieg())
moja_toyota.ustaw_tryb('eco')


slowo1 = 'mama'
slowo2 = 'tata'
print(type('mama'))
liczba = 4
print(type(liczba))

print(slowo1 + slowo2)
print(slowo1.replace('m','M',1))
print(slowo1 * liczba)
#print(slowo1 + liczba)

