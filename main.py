from back_end import *
from front_end import *

listcards = front_end.generateListCards()
usedcards = []

print("Selamat datang di permainan 24")
print("1. User")
print("2. File")
pilihan = int(input("> "))
if (pilihan == 1):
    menuGame()
else:
    back_end.menuFileEksternal()