import random 
from PIL import Image, ImageOps

# ALL POKEMON SPRITES ARE FROM https://pokemondb.net/sprites

class pokemon:
    def __init__(self, hitpoints, maxHitpoints, name, type, move1, move2, move3, move4, ivA, ivD, imageName, imageName2):
        self.name = name
        self.hitpoints = hitpoints
        self.maxHitpoints = maxHitpoints
        self.type = type
        self.moveset = [move1, move2, move3, move4]
        self.ivA = ivA
        self.ivD = ivD
        self.sprite = imageName
        self.combatSprite = imageName2

    def __repr__ (self):
        return str(self.name)
    
# all pokedata comes from https://pokemondb.net/pokedex/all, movesets, damage, etc.
# player pokemon
Dialga = pokemon(404, 404, 'Dialga', ['Steel', 'Dragon'], ['Roar of Time', 'Dragon', 150, 90, None], ['Iron Tail', 'Steel', 100, 75, None], 
                  ['Earth Power', 'Ground', 90, 100, None], ['Thunderbolt', 'Dragon', 90, 100, None], random.randint(5, 15), random.randint(5, 15), 'assets/dialga.png', 'assets/dialgaBack.png')
Palkia = pokemon(384, 384, 'Palkia', ['Water', 'Dragon'], ['Hydro Pump', 'Water', 110, 80, None], ['Spacial Rend', 'Dragon', 100, 95, None], 
                  ['Earth Power', 'Ground', 90, 100, None], ['Blizzard', 'Ice', 110, 70, None], random.randint(1, 15), random.randint(10, 15), 'assets/palkia.png', 'assets/palkiaBack.png')
Lucario = pokemon(344, 344, 'Lucario', ['Fighting', 'Steel'], ['Close Combat', 'Fighting', 120, 100, None], ['Dragon Pulse', 'Steel', 85, 100, None], 
                  ['Metor Mash', 'Steel', 90, 90, None], ['Swords Dance', 'Normal', 0, 100, 'atk2'], random.randint(10, 15), random.randint(1, 15), 'assets/lucario.png', 'assets/lucarioBack.png')
Rhyperior = pokemon(434, 434, 'Rhyperior', ['Ground', 'Rock'], ['Rock Wrecker', 'Rock', 150, 90, None], ['Mega Horn', 'Bug', 120, 85, None], 
                  ['Earthquake', 'Ground', 100, 100, None], ['Horn Drill', 'Normal', 300, 30, None], random.randint(1, 15), random.randint(5, 15), 'assets/rhyperior.png', 'assets/rhyperiorBack.png')
Zekrom = pokemon(404, 404, 'Zekrom', ['Electric', 'Dragon'], ['Thunder', 'Electric', 110, 70, None], ['Outrage', 'Dragon', 120, 100, None], 
                  ['Fusion Bolt', 'Electric', 100, 100, None], ['Zen Headbutt', 'Psychic', 80, 90, None], random.randint(5, 15), random.randint(1, 15), 'assets/zekrom.png', 'assets/zekromBack.png')
Giratina = pokemon(504, 504, 'Giratina', ['Ghost', 'Dragon'], ['Shadow Force', 'Ghost', 120, 100, None], ['Earth Power', 'Ground', 90, 100, None], 
                  ['Dragon Claw', 'Dragon', 80, 100, None], ['Aura Sphere', 'Fighting', 80, 100, None], random.randint(5, 15), random.randint(5, 15), 'assets/giratina.png', 'assets/giratinaBack.png')
Regigigas = pokemon(424, 424, 'Regigigas', ['Normal'], ['Giga Impact', 'Normal', 150, 90, None], ['Hammer Arm', 'Fighting', 100, 90, None], 
                  ['Zen Headbutt', 'Psychic', 80, 90, None], ['Knock Off', 'Dark', 65, 100, None], random.randint(1, 15), random.randint(1, 15), 'assets/regigigas.png', 'assets/regigigasBack.png')
Scolipede = pokemon(324, 324, 'Scolipede', ['Bug', 'Poison'], ['Megahorn', 'Bug', 120, 85, None], ['Double Edge', 'Normal', 120, 100, None], 
                  ['Venoshock', 'Poison', 130, 100, None], ['Rollout', 'Ground', 30, 90, None], random.randint(5, 20), random.randint(1, 15), 'assets/scolipede.png', 'assets/scolipedeBack.png')
Mewtwo = pokemon(416, 416, 'Mewtwo', ['Psychic'], ['Future Sight', 'Psychic', 120, 100, None], ['Aura Sphere', 'Fighting', 80, 100, None], 
                  ['Safeguard', 'Normal', 0, 100, 'def2'], ['Ancient Power', 'Rock', 60, 100, None], random.randint(10, 15), random.randint(10, 15), 'assets/mewtwo.png', 'assets/mewtwoBack.png')
Torterra = pokemon(394, 394, 'Torterra', ['Grass', 'Ground'], ['Headlong Rush', 'Ground', 120, 100, None], ['Leaf Storm', 'Grass', 130, 90, None], 
                  ['Crunch', 'Dark', 80, 100, None], ['Tera Blast', 'Normal', 80, 100, None], random.randint(1, 15), random.randint(5, 20), 'assets/torterra.png', 'assets/torterraBack.png')
Regice = pokemon(364, 364, 'Regice', ['Ice'], ['Zap Cannon', 'Electric', 240, 50, None], ['Superpower', 'Fighting', 120, 100, None], 
                  ['Psych Up', 'Normal', 0, 100, 'def2'], ['Blizzard', 'Ice', 110, 70, None], random.randint(1, 15), random.randint(1, 20), 'assets/regice.png', 'assets/regiceBack.png')
Moltres = pokemon(360, 360, 'Moltres', ['Fire', 'Flying'], ['Brave Bird', 'Flying', 120, 100, None], ['Steel Wing', 'Steel', 70, 90, None], 
                  ['Flare Blitz', 'Fire', 120, 100, None], ['Overheat', 'Fire', 140, 90, None], random.randint(1, 20), random.randint(1, 15), 'assets/moltres.png', 'assets/moltresBack.png')

# enemy pokemon genetically breeded with insane ivs
Luvdisc = pokemon(290, 290, 'Luvdisk', ['Water'], ['Hydro Pump', 'Water', 110, 80, None], ['Moonblast', 'Fairy', 95, 100, None], 
                  ['Blizzard', 'Ice', 110, 70, None], ['Facade', 'Normal', 70, 100, None], random.randint(20, 35), random.randint(20, 35), 'assets/luvdisc.png', 'assets/luvdiscBack.png')
Zubat = pokemon(284, 284, 'Zubat', ['Poison', 'Flying'], ['Air Slash', 'Flying', 75, 95, None], ['Sludge Bomb', 'Poison', 90, 100, None], 
                  ['Steel Wing', 'Steel', 70, 100, None], ['U-Turn', 'Bug', 70, 100, None], random.randint(25, 40), random.randint(25, 40), 'assets/zubat.png', 'assets/zubatBack.png')
Aggron = pokemon(344, 344, 'Aggron', ['Steel', 'Rock'], ['Double Edge', 'Normal', 120, 100, None], ['Rock Smash', 'Rock', 80, 100, None], 
                  ['Earthquake', 'Ground', 100, 100, None], ['Shadow Claw', 'Ghost', 70, 100, None], random.randint(20, 35), random.randint(50, 75), 'assets/aggron.png', 'assets/aggronBack.png')
Shedinja = pokemon(206, 206, 'Shedinja', ['Bug', 'Ghost'], ['Phantom Force', 'Ghost', 90, 100, None], ['Crunch', 'Dark', 95, 100, None], 
                  ['Buzz Bug', 'Bug', 95, 100, None], ['Dream Eater', 'Psychic', 100, 100, None], random.randint(50, 75), random.randint(20, 35), 'assets/shedinja.png', 'assets/shedinjaBack.png')
Drifloon = pokemon(384, 384, 'Drifloon', ['Ghost', 'Flying'], ['Explosion', 'Normal', 250, 100, None], ['Self Destruct', 'Normal', 200, 100, None], 
                  ['Misty Explosion', 'Fairy', 200, 100, None], ['Mind Blown', 'Fire', 150, 100, None], random.randint(60, 75), random.randint(0, 5), 'assets/drifloon.png', 'assets/drifloonBack.png')

playerPokemon = [Dialga, Palkia, Lucario, Rhyperior, Zekrom, Giratina, 
                 Regigigas, Scolipede, Mewtwo, Torterra, Regice, Moltres]
enemyPokemon = [Luvdisc, Zubat, Aggron, Shedinja, Drifloon]
possibleGood = dict()
possibleBad = dict()
saveList = dict()
saveList2 = dict()

for pokemon in playerPokemon:
    saveList[str(pokemon)] = pokemon

for pokemon in enemyPokemon:
    saveList2[str(pokemon)] = pokemon

def randomizeTeams(goodList, badList, possibleGood, possibleBad): # creates teams of len 6 and len 3 for the player to pick and fight
    while len(possibleGood) < 6:
        index = random.randint(0, len(playerPokemon)-1)
        val = playerPokemon.pop(index)
        possibleGood[str(val)] = val
    while len(possibleBad) < 3:
        index = random.randint(0, len(enemyPokemon)-1)
        val = enemyPokemon.pop(index)
        possibleBad[str(val)] = val

randomizeTeams(playerPokemon, enemyPokemon, possibleGood, possibleBad)