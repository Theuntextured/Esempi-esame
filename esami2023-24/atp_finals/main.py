# Write your solution here, DO NOT START A NEW PROJECT
# ATTENTION: if you create a new project, your exam paper will not be collected
#            and you will be obliged to come in the subsequent exam session
#
# ATTENTION: on Win 10 (Italian keyboard) characters like [ ] { } have to be
#            created using ALTgr+è (e.g. for [ ) and NOT CTRL-ALT-è
#
# ATTENTION: on macOS you have to use CTRL-C and CTRL-V inside the virtual
#            machine and NOT command-C command-V
#
# if your keyboard is broken you can do copy/paste also with mouse
# and you can copy special characters like [ ] { } < > here
#
# Scrivete qui la vostra soluzione, NON CREATE UN NUOVO PROGETTO
# ATTENZIONE: se create un nuovo progetto il vostro compito non sara'
#             raccolto correttamente e dovrete tornare all'appello successivo
#
# ATTENZIONE: su Win 10 (tastiera italiana) i caratteri speciali (es. { ) vanno
#             scritti ad esempio con ALTgr+è (caso di [ ) e NON CTRL-ALT-è
#
# ATTENZIONE: su macOS vanno usati CRTL-C e CTRL-V per il copia incolla
#                       nella macchina virtuale e NON command-C command-V
#
# se la vostra tastiera è guasta potete fare copia/incolla anche con il mouse
# e per i caratteri speciali potete copiare da questi caratteri  [  ]  {  }  <  >
# print(string.punctuation)
## ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~

import random

class group:
    global qualificants

    players : list[str] = []
    playerCycle : list[str] = []

    def __init__(self, players, name) -> None:
        self.players = players
        self.playerCycle = players[1:] + [players[0]]
        with open(name + ".txt", "w") as file:
            for i in players:
                print(f"{i} - {qualificants[i]}", file=file)

        
    
    def cycle(self) -> list:
        '''
        Returns list of next matches\n
        Returns empty list if no more matches are to be played
        '''
        if self.players == self.playerCycle:
            return []
        
        out = []
        for (i, p) in enumerate(self.players):
            out.append((p, self.playerCycle[i]))
        
        self.playerCycle = self.playerCycle[1:] + [self.playerCycle[0]]
        return out
    
    def __str__(self) -> str:
        out = ""
        dayCounter = 0
        while True:
            dayMatches = self.cycle()
            if len(dayMatches) == 0:
                return out
            
            dayCounter += 1
            out = out + f"Day {dayCounter}:\n"
            for (p1, p2) in dayMatches:
                out = out + f"{qualificants[p1]} vs {qualificants[p2]}\n"
            

qualificants = []
def main():
    with open('qualificati.txt', 'r') as file:
        for l in file:
            qualificants.append(l.split(",")[1].rstrip())

    greenGroup = [0] #store indices rather than names. the names are stored in qualificants anyways
    redGroup = [1] #start as list, then convert to group class

    for i in range(2, len(qualificants), 2):
        reverse = random.random() >= 0.5 #50% chance
        greenGroup.append(i if reverse else i + 1)
        redGroup.append(i + 1 if reverse else i)

    greenGroup = group(greenGroup, "green")
    redGroup = group(redGroup, "red")

    calendar = open("calendar.txt", "w")

    print("Green Group:", file=calendar)
    print(greenGroup, file=calendar)
    print("Red Group:", file=calendar)
    print(redGroup, file=calendar, end="") #no need for end char

    calendar.close()

main()