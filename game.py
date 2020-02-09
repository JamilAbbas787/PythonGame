import random

player = {"name":"Jamil", "attack": 10, "heal": 10, "health":100}
monster = {"name":"Monster", "attack": 12, "health":100}

def gamePrompts():
    print("Please select action")
    print("(1) Attack")
    print("(2) Heal")

def takeUserInput():
    userInput = int(input())
    if userInput < 1 or userInput > 2:
        print("Invalid Input")
        return False
    return True

def playerTurn():
    gamePrompts()
    playerChoice = takeUserInput()
    if playerChoice == False: 
        playerTurn()
    if playerChoice == 1:
        monster['health'] = monster['health'] - player['attack']
        print('Monster Health Decreased By: ' + str(player['attack']))
        print('New Monster Health: ' +  str(monster['health']))
    else:
        print("Player Healed Themselves")

def monsterAttack():
    if int(random.uniform(1,3)) == 1:
        player['health'] = player['health'] - monster['attack']
        print('Monster Attach Hit!!!')
        print('Player Attacked: New Health = ' + str(player['health']))
        return
    print("Monster attacked missed")


def checkIfAllPlayersAreAlive():
    if player['health'] <= 0 or monster['health'] <= 0:
        print('Game Over')
        print('Player Health = ' + str(player['health']))
        print('Monster Health = ' + str(monster['health']))
        return False
    return True

global allPlayersAreAlivem
allPlayersAreAlive = True
while allPlayersAreAlive == True:
    playerTurn()
    monsterAttack()
    if checkIfAllPlayersAreAlive() == False:
        allPlayersAreAlive = False
    