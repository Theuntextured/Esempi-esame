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

#set up data in list so it is easier to use later on
with open('passeggeri.txt', 'r') as file:
    passengers = list(csv.DictReader(file))

destination_age_data = {}
flight_passenger_data = {}

for p in passengers:
    origine = p["origin"]
    if origine not in destination_age_data:
        destination_age_data[origine] = []
    destination_age_data[origine].append(float(p["age"]))

    flightNum = p["flight_number"]
    if flightNum not in flight_passenger_data:
        flight_passenger_data[flightNum] = [0,0] #0: male, 1: female. note: this is not a tuple because I need to be able to modify the elements
    flight_passenger_data[flightNum][int(p["gender"] == "F")] += 1

flight_passenger_data = list(flight_passenger_data.items())
flight_passenger_data = sorted(flight_passenger_data, key = lambda element : element[1][0] + element[1][1], reverse=True)[0] #get highest number of passengers

for (key, value) in destination_age_data.items():
    destination_age_data[key] = sum(value) / len(value) #from list, make average

destination_age_data = list(destination_age_data.items()) #convert to list

destination_age_data.sort(key=lambda element : element[1], reverse=True)

print("Average ages for each destination:")
for (origin, age) in destination_age_data:
    print(f"Origin: {origin}, Average age: {round(age, 1)}")

print()

print(f"The most popular flight is {flight_passenger_data[0]} with {flight_passenger_data[1][0]} male and {flight_passenger_data[1][1]} female passengers.")