print("Hello world!")
#git-scm.com
def dluga_nazwa_funkcji():
    """parametry: ... """ # tzw. docstring
    print("Hello world!")

# pep8 pep0008
# dlugaNazwaFunkcji
# łańcuch znaków
# ctrl + / - ustaw komentarz/usuń komentarz
# Shift + Alt + strzałka góra/dół -- kopiowanie

imie = "Ala"
imie = 'Ala'
imie = """Ala ma
kota a
kot jest głodny."""
print(type(imie))
#<class 'str'>
imie = str("Ala") #poprzez konstruktor
print(type(5))
print(type(5.6))
print(type(True))
print(type(None))
# isinstance() sprawdzam czy zmienna jest danego typu
#<class 'str'>
#<class 'int'>
#<class 'float'>
#<class 'bool'>
#<class 'NoneType'>


print("Ala " + "ma kota.")
#print("Ala " + "ma " + 5 + " kotów.") #błąd nie można łączyć str z int
#print("Ala " + "ma " + str(5) + " kotów.")
ilosc_kotow=5
print("Ala " + "ma  {}  kotów.".format(ilosc_kotow))
print(f"Ala ma  {ilosc_kotow}  kotów.")
print("Ala ma  {1} {0} {2}  kotów.".format(4, 5, 7))
liczba = 6.84653219
print(f"liczba {liczba:.2f}") #2 miejsca dziesiętne
# http://pyformat.info

print(imie[0])
# imie[0] = "O" nie jest mutowalny
imie = imie.lower() #trzeba przypisać nową zmienną
print(imie)

# liczby
liczba = 1
liczbaf = 4.5
suma = liczba + liczbaf
print(1 + 2)
print(1 - 2)
print(1 / 2)
print(1 * 2)
print(1 // 2) # dzielenie bez reszty
print(1 ** 2) # potęgowanie
print(1 % 2) # modulo

print(0.1 + 0.2 == 0.3)
print(f"{0.1:.30f}")

# listy
lista = []
lista2 = [1, 2, 3]
lista3 = [1, "Ala", 3.4, True, None]
final_list = lista + lista2 + lista3
lista2[2] #wartość 3, indeks 2
lista4 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
lista4[1][1] # 5

# słownik
slownik = {}
slownik2 = {"klucz": "wartosc"}
slownik3 = {0: "Adam"}
slownik2["klucz"]
slownik3[0]
slownik2.keys()
slownik2.values()