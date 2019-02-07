from tkinter import *
import random
import os
import sys

pic = [0,0,0,0]

# def generateRandomNumber():
#     num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
#     return random.choice(num)

# def generateRandomSuit():
#     suit = ['C', 'D', 'H', 'S']
#     return random.choice(suit)

def generateListCards():
    listcards = []
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
    shape = ['C', 'D', 'H', 'S']
    for i in number:
        for j in shape:
            listcards.append(i+j)
    return listcards

def generateRandomCards():
    # numTable = [0,0,0,0]; suitTable = [0,0,0,0]
    for x in range(4):
        # numTable[x] = generateRandomNumber()
        # suitTable[x] = generateRandomSuit()
        # for b in range(x):
        #     if(b != x):
        #         while ((numTable[b] == numTable[x]) and (suitTable[b] == suitTable[x])):
        #             suitTable[x] = generateRandomSuit()
        try:
            coba = random.choice(listcards)
            listcards.remove(coba)
            usedcards.append(coba)
            pic[x] = "Cards_2/" + coba + ".png"
        except IndexError:
            GameOverText = Label(game, text='Game Over!', bg='#90AB76', font=25)
            GameOverText.place(x=380, y=50)
            showGameOverButton = Button(game, text = 'Restart!', command = restartGame)
            showGameOverButton.pack()
            showGameOverButton.place(x=380, y= 120)


    card1 = PhotoImage(file = pic[0]); card1 = card1.subsample(2, 2)
    card2 = PhotoImage(file = pic[1]); card2 = card2.subsample(2, 2)
    card3 = PhotoImage(file = pic[2]); card3 = card3.subsample(2, 2)
    card4 = PhotoImage(file = pic[3]); card4 = card4.subsample(2, 2)

    showCard1 = Label(game, image = card1); showCard1.place(x = 100, y = 300);showCard1.configure( image= card1); showCard1.image = card1 
    showCard2 = Label(game, image = card2); showCard2.place(x = 300, y = 300);showCard2.configure( image= card2); showCard2.image = card2
    showCard3 = Label(game, image = card3); showCard3.place(x = 500, y = 300);showCard3.configure( image= card3); showCard3.image = card3
    showCard4 = Label(game, image = card4); showCard4.place(x = 700, y = 300);showCard4.configure( image= card4); showCard4.image = card4

def restartGame():
    python = sys.executable
    os.execl(python, python, * sys.argv)

# generate list cards and used cards
listcards = generateListCards()
usedcards = []

# def MainKartuKuy():
game = Tk() # game = main windows
#menus
menu = Menu(game)
game.config(menu = menu)
subFile= Menu(menu)
menu.add_cascade(label = "File", menu = subFile)

subFile.add_command(label = "New File", command=restartGame)
# subFile.add_command(label = "Delete File")
subFile.add_separator()
subFile.add_command(label = "Exit", command = game.quit)

subEdit = Menu(menu)
menu.add_cascade(label = "Edit", menu = subEdit)
subEdit.add_command(label = "Edit muka biar ganteng")

game.title("24-Game Solver")
game.geometry("900x500")
game.configure(bg = "#90AB76")

# backCard = PhotoImage(file = "Cards_2/back.png"); backCard = backCard.subsample(2, 2)
# showBackCard = Label(game, image = backCard); showBackCard.place(x = 700, y = 30)

backCard = PhotoImage(file = "Cards_2/back.png"); backCard = backCard.subsample(2, 2)
showBackCard = Button(game, image = backCard, command = generateRandomCards)
showBackCard.pack()
showBackCard.place(x=700, y= 30)

# # Shuffle Button
# shuffleButton = Button(game, image = photo, command = generateRandomCards)
# shuffleButton.pack()

# MainKartuKuy()
game.mainloop()

