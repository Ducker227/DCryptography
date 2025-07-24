#encryption algorithim that checks for a code key to decrypt using a string at the end of the encypted message, that string at the end of the encrypted message is then repeated at the middle, 1/4 and 3/4 of the encrypted text. This ensures that only texted encrypted w/the program is entered protecting agains fake attempts. 
import os

file_path = "EncryptionKey.csv"
if not os.path.exists(file_path):
    file = "KeyGenorator.py"
    exec(open(file).read())

file_path = "Menu.txt"
if not os.path.exists(file_path):
    file = open("Menu.txt","w")
    file.write("Encryptor\n")
    file.write(" \n")
    file.write("1) Encrypt a message\n")
    file.write("2) Decrypt a messages\n")
    file.write("3) Close\n")
    file.close()

file_path = "Menu2.txt"
if not os.path.exists(file_path):
    file = open("Menu2.txt","w")
    file.write("Would you like to go back to the main Menu?\n")
    file.write(" \n")
    file.write("1) Go back to main Menu\n")
    file.write("2) End programe\n")
    file.close()

file_path = "characters.csv"
if not os.path.exists(file_path):
    file = open("characters.csv", "w", encoding="utf-8")
    for i in range(1, 1001):
        chara = chr(i)
        if chara.isprintable() and i != 34:
            file.write(str(chara) + "\n")

def StartMenu():
    file = open("Menu.txt","r")
    print(file.read())
    file.close
    MenuChoice = int(input("♠ "))
    return MenuChoice

End = False

while End == False:
    Choice = StartMenu()
    if Choice == 1:
        file = "Encrypt.py"
        exec(open(file).read())
        file = open("Menu2.txt","r")
        print(file.read())
        file.close
        MenuChoice2 = int(input("♠ "))
        if MenuChoice2 == 2:
            End = True
    if Choice == 2:
        file = "Decrypt.py"
        exec(open(file).read())
        file = open("Menu2.txt","r")
        print(file.read())
        file.close
        MenuChoice2 = int(input("♠ "))
        if MenuChoice2 == 2:
            End = True
    elif Choice == 3:
        End = True