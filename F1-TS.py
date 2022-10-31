from random import randint

# F1 22 Track Selection Randomiser
trackPool = ["Bahrain", "Saudi Arabia", "Austalia", "Imola", "Miami", "Spain", "Monaco", "Azerbaijan", "Canada", "Silverstone", "Austria", "France", "Hungary", "Belgium", "Netherlands", "Monza", "Singapore", "Japan", "USA", "Mexico", "Brazil", "UAE", "Portugal", "China"]
trackSelected = []

def InputSeasonLength():
    selection = input("22, 16 or 10 GP season? ")
    RandomiseTracks(selection)

def RandomiseTracks(selection):
    trackPool = ["Bahrain", "Saudi Arabia", "Austalia", "Imola", "Miami", "Spain", "Monaco", "Azerbaijan", "Canada", "Silverstone", "Austria", "France", "Hungary", "Belgium", "Netherlands", "Monza", "Singapore", "Japan", "USA", "Mexico", "Brazil", "UAE", "Portugal", "China"]
    trackSelected.clear()
    match selection:
        case "22":
            while len(trackSelected) < 22:
                random = randint(0, 23)
                if trackPool[random] != "x":
                    trackSelected.append(trackPool[random])
                    trackPool[random] = "x"
            print(trackSelected)
            InputSeasonLength()
        case "16":
            while len(trackSelected) < 16:
                random = randint(0, 23)
                if trackPool[random] != "x":
                    trackSelected.append(trackPool[random])
                    trackPool[random] = "x"
            print(trackSelected)
            InputSeasonLength()
        case "10":
            while len(trackSelected) < 10:
                random = randint(0, 23)
                if trackPool[random] != "x":
                    trackSelected.append(trackPool[random])
                    trackPool[random] = "x"
            print(trackSelected)
            InputSeasonLength()
        case other:
            print("enter valid input")
            InputSeasonLength()


selection = input("22, 16 or 10 GP season? ")
RandomiseTracks(selection)