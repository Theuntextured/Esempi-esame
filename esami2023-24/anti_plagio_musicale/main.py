def DoesListContainSubList(outer : list, subList : list) -> bool:
    count = 0
    for (i, o) in enumerate(outer[:-(len(subList) - 1)]):
        if o == subList[count]:
            count += 1
            if count == len(subList):
                return True
        else:
            count = 0
    return False

def VerifySong(data : dict[str: dict[str, list[int]]], notes, deltas) -> dict[str, str]: #VictimSong : PlagiarismType
    out = {}
    #first, verify pure plagiarism.
    #then, verify suspect, if found suspicion source, check if it is a copy
    for s in data:
        if notes == data[s]["Notes"]:
            out[s] = "un PLAGIO"
            continue
        #if song is shorter than 4 notes (somehow), then it cannot be a copy/suspect of another song
        if len(notes) < 4:
            continue
        #check for suspects
        Flagged = False
        for i in range(len(deltas) - 3):
            if DoesListContainSubList(data[s]["Deltas"], deltas[i:i + 3]):
                #suspect found
                out[s] = "un SOSPETTO"
                Flagged = True
                break
        
        if not Flagged:
            continue
        
        for i in range(len(notes) - 4):
            if DoesListContainSubList(data[s]["Notes"], notes[i:i + 4]):
                out[s] = "una COPIATURA"
                break

    return out

data = {}

with open('brani.txt', 'r') as file:
    #set up data
    for l in file:
        (name, notesString) = l.rstrip().split(": ")

        notes = []
        for n in notesString.split(" "):
            notes.append(int(n))

        #calculate deltas for notes from previous note, this is to figure out suspects
        noteDeltas = []
        previousNote = notes[0]
        for n in notes[1:]:
            noteDeltas.append(n - previousNote)
            previousNote = n
        
        Result = VerifySong(data, notes, noteDeltas)
        for r in Result:
            print(f"{name} è {Result[r]} di {r}")

        data[name] = {"Notes": notes, "Deltas" : noteDeltas}
