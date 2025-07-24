#encryption[must have binary sort to add code to encrypted message]
import os
import csv
import math
import random
import pandas as pd

count = 0
CodeChecker = 0
IsTheSame = 0
DontStopMeNow = 0
pleasepleasepleaseplease = 0

def CodeCheckerfrfr(code):
    sus = 0
    for i in range (1,36):
        for z in range (1,36):
            if i != z:
                if int(key.iloc[int(code)][i]) == int(key.iloc[int(code)][z]):
                    sus = sus + 1

                if sus == 1:
                    code = "no"
                    return code
    if sus == 0:
        return code

def Encryptinator(letter):
    file = open("characters.csv", "r", encoding = "utf-8")
    reader = csv.reader(file)
    Chara = list(reader)
    file.close()
    if letter == "a" or letter == "A":
        cell = key.iloc[int(code)][1]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == "b" or letter == "B":
        cell = key.iloc[int(code)][2]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == "c" or letter == "C":
        cell = key.iloc[int(code)][3]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == "d" or letter == "D":
        cell = key.iloc[int(code)][4]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == "e" or letter == "E":
        cell = key.iloc[int(code)][5]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    
    #fghij
    elif letter == "f" or letter == "F":
        cell = key.iloc[int(code)][6]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == "g" or letter == "G":
        cell = key.iloc[int(code)][7]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == "h" or letter == "H":
        cell = key.iloc[int(code)][8]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == "i" or letter == "I":
        cell = key.iloc[int(code)][9]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == "j" or letter == "J":
        cell = key.iloc[int(code)][10]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    
    #klmno
    elif letter == "k" or letter == "K":
        cell = key.iloc[int(code)][11]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == "l" or letter == "L":
        cell = key.iloc[int(code)][12]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == "m" or letter == "M":
        cell = key.iloc[int(code)][13]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == "n" or letter == "N":
        cell = key.iloc[int(code)][14]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == "o" or letter == "O":
        cell = key.iloc[int(code)][15]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    
    #pqrst
    elif letter == "p" or letter == "P":
        cell = key.iloc[int(code)][16]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == "q" or letter == "Q":
        cell = key.iloc[int(code)][17]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == "r" or letter == "R":
        cell = key.iloc[int(code)][18]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == "s" or letter == "S":
        cell = key.iloc[int(code)][19]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == "t" or letter == "T":
        cell = key.iloc[int(code)][20]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    
    #uvwxy
    elif letter == "u" or letter == "U":
        cell = key.iloc[int(code)][21]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == "v" or letter == "V":
        cell = key.iloc[int(code)][22]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == "w" or letter == "W":
        cell = key.iloc[int(code)][23]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == "x" or letter == "X":
        cell = key.iloc[int(code)][24]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == "y" or letter == "Y":
        cell = key.iloc[int(code)][25]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    
    #z.,?!
    elif letter == "z" or letter == "Z":
        cell = key.iloc[int(code)][26]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == ".":
        cell = key.iloc[int(code)][27]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == ",":
        cell = key.iloc[int(code)][28]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == "?":
        cell = key.iloc[int(code)][29]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == "!":
        cell = key.iloc[int(code)][30]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    
    #the othe r ones ("';: )
    elif letter == "'":
        cell = key.iloc[int(code)][32]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == ";":
        cell = key.iloc[int(code)][33]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == ":":
        cell = key.iloc[int(code)][34]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    elif letter == " ":
        cell = key.iloc[int(code)][35]
        letter = Chara[(int(cell) - 1)][0]
        return letter
    else:
        return letter

print("Enter the message you wish to encrypt:")
StringToBeEncrypted = str(input("♥ "))

key = pd.read_csv("EncryptionKey.csv", header = None)

one = random.randint(0, 9)
two = random.randint(0, 9)
three = random.randint(0, 9)
four = random.randint(0, 9)
five = random.randint(0, 9)
six = random.randint(0, 9)
seven = random.randint(0, 9)
code = (str(one)+str(two)+str(three)+str(four)+str(five)+str(six)+str(seven))

code = CodeCheckerfrfr(code)
while pleasepleasepleaseplease == False:
    if code == "no":
        one = random.randint(0, 9)
        two = random.randint(0, 9)
        three = random.randint(0, 9)
        four = random.randint(0, 9)
        five = random.randint(0, 9)
        six = random.randint(0, 9)
        seven = random.randint(0, 9)
        code = (str(one)+str(two)+str(three)+str(four)+str(five)+str(six)+str(seven)) 
        code = CodeCheckerfrfr(code)
        pleasepleasepleaseplease = False
    else:
        pleasepleasepleaseplease = True

EncryptedString = str(code)

while count != (len(StringToBeEncrypted)):
    for i in range (0, int(len(StringToBeEncrypted))):
        letter = StringToBeEncrypted[i]
        EncryptedLetter = Encryptinator(letter)
        if EncryptedLetter != ["'"] :
            EncryptedLetter = str(EncryptedLetter)
            EncryptedLetter = EncryptedLetter.replace("[","")
            EncryptedLetter = EncryptedLetter.replace("'","")
            EncryptedLetter = EncryptedLetter.replace("]","")
            EncryptedLetter = EncryptedLetter.replace(" ","")
        else:
            JustSoAphostropheWorks = pd.read_csv("characters.csv", header = None, delimiter='"')
            EncryptedLetter = JustSoAphostropheWorks.iloc[5][0]
        EncryptedString = str(EncryptedString) + str(EncryptedLetter)
        count = count + 1

file = open("note.txt","r")
print(file.read())
file.close()
print("♦ ",EncryptedString)


'''
middle = 9999999 // 2
found = False
z = 0
while found != True:
    if int(code) == int(key.iloc[middle][0]):
        found = True
        row = str(key.iloc[middle])
        print(code)
        print(row)
    elif int(code) > middle:
        if z == 0:
            InitialMiddle = middle
            UpperAdder = middle / 2
            UpperAdder = math.ceil(UpperAdder)
            middle = middle + UpperAdder
            z = z + 1
        else:
            if middle > InitialMiddle:
                DiffInMiddles = middle - InitialMiddle
                middle = middle + DiffInMiddles
            elif middle < InitialMiddle:
                DiffInMiddles = (InitialMiddle - middle) //2
                middle = middle + DiffInMiddles
                middle = math.ceil(middle) 
    elif int(code) < middle:
        if middle == 1:
            InitialMiddle = middle
            middle = 0
        else:
            InitialMiddle = middle
            middle = middle / 2
            middle = math.ceil(middle) 
'''












        

