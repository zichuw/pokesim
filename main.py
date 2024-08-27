from cmu_graphics import * # eventually implement some opacity-based transition scene
import random
from datetime import datetime # from https://stackoverflow.com/questions/10607688/how-to-create-a-file-name-with-the-current-date-time-in-python
import pokemonCards # open() function creates a new text file 
import buttons
import combat
from PIL import Image, ImageOps

def onAppStart(app):
    findSave(app)
    reset(app)

def findSave(app): # initializes and reads all potential saves 
    app.selectedSave = None
    app.title1 = 'save1.py'
    app.title2 = 'save2.py'
    app.title3 = 'save3.py'
    with open(app.title1, 'r') as app.save1:
        save1Text = app.save1.read()
        if save1Text == '':
            app.selectedSave = app.title1
            app.save1Info = None
        else:
            saveData = save1Text.split('--')
            app.save1Info = saveData[30]
    with open(app.title2, 'r') as app.save2:
        save2Text = app.save2.read()
        if save2Text == '':
            app.selectedSave = app.title2
            app.save2Info = None
        else:
            saveData = save2Text.split('--')
            app.save2Info = saveData[30]
    with open(app.title3, 'r') as app.save3:
        save3Text = app.save3.read()
        if save3Text == '':
            app.selectedSave = app.title3
            app.save3Info = None
        else:
            saveData = save3Text.split('--')
            app.save3Info = saveData[30]
    app.save1.close()
    app.save2.close()
    app.save3.close()

def saveFile(app):
    currStr = ''
    saveTime = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") # from https://stackoverflow.com/questions/10607688/how-to-create-a-file-name-with-the-current-date-time-in-python
    match app.selectedSave:
        case 'save1.py':
            app.save1Info = saveTime
        case 'save2.py':
            app.save2Info = saveTime
        case 'save3.py':
            app.save3Info = saveTime
    data = [ # saves all changing data
            app.steps, app.steps4, app.enemyTeamSave, app.playerTeamSave, app.playerItemSave, app.battleResult, 
            app.money, app.currentSelectedItem, app.currentSelectedPokemon, app.battlingEnemy, app.battlingPokemon, 
            app.selectedPokemon, app.pokemonSelection, app.playerTeam[app.selectedPokemon[0]].hitpoints, 
            app.playerTeam[app.selectedPokemon[0]].ivA, app.playerTeam[app.selectedPokemon[0]].ivD, 
            app.playerTeam[app.selectedPokemon[1]].hitpoints, app.playerTeam[app.selectedPokemon[1]].ivA, 
            app.playerTeam[app.selectedPokemon[1]].ivD, app.enemyTeamList[0].hitpoints, app.enemyTeamList[0].ivA, 
            app.enemyTeamList[0].ivD, app.enemyTeamList[1].hitpoints, app.enemyTeamList[1].ivA, app.enemyTeamList[1].ivD, 
            app.enemyTeamList[2].hitpoints, app.enemyTeamList[2].ivA, app.enemyTeamList[2].ivD, app.battleMessage, app.selectionMode, saveTime
            ]
    for elem in data:
        currStr += str(elem)
        currStr += '--'
    with open(app.selectedSave, 'w') as currSave:
        currSave.write(currStr)
        currSave.close()

def readSave(app, saveText): # copies save data into game data
    saveData = saveText.split('--')
    app.steps, app.steps4 = int(saveData[0]), int(saveData[1])
    app.enemyTeam = dict()
    for elem in eval(saveData[2]): # eval function came from https://www.geeksforgeeks.org/python-convert-a-string-representation-of-list-into-list/
        app.enemyTeam[elem] = pokemonCards.saveList2[elem]
    app.playerTeam = dict()
    for elem in eval(saveData[3]):
        app.playerTeam[elem] = pokemonCards.saveList[elem]
    app.playerItems = dict()
    itemsData = eval(saveData[4])
    for i in range(0, len(itemsData), 2):
        app.playerItems[itemsData[i]] = itemsData[i+1]
    app.enemyTeamSave, app.playerTeamSave = [], []
    app.enemyTeamList, app.playerTeamList = [], []
    for elem in app.enemyTeam:
        app.enemyTeamSave.append(elem)
    for elem in app.playerTeam:
        app.playerTeamSave.append(elem)
    for elem in app.enemyTeam:
        app.enemyTeamList.append(app.enemyTeam[elem])
    for elem in app.playerTeam:
        app.playerTeamList.append(app.playerTeam[elem])
    app.battleResult = tuple(saveData[5])
    app.money = int(saveData[6])
    app.currentSelectedItem = saveData[7]
    app.currentSelectedPokemon = eval(saveData[8])
    app.battlingEnemy = saveData[9]
    app.battlingPokemon = saveData[10]
    app.selectedPokemon = eval(saveData[11])
    app.pokemonSelection = eval(saveData[12])
    app.playerTeam[app.selectedPokemon[0]].hitpoints = int(saveData[13])
    app.playerTeam[app.selectedPokemon[0]].ivA = int(saveData[14])
    app.playerTeam[app.selectedPokemon[0]].ivD = int(saveData[15])
    app.playerTeam[app.selectedPokemon[1]].hitpoints = int(saveData[16])
    app.playerTeam[app.selectedPokemon[1]].ivA = int(saveData[17])
    app.playerTeam[app.selectedPokemon[1]].ivD = int(saveData[18])
    app.enemyTeamList[0].hitpoints = int(saveData[19])
    app.enemyTeamList[0].ivA = int(saveData[20])
    app.enemyTeamList[0].ivD = int(saveData[21])
    app.enemyTeamList[1].hitpoints = int(saveData[22])
    app.enemyTeamList[1].ivA = int(saveData[23])
    app.enemyTeamList[1].ivD = int(saveData[24])
    app.enemyTeamList[2].hitpoints = int(saveData[25])
    app.enemyTeamList[2].ivA = int(saveData[26])
    app.enemyTeamList[2].ivD = int(saveData[27])
    app.battleMessage = saveData[28]
    app.selectionMode = saveData[29]

def selectPokemon(app): # initializes pokemon teams
    app.enemyTeamList = []
    app.enemyTeam = pokemonCards.possibleBad
    app.playerTeam = pokemonCards.possibleGood
    for pokemon in app.playerTeam:
        app.playerTeam[pokemon].hitpoints = app.playerTeam[pokemon].maxHitpoints
        app.playerTeamSave.append(pokemon)
    for pokemon in app.enemyTeam:
        app.enemyTeam[pokemon].hitpoints = app.enemyTeam[pokemon].maxHitpoints
        app.enemyTeamList.append(app.enemyTeam[pokemon])
        app.enemyTeamSave.append(pokemon)
    app.listSelectionPokemon = []
    for key in app.playerTeam:
        app.listSelectionPokemon.append(key)
    createSelectablePokemon(app)

def createSelectablePokemon(app): # creates coords for pokemon circles
    yChange = 90
    yCurr = 60
    for i in range(6):
        if (i % 2) == 0:
            app.pokemonSelection.append([100, yCurr, 40, False, False, app.listSelectionPokemon[i], app.playerTeam[app.listSelectionPokemon[i]].sprite]) # first false is for selected, second is for display
        else:
            app.pokemonSelection.append([380, yCurr, 40, False, False, app.listSelectionPokemon[i], app.playerTeam[app.listSelectionPokemon[i]].sprite])
        if (i % 2) == 1:
            yCurr += yChange

def initializeShop(app): # creates coords for shop items
    yChange = 80
    xChange = 200
    x = 120
    y = 60
    for item in app.shopItems:
        app.checkShop.append([x, y, 60, 50, item])
        match x:
            case 120:
                x += xChange 
            case 320:
                x = 120
                y += yChange

def redrawAll(app): # handles every game mode drawing screen
    match app.selectionMode:
        case 'transition':
            pass
        case 'victory':
            victory(app)
        case 'defeat':
            defeat(app)
        case 'surrender':
            defeat(app)
        case 'start':
            drawStartScreen(app)
        case 'saves':
            drawSaves(app)
        case 'choosePokemon':
            drawChoosePokemon(app)
        case 'pokemonStat':
            drawPokemonCard(app)
        case 'shop':
            drawShop(app)
        case 'shopStat':
            drawItem(app)
        case 'chooseOrder':
            drawRotate(app)
        case 'combat':
            drawCombat(app)
        case 'moves':
            drawMoves(app)
        case 'enemyAttack':
            drawMoves(app)
        case 'items':
            drawBag(app)
        case 'feed':
            drawRotate(app)
        case 'rotate':
            drawRotate(app)
        case 'faint':
            drawRotate(app)
    if app.uiMessage != None: # always draws ui message if available
        if (100-app.steps) >= 0:
            drawLabel(app.uiMessage, 240, 160, size=38, fill='red', opacity=100-app.steps, font='pokemon fire red')


def drawStartScreen(app):
    drawImage('assets/pokemonBackGround.png', 240, 160, align='center')
    # png from https://wall.alphacoders.com/big.php?i=922816
    drawLabel('Ultimate Pokemon Showdown', 240, 50, size=48, fill='white', font='pokemon fire red')
    buttons.startContinue.drawButton(app)
    buttons.startSave.drawButton(app)

def drawSaves(app): # load save menu
    drawImage('assets/saveBackground.png', 240, 160, align='center') 
    # png from https://wall.alphacoders.com/big.php?i=641430
    drawLabel('Load A Save!', 240, 40, size=30, font='pokemon fire red', fill='white')
    buttons.save1.drawButton(app)
    buttons.save2.drawButton(app)
    buttons.save3.drawButton(app)
    buttons.delete1.drawButton(app)
    buttons.delete2.drawButton(app)
    buttons.delete3.drawButton(app)
    buttons.saveBack.drawButton(app)
    drawLabel(app.save1Info, 80, 140, size=18, font='pokemon fire red', fill='white')
    drawLabel(app.save2Info, 240, 140, size=18, font='pokemon fire red', fill='white')
    drawLabel(app.save3Info, 400, 140, size=18, font='pokemon fire red', fill='white')

def drawChoosePokemon(app): # bolds chosen pokemon
    drawImage('assets/choosePokemonBackground.png', 240, 160, align='center') 
    # png from https://www.pinterest.com/pin/151574343683447160/
    yChange = 90
    yCurr = 60
    for i in range(6):
        if not app.pokemonSelection[i][3]:
            drawCircle(100 if (i % 2 == 0) else 380, yCurr, 40, border='black', borderWidth=2, fill=None)
        else:
            drawCircle(100 if (i % 2 == 0) else 380, yCurr, 40, border='green', borderWidth=5, fill=None)
        drawImage(app.pokemonSelection[i][6], 100 if (i % 2 == 0) else 380, yCurr, align='center')
        if (i % 2) == 1: 
            yCurr += yChange
    drawLabel('Select 2 Pokemon!', 240, 40, size=32, font='pokemon fire red')
    buttons.choosePokemonContinue.drawButton(app)
        
def drawPokemonCard(app):
    drawImage('assets/choosePokemonBackground.png', 240, 160, align='center')
    # png from https://www.pinterest.com/pin/151574343683447160/
    y = 180
    yChange = 20
    typeFill = None
    for pokemon in app.pokemonSelection:
        if pokemon[4]:
            displayedPokemon = app.playerTeam[pokemon[5]]
            displayedSprite = pokemon[6]
            break
    match displayedPokemon.type[0]:
        case 'Steel':
            typeFill = 'silver'
        case 'Normal':
            typeFill = 'white'
        case 'Fire':
            typeFill = 'red'
        case 'Water':
            typeFill = 'blue'
        case 'Grass':
            typeFill = 'green'
        case 'Flying':
            typeFill = 'lavender'
        case 'Fighting':
            typeFill = 'brown'
        case 'Poison':
            typeFill = 'purple'
        case 'Electric':
            typeFill = 'yellow'
        case 'Ground':
            typeFill = 'wheat'
        case 'Rock':
            typeFill = 'sienna'
        case 'Psychic':
            typeFill = 'deepPink'
        case 'Ice':
            typeFill = 'lightCyan'
        case 'Bug':
            typeFill = 'olive'
        case 'Ghost':
            typeFill = 'indigo'
        case 'Dragon':
            typeFill = 'mediumPurple'  
        case 'Dark':
            typeFill = 'black'
        case 'Fairy':
            typeFill = 'lightPink'
    drawRect(80, 20, 320, 240, border='black', borderWidth=2, fill=typeFill, opacity=40)
    drawLabel(displayedPokemon, 240, 30, size=20, font='pokemon fire red')
    drawLabel(f'Type:{displayedPokemon.type}', 180, 50, size=20, font='pokemon fire red')
    drawLabel(f'Max HP: {displayedPokemon.maxHitpoints}', 300, 50, size=20, font='pokemon fire red')
    drawImage(displayedSprite, 240, 115, align='center', width=100, height=100)
    for i in range(len(displayedPokemon.moveset)):
        if displayedPokemon.moveset[i][2] == 0:
            match displayedPokemon.moveset[i][4]:
                case 'def':
                    drawLabel(f'{displayedPokemon.moveset[i][0]} - {displayedPokemon.moveset[i][1]}, Def+, {displayedPokemon.moveset[i][3]} Accuracy', 
                    240, y, size=20, font='pokemon fire red')
                case 'def2':
                    drawLabel(f'{displayedPokemon.moveset[i][0]} - {displayedPokemon.moveset[i][1]}, Def++, {displayedPokemon.moveset[i][3]} Accuracy', 
                    240, y, size=20, font='pokemon fire red')
                case 'atk':
                    drawLabel(f'{displayedPokemon.moveset[i][0]} - {displayedPokemon.moveset[i][1]}, Atk+, {displayedPokemon.moveset[i][3]} Accuracy', 
                    240, y, size=20, font='pokemon fire red')
                case 'atk2':
                    drawLabel(f'{displayedPokemon.moveset[i][0]} - {displayedPokemon.moveset[i][1]}, Atk++, {displayedPokemon.moveset[i][3]} Accuracy', 
                    240, y, size=20, font='pokemon fire red')
        else:
            drawLabel(f'{displayedPokemon.moveset[i][0]} - {displayedPokemon.moveset[i][1]}, {displayedPokemon.moveset[i][2]} Dmg, {displayedPokemon.moveset[i][3]} Accuracy', 
                  240, y, size=20, font='pokemon fire red')
        y += yChange
    buttons.cardBack.drawButton(app)
    buttons.cardSelect.drawButton(app)

def drawShop(app):
    drawImage('assets/shopBackground.png', 240, 160, align='center')
    # png from https://imgur.com/kpdUnNy
    yChange = 80
    xChange = 200
    x = 110
    y = 60
    drawLabel(f'Welcome To The Pokemart! You have ${app.money}!', 240, 20, font='pokemon fire red', size=26)
    drawLabel(f'Your Bag: {app.playerItems}', 240, 40, font='pokemon fire red', size=22)
    for item in app.shopItems:
        drawRect(x, y, 50, 50, fill='white', border='black', borderWidth=2)
        drawLabel(f'{item}:${app.shopItems[item][0]}', x + 30, y + 60, font='pokemon fire red', size = 20)
        drawImage(app.shopItems[item][1], x, y)
        match x:
            case 110:
                x += xChange
            case 310:
                x = 110
                y += yChange
    buttons.shopContinue.drawButton(app)

def drawItem(app):
    drawImage('assets/shopBackground.png', 240, 160, align='center')
    # png from https://imgur.com/kpdUnNy
    drawLabel(f'{app.currentSelectedItem}: ${app.shopItems[app.currentSelectedItem][0]}', 240, 40, font='pokemon fire red', size=34)
    drawImage(app.shopItems[app.currentSelectedItem][1], 240, 160, width=100, height=100, align='center')
    drawLabel(app.shopDesc[app.currentSelectedItem], 240, 235, font='pokemon fire red', size=24)
    buttons.itemBack.drawButton(app)
    buttons.itemSell.drawButton(app)
    buttons.itemBuy.drawButton(app)

def drawRotate(app):
    drawImage('assets/shopBackground.png', 240, 160, align='center')
    # png from https://imgur.com/kpdUnNy
    yChange = 100
    y = 80
    for pokemon in app.selectedPokemon:
        drawRect(90, y, 300, 60, fill='white', border='black', borderWidth=2)
        stats = app.playerTeam[pokemon] # gives the statblock for this pokemon
        drawHealthBar(app, 225, y + 20, stats.maxHitpoints, stats.hitpoints, None)
        drawImage(stats.sprite, 100, y + 5, width=50, height=50)
        drawLabel(pokemon, 190, y + 30, font='pokemon fire red', size=24)
        y += yChange
    if app.battlingPokemon == None:
        drawLabel('Choose Which Pokemon To Go First!', 240, 25, font='pokemon fire red', size=24)
    elif app.selectionMode == 'rotate' or app.selectionMode == 'faint':
        drawLabel('Choose A Pokemon To Switch In!', 240, 25, font='pokemon fire red', size=24)
    elif app.selectionMode == 'feed':
        drawLabel('Choose A Pokemon!', 240, 25, font='pokemon fire red', size=24)
    if app.selectionMode == 'chooseOrder':
        buttons.orderBack.drawButton(app)
    elif app.selectionMode == 'rotate' or app.selectionMode == 'feed':
        buttons.rotateBack.drawButton(app)

def drawBag(app):
    drawImage('assets/bagBackground.png', 240, 160, align='center')
    # png is a stillframe from https://www.youtube.com/watch?v=Q7A9eftuLTw
    y = 100
    changeY = 40
    drawLabel('Your Bag', 240, 40, font='pokemon fire red', size=40)
    for item in app.playerItems:
        drawLabel(f'{item} X {app.playerItems[item]}', 200, y, font='pokemon fire red', size=30)
        drawLabel('Use', 290, y, font='pokemon fire red', size=20)
        drawRect(270, y - 10, 40, 20, fill=None, borderWidth=2, border='black')
        y += changeY
    buttons.bagBack.drawButton(app)

def drawCombat(app):
    drawImage('assets/combatBackground.png', 240, 160, align='center') 
    # background from https://www.artstation.com/artwork/0PKZ8
    if app.steps3 == 0:
        drawImage(app.playerTeam[app.battlingPokemon].combatSprite, 10, 85, width=140, height=140)
    else:
        drawImage(app.playerTeam[app.battlingPokemon].combatSprite, 10, 90, width=140, height=140)
    drawImage(app.enemyTeam[app.battlingEnemy].sprite, 340, 5, width=130, height=130)
    drawRect(0, 210, 480, 110, fill='white', border='black', borderWidth=2)
    drawLabel(f'What will {app.battlingPokemon} do?', 70, 265, font='pokemon fire red', size=20)
    drawLabel(app.battlingEnemy, 285, 45, font='pokemon fire red', size=26,  bold=True)
    drawLabel(app.battlingPokemon, 200, 177.5, font='pokemon fire red', size=26, bold=True)
    drawHealthBar(app, 95, 40, app.enemyTeam[app.battlingEnemy].maxHitpoints, app.enemyTeam[app.battlingEnemy].hitpoints, True)
    drawHealthBar(app, 240, 170, app.playerTeam[app.battlingPokemon].maxHitpoints, app.playerTeam[app.battlingPokemon].hitpoints, False)
    if app.battleMessage != None:
        drawLabel(app.battleMessage, 310, 195, font='pokemon fire red', size=16)
    buttons.combatFight.drawButton(app)
    buttons.combatBag.drawButton(app)
    buttons.combatPokemon.drawButton(app)
    buttons.combatSurrender.drawButton(app)
    drawLabel(f'Enemies Left:{app.remainingEnemies}', 300, 160, font='pokemon fire red', size=20)

def drawMoves(app):
    drawImage('assets/combatBackground.png', 240, 160, align='center')
    # background from https://www.artstation.com/artwork/0PKZ8
    x = 140
    y = 210
    xChange = 170
    yChange = 55
    pokemon = app.playerTeam[app.battlingPokemon]
    if app.steps3 == 0:
        drawImage(app.playerTeam[app.battlingPokemon].combatSprite, 10, 85, width=140, height=140)
    else:
        drawImage(app.playerTeam[app.battlingPokemon].combatSprite, 10, 90, width=140, height=140)
    drawImage(app.enemyTeam[app.battlingEnemy].sprite, 340, 5, width=130, height=130)
    drawRect(0, 210, 480, 110, fill='white', border='black', borderWidth=2)
    for i in range(len(pokemon.moveset)):
        drawLabel(pokemon.moveset[i][0], x + (xChange/2), y + (yChange/2), font='pokemon fire red', size=24)
        if i % 2 == 0:
            x += xChange
        elif i % 2 == 1:
            y += yChange
            x = 140
    buttons.move1.drawButton(app)
    buttons.move2.drawButton(app)
    buttons.move3.drawButton(app)
    buttons.move4.drawButton(app)
    drawLabel(f'Pick a move!', 70, 265, font='pokemon fire red', size=20)
    drawLabel(app.battlingEnemy, 285, 45, font='pokemon fire red', size=26,  bold=True)
    drawLabel(app.battlingPokemon, 200, 177.5, font='pokemon fire red', size=26, bold=True)
    if app.battlingEnemy != None:
        drawHealthBar(app, 95, 40, app.enemyTeam[app.battlingEnemy].maxHitpoints, app.enemyTeam[app.battlingEnemy].hitpoints, True)
        drawHealthBar(app, 240, 170, app.playerTeam[app.battlingPokemon].maxHitpoints, app.playerTeam[app.battlingPokemon].hitpoints, False)
    if app.battleMessage != None:
        drawLabel(app.battleMessage, 310, 195, font='pokemon fire red', size=16)
    drawLabel(f'Enemies Left:{app.remainingEnemies}', 300, 160, font='pokemon fire red', size=20)

def victory(app):
    drawImage('assets/victory.png', 240, 160, align='center') 
    # png from https://motionbgs.com/rayquaza-flying-in-the-dark-sky
    drawLabel('YOU WIN!', app.width/2, app.height/3, fill='green', size=50, font='pokemon fire red')
    buttons.playAgain.drawButton(app)

def defeat(app):
    drawImage('assets/defeat.png', 240, 160, align='center')
    # png from https://www.reddit.com/r/pokemon/comments/11adu2r/digital_painting_i_did_of_an_abandoned_pok%C3%A9_ball/
    drawLabel('YOU LOSE!', app.width/2 + 65, app.height/3 + 10, fill='red', size=50, font='pokemon fire red')
    buttons.playAgain.drawButton(app)

def onMousePress(app, mouseX, mouseY):
    modeCheck(app, mouseX, mouseY)

def modeCheck(app, mouseX, mouseY): # checks all the modes/gamestates we could be in, tests boundaries/adjusts values accordingly
    match app.selectionMode:
        case 'start':
            if buttons.startContinue.intersection(app, mouseX, mouseY):
                findSave(app)
                app.selectionMode = 'choosePokemon'
            elif buttons.startSave.intersection(app, mouseX, mouseY):
                app.selectionMode = 'saves'
        case 'saves':
            if buttons.saveBack.intersection(app, mouseX, mouseY):
                app.selectionMode = 'start'
            if buttons.save1.intersection(app, mouseX, mouseY):
                with open(app.title1, 'r') as app.save1:
                    save1Text = app.save1.read()
                if save1Text != '':
                    readSave(app, save1Text)
                    app.selectedSave = 'save1.py'
                else:
                    app.uiMessage = 'This save is empty!'
                    app.steps = 0
            elif buttons.save2.intersection(app, mouseX, mouseY):
                with open(app.title2, 'r') as app.save2:
                    save2Text = app.save2.read()
                if save2Text != '':
                    readSave(app, save2Text)
                    app.selectedSave = 'save2.py'
                else:
                    app.uiMessage = 'This save is empty!'
                    app.steps = 0
            elif buttons.save3.intersection(app, mouseX, mouseY):
                with open(app.title3, 'r') as app.save3:
                    save3Text = app.save3.read()
                if save3Text != '':
                    readSave(app, save3Text)
                    app.selectedSave = 'save3.py'
                else:
                    app.uiMessage = 'This save is empty!'
                    app.steps = 0
            elif buttons.delete1.intersection(app, mouseX, mouseY):
                with open(app.title1, 'w') as app.save1:
                    app.save1.write('')
                    app.save1.close()
                    app.save1Info = None
                    app.uiMessage = 'You cleared Save 1!'
                    app.steps = 0
            elif buttons.delete2.intersection(app, mouseX, mouseY):
                with open(app.title2, 'w') as app.save2:
                    app.save2.write('')
                    app.save2.close()
                    app.save2Info = None
                    app.uiMessage = 'You cleared Save 2!'
                    app.steps = 0
            elif buttons.delete3.intersection(app, mouseX, mouseY):
                with open(app.title3, 'w') as app.save3:
                    app.save3.write('')
                    app.save3.close()
                    app.save3Info = None
                    app.uiMessage = 'You cleared Save 3!'
                    app.steps = 0
        case 'choosePokemon':
            if buttons.choosePokemonContinue.intersection(app, mouseX, mouseY):
                if len(app.selectedPokemon) < 2:
                    app.uiMessage = 'Select 2 Pokemon!'
                    app.steps = 0
                else:
                    app.selectionMode = 'shop' 
            else:
                for pokemon in app.pokemonSelection:
                    if distance(app, pokemon[0], pokemon[1], mouseX, mouseY) <= pokemon[2]:
                        app.selectionMode = 'pokemonStat'
                        app.currentSelectedPokemon = pokemon
                        pokemon[4] = True # sets display to true
                        break
        case 'pokemonStat':
            if buttons.cardBack.intersection(app, mouseX, mouseY):
                app.currentSelectedPokemon[4] = False
                app.selectionMode = 'choosePokemon'
            elif buttons.cardSelect.intersection(app, mouseX, mouseY):
                if app.currentSelectedPokemon[3]:
                    app.currentSelectedPokemon[3] = False
                    app.selectedPokemon.remove(app.currentSelectedPokemon[5])
                    app.currentSelectedPokemon[4] = False
                    app.selectionMode = 'choosePokemon'
                elif len(app.selectedPokemon) < 2:
                    if not app.currentSelectedPokemon[3]:
                        app.currentSelectedPokemon[3] = True
                        app.selectedPokemon.append(app.currentSelectedPokemon[5])
                        app.currentSelectedPokemon[4] = False
                        app.selectionMode = 'choosePokemon'
                else:
                    app.uiMessage = 'You have selected two pokemon already!'
                    app.steps = 0
        case 'shop':
            if app.selectedSave != None:
                saveFile(app)
            if buttons.shopContinue.intersection(app, mouseX, mouseY):
                app.selectionMode = 'chooseOrder'
            for item in app.checkShop:
                if ((mouseX >= item[0] and mouseX <= (item[0] + item[2])) and 
                    (mouseY >= item[1] and mouseY <= (item[1] + item[3]))):
                    app.selectionMode = 'shopStat'
                    app.currentSelectedItem = item[4]
                    break
        case 'shopStat':
            if buttons.itemBack.intersection(app, mouseX, mouseY):
                app.selectionMode = 'shop'
            elif buttons.itemBuy.intersection(app, mouseX, mouseY):
                price = app.shopItems[app.currentSelectedItem][0]
                if app.money >= price:
                    app.money -= price
                    if app.currentSelectedItem not in app.playerItems:
                        app.playerItems[app.currentSelectedItem] = 1
                    else:
                        app.playerItems[app.currentSelectedItem] += 1
                    app.playerItemSave = []
                    for item in app.playerItems:
                        app.playerItemSave.append(item)
                        app.playerItemSave.append(app.playerItems[item])
                    app.uiMessage = f'You bought 1 {app.currentSelectedItem}!'
                    app.steps = 0
                    app.selectionMode = 'shop'
                else:
                    app.uiMessage = "You don't have enough money!"
                    app.steps = 0
            elif buttons.itemSell.intersection(app, mouseX, mouseY):
                price = app.shopItems[app.currentSelectedItem][0]
                if (app.currentSelectedItem in app.playerItems) and app.playerItems[app.currentSelectedItem] >= 1:
                    app.money += price
                    if app.playerItems[app.currentSelectedItem] == 1:
                        del app.playerItems[app.currentSelectedItem]
                    else:
                        app.playerItems[app.currentSelectedItem] -= 1
                    app.playerItemSave = []
                    for item in app.playerItems:
                        app.playerItemSave.append(item)
                        app.playerItemSave.append(app.playerItems[item])
                    app.uiMessage = f'You sold 1 {app.currentSelectedItem}!'
                    app.steps = 0
                    app.selectionMode = 'shop'
                else:
                    app.uiMessage = "You don't have this item!"
                    app.steps = 0
        case 'chooseOrder':
            if buttons.orderBack.intersection(app, mouseX, mouseY):
                app.selectionMode = 'shop'
            elif (mouseX >= 90 and mouseX <= 390) and (mouseY >= 80 and mouseY <= 140):
                app.battlingPokemon = app.selectedPokemon[0]
                findNextEnemy(app)
                app.selectionMode = 'combat'
            elif (mouseX >= 90 and mouseX <= 390) and (mouseY >= 180 and mouseY <= 240):
                app.battlingPokemon = app.selectedPokemon[1]
                findNextEnemy(app)
                app.selectionMode = 'combat'
        case 'combat':
            findNextEnemy(app)
            if buttons.combatFight.intersection(app, mouseX, mouseY):
                app.selectionMode = 'moves'
            if buttons.combatBag.intersection(app, mouseX, mouseY):
                app.selectionMode = 'items'
            if buttons.combatPokemon.intersection(app, mouseX, mouseY):
                app.selectionMode = 'rotate'
            if buttons.combatSurrender.intersection(app, mouseX, mouseY):
                app.selectionMode = 'surrender'
        case 'rotate':
            if (mouseX >= 90 and mouseX <= 390) and (mouseY >= 80 and mouseY <= 140):
                if app.playerTeam[app.selectedPokemon[0]].hitpoints <= 0:
                    app.uiMessage = "That Pokemon has fainted."
                    app.steps = 0
                elif app.battlingPokemon == app.selectedPokemon[0]:
                    app.uiMessage = "That Pokemon is already selected!"
                    app.steps = 0
                else:
                    app.battlingPokemon = app.selectedPokemon[0]
                    findNextEnemy(app)
                    if app.selectedSave != None:
                        saveFile(app)
                    app.selectionMode = 'combat'
            elif (mouseX >= 90 and mouseX <= 390) and (mouseY >= 180 and mouseY <= 240):
                if app.playerTeam[app.selectedPokemon[1]].hitpoints <= 0:
                    app.uiMessage = "That Pokemon has fainted."
                    app.steps = 0
                elif app.battlingPokemon == app.selectedPokemon[1]:
                    app.uiMessage = "That Pokemon is already selected!"
                    app.steps = 0
                else:
                    app.battlingPokemon = app.selectedPokemon[1]
                    findNextEnemy(app)
                    app.selectionMode = 'combat'
            elif buttons.rotateBack.intersection(app, mouseX, mouseY):
                app.selectionMode = 'combat'
        case 'faint':
            if (mouseX >= 90 and mouseX <= 390) and (mouseY >= 80 and mouseY <= 140):
                if app.playerTeam[app.selectedPokemon[0]].hitpoints <= 0:
                    app.uiMessage = "That Pokemon has fainted."
                    app.steps = 0
                elif app.battlingPokemon == app.selectedPokemon[0]:
                    app.uiMessage = "That Pokemon is already selected!"
                    app.steps = 0
                else:
                    app.battlingPokemon = app.selectedPokemon[0]
                    findNextEnemy(app)
                    app.selectionMode = 'combat'
            elif (mouseX >= 90 and mouseX <= 390) and (mouseY >= 180 and mouseY <= 240):
                if app.playerTeam[app.selectedPokemon[1]].hitpoints <= 0:
                    app.uiMessage = "That Pokemon has fainted."
                    app.steps = 0
                elif app.battlingPokemon == app.selectedPokemon[1]:
                    app.uiMessage = "That Pokemon is already selected!"
                    app.steps = 0
                else:
                    app.battlingPokemon = app.selectedPokemon[1]
                    findNextEnemy(app)
                    app.selectionMode = 'combat'
        case 'moves':
            pokemon = app.playerTeam[app.battlingPokemon]
            enemPoke = app.enemyTeam[app.battlingEnemy]
            if buttons.move1.intersection(app, mouseX, mouseY):
                app.battleResult = combat.makeMove(pokemon.moveset[0], enemPoke, pokemon, app.superEffective, True)
                supertext = app.battleResult[5]
                if app.battleResult[1]:
                    app.battleMessage = f'{app.battlingPokemon} missed {app.battleResult[2]}.'
                else:
                    match app.battleResult[4]:
                        case None:
                            if supertext == None:
                                app.battleMessage = f'{app.battlingPokemon} used {app.battleResult[2]}, for {app.battleResult[3]} damage.'
                            else:
                                app.battleMessage = f"{app.battlingPokemon} used {app.battleResult[2]}. It's supereffective for {app.battleResult[3]} damage."
                        case 'def1':
                            app.battleMessage = f'{app.battlingPokemon} used {app.battleResult[2]}, raising its defence.'
                        case 'def2':
                            app.battleMessage = f'{app.battlingPokemon} used {app.battleResult[2]}, sharply raising its defence.'
                        case 'atk1':
                            app.battleMessage = f'{app.battlingPokemon} used {app.battleResult[2]}, raising its attack.'
                        case 'atk2':
                            app.battleMessage = f'{app.battlingPokemon} used {app.battleResult[2]}, sharply raising its attack.'
                if enemPoke.hitpoints <= 0:
                    app.battleMessage = f'{app.battlingEnemy} has fainted.'
                findNextEnemy(app)
                app.steps4 = 0
                if app.selectionMode != 'victory':
                    app.selectionMode = 'enemyAttack'
            elif buttons.move2.intersection(app, mouseX, mouseY):
                app.battleResult = combat.makeMove(pokemon.moveset[1], enemPoke, pokemon, app.superEffective, True)
                supertext = app.battleResult[5]
                if app.battleResult[1]:
                    app.battleMessage = f'{app.battlingPokemon} missed {app.battleResult[2]}.'
                else:
                    match app.battleResult[4]:
                        case None:
                            if supertext == None:
                                app.battleMessage = f'{app.battlingPokemon} used {app.battleResult[2]}, dealing {app.battleResult[3]} damage.'
                            else:
                                app.battleMessage = f"{app.battlingPokemon} used {app.battleResult[2]}. It's supereffective for {app.battleResult[3]} damage."                        
                        case 'def1':
                            app.battleMessage = f'{app.battlingPokemon} used {app.battleResult[2]}, raising its defence.'
                        case 'def2':
                            app.battleMessage = f'{app.battlingPokemon} used {app.battleResult[2]}, sharply raising its defence.'
                        case 'atk1':
                            app.battleMessage = f'{app.battlingPokemon} used {app.battleResult[2]}, raising its attack.'
                        case 'atk2':
                            app.battleMessage = f'{app.battlingPokemon} used {app.battleResult[2]}, sharply raising its attack.'
                if enemPoke.hitpoints <= 0:
                    app.battleMessage = f'{app.battlingEnemy} has fainted.'
                findNextEnemy(app)
                app.steps4 = 0
                if app.selectionMode != 'victory':
                    app.selectionMode = 'enemyAttack'
            elif buttons.move3.intersection(app, mouseX, mouseY):
                app.battleResult = combat.makeMove(pokemon.moveset[2], enemPoke, pokemon, app.superEffective, True)
                supertext = app.battleResult[5]
                if app.battleResult[1]:
                    app.battleMessage = f'{app.battlingPokemon} missed {app.battleResult[2]}.'
                else:
                    match app.battleResult[4]:
                        case None:
                            if supertext == None:
                                app.battleMessage = f'{app.battlingPokemon} used {app.battleResult[2]}, dealing {app.battleResult[3]} damage.'
                            else:
                                app.battleMessage = f"{app.battlingPokemon} used {app.battleResult[2]}. It's supereffective, dealing {app.battleResult[3]} damage."                        
                        case 'def1':
                            app.battleMessage = f'{app.battlingPokemon} used {app.battleResult[2]}, raising its defence.'
                        case 'def2':
                            app.battleMessage = f'{app.battlingPokemon} used {app.battleResult[2]}, sharply raising its defence.'
                        case 'atk1':
                            app.battleMessage = f'{app.battlingPokemon} used {app.battleResult[2]}, raising its attack.'
                        case 'atk2':
                            app.battleMessage = f'{app.battlingPokemon} used {app.battleResult[2]}, sharply raising its attack.'
                if enemPoke.hitpoints <= 0:
                    app.battleMessage = f'{app.battlingEnemy} has fainted.'
                findNextEnemy(app)
                app.steps4 = 0
                if app.selectionMode != 'victory':
                    app.selectionMode = 'enemyAttack'
            elif buttons.move4.intersection(app, mouseX, mouseY):
                app.battleResult = combat.makeMove(pokemon.moveset[3], enemPoke, pokemon, app.superEffective, True)
                supertext = app.battleResult[5]
                if app.battleResult[1]:
                    app.battleMessage = f'{app.battlingPokemon} missed {app.battleResult[2]}.'
                else:
                    match app.battleResult[4]:
                        case None:
                            if supertext == None:
                                app.battleMessage = f'{app.battlingPokemon} used {app.battleResult[2]}, dealing {app.battleResult[3]} damage.'
                            else:
                                app.battleMessage = f"{app.battlingPokemon} used {app.battleResult[2]}. It's supereffective, dealing {app.battleResult[3]} damage."                        
                        case 'def1':
                            app.battleMessage = f'{app.battlingPokemon} used {app.battleResult[2]}, raising its defence.'
                        case 'def2':
                            app.battleMessage = f'{app.battlingPokemon} used {app.battleResult[2]}, sharply raising its defence.'
                        case 'atk1':
                            app.battleMessage = f'{app.battlingPokemon} used {app.battleResult[2]}, raising its attack.'
                        case 'atk2':
                            app.battleMessage = f'{app.battlingPokemon} used {app.battleResult[2]}, sharply raising its attack.'
                if enemPoke.hitpoints <= 0:
                    app.battleMessage = f'{app.battlingEnemy} has fainted.'
                findNextEnemy(app)
                app.steps4 = 0
                if app.selectionMode != 'victory':
                    app.selectionMode = 'enemyAttack'
        case 'items':
            if buttons.bagBack.intersection(app, mouseX, mouseY):
                app.selectionMode = 'combat'
            else:
                y = 90
                for item in app.playerItems:
                    if ((mouseX >= 270 and mouseX <= 360) and (mouseY >= y and mouseY <= y + 20)):
                        app.currentSelectedItem = item
                        app.selectionMode = 'feed'
                        break
                    y += 40
        case 'feed':
            if buttons.rotateBack.intersection(app, mouseX, mouseY):
                app.selectionMode = 'items'
            elif (((mouseX >= 90 and mouseX <= 390) and (mouseY >= 80 and mouseY <= 140)) or 
                ((mouseX >= 90 and mouseX <= 390) and (mouseY >= 180 and mouseY <= 240))):
                if (mouseX >= 90 and mouseX <= 390) and (mouseY >= 80 and mouseY <= 140):
                    pokemon = app.playerTeam[app.selectedPokemon[0]]
                else:
                    pokemon = app.playerTeam[app.selectedPokemon[1]]
                match app.currentSelectedItem:
                    case 'Revive':
                        if pokemon.hitpoints <= 0:
                            app.uiMessage = f'You Revived {pokemon}!'
                            app.steps = 0
                            pokemon.hitpoints = rounded(0.5 * pokemon.maxHitpoints)
                            app.playerItems[app.currentSelectedItem] -= 1
                            if app.playerItems[app.currentSelectedItem] == 0:
                                del app.playerItems[app.currentSelectedItem]
                        else:
                            app.uiMessage = f'{pokemon} has not fainted!'
                            app.steps = 0
                    case 'Max Revive':
                        if pokemon.hitpoints <= 0:
                            app.uiMessage = f'You Revived {pokemon}!'
                            app.steps = 0
                            pokemon.hitpoints = pokemon.maxHitpoints
                            app.playerItems[app.currentSelectedItem] -= 1
                            if app.playerItems[app.currentSelectedItem] == 0:
                                del app.playerItems[app.currentSelectedItem]
                        else:
                            app.uiMessage = f'{pokemon} has not fainted!'
                            app.steps = 0
                    case 'Max Potion':
                        if pokemon.hitpoints <= 0:
                            app.uiMessage = f'{pokemon} has fainted.'
                            app.steps = 0
                        elif pokemon.hitpoints == pokemon.maxHitpoints:
                            app.uiMessage = f'{pokemon} has max HP.'
                            app.steps = 0                        
                        else:
                            pokemon.hitpoints = pokemon.maxHitpoints
                            app.uiMessage = f'You healed {pokemon} fully!'
                            app.steps = 0
                            app.playerItems[app.currentSelectedItem] -= 1
                            if app.playerItems[app.currentSelectedItem] == 0:
                                del app.playerItems[app.currentSelectedItem]
                    case 'Potion':
                        if pokemon.hitpoints <= 0:
                            app.uiMessage = f'{pokemon} has fainted.'
                            app.steps = 0
                        elif pokemon.hitpoints == pokemon.maxHitpoints:
                            app.uiMessage = f'{pokemon} has max HP.'
                            app.steps = 0  
                        else:
                            if pokemon.hitpoints + app.potionHeal[app.currentSelectedItem] < pokemon.maxHitpoints:
                                pokemon.hitpoints += app.potionHeal[app.currentSelectedItem]
                                app.uiMessage = f'You healed {pokemon} by {app.potionHeal[app.currentSelectedItem]}.'
                                app.steps = 0
                                app.playerItems[app.currentSelectedItem] -= 1
                            else:
                                pokemon.hitpoints = pokemon.maxHitpoints
                                app.uiMessage = f'You healed {pokemon} to max.'
                            if app.playerItems[app.currentSelectedItem] == 0:
                                del app.playerItems[app.currentSelectedItem]
                    case 'Super Potion':
                        if pokemon.hitpoints <= 0:
                            app.uiMessage = f'{pokemon} has fainted.'
                            app.steps = 0
                        elif pokemon.hitpoints == pokemon.maxHitpoints:
                            app.uiMessage = f'{pokemon} has max HP.'
                            app.steps = 0  
                        else:
                            if pokemon.hitpoints + app.potionHeal[app.currentSelectedItem] < pokemon.maxHitpoints:
                                pokemon.hitpoints += app.potionHeal[app.currentSelectedItem]
                                app.uiMessage = f'You healed {pokemon} by {app.potionHeal[app.currentSelectedItem]}.'
                                app.steps = 0
                                app.playerItems[app.currentSelectedItem] -= 1
                            else:
                                pokemon.hitpoints = pokemon.maxHitpoints
                                app.uiMessage = f'You healed {pokemon} to max.'
                            if app.playerItems[app.currentSelectedItem] == 0:
                                del app.playerItems[app.currentSelectedItem]
                    case 'Hyper Potion':
                        if pokemon.hitpoints <= 0:
                            app.uiMessage = f'{pokemon} has fainted.'
                            app.steps = 0
                        elif pokemon.hitpoints == pokemon.maxHitpoints:
                            app.uiMessage = f'{pokemon} has max HP.'
                            app.steps = 0  
                        else:
                            if pokemon.hitpoints + app.potionHeal[app.currentSelectedItem] < pokemon.maxHitpoints:
                                pokemon.hitpoints += app.potionHeal[app.currentSelectedItem]
                                app.uiMessage = f'You healed {pokemon} by {app.potionHeal[app.currentSelectedItem]}.'
                                app.steps = 0
                                app.playerItems[app.currentSelectedItem] -= 1
                            else:
                                pokemon.hitpoints = pokemon.maxHitpoints
                                app.uiMessage = f'You healed {pokemon} to max.'
                                app.steps = 0
                                app.playerItems[app.currentSelectedItem] -= 1
                            if app.playerItems[app.currentSelectedItem] == 0:
                                del app.playerItems[app.currentSelectedItem]
        case 'surrender':
            if buttons.playAgain.intersection(app, mouseX, mouseY):
                reset(app)
        case 'defeat':
            if buttons.playAgain.intersection(app, mouseX, mouseY):
                reset(app)
        case 'victory':
            if buttons.playAgain.intersection(app, mouseX, mouseY):
                match app.selectedSave:
                    case 'save1.py':
                        with open(app.title1, 'w') as app.save1:
                            app.save1.write('')
                            app.save1.close()
                            app.save1Info = None
                    case 'save2.py':
                        with open(app.title2, 'w') as app.save2:
                            app.save2.write('')
                            app.save2.close()
                            app.save2Info = None
                    case 'save3.py':
                        with open(app.title3, 'w') as app.save3:
                            app.save3.write('')
                            app.save3.close()
                            app.save3Info = None
                reset(app)

def onStep(app):
    app.steps += 1
    app.steps4 += 1
    if app.steps % 40 == 0:
        app.steps3 += 1
    if app.steps3 % 2 == 0:
        app.steps3 = 0
    if app.selectionMode == 'enemyAttack':
        if app.steps4 >= 120:
            app.battleResult = combat.enemyAI(pokemonCards, app.superEffective, 
                                app.enemyTeam[app.battlingEnemy], app.playerTeam[app.battlingPokemon])
            supertext = app.battleResult[5]
            if app.battleResult[1]:
                app.battleMessage = f'{app.battlingEnemy} missed {app.battleResult[2]}.'
            else:
                    match app.battleResult[4]:
                        case None:
                            if supertext == None:
                                app.battleMessage = f'{app.battlingEnemy} used {app.battleResult[2]}, dealing {app.battleResult[3]} damage.'
                            else:
                                app.battleMessage = f"{app.battlingEnemy} used {app.battleResult[2]}. It's supereffective, dealing {app.battleResult[3]} damage."
                        case 'def1':
                            app.battleMessage = f'{app.battlingEnemy} used {app.battleResult[2]}, raising its defence.'
                        case 'def2':
                            app.battleMessage = f'{app.battlingEnemy} used {app.battleResult[2]}, sharply raising its defence.'
                        case 'atk1':
                            app.battleMessage = f'{app.battlingEnemy} used {app.battleResult[2]}, raising its attack.'
                        case 'atk2':
                            app.battleMessage = f'{app.battlingEnemy} used {app.battleResult[2]}, sharply raising its attack.'
            if app.playerTeam[app.battlingPokemon].hitpoints <= 0:
                app.uiMessage = f'{app.battlingPokemon} has fainted!'
                app.steps = 0
                loseCondition = True
                for pokemon in app.selectedPokemon:
                    if app.battlingPokemon != pokemon and app.playerTeam[pokemon].hitpoints > 0:
                        loseCondition = False
                        app.selectionMode = 'faint'
                        if app.selectedSave != None:
                            saveFile(app)
                if loseCondition:
                    app.selectionMode = 'defeat'
            else:
                app.selectionMode = 'combat'
                if app.selectedSave != None:
                    saveFile(app)
    
def drawHealthBar(app, x0, y0, maxHealth, health, left):
    width = 150
    height = 15
    if health >= 0:
        if health > 0:
            drawRect(x0, y0, width, height, border='black', borderWidth=2, fill=None)
            if health >= 0.5 * maxHealth:
                drawRect(x0, y0, width*(health/maxHealth), height, border='black', borderWidth=2, fill='green')
            elif health >= 0.2 * maxHealth:
                drawRect(x0, y0, width*(health/maxHealth), height, border='black', borderWidth=2, fill='yellow')
            else:
                drawRect(x0, y0, width*(health/maxHealth), height, border='black', borderWidth=2, fill='red')
        else:
            drawRect(x0, y0, width, height, border='black', borderWidth=2, fill=None)
        if left == None:
            drawLabel(f'{health}/{maxHealth}', x0 + 30, y0 + 23, font='pokemon fire red', size=20, bold=True)
        elif left:
            drawLabel(f'{health}/{maxHealth}', x0 - 30, y0 + 7, font='pokemon fire red', size=20, bold=True)
        else:
            drawLabel(f'{health}/{maxHealth}', x0 + width + 30, y0 + 7, font='pokemon fire red', size=20, bold=True)

def findNextEnemy(app):
    app.remainingEnemies = 3
    for pokemon in app.enemyTeam:
        if app.enemyTeam[pokemon].hitpoints > 0:
            app.battlingEnemy = pokemon
            break
        else:
            app.battlingEnemy = None
            app.remainingEnemies -= 1
    if app.battlingEnemy == None:
        app.selectionMode = 'victory'

def distance(app, x0, y0, x1, y1):
    return ((x0 - x1)**2 + (y0 - y1)**2)**0.5

def reset(app):
    app.enemyTeamSave = [] # list of enemy pokemon 
    app.playerTeamSave = [] # list of player pokemon you can choose
    app.playerItemSave = [] # list of player items
    app.stepsPerSecond = 40
    app.steps = 0
    app.steps3 = 0 # pokemon idle animation
    app.steps4 = 0 # buffer timer after player and enemy move
    app.uiMessage = None
    app.battleMessage = None
    app.selectionMode = 'start'
    app.width, app.height = 480, 320
    app.pokemonSelection = [] # coords for drawing pokemon circles
    app.selectedPokemon = [] # the pokemon you chose
    app.battlingPokemon = None
    app.battlingEnemy = None
    app.currentSelectedPokemon = None
    app.currentSelectedItem = None
    app.money = 10000
    app.battleMessage = None
    app.shopItems = {'Revive':[4900, 'assets/revive.png'], 'Max Revive':[7000, 'assets/maxRevive.png'],'Potion':[800, 'assets/potion.png'], 
                    'Super Potion':[1500, 'assets/superPotion.png'], 'Hyper Potion':[3000, 'assets/hyperPotion.png'], 'Max Potion':[4000, 'assets/maxPotion.png']}
    app.shopDesc = {'Revive':'Revives a fainted Pokemon and restores half its HP', 'Max Revive':'Revives a fainted Pokemon and fully restores its HP',
                    'Potion':'Restores 20 HP', 'Super Potion':'Restores 50 HP', 'Hyper Potion':'Restores 200 HP', 'Max Potion':'Fully restores HP'} 
                    # shop sprites from here: https://msikma.github.io/pokesprite/overview/inventory.html
    app.potionHeal = {'Potion':20, 'Super Potion':50, 'Hyper Potion':200}
    app.superEffective = {'Normal':['Fighting'], 'Fighting':['Flying', 'Psychic', 'Fairy'], 'Flying':['Electric', 'Ice', 'Rock'], 
                  'Poison':['Ground', 'Psychic'], 'Ground':['Grass', 'Ice', 'Water'], 
                  'Rock':['Fighting', 'Grass', 'Ground', 'Steel', 'Water'], 'Bug':['Fire', 'Flying', 'Rock'], 
                  'Ghost':['Dark', 'Ghost'], 'Steel':['Fighting', 'Fire', 'Ground'], 'Fire':['Ground', 'Rock', 'Water'], 
                  'Water':['Electric', 'Grass'], 'Grass':['Bug', 'Fire', 'Flying', 'Ice', 'Poison'], 
                  'Electric':['Ground'], 'Psychic':['Bug', 'Dark', 'Ghost'], 'Ice':['Fighting', 'Fire', 'Rock', 'Steel'], 
                  'Dragon':['Dragon', 'Ice', 'Fairy'], 'Dark':['Bug', 'Fairy', 'Fighting'], 'Fairy':['Poison', 'Steel']} # is from my memory
    app.playerItems = {}
    app.checkShop = []
    app.battleResult = None
    app.faintedTransition = False
    app.remainingEnemies = 3
    initializeShop(app)
    selectPokemon(app)

def main():
    runApp()

main()