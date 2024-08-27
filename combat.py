import random
import math
import pokemonCards

def enemyAI(pokemonCards, superEffective, enemyPokemon, playerPokemon):
    maxEffective = 0
    bestMove = None
    bestDamage = 0
    for move in enemyPokemon.moveset: # test supereffective case, is the base AI for making attacks
        effective = 0
        if move[2] == 0:
            continue
        for elem in playerPokemon.type:
            if move[1] in superEffective[elem]:
                effective += 1
        if effective >= maxEffective:
            if bestMove == None:
                bestMove = move
                maxEffective = effective
            elif (2 ** effective) * move[2] >= (2 ** maxEffective) * bestMove[2]: # these test supereffective damage
                maxEffective = effective
                bestMove = move
    enemyDamage = 0
    for move in playerPokemon.moveset: # test if the enemy pokemon can die within two turns
        if move[2] >= enemyDamage:
            enemyDamage = move[2]
    if (enemyDamage * 2 >= enemyPokemon.hitpoints) and (enemyPokemon.hitpoints > math.ceil((1/5) * enemyPokemon.maxHitpoints)):
        for move in enemyPokemon.moveset:
            if move[3] == 'def2': # ups defense if it can die
                bestMove = move
                break
            elif move[3] == 'def1':
                bestMove = move
                print(bestMove)
    prob = random.randint(1, 100)
    if prob > 75:
        bestMove = enemyPokemon.moveset[random.randint(0, 3)]
    return(makeMove(bestMove, enemyPokemon, playerPokemon, superEffective, False))

def makeMove(move, enemyPokemon, playerPokemon, superEffective, turn):
    supertext = None
    missed = False
    ppAIV = 0.95 + (playerPokemon.ivA/100)
    ppDIV = 0.95 + (playerPokemon.ivD/100)
    epAIV = 0.95 + (enemyPokemon.ivA/100)
    epDIV = 0.95 + (enemyPokemon.ivD/100)
    randomDamage = random.randint(95, 105) / 100
    name = move[0]
    type = move[1]
    damage = move[2] * randomDamage
    accuracy = move[3]
    status = move[4]
    enemyType = enemyPokemon.type
    playerType = playerPokemon.type
    if turn:
        damage = math.ceil((ppAIV * damage) / epDIV)
        hit = random.randint(1, 100)
        if hit <= accuracy:
            for elem in enemyPokemon.type:
                if type in superEffective[elem] and damage != 0:
                    damage *= 2
                    supertext = True
            if status != None:
                match status:
                    case 'atk1':
                        playerPokemon.ivA += 30
                    case 'atk2':
                        playerPokemon.ivA += 60
                    case 'def1':
                        playerPokemon.ivD += 30
                    case 'def2':
                        playerPokemon.ivD += 60
            enemyPokemon.hitpoints -= damage
            if enemyPokemon.hitpoints <= 0:
                enemyPokemon.hitpoints = 0
        else:
            missed = True
    else:
        damage = math.ceil((epAIV * damage) / ppDIV)
        hit = random.randint(1, 100)
        if hit <= accuracy:
            for elem in playerPokemon.type:
                if type in superEffective[elem] and damage != 0:
                    damage *= 2
                    supertext = True
            if status != None:
                match status:
                    case 'atk1':
                        enemyPokemon.ivA += 30
                    case 'atk2':
                        enemyPokemon.ivA += 60
                    case 'def1':
                        enemyPokemon.ivD += 30
                    case 'def2':
                        enemyPokemon.ivD += 60
            playerPokemon.hitpoints -= damage
            if playerPokemon.hitpoints <= 0:
                playerPokemon.hitpoints = 0
        else:
            missed = True
    return(turn, missed, name, damage, status, supertext)