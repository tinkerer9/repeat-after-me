def listToString(s): 

    str1 = " " 
    
    return str1.join(s)

def randomList(Words):
    Phrase = []
    for i in range(0,randint(1, 3)):
        word = choice(Words).lower()
        Phrase.append(word)

    return Phrase

def mixCase(WOrds):
    return ''.join(choice((str.upper, str.lower, str.lower))(c) for c in WOrds)

def makePhrase():
    with open("words.txt", "r") as words:
        allWords = words.read()

    Words = list(map(str, allWords.split("\n")))

    a = randomList(Words)
    b = listToString(a)
    c = mixCase(b)
    return c

def getNames():
    valid = 1
    while valid == 1:
        MultiIn = typewriterInput("Play Multiplayer? (y/n) ", 1)
        if MultiIn == "y":
            Multiplayer = 1
            valid = 0
        elif MultiIn == "n":
            Multiplayer = 0
            valid = 0
        else:
            typewriter("\aInvalid y/n.\n", 0.5)
            valid = 1

    if Multiplayer == 0:
        valid = 1
        while valid == 1:
            Forever = typewriterInput("Play Forever (until \"x\" entered)? (y/n) ", 1.8)
            if Forever == "y":
                FOrever = 1
                valid = 0
            elif Forever == "n":
                FOrever = 0
                valid = 0
            else:
                typewriter("\aInvalid y/n.\n", 0.5)
                valid = 1
        if FOrever == 0:
            valid = 1
            while valid == 1:
                PointsPerP = typewriterInput("\nPlay up to how many points? ", 1)
                if PointsPerP.isdigit():
                    PointsPerP = int(PointsPerP)
                else:
                    typewriter("\aInvalid Number.", 0.5)
                    valid = 1
                    continue
                if PointsPerP > 0:
                    valid = 0
                else:
                    typewriter("\aInvalid Number.", 0.5)
                    valid = 1
            
            return 0, None, None, PointsPerP
        else:
            infinity = float('inf')
            return 0, None, None, infinity
    
    Names = ["","","",""]
    
    valid = 1
    while valid == 1:
        Players = typewriterInput("How many people are playing? (2-4) ", 1.5)
        if Players.isdigit():
            Players = int(Players)
        else:
            typewriter("\aInvalid Number.\n", 0.5)
            valid = 1
            continue
        if Players >= 2 and Players <= 4:
            valid = 0
        else:
            typewriter("\aInvalid Number.\n", 0.5)
            valid = 1
        
    print("")
    for i in range(0, Players):
        Names[i] = typewriterInput("What is Player " + str(i+1) + "'s name? ", 1)

    if Players > 2:
        hStr = "Hello "
        for i in range(0, Players - 1):
            hStr = hStr + Names[i] + ", "
        hStr = hStr + "and " + Names[Players - 1] + "!\n"
        typewriter(hStr, 1.5)
    else:
        typewriter("Hello " + Names[0] + " and " + Names[1] + "!\n", 1)


    valid = 1
    while valid == 1:
        PointsPerP = typewriterInput("Play up to how many points per person? ", 1.3)
        if PointsPerP.isdigit():
            PointsPerP = int(PointsPerP)
        else:
            typewriter("\aInvalid Number.\n", 0.5)
            valid = 1
            continue
        if PointsPerP > 0:
            valid = 0
        else:
            typewriter("\aInvalid Number.\n", 0.5)
            valid = 1
    
    return 1, Names, Players, PointsPerP

def resetScore():
    score = [0,0,0,0]
    return 0

def rankTime(TIme, PLayers, NAmes):
    nameTime = [
        [NAmes[0], TIme[0]],
        [NAmes[1], TIme[1]],
        [NAmes[2], TIme[2]],
        [NAmes[3], TIme[3]]
    ]

    if PLayers == 2:
        nameTime.pop(2)
        nameTime.pop(2)
    elif PLayers == 3:
        nameTime.pop(3)
    
    nameTime = Sort(nameTime)
    
    return nameTime

def announceRanking(NameTime, PLAyers):
    typewriter("\n" + NameTime[0][0] + " won with a time of " + str(NameTime[0][1]) + " " + plural(NameTime[0][1], "second", "seconds") + "!", 1.5)
    tStr = "All times (in order):\n"
    for i in range(0, PLAyers):
        tStr = tStr + NameTime[i][0] + ": " + str(NameTime[i][1]) + " (" + str(i+1) + numEnding(i+1) + " place)"
        if i < PLAyers-1:
            tStr = tStr + ", "

    typewriter(tStr, 2)
    return 0

def Sort(sub_li):
    return(sorted(sub_li, key = lambda x: x[1]))

def numEnding(num):
    if num == 1:
        return "st"
    elif num == 2:
        return "nd"
    elif num == 3:
        return "rd"
    else:
        return "th"

def generateCompliment():
    with open("compliments.txt", "r") as compliments:
        allCompliments = compliments.read()

    Compliments = list(map(str, allCompliments.split("\n")))

    compliment = choice(Compliments)

    return compliment

def generateMotivation():
    with open("motivations.txt", "r") as motivations:
        allMotivations = motivations.read()

    Motivations = list(map(str, allMotivations.split("\n")))

    motivation = choice(Motivations)

    return motivation

def plural(Num, single, plural):
    if (Num < 2 and Num >= 1) or (Num <= -1 and Num > -2):
        return single
    else:
        return plural

def directions(POIntsPerP):
    intrStr = "\nRepeat After Me - Single Player\nEnter the phrase as shown (until the \":\")\nIf you get the phrase correct, you get as many points as the characters in the phrase (ex. for \"hAppY\" you get 5 points)\nIf you get the phrase wrong, you lose 10 points, BUT if you get only the capitilation wrong, you don't lose points\nType \"x\" to exit; type \"y\" to reset score to 0 (only if score is greater than 0)\n"
    INfinity = float('inf')
    if POIntsPerP != INfinity:
        intrStr = intrStr + "Time gets divided to account for getting more than " + str(POIntsPerP) + " " + plural(POIntsPerP, "point", "points") + ". (real, undivided time in parentheses)\n"
    typewriter(intrStr + "\n", 5)
    return 0

def directionsMulti(POintsPerP):
    typewriter(
                "\nRepeat After Me - Multiplayer" +
                "\nEnter the phrase as shown (until the \":\")" +
                "\nIf you get the phrase correct, you get as many points as the characters in the phrase (ex. for \"hAppY\" you get 5 points)" +
                "\nIf you get the phrase wrong, you lose 10 points, BUT if you get only the capitilation wrong, you don't get points" +
                "\nTry to get to " + str(POintsPerP) + " " + plural(POintsPerP, "point", "points") + " faster than the other competitors." +
                "\nType \"x\" to give up as a player" +
                "\nTime gets divided to account for getting more than " + str(POintsPerP) + " " + plural(POintsPerP, "point", "points") + ".\n"
    , 5)
    return 0

def typewriter(sentence, totalTime):
    elapsedTime = round(totalTime / len(sentence), 2)
    for char in sentence:
        sleep(elapsedTime)
        if char == "\n":
            sleep(0.5)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    return 0

def typewriterInput(Sentence, TotalTime):
    ElapsedTime = round(TotalTime / len(Sentence), 2)
    for Char in Sentence:
        sleep(ElapsedTime)
        if Char == "\n":
            sleep(0.5)
        sys.stdout.write(Char)
        sys.stdout.flush()
    return input("")

def main():
    Infinity = float('inf')

    score = [0,0,0,0]
    startTime = [0,0,0,0]
    times = [0,0,0,0]

    multiplayer, names, players, pointsPerP = getNames()

    if multiplayer == 0:
        directions(pointsPerP)
        if pointsPerP != Infinity:
            typewriterInput("Click ENTER to start", 0.5)
            startTime[0] = time()
        removed = 0
        while score[0] < pointsPerP:
            typewriter("\nGenerating Phrase", 0.25)
            phrase = makePhrase()
            x = typewriterInput(phrase + ": ", 0.75)
            if x == "x":
                removed = 1
                break
            elif x == "y":
                if score >= 0:
                    resetScore()
                    typewriter("Score is 0", 0.5)
                else:
                    typewriter("Score must be greater than 0 to reset score.", 1)
            elif x == phrase:
                score[0] += len(phrase)
                typewriter("Correct! " + str(score[0]) + " " + plural(score[0], "point", "points") + " (+" + str(len(phrase)) + ") " + generateCompliment(), 0.75)
            elif x.lower() == phrase.lower():
                typewriter("Capitilation incorrect. " + str(score[0]) + " " + plural(score[0], "point", "points") + "(no points lost) " + generateMotivation(), 0.75)
            else:
                score[0] -= 10
                typewriter("Incorrect. " + str(score[0]) + " " + plural(score[0], "point", "points") + " (-10) " + generateMotivation(), 0.75)
            if removed == 1:
                break
            
        if pointsPerP != float('inf') and removed == 0:
            times[0] = round(time() - startTime[0], 2)
            timeRaw = times[0]
            pointsMuch = pointsPerP / score[0]
            times[0] = round(times[0] * pointsMuch, 2)
            typewriterInput("\nClick ENTER to see results", 0.7)
            typewriter("You completed " + str(pointsPerP) + " " + plural(pointsPerP, "point", "points") + " in " + str(times[0]) + " " + plural(pointsPerP, "second", "seconds") + "! (" + str(score[0]) + " " + plural(score[0], "point", "points") + " in " + str(timeRaw) + " " + plural(timeRaw, "second", "seconds") + ")", 2)    
    else:
        directionsMulti(pointsPerP)
        for j in range(0, players):
            typewriter("\n" + names[j] + "'s turn!", 0.5)
            typewriterInput("Click ENTER to start", 0.5)
            startTime[j] = time()
            removed = 0
            while score[j] < pointsPerP:
                typewriter("\nGenerating Phrase", 0.25)
                phrase = makePhrase()
                x = typewriterInput(phrase + ": ", 0.75)
                if x == "x":
                    times[j] = Infinity
                    names[j] = "[removed player]"
                    removed = 1
                    break
                elif x == phrase:
                    score[j] += len(phrase)
                    typewriter("Correct! " + str(score[j]) + " " + plural(score[j], "point", "points") + " (+" + str(len(phrase)) + ") " + generateCompliment(), 0.75)
                elif x.lower() == phrase.lower():
                    typewriter("Capitilation incorrect. " + str(score[j]) + " " + plural(score[j], "point", "points") + " (no points lost) " + generateMotivation(), 0.75)
                else:
                    score[j] -= 10
                    typewriter("Incorrect. " + str(score[j]) + " " + plural(score[j], "point", "points") + " (-10) " + generateMotivation(), 0.75)
                if removed == 1:
                    break
            if removed == 0:
                times[j] = round(time() - startTime[j], 2)
                pointsMuch = pointsPerP / score[j]
                times[j] = round(times[j] * pointsMuch, 2)
        typewriterInput("\nClick ENTER to see results", 0.7)
        announceRanking(rankTime(times, players, names), players)

    return 0

from random import randint, choice
from time import time, sleep
import sys

if __name__ == "__main__":
    main()
