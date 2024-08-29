# e per i caratteri speciali potete copiare da questi caratteri  [  ]  {  }  <  >
## ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~

class reactor:
    #index 0 is A, 1 is B etc
    CONSUMPTIONS = [10, 3, 7, 6, 5]
    PRODUCTIONS = [5, 7, 11, 10, 15]

    FN_POWER = 1
    FA_POWER = 2
    amounts = []

    def __init__(self) -> None:
        with open('risorse.txt', 'r') as resources:
            amountsStr = resources.read().rstrip().split()
            for a in amountsStr:
                self.amounts.append(int(a))
        self.amounts.extend((0, 0))
    
    def GetMaxIterationsForReactantIndex(self, index : int) -> int:
        return self.amounts[index] // self.CONSUMPTIONS[index]

    def cycleFN(self) -> int: #return power generated
        ReactionScale = self.GetMaxIterationsForReactantIndex(0)
        ReactionScale = min(ReactionScale, self.GetMaxIterationsForReactantIndex(1))
        ReactionScale = min(ReactionScale, self.GetMaxIterationsForReactantIndex(2))

        for i in range(3):
            self.amounts[i] -= self.CONSUMPTIONS[i] * ReactionScale
        for i in range(3, 5):
            self.amounts[i] += self.PRODUCTIONS[i] * ReactionScale
        return self.FN_POWER * ReactionScale


    def cycleFA(self) -> int:
        ReactionScale = self.GetMaxIterationsForReactantIndex(3)
        ReactionScale = min(ReactionScale, self.GetMaxIterationsForReactantIndex(4))

        for i in range(3):
            self.amounts[i] += self.PRODUCTIONS[i] * ReactionScale
        for i in range(3, 5):
            self.amounts[i] -= self.CONSUMPTIONS[i] * ReactionScale
        return self.FA_POWER * ReactionScale

    #- index 1: Finished : bool
    #- index 2: Power Output : int
    def cycle(self) -> dict:
        generated = self.cycleFN()
        if generated == 0:
            return (True, 0)
        generatedFA = self.cycleFA()
        generated += generatedFA
        return (generatedFA == 0, generated)

def main() -> None:
    powerGenerated = 0
    mostProductiveCycle = 0
    highestCycleProduction = 0

    r = reactor()

    for i in range(1000):
        (finished, output) = r.cycle()
        powerGenerated += output
        if highestCycleProduction <= output:
            highestCycleProduction = output
            mostProductiveCycle = i
        if finished:
            break
    
    print(f"Power generated: {powerGenerated} MW.")
    print(f"The most efficient cycle was {mostProductiveCycle} with a production of {highestCycleProduction} MW.")

main()
