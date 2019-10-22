player = {
    'name' :"Zucker",
    'health' : 100,
    'attack' : 50,
    'heal' : 35,
    'heal_potion' : 3
}

minion = {
    'name' :"Muku Minions",
    'health' : 220,
    'attack' : 25
}
def choose():
    print("What you can Do")
    print("1) Attack")
    print("2) Heal ({} Heal Potion Left)".format(player['heal_potion']))
    actn = input("Choose by inserting Number :")
    return int(actn)

def attack(who, whom):
    whom['health'] -= who['attack']
    print("{} attacked {} and dealt {} damage".format(who['name'],whom['name'], who['attack']))
def heal(who):
    if who['heal_potion'] == 0:
        print("{} searched the bag to find No potions left... Opps".format(who['name']))
    else:
        who['health'] += who['heal']
        who['heal_potion'] -= 1
        print("{} heals, +{} to health.".format(who['name'],who['heal']))
        
def action(who, whom, act):
    if act == 1:
        attack(who,whom)
    if act == 2:
        heal(who)

print("Wellcome to MightFight")
print(" This is a Turn-Based-Fighter Game. Your goal is to defeat the minion army.")
print("Begain!!!!!")
round = 1
while minion['health'] > 0:
    print("-------------Round {}-------------".format(round))
    print("{} health: {}".format(player['name'],player['health']))
    print("{} health: {}".format(minion['name'],minion['health']))
    act = choose()
    
    # player action
    action(player, minion, act)
    action(minion, player,1)
    round += 1
    
    
    if player['health'] <= 0:
        print(" Oh! You Died!!!!!!!! Good Luck next Time...")
        break

if minion['health'] <= 0:
    print("Yay!!! {} wins!!!!!!!".format(player['name']))

print("Good Game!!!")
