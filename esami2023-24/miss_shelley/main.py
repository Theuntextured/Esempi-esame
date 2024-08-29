# e per i caratteri speciali potete copiare da questi caratteri  [  ]  {  }  <  >
## ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~

#DEFINE FUNCTIONS

def isSubList(outer : list, subList : list) -> bool:
    o = outer.copy()
    for s in subList:
        if s not in o:
            return False
        o.remove(s)
    return True

#END DEFINE FUNCTIONS


#SET UP INPUT DATA

pricesFile = open('prices.dat', 'r')

prices = {}
for l in pricesFile:
    (shellName, shellPrice) = l.split(": ")
    prices[shellName] = float(shellPrice)
pricesFile.close()

offersFile = open('offers.dat', 'r')
offers = [] #has to be an array rather than dict: multiple offers can lead to same gift and another list is not hashable
#each element is tuple with format: (requirements, gift)
for l in offersFile:
    (requirementsStr, gift) = l.rstrip().split(": ")
    requirements = requirementsStr.split()
    tempArr = []
    for r in requirements:
        tempArr.append(r)
    offers.append((tempArr, gift))
offersFile.close()

cartFile = open('cart.dat', 'r')
cart = []
for l in cartFile:
    cart.append(l.rstrip())
cartFile.close()

#FINISHED SETTING UP INPUT DATA

usableInOffer = cart.copy() #for now make a copy, as offers are found, remove items from here
print(cart)
print()
print(prices)
print()
print(offers)
print()
for (index, (requirements, gift)) in enumerate(offers):
    finishedApplyingOffers = False
    while not finishedApplyingOffers: #can apply an offer more than once
        if isSubList(usableInOffer, requirements):
            for e in requirements: 
                usableInOffer.remove(e)
            if gift in usableInOffer:
                usableInOffer.remove(gift)
            if gift in cart:
                cart.remove(gift)
            print(f"By purchasing {str(requirements).strip("[]").replace("'", "")}; you have receuved {gift} as a gift.")
        else:
            finishedApplyingOffers = True

finalPrice = 0.0
for c in cart:
    finalPrice += prices[c]

print(f"The final price is {finalPrice}.")
print(cart)