from cmu_graphics import *

class buttons:
    def __init__(self, x0, y0, x, y, fill, color, border, width, textSize, text, font):
        self.x0 = x0
        self.y0 = y0
        self.x = x
        self.y = y
        self.fill = fill
        self.color = color
        self.width = width
        self.border = border
        self.textSize = textSize
        self.text = text
        self.font = font

    def drawButton(self, app):
        drawRect(self.x0, self.y0, self.x, self.y, fill=self.fill, border=self.border, borderWidth=self.width)
        drawLabel(self.text, self.x0 + (self.x/2), self.y0 + (self.y/2), size=self.textSize, font=self.font, fill=self.color)

    def intersection(self, app, mouseX, mouseY):
        return ((mouseX >= self.x0 and mouseX <= self.x0 + self.x) and (mouseY >= self.y0 and mouseY <= self.y0 + self.y))
    
# pokemon fire red font from https://www.cufonfonts.com/font/pokemon-fire-red
startContinue = buttons(100, 200, 80, 40, None, 'white', 'white', 2, 22, 'Start Game', font='pokemon fire red') # all buttons you can click
startSave = buttons(300, 200, 80, 40, None, 'white', 'white',  2, 22, 'Load Saves', font='pokemon fire red')
save1 = buttons(20, 80, 120, 40, None, 'white', 'white',  2, 22, 'Save 1', font='pokemon fire red')
save2 = buttons(180, 80, 120, 40, None, 'white', 'white',  2, 22, 'Save 2', font='pokemon fire red')
save3 = buttons(340, 80, 120, 40, None, 'white', 'white',  2, 22, 'Save 3', font='pokemon fire red')
delete1 = buttons(20, 185, 120, 40, None, 'white', 'white',  2, 22, 'Delete Save 1', font='pokemon fire red')
delete2 = buttons(180, 185, 120, 40, None, 'white', 'white',  2, 22, 'Delete Save 2', font='pokemon fire red')
delete3 = buttons(340, 185, 120, 40, None, 'white', 'white',  2, 22, 'Delete Save 3', font='pokemon fire red')
saveBack = buttons(180, 280, 120, 40, None, 'white', 'white',  2, 22, 'Back', font='pokemon fire red')
choosePokemonContinue = buttons(200, 260, 80, 40, None, 'black', 'black', 2, 22, 'Continue', font='pokemon fire red')
cardBack = buttons(0, 280, 120, 40, None, 'black', 'black', 2, 22, 'Back', font='pokemon fire red')
cardSelect = buttons(360, 280, 120, 40, None, 'black', 'black', 2, 22, 'Select/Unselect', font='pokemon fire red')
shopContinue = buttons(200, 290, 80, 20, None, 'black', 'black', 2, 22, 'Continue', font='pokemon fire red')
orderBack = buttons(200, 290, 80, 20, None, 'black', 'black', 2, 22, 'Back', font='pokemon fire red')
itemBack = buttons(0, 280, 120, 40, None, 'black', 'black', 2, 22, 'Back', font='pokemon fire red')
itemSell = buttons(180, 280, 120, 40, None, 'black', 'black', 2, 22, 'Sell', font='pokemon fire red')
itemBuy = buttons(360, 280, 120, 40, None, 'black', 'black', 2, 22, 'Buy', font='pokemon fire red')
combatFight = buttons(140, 210, 170, 55, 'white', 'black', 'black', 2, 24, 'Fight', font='pokemon fire red')
combatBag = buttons(310, 210, 170, 55, 'white', 'black', 'black', 2, 24, 'Bag', font='pokemon fire red')
combatPokemon = buttons(140, 265, 170, 55, 'white', 'black', 'black', 2, 24, 'Pokemon', font='pokemon fire red')
combatSurrender = buttons(310, 265, 170, 55, 'white', 'black', 'black', 2, 24, 'Surrender', font='pokemon fire red')
move1 = buttons(140, 210, 170, 55, None, 'black', 'black', 2, 22, '', font='pokemon fire red')
move2 = buttons(310, 210, 170, 55, None, 'black', 'black', 2, 22, '', font='pokemon fire red')
move3 = buttons(140, 265, 170, 55, None, 'black', 'black', 2, 22, '', font='pokemon fire red')
move4 = buttons(310, 265, 170, 55, None, 'black', 'black', 2, 22, '', font='pokemon fire red')
rotateBack = buttons(200, 290, 80, 20, None, 'black', 'black', 2, 22, 'Back', font='pokemon fire red')
bagBack = buttons(180, 280, 120, 40, None, 'black', 'black', 2, 22, 'Back', font='pokemon fire red')
playAgain = buttons(180, 280, 120, 40, 'white', 'black', 'black', 2, 22, 'Play Again', font='pokemon fire red')