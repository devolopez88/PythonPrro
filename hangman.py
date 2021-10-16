import random
import os
#   It picks a work from the list returned by the file
def pickword(file):
    word = ""
    ln = random.randrange(0, len(file))
    word = file[ln]
    return word

#   It prints the spot for each letter
def printSpace(word):
    print("You have " + str( len(word)) + " opportunities to WIN. let's tring")
    for l in word[:-1]:
        print("_", end =" ")

#   It reads the file has the list of work will be using in the game
def readFile():
    w = []
    word = ""
    with open("./files/words.txt", "r") as file:
        for wln in file:
            w.append(wln)            
    word = pickword(w) 
    printSpace(word)
    return word


#   It looks the letter type by the user
def searchArray(x, word):
    p = 0
    for i in word:
        for l in x:
            if i == l:
                print(l, end=" ")
                p = p + 1
    return p
    

def run():
    word = readFile()
    lInput = []
    l = ""
    tryed = len(word[:-1])
    for i in range(0,len(word[:-1])):    
        print("\nType a letter : ")
        l = input()
        lInput.append(l)
        p = searchArray(lInput,word)
        if tryed == p:
            print("\nCongratulation you WIN!!!")
            break
        elif p - tryed == 1:
            print("\nJust need one more letter to WIN!!!\n")
        else:
            print("\nKeep try it.\n")
    
    if p < tryed:
        print("\nSorry, you lose. the word was: " +  word +"\n")




        #v = [i for i in word if i in word ]
        #print(v)
        #print("\n")
        
        #print( lInput)
        #lInput.append(input())
        #searchArray(lInput, word)
        #""""
        #v = search(l, word)
        #v = search(lInput, word)
        #if v==1:
        #    print("\nG,")
        #else:
        #    print("\nX,")
        #"""
        
        #os.system('cls')


if __name__ == "__main__":
    run()
