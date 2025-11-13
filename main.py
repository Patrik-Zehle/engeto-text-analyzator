import sys

UZIVATELE = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

TEXTS = [
    '''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30 and the Union Pacific Railroad,
which traverse the valley.
''',
    '''
At the base of Fossil Butte are the bright
red, purple, yellow and green beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.
''',
    '''
The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.
'''
]

ODDELOVAC = "-" * 40

print(ODDELOVAC)
username = input("username: ")
password = input("password: ")
print(ODDELOVAC)

if UZIVATELE.get(username) != password:
    print("unregistered user, terminating the program..")
    sys.exit()

print(f"Welcome to the app, {username}")
pocet_textu = len(TEXTS)
print(f"We have {pocet_textu} texts to be analyzed.")
print(ODDELOVAC)

vyber = input(f"Enter a number btw. 1 and {pocet_textu} to select: ")

if not vyber.isnumeric():
    print("Invalid input, terminating the program..")
    sys.exit()

vyber_cislo = int(vyber)

if not (1 <= vyber_cislo <= pocet_textu):
    print("Invalid number, terminating the program..")
    sys.exit()

print(ODDELOVAC)

text = TEXTS[vyber_cislo - 1]
slova = text.split()

pocet_slov = 0
slova_title = 0
slova_upper = 0
slova_lower = 0
pocet_cisel = 0
suma_cisel = 0
delky_slov = {}

for slovo in slova:
    ciste_slovo = slovo.strip(".,:;")

    if not ciste_slovo:
        continue

    pocet_slov += 1

    if ciste_slovo.istitle():
        slova_title += 1
    elif ciste_slovo.isupper() and ciste_slovo.isalpha():
        slova_upper += 1
    elif ciste_slovo.islower():
        slova_lower += 1
    
    if ciste_slovo.isnumeric():
        pocet_cisel += 1
        suma_cisel += int(ciste_slovo)

    delka = len(ciste_slovo)
    delky_slov[delka] = delky_slov.get(delka, 0) + 1

print(f"There are {pocet_slov} words in the selected text.")
print(f"There are {slova_title} titlecase words.")
print(f"There are {slova_upper} uppercase words.")
print(f"There are {slova_lower} lowercase words.")
print(f"There are {pocet_cisel} numeric strings.")
print(f"The sum of all the numbers {suma_cisel}")
print(ODDELOVAC)

print(f"{'LEN':>3} | {'OCCURRENCES':<20} | {'NR.':<3}")
print(ODDELOVAC)

if delky_slov:
    max_pocet = max(delky_slov.values())
else:
    max_pocet = 0

for delka in sorted(delky_slov.keys()):
    pocet = delky_slov[delka]
    hvezdy = "*" * pocet
    print(f"{delka:>3} | {hvezdy:<{max_pocet}} | {pocet}")

print(ODDELOVAC)