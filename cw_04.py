# zadanie 1 ---------
text = '4 8 12 16 20 24 28'

plik = open('Dzielniki_liczby_4.txt', 'w', encoding = 'utf-8')

plik.write (text)


plik.close()
# zadanie 2 ------------

plik = open('Dzielniki_liczby_4.txt', 'r')

text = plik.read()

print(text)

plik.close()

# zadanie 3 -----------
plik = open('Dzielniki_liczby_4.txt', 'w')
plik.write(text)
plik.write ("\n to sa kolejne linijki\n")
plik.write ("a to jeszcze inne\n")
plik.close()

plik = open('Dzielniki_liczby_4.txt', 'r')
text = plik.read()
print(text)
plik.close()

# zaadanie 4 -----------

class NaZakupy:
    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    def wyswietl(self):
        print(f"{self.nazwa_produktu}")
        print(f"ilosc: {self.ilosc}")
        print(f"jednostka miary: {self.jednostka_miary}")
        print(f"cena: {self.cena_jed} zlote")
    def ile_produktu(self):
        self.ilosc = str(self.ilosc)
        return print(f"ilosc: {self.ilosc} {self.jednostka_miary} ")
    def ile_kosztuje(self):
        self.ilosc = int(self.ilosc)
        self.koszt = self.ilosc * self.cena_jed
        return print (f"kosztuje: {self.koszt} zlote")
ziemniaki = NaZakupy("ziemniaki",2,"kilogramy",4)
sok=NaZakupy("sok",6,"sztuki",2)
ziemniaki.wyswietl()
ziemniaki.ile_produktu()
ziemniaki.ile_kosztuje()
sok.wyswietl()
sok.ile_produktu()
sok.ile_kosztuje()

# zadanie 5 ---------------

class Ciag:
    def __init__(self,wyswietl_dane,pobierz_elementy,pobierz_parametry,policz_sume,policz_elementy):
        self.wyswietl_dane = wyswietl_dane
        self.pobierz_elementy = pobierz_elementy
        self.pobierz_parametry = pobierz_parametry
        self.policz_sume = policz_sume
        self.policz_elementy = policz_elementy
    def wyswietl_dane(self):
        print(f"dane: {self.wyswietl_dane}")
        print(f"pobrane elementy: {self.pobierz_elementy}")
        print(f"pobrane parametry: {self.pobierz_parametry}")
        print(f"suma: {self.policz_sume}")
        print(f"ilosc elementow: {self.policz_elementy}")
   # def pobierz_elementy(self):

   # def pobierz_parametry(self):
    #def policz_sume(self):
    #def policz_elementy(self):

# zadanie 6 -----------

class slowa:
    def __init__(self,x,y):
        self.wyraz1=x
        self.wyraz2=y
    def sprawdz_czy_palindrom(self):
        if (len(self.wyraz1)%2==0):
            for i in range(0, int(len(self.wyraz1)/2-1)):
                if(self.wyraz1[i]!=self.wyraz1[len(self.wyraz1)-i-1]):
                    return print ('Wyraz nie jest palindromem')
        else:
            for i in range(0,int((len(self.wyraz1)-1)/2)):
                if(self.wyraz1[i]!=self.wyraz1[len(self.wyraz1)-i-1]):
                    return print ('Wyraz nie jest palindromem')
        return print ('Wyraz 1 jest palindromem')
    def sprawdz_czy_metagramy(self):
        if(len(self.wyraz1)!=len(self.wyraz2)):
            return print("Wyrazu nie sa metagramami")
        else:
            count = 0
            for i in range(0,len(self.wyraz1)-1):
                if(self.wyraz1[i]!=self.wyraz2[i]):
                    count+=1
                    if (count>1):
                        return print ('Wyrazy nie sa metagramami')
            if(count!=1):
                return print ('Wyrazy nie sa metagramami')
            
        return print ('Wyrazy sa metagramami')
    def sprawdz_czy_anagramy(self):
        if(len(self.wyraz1)!=len(self.wyraz2)):
            return print ('Wyrazy nie sa anagramami')
        else:
            for i in range(0,len(self.wyraz1)):
                if (self.wyraz1.count(self.wyraz1[i])!=self.wyraz2.count(self.wyraz1[i])):
                    return print ('Wyrazy nie sa anagrami')
        return print ('Wyrazy sa anagrami')
    def wyswietl_wyraz(self):
        print(self.wyraz1)
        print(self.wyraz2)
    
wyrazy = slowa('kajak','majak')
wyrazy.sprawdz_czy_palindrom()
wyrazy.sprawdz_czy_metagramy()
wyrazy.sprawdz_czy_anagramy()
wyrazy.wyswietl_wyraz()
