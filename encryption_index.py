#encryption algorithim that checks for a code key to decrypt using a string at the end of the encypted message, that string at the end of the encrypted message is then repeated at the middle, 1/4 and 3/4 of the encrypted text. This ensures that only texted encrypted w/the program is entered protecting agains fake attempts. 
import os
import random

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
    file = open("characters.csv","w")
    file.write("!\n")
    file.write("#\n")
    file.write("$\n")
    file.write("%\n")
    file.write("&\n")
    file.write("'\n")
    file.write("(\n")
    file.write(")\n")
    file.write("*\n")
    file.write("+\n")
    file.write(",\n")
    file.write("-\n")
    file.write(".\n")
    file.write("/\n")
    file.write("0\n")
    file.write("1\n")
    file.write("2\n")
    file.write("3\n")
    file.write("4\n")
    file.write("5\n")
    file.write("6\n")
    file.write("7\n")
    file.write("8\n")
    file.write("9\n")
    file.write(":\n")
    file.write(";\n")
    file.write("<\n")
    file.write("=\n")
    file.write(">\n")
    file.write("?\n")
    file.write("@\n")
    file.write("A\n")
    file.write("B\n")
    file.write("C\n")
    file.write("D\n")
    file.write("E\n")
    file.write("F\n")
    file.write("G\n")
    file.write("H\n")
    file.write("I\n")
    file.write("J\n")
    file.write("K\n")
    file.write("L\n")
    file.write("M\n")
    file.write("N\n")
    file.write("O\n")
    file.write("P\n")
    file.write("Q\n")
    file.write("R\n")
    file.write("S\n")
    file.write("T\n")
    file.write("U\n")
    file.write("V\n")
    file.write("W\n")
    file.write("X\n")
    file.write("Y\n")
    file.write("Z\n")
    file.write("[\n")
    file.write("\ " + "\n")
    file.write("]\n")
    file.write("^\n")
    file.write("_\n")
    file.write("`\n")
    file.write("a\n")
    file.write("b\n")
    file.write("c\n")
    file.write("d\n")
    file.write("e\n")
    file.write("f\n")
    file.write("g\n")
    file.write("h\n")
    file.write("i\n")
    file.write("j\n")
    file.write("k\n")
    file.write("l\n")
    file.write("m\n")
    file.write("n\n")
    file.write("o\n")
    file.write("p\n")
    file.write("q\n")
    file.write("r\n")
    file.write("s\n")
    file.write("t\n")
    file.write("u\n")
    file.write("v\n")
    file.write("w\n")
    file.write("x\n")
    file.write("y\n")
    file.write("z\n")
    file.write("{\n")
    file.write("|\n")
    file.write("}\n")
    file.write("~\n")
    file.write("¬\n")
    file.close()

End = 0

def StartMenu():
    file = open("Menu.txt","r")
    print(file.read())
    file.close
    MenuChoice = int(input("♠ "))
    return MenuChoice

while End == 0:
    Choice = StartMenu()
    if Choice == 1:
        file = "Encrypt.py"
        exec(open(file).read())
        file = open("Menu2.txt","r")
        print(file.read())
        file.close
        MenuChoice2 = int(input("♠ "))
        if MenuChoice2 == 2:
            End = 1
    if Choice == 2:
        file = "Decrypt.py"
        exec(open(file).read())
        file = open("Menu2.txt","r")
        print(file.read())
        file.close
        MenuChoice2 = int(input("♠ "))
        if MenuChoice2 == 2:
            End = 1
    elif Choice == 3:
        End = 1