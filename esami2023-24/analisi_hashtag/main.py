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


import csv

day1Tags = {}
day2Tags = {}

day1Tags.setdefault(0,0)

with open('hashtags.csv', 'r') as csvFile:
    reader = csv.reader(csvFile, delimiter=" ")
    day1 = None 

    for r in reader:
        if day1 == None:
            day1 = r[0] #data is in chronological order, so I can do this.
        targetDict = day1Tags if r[0] == day1 else day2Tags #create alias of the desired map to edit
        for h in r[2:]: #hashtags start from index 2
            if h not in targetDict:
                targetDict[h] = 1 #create
            else:
                targetDict[h] += 1

hashTagGrowth = []

for (key, item) in day1Tags.items():
    if key not in day2Tags:
        continue
    growth = round((float(day2Tags[key]) / float(item) - 1) * 100)
    if growth >= 50:
        hashTagGrowth.append((key, growth))

hashTagGrowth.sort(key=lambda val : val[1], reverse=True)

print("Hashtag in tendenza:")
for (tag, percent) in hashTagGrowth:
    print(f"{tag} con un'incremento del {percent}%")