import os
import random
import csv

count = 0
SystemsGo = 0

ThisMakesSureThatAllTheDifferentsNumbersForOneDigetArentLikeTheExactSame = 0
ThisMakesSureThatAllTheDifferentsNumbersForTwoDigetArentLikeTheExactSame = 0
ThisMakesSureThatAllTheDifferentsNumbersForThreeDigetArentLikeTheExactSame = 0
ThisMakesSureThatAllTheDifferentsNumbersForFourDigetArentLikeTheExactSame = 0
ThisMakesSureThatAllTheDifferentsNumbersForFiveDigetArentLikeTheExactSame = 0
ThisMakesSureThatAllTheDifferentsNumbersForSixDigetArentLikeTheExactSame = 0
ThisMakesSureThatAllTheDifferentsNumbersForSevenDigetArentLikeTheExactSame = 0

ThisMakesSureThatAllTheDigetsArentTheExactSame = 0

ThisIsACounterSoTheCodeWorks = 0
ThisIsACounterSoTheCodeWorksbutdifferent1 = 0
ThisIsACounterSoTheCodeWorksbutdifferent2 = 0
ThisIsACounterSoTheCodeWorksbutdifferent3 = 0
ThisIsACounterSoTheCodeWorksbutdifferent4 = 0
ThisIsACounterSoTheCodeWorksbutdifferent5 = 0 
ThisIsACounterSoTheCodeWorksbutdifferent6 = 0
ThisIsACounterSoTheCodeWorksbutdifferent7 = 0
ThisIsACounterSoTheCodeWorksbutdifferent8 = 0
ThisIsACounterSoTheCodeWorksbutdifferent9 = 0
ThisIsACounterSoTheCodeWorksbutdifferent10 = 0
ThisIsACounterSoTheCodeWorksbutdifferent11= 0 
ThisIsACounterSoTheCodeWorksbutdifferent12= 0
ThisIsACounterSoTheCodeWorksbutdifferent13= 0
ThisIsACounterSoTheCodeWorksbutdifferent14= 0
ThisIsACounterSoTheCodeWorksbutdifferent15= 0
ThisIsACounterSoTheCodeWorksbutdifferent16= 0
ThisIsACounterSoTheCodeWorksbutdifferent17= 0 
ThisIsACounterSoTheCodeWorksbutdifferent18= 0
ThisIsACounterSoTheCodeWorksbutdifferent19= 0
ThisIsACounterSoTheCodeWorksbutdifferent20= 0
ThisIsACounterSoTheCodeWorksbutdifferent21= 0
ThisIsACounterSoTheCodeWorksbutdifferent22= 0
ThisIsACounterSoTheCodeWorksbutdifferent23= 0 
ThisIsACounterSoTheCodeWorksbutdifferent24= 0
ThisIsACounterSoTheCodeWorksbutdifferent25= 0
ThisIsACounterSoTheCodeWorksbutdifferent26= 0
ThisIsACounterSoTheCodeWorksbutdifferent27= 0
ThisIsACounterSoTheCodeWorksbutdifferent28= 0
ThisIsACounterSoTheCodeWorksbutdifferent29= 0 
ThisIsACounterSoTheCodeWorksbutdifferent30= 0
ThisIsACounterSoTheCodeWorksbutdifferent31= 0
ThisIsACounterSoTheCodeWorksbutdifferent32= 0
ThisIsACounterSoTheCodeWorksbutdifferent33= 0
ThisIsACounterSoTheCodeWorksbutdifferent34= 0
ThisIsACounterSoTheCodeWorksbutdifferent35= 0 
ThisIsACounterSoTheCodeWorksbutdifferent36= 0
ThisIsACounterSoTheCodeWorksbutdifferent37= 0
ThisIsACounterSoTheCodeWorksbutdifferent38= 0
ThisIsACounterSoTheCodeWorksbutdifferent39= 0
ThisIsACounterSoTheCodeWorksbutdifferent40= 0
ThisIsACounterSoTheCodeWorksbutdifferent41= 0 
ThisIsACounterSoTheCodeWorksbutdifferent42= 0
ThisIsACounterSoTheCodeWorksbutdifferent43= 0
ThisIsACounterSoTheCodeWorksbutdifferent44= 0
ThisIsACounterSoTheCodeWorksbutdifferent45= 0
ThisIsACounterSoTheCodeWorksbutdifferent46= 0
ThisIsACounterSoTheCodeWorksbutdifferent47= 0 
ThisIsACounterSoTheCodeWorksbutdifferent48= 0
ThisIsACounterSoTheCodeWorksbutdifferent49= 0
ThisIsACounterSoTheCodeWorksbutdifferent50= 0
ThisIsACounterSoTheCodeWorksbutdifferent51= 0
ThisIsACounterSoTheCodeWorksbutdifferent52= 0
ThisIsACounterSoTheCodeWorksbutdifferent53= 0 
ThisIsACounterSoTheCodeWorksbutdifferent54= 0
ThisIsACounterSoTheCodeWorksbutdifferent55= 0
ThisIsACounterSoTheCodeWorksbutdifferent56= 0
ThisIsACounterSoTheCodeWorksbutdifferent57= 0
ThisIsACounterSoTheCodeWorksbutdifferent58= 0
ThisIsACounterSoTheCodeWorksbutdifferent59= 0 
ThisIsACounterSoTheCodeWorksbutdifferent60= 0
ThisIsACounterSoTheCodeWorksbutdifferent61= 0
ThisIsACounterSoTheCodeWorksbutdifferent62= 0
ThisIsACounterSoTheCodeWorksbutdifferent63= 0
ThisIsACounterSoTheCodeWorksbutdifferent64= 0
ThisIsACounterSoTheCodeWorksbutdifferent65= 0 
ThisIsACounterSoTheCodeWorksbutdifferent66= 0
ThisIsACounterSoTheCodeWorksbutdifferent67= 0
ThisIsACounterSoTheCodeWorksbutdifferent68= 0
ThisIsACounterSoTheCodeWorksbutdifferent69= 0

ThisMakesSureThatAllTheDifferentsNumbersForOneDigetArentLikeTheExactSame = 0
ThisMakesSureThatAllTheDigetsArentTheExactSame = 0

ZeroALocked = 0
OneALocked = 0
TwoALocked = 0
ThreeALocked = 0
FourALocked = 0
FiveALocked = 0
SixALocked = 0
SevenALocked = 0
EightALocked = 0
NineALocked = 0

ZeroFLocked = 0
OneFLocked = 0
TwoFLocked = 0
ThreeFLocked = 0
FourFLocked = 0
FiveFLocked = 0
SixFLocked = 0
SevenFLocked = 0
EightFLocked = 0
NineFLocked = 0

ZeroKLocked = 0
OneKLocked = 0
TwoKLocked = 0
ThreeKLocked = 0
FourKLocked = 0
FiveKLocked = 0
SixKLocked = 0
SevenKLocked = 0
EightKLocked = 0
NineKLocked = 0

ZeroPLocked = 0
OnePLocked = 0
TwoPLocked = 0
ThreePLocked = 0
FourPLocked = 0
FivePLocked = 0
SixPLocked = 0
SevenPLocked = 0
EightPLocked = 0
NinePLocked = 0

ZeroULocked = 0
OneULocked = 0
TwoULocked = 0
ThreeULocked = 0
FourULocked = 0
FiveULocked = 0
SixULocked = 0
SevenULocked = 0
EightULocked = 0
NineULocked = 0

ZeroZLocked = 0
OneZLocked = 0
TwoZLocked = 0
ThreeZLocked = 0
FourZLocked = 0
FiveZLocked = 0
SixZLocked = 0
SevenZLocked = 0
EightZLocked = 0
NineZLocked = 0

ZeroQuoteLocked = 0
OneQuoteLocked = 0
TwoQuoteLocked = 0
ThreeQuoteLocked = 0
FourQuoteLocked = 0
FiveQuoteLocked = 0
SixQuoteLocked = 0
SevenQuoteLocked = 0
EightQuoteLocked = 0
NineQuoteLocked = 0

check = 0
CheckDonCheckOne = 0
CheckDonCheckTwo = 0
CheckDonCheckThree = 0
CheckDonCheckFour = 0
CheckDonCheckFive = 0
CheckDonCheckSix = 0
CheckDonCheckSeven = 0

 
code = 0
CodeChecker = 0
Position = 0
EncryptionArray = []

def ArrayAdder(grid, row, col, iteam):

    while len(grid) <= row:
        grid.append([0])

    while len(grid[row]) <= col:
        grid[row].append(0)

    grid[row][col] = iteam


def CubicNumberChecker(one, two, three, four, five):
    CubeOne = int(one)*int(one)*int(one)
    CubeTwo = int(two)*int(two)*int(two)
    CubeThree = int(three)*int(three)*int(three)
    CubeFour = int(four)*int(four)*int(four)
    CubeFive = int(five)*int(five)*int(five)
    FullDigit = CubeOne + CubeTwo + CubeThree + CubeFour + CubeFive
    return FullDigit

while count != 10000000:



    while ZeroALocked == 0 or OneALocked == 0 or TwoALocked == 0 or ThreeALocked == 0 or FourALocked == 0 or FiveALocked == 0 or SixALocked == 0 or SevenALocked == 0 or EightALocked == 0 or NineALocked == 0 or ZeroFLocked == 0 or OneFLocked == 0 or TwoFLocked == 0 or ThreeFLocked == 0 or FourFLocked == 0 or FiveFLocked == 0 or SixFLocked == 0 or SevenFLocked == 0 or EightFLocked == 0 or NineFLocked == 0 or ZeroKLocked == 0 or OneKLocked == 0 or TwoKLocked == 0 or ThreeKLocked == 0 or FourKLocked == 0 or SixKLocked == 0 or SevenKLocked == 0 or EightKLocked == 0 or NineKLocked == 0 or ZeroPLocked == 0 or OnePLocked == 0 or TwoPLocked == 0 or ThreePLocked == 0 or FourPLocked == 0 or FivePLocked == 0 or SixPLocked == 0 or SevenPLocked == 0 or EightPLocked == 0 or NinePLocked == 0 or ZeroULocked == 0 or OneULocked == 0 or TwoULocked == 0 or ThreeULocked == 0 or FourULocked == 0 or FiveULocked == 0 or SixULocked == 0 or SevenULocked == 0 or EightULocked == 0 or NineULocked == 0 or ZeroZLocked == 0 or OneZLocked == 0 or TwoZLocked == 0 or ThreeZLocked == 0 or FourZLocked == 0 or FiveZLocked == 0 or SixZLocked == 0 or SevenZLocked == 0 or EightZLocked == 0 or NineZLocked == 0 or ZeroQuoteLocked == 0 or OneQuoteLocked == 0 or TwoQuoteLocked == 0 or ThreeQuoteLocked == 0 or FourQuoteLocked == 0 or FiveQuoteLocked == 0 or SixQuoteLocked == 0 or SevenQuoteLocked == 0 or EightQuoteLocked == 0 or NineQuoteLocked == 0 and ThisMakesSureThatAllTheDifferentsNumbersForOneDigetArentLikeTheExactSame == 0 and ThisMakesSureThatAllTheDifferentsNumbersForTwoDigetArentLikeTheExactSame == 0 and ThisMakesSureThatAllTheDifferentsNumbersForThreeDigetArentLikeTheExactSame == 0 and ThisMakesSureThatAllTheDifferentsNumbersForFourDigetArentLikeTheExactSame == 0 and ThisMakesSureThatAllTheDifferentsNumbersForFiveDigetArentLikeTheExactSame == 0 and ThisMakesSureThatAllTheDifferentsNumbersForSixDigetArentLikeTheExactSame == 0 and ThisMakesSureThatAllTheDifferentsNumbersForSevenDigetArentLikeTheExactSame == 0 or SystemsGo == 0:

        one = random.randint(0, 9)
        two = random.randint(0, 9)
        three = random.randint(0, 9)
        four = random.randint(0, 9)
        five = random.randint(0, 9)
        six = random.randint(0, 9)
        seven = random.randint(0, 9)
        code = (str(one)+str(two)+str(three)+str(four)+str(five)+str(six)+str(seven)) 

        #First digit code for abcde
        if one == 0:
            while ThisIsACounterSoTheCodeWorks != 1:
                if ZeroALocked == 0:
                    a = random.randint(1, 94)
                    b = random.randint(1, 94)
                    c = random.randint(1, 94)
                    d = random.randint(1, 94)
                    e = random.randint(1, 94)
                    ZeroALocked = a
                    ZeroBLocked = b
                    ZeroCLocked = c
                    ZeroDLocked = d
                    ZeroELocked = e
                if a == b or a == c or a == d or a== e or b == c or b == d or b == e or c == d or c == e or d == e:
                    ZeroALocked = 0
                    ThisIsACounterSoTheCodeWorks = 0
                else:
                    ThisIsACounterSoTheCodeWorks = 1
        elif one == 1:
            while ThisIsACounterSoTheCodeWorksbutdifferent1 != 1:
                if OneALocked == 0:
                    a = random.randint(1, 94)
                    b = random.randint(1, 94)
                    c = random.randint(1, 94)
                    d = random.randint(1, 94)
                    e = random.randint(1, 94)
                    OneALocked = a
                    OneBLocked = b
                    OneCLocked = c
                    OneDLocked = d
                    OneELocked = e
                if a == b or a == c or a == d or a== e or b == c or b == d or b == e or c == d or c == e or d == e:
                    OneALocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent1 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent1 = 1
        elif one == 2:
            while ThisIsACounterSoTheCodeWorksbutdifferent2 != 1:
                if TwoALocked == 0:
                    a = random.randint(1, 94)
                    b = random.randint(1, 94)
                    c = random.randint(1, 94)
                    d = random.randint(1, 94)
                    e = random.randint(1, 94)
                    TwoALocked = a
                    TwoBLocked = b
                    TwoCLocked = c
                    TwoDLocked = d
                    TwoELocked = e
                if a == b or a == c or a == d or a== e or b == c or b == d or b == e or c == d or c == e or d == e:
                    TwoALocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent2 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent2 = 1
        elif one == 3:
            while ThisIsACounterSoTheCodeWorksbutdifferent3 != 1:
                if ThreeALocked == 0:
                    a = random.randint(1, 94)
                    b = random.randint(1, 94)
                    c = random.randint(1, 94)
                    d = random.randint(1, 94)
                    e = random.randint(1, 94)
                    ThreeALocked = a
                    ThreeBLocked = b
                    ThreeCLocked = c
                    ThreeDLocked = d
                    ThreeELocked = e
                if a == b or a == c or a == d or a== e or b == c or b == d or b == e or c == d or c == e or d == e:
                    ThreeALocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent3 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent3 = 1
        elif one == 4: 
            while ThisIsACounterSoTheCodeWorksbutdifferent4 != 1:
                if FourALocked == 0:
                    a = random.randint(1, 94)
                    b = random.randint(1, 94)
                    c = random.randint(1, 94)
                    d = random.randint(1, 94)
                    e = random.randint(1, 94)
                    FourALocked = a
                    FourBLocked = b
                    FourCLocked = c
                    FourDLocked = d
                    FourELocked = e
                if a == b or a == c or a == d or a== e or b == c or b == d or b == e or c == d or c == e or d == e:
                    FourALocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent4 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent4 = 1
        elif one == 5: 
            while ThisIsACounterSoTheCodeWorksbutdifferent5 != 1:
                if FiveALocked == 0:
                    a = random.randint(1, 94)
                    b = random.randint(1, 94)
                    c = random.randint(1, 94)
                    d = random.randint(1, 94)
                    e = random.randint(1, 94)
                    FiveALocked = a
                    FiveBLocked = b
                    FiveCLocked = c
                    FiveDLocked = d
                    FiveELocked = e
                if a == b or a == c or a == d or a== e or b == c or b == d or b == e or c == d or c == e or d == e:
                    FiveALocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent5 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent5 = 1
        elif one == 6:
            while ThisIsACounterSoTheCodeWorksbutdifferent6 != 1:
                if SixALocked == 0:
                    a = random.randint(1, 94)
                    b = random.randint(1, 94)
                    c = random.randint(1, 94)
                    d = random.randint(1, 94)
                    e = random.randint(1, 94)
                    SixALocked = a
                    SixBLocked = b
                    SixCLocked = c
                    SixDLocked = d
                    SixELocked = e
                if a == b or a == c or a == d or a== e or b == c or b == d or b == e or c == d or c == e or d == e:
                    SixALocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent6 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent6 = 1
        elif one == 7:
            while ThisIsACounterSoTheCodeWorksbutdifferent7 != 1:
                if SevenALocked == 0:
                    a = random.randint(1, 94)
                    b = random.randint(1, 94)
                    c = random.randint(1, 94)
                    d = random.randint(1, 94)
                    e = random.randint(1, 94)
                    SevenALocked = a
                    SevenBLocked = b
                    SevenCLocked = c
                    SevenDLocked = d
                    SevenELocked = e
                if a == b or a == c or a == d or a== e or b == c or b == d or b == e or c == d or c == e or d == e:
                    SevenALocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent7 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent7 = 1
        elif one == 8: 
            while ThisIsACounterSoTheCodeWorksbutdifferent8 != 1:
                if EightALocked == 0:
                    a = random.randint(1, 94)
                    b = random.randint(1, 94)
                    c = random.randint(1, 94)
                    d = random.randint(1, 94)
                    e = random.randint(1, 94)
                    EightALocked = a
                    EightBLocked = b
                    EightCLocked = c
                    EightDLocked = d
                    EightELocked = e
                if a == b or a == c or a == d or a== e or b == c or b == d or b == e or c == d or c == e or d == e:
                    EightALocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent8 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent8 = 1
        elif one == 9: 
            while ThisIsACounterSoTheCodeWorksbutdifferent9 != 1:
                if NineALocked == 0:
                    a = random.randint(1, 94)
                    b = random.randint(1, 94)
                    c = random.randint(1, 94)
                    d = random.randint(1, 94)
                    e = random.randint(1, 94)
                    NineALocked = a
                    NineBLocked = b
                    NineCLocked = c
                    NineDLocked = d
                    NineELocked = e
                if a == b or a == c or a == d or a== e or b == c or b == d or b == e or c == d or c == e or d == e:
                    NineALocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent9 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent9 = 1

        if ZeroALocked != 0 and OneALocked != 0 and TwoALocked != 0 and ThreeALocked != 0 and FourALocked != 0 and FiveALocked != 0 and SixALocked != 0 and SevenALocked != 0 and EightALocked != 0 and NineALocked != 0:
            SumOfZero = CubicNumberChecker(ZeroALocked, ZeroBLocked, ZeroCLocked, ZeroDLocked, ZeroELocked)
            SumOfOne = CubicNumberChecker(OneALocked, OneBLocked, OneCLocked, OneDLocked, OneELocked)
            SumOfTwo = CubicNumberChecker(TwoALocked, TwoBLocked, TwoCLocked, TwoDLocked, TwoELocked)
            SumOfThree = CubicNumberChecker(ThreeALocked, ThreeBLocked, ThreeCLocked, ThreeDLocked, ThreeELocked)
            SumOfFour = CubicNumberChecker(FourALocked, FourBLocked, FourCLocked, FourDLocked, FourELocked)
            SumOfFive = CubicNumberChecker(FiveALocked, FiveBLocked, FiveCLocked, FiveDLocked, FiveELocked)
            SumOfSix = CubicNumberChecker(SixALocked, SixBLocked, SixCLocked, SixDLocked, SixELocked)
            SumOfSeven = CubicNumberChecker(SevenALocked, SevenBLocked, SevenCLocked, SevenDLocked, SevenELocked)
            SumOfEight = CubicNumberChecker(EightALocked, EightBLocked, EightCLocked, EightDLocked, EightELocked)
            SumOfNine = CubicNumberChecker(NineALocked, NineBLocked, NineCLocked, NineDLocked, NineELocked)
            OneSumOfZero = SumOfZero
            OneSumOfOne = SumOfOne
            OneSumOfTwo = SumOfTwo
            OneSumOfThree = SumOfThree
            OneSumOfFour = SumOfFour
            OneSumOfFive = SumOfFive
            OneSumOfSix = SumOfSix
            OneSumOfSeven = SumOfSeven
            OneSumOfEight = SumOfEight
            OneSumOfNine = SumOfNine
            if SumOfZero != SumOfOne and SumOfZero != SumOfTwo and SumOfZero != SumOfThree and SumOfZero != SumOfFour and SumOfZero != SumOfFive and SumOfZero != SumOfSix and SumOfZero != SumOfSeven and SumOfZero != SumOfEight and SumOfZero != SumOfNine and SumOfOne != SumOfTwo and SumOfOne != SumOfThree and SumOfOne != SumOfFour and SumOfOne != SumOfFive and SumOfOne != SumOfSix and SumOfOne != SumOfSeven and SumOfOne != SumOfEight and SumOfOne != SumOfNine and SumOfTwo != SumOfThree and SumOfTwo != SumOfFour and SumOfTwo != SumOfFive and SumOfTwo != SumOfSix and SumOfTwo != SumOfSeven and SumOfTwo != SumOfEight and SumOfTwo != SumOfNine and SumOfThree != SumOfFour and SumOfThree != SumOfFive and SumOfThree != SumOfSix and SumOfThree != SumOfSeven and SumOfThree != SumOfEight and SumOfThree != SumOfNine and SumOfFour != SumOfFive and SumOfFour != SumOfSix and SumOfFour != SumOfSeven and SumOfFour != SumOfEight and SumOfFour != SumOfNine and SumOfFive != SumOfSix and SumOfFive != SumOfSeven and SumOfFive != SumOfEight and SumOfFive != SumOfNine and SumOfSix != SumOfSeven and SumOfSix != SumOfEight and SumOfSix != SumOfNine and SumOfSeven != SumOfEight and SumOfSeven != SumOfNine and SumOfEight != SumOfNine:
                print("processing1")
                ThisMakesSureThatAllTheDifferentsNumbersForOneDigetArentLikeTheExactSame = 1
                if CheckDonCheckOne != 1:
                    CheckDonCheckOne = 1
                    check = check + 1
            else:
                ZeroALocked = 0
                OneALocked = 0
                TwoALocked = 0
                ThreeALocked = 0
                FourALocked = 0
                FiveALocked = 0
                SixALocked = 0
                SevenALocked = 0
                EightALocked = 0
                NineALocked = 0
            #This makes sure all the different possible numbers for the first aren't the same




        #The Second Digit code for fghij
        if two == 0:
            while ThisIsACounterSoTheCodeWorksbutdifferent10 != 1:
                if ZeroFLocked == 0:
                    f = random.randint(1, 94)
                    g = random.randint(1, 94)
                    h = random.randint(1, 94)
                    i = random.randint(1, 94)
                    j = random.randint(1, 94)
                    ZeroFLocked = f
                    ZeroGLocked = g
                    ZeroHLocked = h
                    ZeroILocked = i
                    ZeroJLocked = j
                if f == g or f == h or f == i or f == j or g == h or g == i or g == j or h == i or h == j or i == j:
                    ZeroFLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent10 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent10 = 1
        elif two == 1:
            while ThisIsACounterSoTheCodeWorksbutdifferent11 != 1:
                if OneFLocked == 0:
                    f = random.randint(1, 94)
                    g = random.randint(1, 94)
                    h = random.randint(1, 94)
                    i = random.randint(1, 94)
                    j = random.randint(1, 94)
                    OneFLocked = f
                    OneGLocked = g
                    OneHLocked = h
                    OneILocked = i
                    OneJLocked = j
                if f == g or f == h or f == i or f == j or g == h or g == i or g == j or h == i or h == j or i == j:
                    OneFLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent11 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent11 = 1
        elif two == 2:
            while ThisIsACounterSoTheCodeWorksbutdifferent12 != 1:
                if TwoFLocked == 0:
                    f = random.randint(1, 94)
                    g = random.randint(1, 94)
                    h = random.randint(1, 94)
                    i = random.randint(1, 94)
                    j = random.randint(1, 94)
                    TwoFLocked = f
                    TwoGLocked = g
                    TwoHLocked = h
                    TwoILocked = i
                    TwoJLocked = j
                if f == g or f == h or f == i or f == j or g == h or g == i or g == j or h == i or h == j or i == j:
                    TwoFLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent12 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent12 = 1
        elif two == 3:
            while ThisIsACounterSoTheCodeWorksbutdifferent13 != 1:
                if ThreeFLocked == 0:
                    f = random.randint(1, 94)
                    g = random.randint(1, 94)
                    h = random.randint(1, 94)
                    i = random.randint(1, 94)
                    j = random.randint(1, 94)
                    ThreeFLocked = f
                    ThreeGLocked = g
                    ThreeHLocked = h
                    ThreeILocked = i
                    ThreeJLocked = j
                if f == g or f == h or f == i or f == j or g == h or g == i or g == j or h == i or h == j or i == j:
                    ThreeFLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent13 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent13 = 1
        elif two == 4: 
            while ThisIsACounterSoTheCodeWorksbutdifferent14 != 1:
                if FourFLocked == 0:
                    f = random.randint(1, 94)
                    g = random.randint(1, 94)
                    h = random.randint(1, 94)
                    i = random.randint(1, 94)
                    j = random.randint(1, 94)
                    FourFLocked = f
                    FourGLocked = g
                    FourHLocked = h
                    FourILocked = i
                    FourJLocked = j
                if f == g or f == h or f == i or f == j or g == h or g == i or g == j or h == i or h == j or i == j:
                    FourFLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent14 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent14 = 1
        elif two == 5: 
            while ThisIsACounterSoTheCodeWorksbutdifferent15 != 1:
                if FiveFLocked == 0:
                    f = random.randint(1, 94)
                    g = random.randint(1, 94)
                    h = random.randint(1, 94)
                    i = random.randint(1, 94)
                    j = random.randint(1, 94)
                    FiveFLocked = f
                    FiveGLocked = g
                    FiveHLocked = h
                    FiveILocked = i
                    FiveJLocked = j
                if f == g or f == h or f == i or f == j or g == h or g == i or g == j or h == i or h == j or i == j:
                    FiveFLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent15 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent15 = 1
        elif two == 6:
            while ThisIsACounterSoTheCodeWorksbutdifferent16 != 1:
                if SixFLocked == 0:
                    f = random.randint(1, 94)
                    g = random.randint(1, 94)
                    h = random.randint(1, 94)
                    i = random.randint(1, 94)
                    j = random.randint(1, 94)
                    SixFLocked = f
                    SixGLocked = g
                    SixHLocked = h
                    SixILocked = i
                    SixJLocked = j
                if f == g or f == h or f == i or f == j or g == h or g == i or g == j or h == i or h == j or i == j:
                    SixFLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent16 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent16 = 1
        elif two == 7:
            while ThisIsACounterSoTheCodeWorksbutdifferent17 != 1:
                if SevenFLocked == 0:
                    f = random.randint(1, 94)
                    g = random.randint(1, 94)
                    h = random.randint(1, 94)
                    i = random.randint(1, 94)
                    j = random.randint(1, 94)
                    SevenFLocked = f
                    SevenGLocked = g
                    SevenHLocked = h
                    SevenILocked = i
                    SevenJLocked = j
                if f == g or f == h or f == i or f == j or g == h or g == i or g == j or h == i or h == j or i == j:
                    SevenFLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent17 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent17 = 1
        elif two == 8: 
            while ThisIsACounterSoTheCodeWorksbutdifferent18 != 1:
                if EightFLocked == 0:
                    f = random.randint(1, 94)
                    g = random.randint(1, 94)
                    h = random.randint(1, 94)
                    i = random.randint(1, 94)
                    j = random.randint(1, 94)
                    EightFLocked = f
                    EightGLocked = g
                    EightHLocked = h
                    EightILocked = i
                    EightJLocked = j
                if f == g or f == h or f == i or f == j or g == h or g == i or g == j or h == i or h == j or i == j:
                    EightFLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent18 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent18 = 1
        elif two == 9: 
            while ThisIsACounterSoTheCodeWorksbutdifferent19 != 1:
                if NineFLocked == 0:
                    f = random.randint(1, 94)
                    g = random.randint(1, 94)
                    h = random.randint(1, 94)
                    i = random.randint(1, 94)
                    j = random.randint(1, 94)
                    NineFLocked = f
                    NineGLocked = g
                    NineHLocked = h
                    NineILocked = i
                    NineJLocked = j
                if f == g or f == h or f == i or f == j or g == h or g == i or g == j or h == i or h == j or i == j:
                    NineFLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent19 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent19 = 1

        if ZeroFLocked != 0 and OneFLocked != 0 and TwoFLocked != 0 and ThreeFLocked != 0 and FourFLocked != 0 and FiveFLocked != 0 and SixFLocked != 0 and SevenFLocked != 0 and EightFLocked != 0 and NineFLocked != 0:
            SumOfZero = CubicNumberChecker(ZeroFLocked, ZeroGLocked, ZeroHLocked, ZeroILocked, ZeroJLocked)
            SumOfOne = CubicNumberChecker(OneFLocked, OneGLocked, OneHLocked, OneILocked, OneJLocked)
            SumOfTwo = CubicNumberChecker(TwoFLocked, TwoGLocked, TwoHLocked, TwoILocked, TwoJLocked)
            SumOfThree = CubicNumberChecker(ThreeFLocked, ThreeGLocked, ThreeHLocked, ThreeILocked, ThreeJLocked)
            SumOfFour = CubicNumberChecker(FourFLocked, FourGLocked, FourHLocked, FourILocked, FourJLocked)
            SumOfFive = CubicNumberChecker(FiveFLocked, FiveGLocked, FiveHLocked, FiveILocked, FiveJLocked)
            SumOfSix = CubicNumberChecker(SixFLocked, SixGLocked, SixHLocked, SixILocked, SixJLocked)
            SumOfSeven = CubicNumberChecker(SevenFLocked, SevenGLocked, SevenHLocked, SevenILocked, SevenJLocked)
            SumOfEight = CubicNumberChecker(EightFLocked, EightGLocked, EightHLocked, EightILocked, EightJLocked)
            SumOfNine = CubicNumberChecker(NineFLocked, NineGLocked, NineHLocked, NineILocked, NineJLocked)
            TwoSumOfZero = SumOfZero
            TwoSumOfOne = SumOfOne
            TwoSumOfTwo = SumOfTwo
            TwoSumOfThree = SumOfThree
            TwoSumOfFour = SumOfFour
            TwoSumOfFive = SumOfFive
            TwoSumOfSix = SumOfSix
            TwoSumOfSeven = SumOfSeven
            TwoSumOfEight = SumOfEight
            TwoSumOfNine = SumOfNine
            if SumOfZero != SumOfOne and SumOfZero != SumOfTwo and SumOfZero != SumOfThree and SumOfZero != SumOfFour and SumOfZero != SumOfFive and SumOfZero != SumOfSix and SumOfZero != SumOfSeven and SumOfZero != SumOfEight and SumOfZero != SumOfNine and SumOfOne != SumOfTwo and SumOfOne != SumOfThree and SumOfOne != SumOfFour and SumOfOne != SumOfFive and SumOfOne != SumOfSix and SumOfOne != SumOfSeven and SumOfOne != SumOfEight and SumOfOne != SumOfNine and SumOfTwo != SumOfThree and SumOfTwo != SumOfFour and SumOfTwo != SumOfFive and SumOfTwo != SumOfSix and SumOfTwo != SumOfSeven and SumOfTwo != SumOfEight and SumOfTwo != SumOfNine and SumOfThree != SumOfFour and SumOfThree != SumOfFive and SumOfThree != SumOfSix and SumOfThree != SumOfSeven and SumOfThree != SumOfEight and SumOfThree != SumOfNine and SumOfFour != SumOfFive and SumOfFour != SumOfSix and SumOfFour != SumOfSeven and SumOfFour != SumOfEight and SumOfFour != SumOfNine and SumOfFive != SumOfSix and SumOfFive != SumOfSeven and SumOfFive != SumOfEight and SumOfFive != SumOfNine and SumOfSix != SumOfSeven and SumOfSix != SumOfEight and SumOfSix != SumOfNine and SumOfSeven != SumOfEight and SumOfSeven != SumOfNine and SumOfEight != SumOfNine:
                print("processing2")
                ThisMakesSureThatAllTheDifferentsNumbersForTwoDigetArentLikeTheExactSame = 1
                if CheckDonCheckTwo != 1:
                    CheckDonCheckTwo = 1
                    check = check + 1
            else:
                ZeroFLocked = 0
                OneFLocked = 0
                TwoFLocked = 0
                ThreeFLocked = 0
                FourFLocked = 0
                FiveFLocked = 0
                SixFLocked = 0
                SevenFLocked = 0
                EightFLocked = 0
                NineFLocked = 0
            #This makes sure all the different possible numbers for the secohnd aren't the same


        #The third diget code for klmno
        if three == 0:
            while ThisIsACounterSoTheCodeWorksbutdifferent20 != 1:
                if ZeroKLocked == 0:
                    k = random.randint(1, 94)
                    l = random.randint(1, 94)
                    m = random.randint(1, 94)
                    n = random.randint(1, 94)
                    o = random.randint(1, 94)
                    ZeroKLocked = k
                    ZeroLLocked = l
                    ZeroMLocked = m
                    ZeroNLocked = n
                    ZeroOLocked = o
                if k == l or k == m or k == n or k == o or l == m or l == n or l == o or m == n or m == o or n == o:
                    ZeroKLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent20 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent20 = 1
        elif three == 1:
            while ThisIsACounterSoTheCodeWorksbutdifferent21 != 1:
                if OneKLocked == 0:
                    k = random.randint(1, 94)
                    l = random.randint(1, 94)
                    m = random.randint(1, 94)
                    n = random.randint(1, 94)
                    o = random.randint(1, 94)
                    OneKLocked = k
                    OneLLocked = l
                    OneMLocked = m
                    OneNLocked = n
                    OneOLocked = o
                if k == l or k == m or k == n or k == o or l == m or l == n or l == o or m == n or m == o or n == o:
                    OneKLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent21 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent21 = 1
        elif three == 2:
            while ThisIsACounterSoTheCodeWorksbutdifferent22 != 1:
                if TwoKLocked == 0:
                    k = random.randint(1, 94)
                    l = random.randint(1, 94)
                    m = random.randint(1, 94)
                    n = random.randint(1, 94)
                    o = random.randint(1, 94)
                    TwoKLocked = k
                    TwoLLocked = l
                    TwoMLocked = m
                    TwoNLocked = n
                    TwoOLocked = o
                if k == l or k == m or k == n or k == o or l == m or l == n or l == o or m == n or m == o or n == o:
                    TwoKLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent22 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent22 = 1
        elif three == 3:
            while ThisIsACounterSoTheCodeWorksbutdifferent23 != 1:
                if ThreeKLocked == 0:
                    k = random.randint(1, 94)
                    l = random.randint(1, 94)
                    m = random.randint(1, 94)
                    n = random.randint(1, 94)
                    o = random.randint(1, 94)
                    ThreeKLocked = k
                    ThreeLLocked = l
                    ThreeMLocked = m
                    ThreeNLocked = n
                    ThreeOLocked = o
                if k == l or k == m or k == n or k == o or l == m or l == n or l == o or m == n or m == o or n == o:
                    ThreeKLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent23 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent23 = 1
        elif three == 4: 
            while ThisIsACounterSoTheCodeWorksbutdifferent24 != 1:
                if FourKLocked == 0:
                    k = random.randint(1, 94)
                    l = random.randint(1, 94)
                    m = random.randint(1, 94)
                    n = random.randint(1, 94)
                    o = random.randint(1, 94)
                    FourKLocked = k
                    FourLLocked = l
                    FourMLocked = m
                    FourNLocked = n
                    FourOLocked = o
                if k == l or k == m or k == n or k == o or l == m or l == n or l == o or m == n or m == o or n == o:
                    FourKLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent24 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent24 = 1
        elif three == 5: 
            while ThisIsACounterSoTheCodeWorksbutdifferent25 != 1:
                if FiveKLocked == 0:
                    k = random.randint(1, 94)
                    l = random.randint(1, 94)
                    m = random.randint(1, 94)
                    n = random.randint(1, 94)
                    o = random.randint(1, 94)
                    FiveKLocked = k
                    FiveLLocked = l
                    FiveMLocked = m
                    FiveNLocked = n
                    FiveOLocked = o
                if k == l or k == m or k == n or k == o or l == m or l == n or l == o or m == n or m == o or n == o:
                    FiveKLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent25 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent25 = 1
        elif three == 6:
            while ThisIsACounterSoTheCodeWorksbutdifferent26 != 1:
                if SixKLocked == 0:
                    k = random.randint(1, 94)
                    l = random.randint(1, 94)
                    m = random.randint(1, 94)
                    n = random.randint(1, 94)
                    o = random.randint(1, 94)
                    SixKLocked = k
                    SixLLocked = l
                    SixMLocked = m
                    SixNLocked = n
                    SixOLocked = o
                if k == l or k == m or k == n or k == o or l == m or l == n or l == o or m == n or m == o or n == o:
                    SixKLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent26 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent26 = 1
        elif three == 7:
            while ThisIsACounterSoTheCodeWorksbutdifferent27 != 1:
                if SevenKLocked == 0:
                    k = random.randint(1, 94)
                    l = random.randint(1, 94)
                    m = random.randint(1, 94)
                    n = random.randint(1, 94)
                    o = random.randint(1, 94)
                    SevenKLocked = k
                    SevenLLocked = l
                    SevenMLocked = m
                    SevenNLocked = n
                    SevenOLocked = o
                if k == l or k == m or k == n or k == o or l == m or l == n or l == o or m == n or m == o or n == o:
                    SevenKLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent27 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent27 = 1
        elif three == 8: 
            while ThisIsACounterSoTheCodeWorksbutdifferent28 != 1:
                if EightKLocked == 0:
                    k = random.randint(1, 94)
                    l = random.randint(1, 94)
                    m = random.randint(1, 94)
                    n = random.randint(1, 94)
                    o = random.randint(1, 94)
                    EightKLocked = k
                    EightLLocked = l
                    EightMLocked = m
                    EightNLocked = n
                    EightOLocked = o
                if k == l or k == m or k == n or k == o or l == m or l == n or l == o or m == n or m == o or n == o:
                    EightKLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent28 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent28 = 1
        elif three == 9: 
            while ThisIsACounterSoTheCodeWorksbutdifferent29 != 1:
                if NineKLocked == 0:
                    k = random.randint(1, 94)
                    l = random.randint(1, 94)
                    m = random.randint(1, 94)
                    n = random.randint(1, 94)
                    o = random.randint(1, 94)
                    NineKLocked = k
                    NineLLocked = l
                    NineMLocked = m
                    NineNLocked = n
                    NineOLocked = o
                if k == l or k == m or k == n or k == o or l == m or l == n or l == o or m == n or m == o or n == o:
                    NineKLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent29 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent29 = 1

        if ZeroKLocked != 0 and OneKLocked != 0 and TwoKLocked != 0 and ThreeKLocked != 0 and FourKLocked != 0 and FiveKLocked != 0 and SixKLocked != 0 and SevenKLocked != 0 and EightKLocked != 0 and NineKLocked != 0:
            SumOfZero = CubicNumberChecker(ZeroKLocked, ZeroLLocked, ZeroMLocked, ZeroNLocked, ZeroOLocked)
            SumOfOne = CubicNumberChecker(OneKLocked, OneLLocked, OneMLocked, OneNLocked, OneOLocked)
            SumOfTwo = CubicNumberChecker(TwoKLocked, TwoLLocked, TwoMLocked, TwoNLocked, TwoOLocked)
            SumOfThree = CubicNumberChecker(ThreeFLocked, ThreeLLocked, ThreeMLocked, ThreeNLocked, ThreeOLocked)
            SumOfFour = CubicNumberChecker(FourKLocked, FourLLocked, FourMLocked, FourNLocked, FourOLocked)
            SumOfFive = CubicNumberChecker(FiveKLocked, FiveLLocked, FiveMLocked, FiveNLocked, FiveOLocked)
            SumOfSix = CubicNumberChecker(SixKLocked, SixLLocked, SixMLocked, SixNLocked, SixOLocked)
            SumOfSeven = CubicNumberChecker(SevenKLocked, SevenLLocked, SevenMLocked, SevenNLocked, SevenOLocked)
            SumOfEight = CubicNumberChecker(EightKLocked, EightLLocked, EightMLocked, EightNLocked, EightOLocked)
            SumOfNine = CubicNumberChecker(NineKLocked, NineLLocked, NineMLocked, NineNLocked, NineOLocked)
            ThreeSumOfZero = SumOfZero
            ThreeSumOfOne = SumOfOne
            ThreeSumOfTwo = SumOfTwo
            ThreeSumOfThree = SumOfThree
            ThreeSumOfFour = SumOfFour
            ThreeSumOfFive = SumOfFive
            ThreeSumOfSix = SumOfSix
            ThreeSumOfSeven = SumOfSeven
            ThreeSumOfEight = SumOfEight
            ThreeSumOfNine = SumOfNine
            if SumOfZero != SumOfOne and SumOfZero != SumOfTwo and SumOfZero != SumOfThree and SumOfZero != SumOfFour and SumOfZero != SumOfFive and SumOfZero != SumOfSix and SumOfZero != SumOfSeven and SumOfZero != SumOfEight and SumOfZero != SumOfNine and SumOfOne != SumOfTwo and SumOfOne != SumOfThree and SumOfOne != SumOfFour and SumOfOne != SumOfFive and SumOfOne != SumOfSix and SumOfOne != SumOfSeven and SumOfOne != SumOfEight and SumOfOne != SumOfNine and SumOfTwo != SumOfThree and SumOfTwo != SumOfFour and SumOfTwo != SumOfFive and SumOfTwo != SumOfSix and SumOfTwo != SumOfSeven and SumOfTwo != SumOfEight and SumOfTwo != SumOfNine and SumOfThree != SumOfFour and SumOfThree != SumOfFive and SumOfThree != SumOfSix and SumOfThree != SumOfSeven and SumOfThree != SumOfEight and SumOfThree != SumOfNine and SumOfFour != SumOfFive and SumOfFour != SumOfSix and SumOfFour != SumOfSeven and SumOfFour != SumOfEight and SumOfFour != SumOfNine and SumOfFive != SumOfSix and SumOfFive != SumOfSeven and SumOfFive != SumOfEight and SumOfFive != SumOfNine and SumOfSix != SumOfSeven and SumOfSix != SumOfEight and SumOfSix != SumOfNine and SumOfSeven != SumOfEight and SumOfSeven != SumOfNine and SumOfEight != SumOfNine:
                print("processing3")
                ThisMakesSureThatAllTheDifferentsNumbersForThreeDigetArentLikeTheExactSame = 1
                if CheckDonCheckThree != 1:
                    CheckDonCheckThree = 1
                    check = check + 1
            else:
                ZeroKLocked = 0
                OneKLocked = 0
                TwoKLocked = 0
                ThreeKLocked = 0
                FourKLocked = 0
                FiveKLocked = 0
                SixKLocked = 0
                SevenKLocked = 0
                EightKLocked = 0
                NineKLocked = 0
            #This makes sure all the different possible numbers for the third aren't the same



        #The forth digit code for pqrst
        if four == 0:
            while ThisIsACounterSoTheCodeWorksbutdifferent30 != 1:
                if ZeroPLocked == 0:
                    p = random.randint(1, 94)
                    q = random.randint(1, 94)
                    r = random.randint(1, 94)
                    s = random.randint(1, 94)
                    t = random.randint(1, 94)
                    ZeroPLocked = p
                    ZeroQLocked = q
                    ZeroRLocked = r
                    ZeroSLocked = s
                    ZeroTLocked = t
                if p == q or p == r or p == s or p == t or q == r or q == s or q == t or r == s or r == t or s == t:
                    ZeroPLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent30 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent30 = 1
        elif four == 1:
            while ThisIsACounterSoTheCodeWorksbutdifferent31 != 1:
                if OnePLocked == 0:
                    p = random.randint(1, 94)
                    q = random.randint(1, 94)
                    r = random.randint(1, 94)
                    s = random.randint(1, 94)
                    t = random.randint(1, 94)
                    OnePLocked = p
                    OneQLocked = q
                    OneRLocked = r
                    OneSLocked = s
                    OneTLocked = t
                if p == q or p == r or p == s or p == t or q == r or q == s or q == t or r == s or r == t or s == t:
                    OnePLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent31 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent31 = 1
        elif four == 2:
            while ThisIsACounterSoTheCodeWorksbutdifferent32 != 1:
                if TwoPLocked == 0:
                    p = random.randint(1, 94)
                    q = random.randint(1, 94)
                    r = random.randint(1, 94)
                    s = random.randint(1, 94)
                    t = random.randint(1, 94)
                    TwoPLocked = p
                    TwoQLocked = q
                    TwoRLocked = r
                    TwoSLocked = s
                    TwoTLocked = t
                if p == q or p == r or p == s or p == t or q == r or q == s or q == t or r == s or r == t or s == t:
                    TwoPLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent32 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent32 = 1
        elif four == 3:
            while ThisIsACounterSoTheCodeWorksbutdifferent33 != 1:
                if ThreePLocked == 0:
                    p = random.randint(1, 94)
                    q = random.randint(1, 94)
                    r = random.randint(1, 94)
                    s = random.randint(1, 94)
                    t = random.randint(1, 94)
                    ThreePLocked = p
                    ThreeQLocked = q
                    ThreeRLocked = r
                    ThreeSLocked = s
                    ThreeTLocked = t
                if p == q or p == r or p == s or p == t or q == r or q == s or q == t or r == s or r == t or s == t:
                    ThreePLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent33 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent33 = 1
        elif four == 4: 
            while ThisIsACounterSoTheCodeWorksbutdifferent34 != 1:
                if FourPLocked == 0:
                    p = random.randint(1, 94)
                    q = random.randint(1, 94)
                    r = random.randint(1, 94)
                    s = random.randint(1, 94)
                    t = random.randint(1, 94)
                    FourPLocked = p
                    FourQLocked = q
                    FourRLocked = r
                    FourSLocked = s
                    FourTLocked = t
                if p == q or p == r or p == s or p == t or q == r or q == s or q == t or r == s or r == t or s == t:
                    FourPLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent34 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent34 = 1
        elif four == 5: 
            while ThisIsACounterSoTheCodeWorksbutdifferent35 != 1:
                if FivePLocked == 0:
                    p = random.randint(1, 94)
                    q = random.randint(1, 94)
                    r = random.randint(1, 94)
                    s = random.randint(1, 94)
                    t = random.randint(1, 94)
                    FivePLocked = p
                    FiveQLocked = q
                    FiveRLocked = r
                    FiveSLocked = s
                    FiveTLocked = t
                if p == q or p == r or p == s or p == t or q == r or q == s or q == t or r == s or r == t or s == t:
                    FivePLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent35 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent35 = 1
        elif four == 6:
            while ThisIsACounterSoTheCodeWorksbutdifferent36 != 1:
                if SixPLocked == 0:
                    p = random.randint(1, 94)
                    q = random.randint(1, 94)
                    r = random.randint(1, 94)
                    s = random.randint(1, 94)
                    t = random.randint(1, 94)
                    SixPLocked = p
                    SixQLocked = q
                    SixRLocked = r
                    SixSLocked = s
                    SixTLocked = t
                if p == q or p == r or p == s or p == t or q == r or q == s or q == t or r == s or r == t or s == t:
                    SixPLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent36 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent36 = 1
        elif four == 7:
            while ThisIsACounterSoTheCodeWorksbutdifferent37 != 1:
                if SevenPLocked == 0:
                    p = random.randint(1, 94)
                    q = random.randint(1, 94)
                    r = random.randint(1, 94)
                    s = random.randint(1, 94)
                    t = random.randint(1, 94)
                    SevenPLocked = p
                    SevenQLocked = q
                    SevenRLocked = r
                    SevenSLocked = s
                    SevenTLocked = t
                if p == q or p == r or p == s or p == t or q == r or q == s or q == t or r == s or r == t or s == t:
                    SevenPLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent37 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent37 = 1
        elif four == 8: 
            while ThisIsACounterSoTheCodeWorksbutdifferent38 != 1:
                if EightPLocked == 0:
                    p = random.randint(1, 94)
                    q = random.randint(1, 94)
                    r = random.randint(1, 94)
                    s = random.randint(1, 94)
                    t = random.randint(1, 94)
                    EightPLocked = p
                    EightQLocked = q
                    EightRLocked = r
                    EightSLocked = s
                    EightTLocked = t
                if p == q or p == r or p == s or p == t or q == r or q == s or q == t or r == s or r == t or s == t:
                    EightPLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent38 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent38 = 1
        elif four == 9: 
            while ThisIsACounterSoTheCodeWorksbutdifferent39 != 1:
                if NinePLocked == 0:
                    p = random.randint(1, 94)
                    q = random.randint(1, 94)
                    r = random.randint(1, 94)
                    s = random.randint(1, 94)
                    t = random.randint(1, 94)
                    NinePLocked = p
                    NineQLocked = q
                    NineRLocked = r
                    NineSLocked = s
                    NineTLocked = t
                if p == q or p == r or p == s or p == t or q == r or q == s or q == t or r == s or r == t or s == t:
                    NinePLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent39 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent39 = 1

        if ZeroPLocked != 0 and OnePLocked != 0 and TwoPLocked != 0 and ThreePLocked != 0 and FourPLocked != 0 and FivePLocked != 0 and SixPLocked != 0 and SevenPLocked != 0 and EightPLocked != 0 and NinePLocked != 0:
            SumOfZero = CubicNumberChecker(ZeroPLocked, ZeroQLocked, ZeroRLocked, ZeroSLocked, ZeroTLocked)
            SumOfOne = CubicNumberChecker(OnePLocked, OneQLocked, OneRLocked, OneSLocked, OneTLocked)
            SumOfTwo = CubicNumberChecker(TwoPLocked, TwoQLocked, TwoRLocked, TwoSLocked, TwoTLocked)
            SumOfThree = CubicNumberChecker(ThreePLocked, ThreeQLocked, ThreeRLocked, ThreeSLocked, ThreeTLocked)
            SumOfFour = CubicNumberChecker(FourPLocked, FourQLocked, FourRLocked, FourSLocked, FourTLocked)
            SumOfFive = CubicNumberChecker(FivePLocked, FiveQLocked, FiveRLocked, FiveSLocked, FiveTLocked)
            SumOfSix = CubicNumberChecker(SixPLocked, SixQLocked, SixRLocked, SixSLocked, SixTLocked)
            SumOfSeven = CubicNumberChecker(SevenPLocked, SevenQLocked, SevenRLocked, SevenSLocked, SevenTLocked)
            SumOfEight = CubicNumberChecker(EightPLocked, EightQLocked, EightRLocked, EightSLocked, EightTLocked)
            SumOfNine = CubicNumberChecker(NinePLocked, NineQLocked, NineRLocked, NineSLocked, NineTLocked)
            FourSumOfZero = SumOfZero
            FourSumOfOne = SumOfOne
            FourSumOfTwo = SumOfTwo
            FourSumOfThree = SumOfThree
            FourSumOfFour = SumOfFour
            FourSumOfFive = SumOfFive
            FourSumOfSix = SumOfSix
            FourSumOfSeven = SumOfSeven
            FourSumOfEight = SumOfEight
            FourSumOfNine = SumOfNine
            if SumOfZero != SumOfOne and SumOfZero != SumOfTwo and SumOfZero != SumOfThree and SumOfZero != SumOfFour and SumOfZero != SumOfFive and SumOfZero != SumOfSix and SumOfZero != SumOfSeven and SumOfZero != SumOfEight and SumOfZero != SumOfNine and SumOfOne != SumOfTwo and SumOfOne != SumOfThree and SumOfOne != SumOfFour and SumOfOne != SumOfFive and SumOfOne != SumOfSix and SumOfOne != SumOfSeven and SumOfOne != SumOfEight and SumOfOne != SumOfNine and SumOfTwo != SumOfThree and SumOfTwo != SumOfFour and SumOfTwo != SumOfFive and SumOfTwo != SumOfSix and SumOfTwo != SumOfSeven and SumOfTwo != SumOfEight and SumOfTwo != SumOfNine and SumOfThree != SumOfFour and SumOfThree != SumOfFive and SumOfThree != SumOfSix and SumOfThree != SumOfSeven and SumOfThree != SumOfEight and SumOfThree != SumOfNine and SumOfFour != SumOfFive and SumOfFour != SumOfSix and SumOfFour != SumOfSeven and SumOfFour != SumOfEight and SumOfFour != SumOfNine and SumOfFive != SumOfSix and SumOfFive != SumOfSeven and SumOfFive != SumOfEight and SumOfFive != SumOfNine and SumOfSix != SumOfSeven and SumOfSix != SumOfEight and SumOfSix != SumOfNine and SumOfSeven != SumOfEight and SumOfSeven != SumOfNine and SumOfEight != SumOfNine:
                print("processing4")
                ThisMakesSureThatAllTheDifferentsNumbersForFourDigetArentLikeTheExactSame = 1
                if CheckDonCheckFour != 1:
                    CheckDonCheckFour = 1
                    check = check + 1
            else:
                ZeroPLocked = 0
                OnePLocked = 0
                TwoPLocked = 0
                ThreePLocked = 0
                FourPLocked = 0
                FivePLocked = 0
                SixPLocked = 0
                SevenPLocked = 0
                EightPLocked = 0
                NinePLocked = 0
            #This makes sure all the different possible numbers for the fourth aren't the same



        #The fifth digit code for uvwxy
        if five == 0:
            while ThisIsACounterSoTheCodeWorksbutdifferent40 != 1:
                if ZeroULocked == 0:
                    u = random.randint(1, 94)
                    v = random.randint(1, 94)
                    w = random.randint(1, 94)
                    x = random.randint(1, 94)
                    y = random.randint(1, 94)
                    ZeroULocked = u
                    ZeroVLocked = v
                    ZeroWLocked = w
                    ZeroXLocked = x
                    ZeroYLocked = y
                if u == v or u == w or u == x or u == y or v == w or v == x or v == y or w == x or w == y or x == y:
                    ZeroULocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent40 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent40 = 1
        elif five == 1:
            while ThisIsACounterSoTheCodeWorksbutdifferent41 != 1:
                if OneULocked == 0:
                    u = random.randint(1, 94)
                    v = random.randint(1, 94)
                    w = random.randint(1, 94)
                    x = random.randint(1, 94)
                    y = random.randint(1, 94)
                    OneULocked = u
                    OneVLocked = v
                    OneWLocked = w
                    OneXLocked = x
                    OneYLocked = y
                if u == v or u == w or u == x or u == y or v == w or v == x or v == y or w == x or w == y or x == y:
                    OneULocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent41 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent41 = 1
        elif five == 2:
            while ThisIsACounterSoTheCodeWorksbutdifferent42 != 1:
                if TwoULocked == 0:
                    u = random.randint(1, 94)
                    v = random.randint(1, 94)
                    w = random.randint(1, 94)
                    x = random.randint(1, 94)
                    y = random.randint(1, 94)
                    TwoULocked = u
                    TwoVLocked = v
                    TwoWLocked = w
                    TwoXLocked = x
                    TwoYLocked = y
                if u == v or u == w or u == x or u == y or v == w or v == x or v == y or w == x or w == y or x == y:
                    TwoULocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent42 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent42 = 1
        elif five == 3:
            while ThisIsACounterSoTheCodeWorksbutdifferent43 != 1:
                if ThreeULocked == 0:
                    u = random.randint(1, 94)
                    v = random.randint(1, 94)
                    w = random.randint(1, 94)
                    x = random.randint(1, 94)
                    y = random.randint(1, 94)
                    ThreeULocked = u
                    ThreeVLocked = v
                    ThreeWLocked = w
                    ThreeXLocked = x
                    ThreeYLocked = y
                if u == v or u == w or u == x or u == y or v == w or v == x or v == y or w == x or w == y or x == y:
                    ThreeULocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent43 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent43 = 1
        elif five == 4: 
            while ThisIsACounterSoTheCodeWorksbutdifferent44 != 1:
                if FourULocked == 0:
                    u = random.randint(1, 94)
                    v = random.randint(1, 94)
                    w = random.randint(1, 94)
                    x = random.randint(1, 94)
                    y = random.randint(1, 94)
                    FourULocked = u
                    FourVLocked = v
                    FourWLocked = w
                    FourXLocked = x
                    FourYLocked = y
                if u == v or u == w or u == x or u == y or v == w or v == x or v == y or w == x or w == y or x == y:
                    FourULocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent44 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent44 = 1
        elif five == 5: 
            while ThisIsACounterSoTheCodeWorksbutdifferent45 != 1:
                if FiveULocked == 0:
                    u = random.randint(1, 94)
                    v = random.randint(1, 94)
                    w = random.randint(1, 94)
                    x = random.randint(1, 94)
                    y = random.randint(1, 94)
                    FiveULocked = u
                    FiveVLocked = v
                    FiveWLocked = w
                    FiveXLocked = x
                    FiveYLocked = y
                if u == v or u == w or u == x or u == y or v == w or v == x or v == y or w == x or w == y or x == y:
                    FiveULocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent45 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent45 = 1
        elif five == 6:
            while ThisIsACounterSoTheCodeWorksbutdifferent46 != 1:
                if SixULocked == 0:
                    u = random.randint(1, 94)
                    v = random.randint(1, 94)
                    w = random.randint(1, 94)
                    x = random.randint(1, 94)
                    y = random.randint(1, 94)
                    SixULocked = u
                    SixVLocked = v
                    SixWLocked = w
                    SixXLocked = x
                    SixYLocked = y
                if u == v or u == w or u == x or u == y or v == w or v == x or v == y or w == x or w == y or x == y:
                    SixULocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent46 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent46 = 1
        elif five == 7:
            while ThisIsACounterSoTheCodeWorksbutdifferent47 != 1:
                if SevenULocked == 0:
                    u = random.randint(1, 94)
                    v = random.randint(1, 94)
                    w = random.randint(1, 94)
                    x = random.randint(1, 94)
                    y = random.randint(1, 94)
                    SevenULocked = u
                    SevenVLocked = v
                    SevenWLocked = w
                    SevenXLocked = x
                    SevenYLocked = y
                if u == v or u == w or u == x or u == y or v == w or v == x or v == y or w == x or w == y or x == y:
                    SevenULocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent47 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent47 = 1
        elif five == 8: 
            while ThisIsACounterSoTheCodeWorksbutdifferent48 != 1:
                if EightULocked == 0:
                    u = random.randint(1, 94)
                    v = random.randint(1, 94)
                    w = random.randint(1, 94)
                    x = random.randint(1, 94)
                    y = random.randint(1, 94)
                    EightULocked = u
                    EightVLocked = v
                    EightWLocked = w
                    EightXLocked = x
                    EightYLocked = y
                if u == v or u == w or u == x or u == y or v == w or v == x or v == y or w == x or w == y or x == y:
                    EightULocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent48 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent48 = 1
        elif five == 9: 
            while ThisIsACounterSoTheCodeWorksbutdifferent49 != 1:
                if NineULocked == 0:
                    u = random.randint(1, 94)
                    v = random.randint(1, 94)
                    w = random.randint(1, 94)
                    x = random.randint(1, 94)
                    y = random.randint(1, 94)
                    NineULocked = u
                    NineVLocked = v
                    NineWLocked = w
                    NineXLocked = x
                    NineYLocked = y
                if u == v or u == w or u == x or u == y or v == w or v == x or v == y or w == x or w == y or x == y:
                    NineULocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent49 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent49 = 1

        if ZeroULocked != 0 and OneULocked != 0 and TwoULocked != 0 and ThreeULocked != 0 and FourULocked != 0 and FiveULocked != 0 and SixULocked != 0 and SevenULocked != 0 and EightULocked != 0 and NineULocked != 0:
            SumOfZero = CubicNumberChecker(ZeroULocked, ZeroVLocked, ZeroWLocked, ZeroXLocked, ZeroYLocked)
            SumOfOne = CubicNumberChecker(OneULocked, OneVLocked, OneWLocked, OneXLocked, OneYLocked)
            SumOfTwo = CubicNumberChecker(TwoULocked, TwoVLocked, TwoWLocked, TwoXLocked, TwoYLocked)
            SumOfThree = CubicNumberChecker(ThreeULocked, ThreeVLocked, ThreeWLocked, ThreeXLocked, ThreeYLocked)
            SumOfFour = CubicNumberChecker(FourULocked, FourVLocked, FourWLocked, FourXLocked, FourYLocked)
            SumOfFive = CubicNumberChecker(FiveULocked, FiveVLocked, FiveWLocked, FiveXLocked, FiveYLocked)
            SumOfSix = CubicNumberChecker(SixULocked, SixVLocked, SixWLocked, SixXLocked, SixYLocked)
            SumOfSeven = CubicNumberChecker(SevenULocked, SevenVLocked, SevenWLocked, SevenXLocked, SevenYLocked)
            SumOfEight = CubicNumberChecker(EightULocked, EightVLocked, EightWLocked, EightXLocked, EightYLocked)
            SumOfNine = CubicNumberChecker(NineULocked, NineVLocked, NineWLocked, NineXLocked, NineYLocked)
            FiveSumOfZero = SumOfZero
            FiveSumOfOne = SumOfOne
            FiveSumOfTwo = SumOfTwo
            FiveSumOfThree = SumOfThree
            FiveSumOfFour = SumOfFour
            FiveSumOfFive = SumOfFive
            FiveSumOfSix = SumOfSix
            FiveSumOfSeven = SumOfSeven
            FiveSumOfEight = SumOfEight
            FiveSumOfNine = SumOfNine
            if SumOfZero != SumOfOne and SumOfZero != SumOfTwo and SumOfZero != SumOfThree and SumOfZero != SumOfFour and SumOfZero != SumOfFive and SumOfZero != SumOfSix and SumOfZero != SumOfSeven and SumOfZero != SumOfEight and SumOfZero != SumOfNine and SumOfOne != SumOfTwo and SumOfOne != SumOfThree and SumOfOne != SumOfFour and SumOfOne != SumOfFive and SumOfOne != SumOfSix and SumOfOne != SumOfSeven and SumOfOne != SumOfEight and SumOfOne != SumOfNine and SumOfTwo != SumOfThree and SumOfTwo != SumOfFour and SumOfTwo != SumOfFive and SumOfTwo != SumOfSix and SumOfTwo != SumOfSeven and SumOfTwo != SumOfEight and SumOfTwo != SumOfNine and SumOfThree != SumOfFour and SumOfThree != SumOfFive and SumOfThree != SumOfSix and SumOfThree != SumOfSeven and SumOfThree != SumOfEight and SumOfThree != SumOfNine and SumOfFour != SumOfFive and SumOfFour != SumOfSix and SumOfFour != SumOfSeven and SumOfFour != SumOfEight and SumOfFour != SumOfNine and SumOfFive != SumOfSix and SumOfFive != SumOfSeven and SumOfFive != SumOfEight and SumOfFive != SumOfNine and SumOfSix != SumOfSeven and SumOfSix != SumOfEight and SumOfSix != SumOfNine and SumOfSeven != SumOfEight and SumOfSeven != SumOfNine and SumOfEight != SumOfNine:
                print("processing5")
                ThisMakesSureThatAllTheDifferentsNumbersForFiveDigetArentLikeTheExactSame = 1
                if CheckDonCheckFive != 1:
                    CheckDonCheckFive = 1
                    check = check + 1
            else:
                ZeroULocked = 0
                OneULocked = 0
                TwoULocked = 0
                ThreeULocked = 0
                FourULocked = 0
                FiveULocked = 0
                SixULocked = 0
                SevenULocked = 0
                EightULocked = 0
                NineULocked = 0
            #This makes sure all the different possible numbers for the fith aren't the same



        #TheSixth digit code for z.,?!
        if six == 0:
            while ThisIsACounterSoTheCodeWorksbutdifferent50 != 1:
                if ZeroZLocked == 0:
                    z = random.randint(1, 94)
                    fullstop = random.randint(1, 94)
                    comma = random.randint(1, 94)
                    questionMark = random.randint(1, 94)
                    exclimationPoint = random.randint(1, 94)
                    ZeroZLocked = z
                    ZeroFullstopLocked = fullstop
                    ZeroCommaLocked = comma
                    ZeroQuestionMarkLocked = questionMark
                    ZeroExclimationPointLocked = exclimationPoint
                if z == fullstop or z == comma or z == questionMark or z == exclimationPoint or fullstop == comma or fullstop == questionMark or fullstop == exclimationPoint or comma == questionMark or comma == exclimationPoint or questionMark == exclimationPoint:
                    ZeroZLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent50 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent50 = 1
        elif six == 1:
            while ThisIsACounterSoTheCodeWorksbutdifferent51 != 1:
                if OneZLocked == 0:
                    z = random.randint(1, 94)
                    fullstop = random.randint(1, 94)
                    comma = random.randint(1, 94)
                    questionMark = random.randint(1, 94)
                    exclimationPoint = random.randint(1, 94)
                    OneZLocked = z
                    OneFullstopLocked = fullstop
                    OneCommaLocked = comma
                    OneQuestionMarkLocked = questionMark
                    OneExclimationPointLocked = exclimationPoint
                if z == fullstop or z == comma or z == questionMark or z == exclimationPoint or fullstop == comma or fullstop == questionMark or fullstop == exclimationPoint or comma == questionMark or comma == exclimationPoint or questionMark == exclimationPoint:
                    OneZLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent51 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent51 = 1
        elif six == 2:
            while ThisIsACounterSoTheCodeWorksbutdifferent52 != 1:
                if TwoZLocked == 0:
                    z = random.randint(1, 94)
                    fullstop = random.randint(1, 94)
                    comma = random.randint(1, 94)
                    questionMark = random.randint(1, 94)
                    exclimationPoint = random.randint(1, 94)
                    TwoZLocked = z
                    TwoFullstopLocked = fullstop
                    TwoCommaLocked = comma
                    TwoQuestionMarkLocked = questionMark
                    TwoExclimationPointLocked = exclimationPoint
                if z == fullstop or z == comma or z == questionMark or z == exclimationPoint or fullstop == comma or fullstop == questionMark or fullstop == exclimationPoint or comma == questionMark or comma == exclimationPoint or questionMark == exclimationPoint:
                    TwoZLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent52 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent52 = 1
        elif six == 3:
            while ThisIsACounterSoTheCodeWorksbutdifferent53 != 1:
                if ThreeZLocked == 0:
                    z = random.randint(1, 94)
                    fullstop = random.randint(1, 94)
                    comma = random.randint(1, 94)
                    questionMark = random.randint(1, 94)
                    exclimationPoint = random.randint(1, 94)
                    ThreeZLocked = z
                    ThreeFullstopLocked = fullstop
                    ThreeCommaLocked = comma
                    ThreeQuestionMarkLocked = questionMark
                    ThreeExclimationPointLocked = exclimationPoint
                if z == fullstop or z == comma or z == questionMark or z == exclimationPoint or fullstop == comma or fullstop == questionMark or fullstop == exclimationPoint or comma == questionMark or comma == exclimationPoint or questionMark == exclimationPoint:
                    ThreeZLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent53 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent53 = 1
        elif six == 4: 
            while ThisIsACounterSoTheCodeWorksbutdifferent54 != 1:
                if FourZLocked == 0:
                    z = random.randint(1, 94)
                    fullstop = random.randint(1, 94)
                    comma = random.randint(1, 94)
                    questionMark = random.randint(1, 94)
                    exclimationPoint = random.randint(1, 94)
                    FourZLocked = z
                    FourFullstopLocked = fullstop
                    FourCommaLocked = comma
                    FourQuestionMarkLocked = questionMark
                    FourExclimationPointLocked = exclimationPoint
                if z == fullstop or z == comma or z == questionMark or z == exclimationPoint or fullstop == comma or fullstop == questionMark or fullstop == exclimationPoint or comma == questionMark or comma == exclimationPoint or questionMark == exclimationPoint:
                    FourZLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent54 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent54 = 1
        elif six == 5: 
            while ThisIsACounterSoTheCodeWorksbutdifferent55 != 1:
                if FiveZLocked == 0:
                    z = random.randint(1, 94)
                    fullstop = random.randint(1, 94)
                    comma = random.randint(1, 94)
                    questionMark = random.randint(1, 94)
                    exclimationPoint = random.randint(1, 94)
                    FiveZLocked = z
                    FiveFullstopLocked = fullstop
                    FiveCommaLocked = comma
                    FiveQuestionMarkLocked = questionMark
                    FiveExclimationPointLocked = exclimationPoint
                if z == fullstop or z == comma or z == questionMark or z == exclimationPoint or fullstop == comma or fullstop == questionMark or fullstop == exclimationPoint or comma == questionMark or comma == exclimationPoint or questionMark == exclimationPoint:
                    FiveZLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent55 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent55 = 1
        elif six == 6:
            while ThisIsACounterSoTheCodeWorksbutdifferent56 != 1:
                if SixZLocked == 0:
                    z = random.randint(1, 94)
                    fullstop = random.randint(1, 94)
                    comma = random.randint(1, 94)
                    questionMark = random.randint(1, 94)
                    exclimationPoint = random.randint(1, 94)
                    SixZLocked = z
                    SixFullstopLocked = fullstop
                    SixCommaLocked = comma
                    SixQuestionMarkLocked = questionMark
                    SixExclimationPointLocked = exclimationPoint
                if z == fullstop or z == comma or z == questionMark or z == exclimationPoint or fullstop == comma or fullstop == questionMark or fullstop == exclimationPoint or comma == questionMark or comma == exclimationPoint or questionMark == exclimationPoint:
                    SixZLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent56 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent56 = 1
        elif six == 7:
            while ThisIsACounterSoTheCodeWorksbutdifferent57 != 1:
                if SevenZLocked == 0:
                    z = random.randint(1, 94)
                    fullstop = random.randint(1, 94)
                    comma = random.randint(1, 94)
                    questionMark = random.randint(1, 94)
                    exclimationPoint = random.randint(1, 94)
                    SevenZLocked = z
                    SevenFullstopLocked = fullstop
                    SevenCommaLocked = comma
                    SevenQuestionMarkLocked = questionMark
                    SevenExclimationPointLocked = exclimationPoint
                if z == fullstop or z == comma or z == questionMark or z == exclimationPoint or fullstop == comma or fullstop == questionMark or fullstop == exclimationPoint or comma == questionMark or comma == exclimationPoint or questionMark == exclimationPoint:
                    SevenZLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent57 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent57 = 1
        elif six == 8: 
            while ThisIsACounterSoTheCodeWorksbutdifferent58 != 1:
                if EightZLocked == 0:
                    z = random.randint(1, 94)
                    fullstop = random.randint(1, 94)
                    comma = random.randint(1, 94)
                    questionMark = random.randint(1, 94)
                    exclimationPoint = random.randint(1, 94)
                    EightZLocked = z
                    EightFullstopLocked = fullstop
                    EightCommaLocked = comma
                    EightQuestionMarkLocked = questionMark
                    EightExclimationPointLocked = exclimationPoint
                if z == fullstop or z == comma or z == questionMark or z == exclimationPoint or fullstop == comma or fullstop == questionMark or fullstop == exclimationPoint or comma == questionMark or comma == exclimationPoint or questionMark == exclimationPoint:
                    EightZLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent58 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent58 = 1
        elif six == 9: 
            while ThisIsACounterSoTheCodeWorksbutdifferent59 != 1:
                if NineZLocked == 0:
                    z = random.randint(1, 94)
                    fullstop = random.randint(1, 94)
                    comma = random.randint(1, 94)
                    questionMark = random.randint(1, 94)
                    exclimationPoint = random.randint(1, 94)
                    NineZLocked = z
                    NineFullstopLocked = fullstop
                    NineCommaLocked = comma
                    NineQuestionMarkLocked = questionMark
                    NineExclimationPointLocked = exclimationPoint
                if z == fullstop or z == comma or z == questionMark or z == exclimationPoint or fullstop == comma or fullstop == questionMark or fullstop == exclimationPoint or comma == questionMark or comma == exclimationPoint or questionMark == exclimationPoint:
                    NineZLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent59 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent59 = 1

        if ZeroZLocked != 0 and OneZLocked != 0 and TwoZLocked != 0 and ThreeZLocked != 0 and FourZLocked != 0 and FiveZLocked != 0 and SixZLocked != 0 and SevenZLocked != 0 and EightZLocked != 0 and NineZLocked != 0:
            SumOfZero = CubicNumberChecker(ZeroZLocked, ZeroFullstopLocked, ZeroCommaLocked, ZeroQuestionMarkLocked, ZeroExclimationPointLocked)
            SumOfOne = CubicNumberChecker(OneZLocked, OneFullstopLocked, OneCommaLocked, OneQuestionMarkLocked, OneExclimationPointLocked)
            SumOfTwo = CubicNumberChecker(TwoZLocked, TwoFullstopLocked, TwoCommaLocked, TwoQuestionMarkLocked, TwoExclimationPointLocked)
            SumOfThree = CubicNumberChecker(ThreeZLocked, ThreeFullstopLocked, ThreeCommaLocked, ThreeQuestionMarkLocked, ThreeExclimationPointLocked)
            SumOfFour = CubicNumberChecker(FourZLocked, FourFullstopLocked, FourCommaLocked, FourQuestionMarkLocked, FourExclimationPointLocked)
            SumOfFive = CubicNumberChecker(FiveZLocked, FiveFullstopLocked, FiveCommaLocked, FiveQuestionMarkLocked, FiveExclimationPointLocked)
            SumOfSix = CubicNumberChecker(SixZLocked, SixFullstopLocked, SixCommaLocked, SixQuestionMarkLocked, SixExclimationPointLocked)
            SumOfSeven = CubicNumberChecker(SevenZLocked, SevenFullstopLocked, SevenCommaLocked, SevenQuestionMarkLocked, SevenExclimationPointLocked)
            SumOfEight = CubicNumberChecker(EightZLocked, EightFullstopLocked, EightCommaLocked, EightQuestionMarkLocked, EightExclimationPointLocked)
            SumOfNine = CubicNumberChecker(NineZLocked, NineFullstopLocked, NineCommaLocked, NineQuestionMarkLocked, NineExclimationPointLocked)
            SixSumOfZero = SumOfZero
            SixSumOfOne = SumOfOne
            SixSumOfTwo = SumOfTwo
            SixSumOfThree = SumOfThree
            SixSumOfFour = SumOfFour
            SixSumOfFive = SumOfFive
            SixSumOfSix = SumOfSix
            SixSumOfSeven = SumOfSeven
            SixSumOfEight = SumOfEight
            SixSumOfNine = SumOfNine
            if SumOfZero != SumOfOne and SumOfZero != SumOfTwo and SumOfZero != SumOfThree and SumOfZero != SumOfFour and SumOfZero != SumOfFive and SumOfZero != SumOfSix and SumOfZero != SumOfSeven and SumOfZero != SumOfEight and SumOfZero != SumOfNine and SumOfOne != SumOfTwo and SumOfOne != SumOfThree and SumOfOne != SumOfFour and SumOfOne != SumOfFive and SumOfOne != SumOfSix and SumOfOne != SumOfSeven and SumOfOne != SumOfEight and SumOfOne != SumOfNine and SumOfTwo != SumOfThree and SumOfTwo != SumOfFour and SumOfTwo != SumOfFive and SumOfTwo != SumOfSix and SumOfTwo != SumOfSeven and SumOfTwo != SumOfEight and SumOfTwo != SumOfNine and SumOfThree != SumOfFour and SumOfThree != SumOfFive and SumOfThree != SumOfSix and SumOfThree != SumOfSeven and SumOfThree != SumOfEight and SumOfThree != SumOfNine and SumOfFour != SumOfFive and SumOfFour != SumOfSix and SumOfFour != SumOfSeven and SumOfFour != SumOfEight and SumOfFour != SumOfNine and SumOfFive != SumOfSix and SumOfFive != SumOfSeven and SumOfFive != SumOfEight and SumOfFive != SumOfNine and SumOfSix != SumOfSeven and SumOfSix != SumOfEight and SumOfSix != SumOfNine and SumOfSeven != SumOfEight and SumOfSeven != SumOfNine and SumOfEight != SumOfNine:
                print("processing6")
                ThisMakesSureThatAllTheDifferentsNumbersForSixDigetArentLikeTheExactSame = 1
                if CheckDonCheckSix != 1:
                    CheckDonCheckSix = 1
                    check = check + 1
            else:
                ZeroZLocked = 0
                OneZLocked = 0
                TwoZLocked = 0
                ThreeZLocked = 0
                FourZLocked = 0
                FiveZLocked = 0
                SixZLocked = 0
                SevenZLocked = 0
                EightZLocked = 0
                NineZLocked = 0
                #This makes sure all the different possible numbers for the sixth aren't the same




        #The seventh digit code for "';: 
        if seven == 0:
            while ThisIsACounterSoTheCodeWorksbutdifferent60 != 1:
                if ZeroQuoteLocked == 0:
                    quote = random.randint(1, 94)
                    aphostrophe = random.randint(1, 94)
                    semicolon = random.randint(1, 94)
                    colon = random.randint(1, 94)
                    space = random.randint(1, 94)
                    ZeroQuoteLocked = quote
                    ZeroAphostropheLocked = aphostrophe
                    ZeroSemicolonLocked = semicolon
                    ZeroColonLocked = colon
                    ZeroSpaceLocked = space
                if quote == aphostrophe or quote == semicolon or quote == colon or quote == space or aphostrophe == semicolon or aphostrophe == colon or aphostrophe == space or semicolon == colon or semicolon == space or colon == space:
                    ZeroQuoteLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent60 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent60 = 1
        elif seven == 1:
            while ThisIsACounterSoTheCodeWorksbutdifferent61 != 1:
                if OneQuoteLocked == 0:
                    quote = random.randint(1, 94)
                    aphostrophe = random.randint(1, 94)
                    semicolon = random.randint(1, 94)
                    colon = random.randint(1, 94)
                    space = random.randint(1, 94)
                    OneQuoteLocked = quote
                    OneAphostropheLocked = aphostrophe
                    OneSemicolonLocked = semicolon
                    OneColonLocked = colon
                    OneSpaceLocked = space
                if quote == aphostrophe or quote == semicolon or quote == colon or quote == space or aphostrophe == semicolon or aphostrophe == colon or aphostrophe == space or semicolon == colon or semicolon == space or colon == space:
                    OneQuoteLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent61 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent61 = 1
        elif seven == 2:
            while ThisIsACounterSoTheCodeWorksbutdifferent62 != 1:
                if TwoQuoteLocked == 0:
                    quote = random.randint(1, 94)
                    aphostrophe = random.randint(1, 94)
                    semicolon = random.randint(1, 94)
                    colon = random.randint(1, 94)
                    space = random.randint(1, 94)
                    TwoQuoteLocked = quote
                    TwoAphostropheLocked = aphostrophe
                    TwoSemicolonLocked = semicolon
                    TwoColonLocked = colon
                    TwoSpaceLocked = space
                if quote == aphostrophe or quote == semicolon or quote == colon or quote == space or aphostrophe == semicolon or aphostrophe == colon or aphostrophe == space or semicolon == colon or semicolon == space or colon == space:
                    TwoQuoteLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent62 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent62 = 1
        elif seven == 3:
            while ThisIsACounterSoTheCodeWorksbutdifferent63 != 1:
                if ThreeQuoteLocked == 0:
                    quote = random.randint(1, 94)
                    aphostrophe = random.randint(1, 94)
                    semicolon = random.randint(1, 94)
                    colon = random.randint(1, 94)
                    space = random.randint(1, 94)
                    ThreeQuoteLocked = quote
                    ThreeAphostropheLocked = aphostrophe
                    ThreeSemicolonLocked = semicolon
                    ThreeColonLocked = colon
                    ThreeSpaceLocked = space
                if quote == aphostrophe or quote == semicolon or quote == colon or quote == space or aphostrophe == semicolon or aphostrophe == colon or aphostrophe == space or semicolon == colon or semicolon == space or colon == space:
                    ThreeQuoteLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent63 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent63 = 1
        elif seven == 4: 
            while ThisIsACounterSoTheCodeWorksbutdifferent64 != 1:
                if FourQuoteLocked == 0:
                    quote = random.randint(1, 94)
                    aphostrophe = random.randint(1, 94)
                    semicolon = random.randint(1, 94)
                    colon = random.randint(1, 94)
                    space = random.randint(1, 94)
                    FourQuoteLocked = quote
                    FourAphostropheLocked = aphostrophe
                    FourSemicolonLocked = semicolon
                    FourColonLocked = colon
                    FourSpaceLocked = space
                if quote == aphostrophe or quote == semicolon or quote == colon or quote == space or aphostrophe == semicolon or aphostrophe == colon or aphostrophe == space or semicolon == colon or semicolon == space or colon == space:
                    FourQuoteLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent64 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent64 = 1
        elif seven == 5: 
            while ThisIsACounterSoTheCodeWorksbutdifferent65 != 1:
                if FiveQuoteLocked == 0:
                    quote = random.randint(1, 94)
                    aphostrophe = random.randint(1, 94)
                    semicolon = random.randint(1, 94)
                    colon = random.randint(1, 94)
                    space = random.randint(1, 94)
                    FiveQuoteLocked = quote
                    FiveAphostropheLocked = aphostrophe
                    FiveSemicolonLocked = semicolon
                    FiveColonLocked = colon
                    FiveSpaceLocked = space
                if quote == aphostrophe or quote == semicolon or quote == colon or quote == space or aphostrophe == semicolon or aphostrophe == colon or aphostrophe == space or semicolon == colon or semicolon == space or colon == space:
                    FiveQuoteLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent65 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent65 = 1
        elif seven == 6:
            while ThisIsACounterSoTheCodeWorksbutdifferent66 != 1:
                if SixQuoteLocked == 0:
                    quote = random.randint(1, 94)
                    aphostrophe = random.randint(1, 94)
                    semicolon = random.randint(1, 94)
                    colon = random.randint(1, 94)
                    space = random.randint(1, 94)
                    SixQuoteLocked = quote
                    SixAphostropheLocked = aphostrophe
                    SixSemicolonLocked = semicolon
                    SixColonLocked = colon
                    SixSpaceLocked = space
                if quote == aphostrophe or quote == semicolon or quote == colon or quote == space or aphostrophe == semicolon or aphostrophe == colon or aphostrophe == space or semicolon == colon or semicolon == space or colon == space:
                    SixQuoteLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent66 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent66 = 1
        elif seven == 7:
            while ThisIsACounterSoTheCodeWorksbutdifferent67 != 1:
                if SevenQuoteLocked == 0:
                    quote = random.randint(1, 94)
                    aphostrophe = random.randint(1, 94)
                    semicolon = random.randint(1, 94)
                    colon = random.randint(1, 94)
                    space = random.randint(1, 94)
                    SevenQuoteLocked = quote
                    SevenAphostropheLocked = aphostrophe
                    SevenSemicolonLocked = semicolon
                    SevenColonLocked = colon
                    SevenSpaceLocked = space
                if quote == aphostrophe or quote == semicolon or quote == colon or quote == space or aphostrophe == semicolon or aphostrophe == colon or aphostrophe == space or semicolon == colon or semicolon == space or colon == space:
                    SevenQuoteLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent67 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent67 = 1
        elif seven == 8: 
            while ThisIsACounterSoTheCodeWorksbutdifferent68 != 1:
                if EightQuoteLocked == 0:
                    quote = random.randint(1, 94)
                    aphostrophe = random.randint(1, 94)
                    semicolon = random.randint(1, 94)
                    colon = random.randint(1, 94)
                    space = random.randint(1, 94)
                    EightQuoteLocked = quote
                    EightAphostropheLocked = aphostrophe
                    EightSemicolonLocked = semicolon
                    EightColonLocked = colon
                    EightSpaceLocked = space
                if quote == aphostrophe or quote == semicolon or quote == colon or quote == space or aphostrophe == semicolon or aphostrophe == colon or aphostrophe == space or semicolon == colon or semicolon == space or colon == space:
                    EightQuoteLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent68 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent68 = 1
        elif seven == 9: 
            while ThisIsACounterSoTheCodeWorksbutdifferent69 != 1:
                if NineQuoteLocked == 0:
                    quote = random.randint(1, 94)
                    aphostrophe = random.randint(1, 94)
                    semicolon = random.randint(1, 94)
                    colon = random.randint(1, 94)
                    space = random.randint(1, 94)
                    NineQuoteLocked = quote
                    NineAphostropheLocked = aphostrophe
                    NineSemicolonLocked = semicolon
                    NineColonLocked = colon
                    NineSpaceLocked = space
                if quote == aphostrophe or quote == semicolon or quote == colon or quote == space or aphostrophe == semicolon or aphostrophe == colon or aphostrophe == space or semicolon == colon or semicolon == space or colon == space:
                    NineQuoteLocked = 0
                    ThisIsACounterSoTheCodeWorksbutdifferent69 = 0
                else:
                    ThisIsACounterSoTheCodeWorksbutdifferent69 = 1

        if ZeroQuoteLocked != 0 and OneQuoteLocked != 0 and TwoQuoteLocked != 0 and ThreeQuoteLocked != 0 and FourQuoteLocked != 0 and FiveQuoteLocked != 0 and SixQuoteLocked != 0 and SevenQuoteLocked != 0 and EightQuoteLocked != 0 and NineQuoteLocked != 0:
            SumOfZero = CubicNumberChecker(ZeroQuoteLocked, ZeroAphostropheLocked, ZeroSemicolonLocked, ZeroColonLocked, ZeroSpaceLocked)
            SumOfOne = CubicNumberChecker(OneQuoteLocked, OneAphostropheLocked, OneSemicolonLocked, OneColonLocked, OneSpaceLocked)
            SumOfTwo = CubicNumberChecker(TwoQuoteLocked, TwoAphostropheLocked, TwoSemicolonLocked, TwoColonLocked, TwoSpaceLocked)
            SumOfThree = CubicNumberChecker(ThreeQuoteLocked, ThreeAphostropheLocked, ThreeSemicolonLocked, ThreeColonLocked, ThreeSpaceLocked)
            SumOfFour = CubicNumberChecker(FourQuoteLocked, FourAphostropheLocked, FourSemicolonLocked, FourColonLocked, FourSpaceLocked)
            SumOfFive = CubicNumberChecker(FiveQuoteLocked, FiveAphostropheLocked, FiveSemicolonLocked, FiveColonLocked, FiveSpaceLocked)
            SumOfSix = CubicNumberChecker(SixQuoteLocked, SixAphostropheLocked, SixSemicolonLocked, SixColonLocked, SixSpaceLocked)
            SumOfSeven = CubicNumberChecker(SevenQuoteLocked, SevenAphostropheLocked, SevenSemicolonLocked, SevenColonLocked, SevenSpaceLocked)
            SumOfEight = CubicNumberChecker(EightQuoteLocked, EightAphostropheLocked, EightSemicolonLocked, EightColonLocked, EightSpaceLocked)
            SumOfNine = CubicNumberChecker(NineQuoteLocked, NineAphostropheLocked, NineSemicolonLocked, NineColonLocked, NineSpaceLocked)
            SevenSumOfZero = SumOfZero
            SevenSumOfOne = SumOfOne
            SevenSumOfTwo = SumOfTwo
            SevenSumOfThree = SumOfThree
            SevenSumOfFour = SumOfFour
            SevenSumOfFive = SumOfFive
            SevenSumOfSix = SumOfSix
            SevenSumOfSeven = SumOfSeven
            SevenSumOfEight = SumOfEight
            SevenSumOfNine = SumOfNine
            if SumOfZero != SumOfOne and SumOfZero != SumOfTwo and SumOfZero != SumOfThree and SumOfZero != SumOfFour and SumOfZero != SumOfFive and SumOfZero != SumOfSix and SumOfZero != SumOfSeven and SumOfZero != SumOfEight and SumOfZero != SumOfNine and SumOfOne != SumOfTwo and SumOfOne != SumOfThree and SumOfOne != SumOfFour and SumOfOne != SumOfFive and SumOfOne != SumOfSix and SumOfOne != SumOfSeven and SumOfOne != SumOfEight and SumOfOne != SumOfNine and SumOfTwo != SumOfThree and SumOfTwo != SumOfFour and SumOfTwo != SumOfFive and SumOfTwo != SumOfSix and SumOfTwo != SumOfSeven and SumOfTwo != SumOfEight and SumOfTwo != SumOfNine and SumOfThree != SumOfFour and SumOfThree != SumOfFive and SumOfThree != SumOfSix and SumOfThree != SumOfSeven and SumOfThree != SumOfEight and SumOfThree != SumOfNine and SumOfFour != SumOfFive and SumOfFour != SumOfSix and SumOfFour != SumOfSeven and SumOfFour != SumOfEight and SumOfFour != SumOfNine and SumOfFive != SumOfSix and SumOfFive != SumOfSeven and SumOfFive != SumOfEight and SumOfFive != SumOfNine and SumOfSix != SumOfSeven and SumOfSix != SumOfEight and SumOfSix != SumOfNine and SumOfSeven != SumOfEight and SumOfSeven != SumOfNine and SumOfEight != SumOfNine:
                print("processing7")
                ThisMakesSureThatAllTheDifferentsNumbersForSevenDigetArentLikeTheExactSame = 1
                if CheckDonCheckSeven != 1:
                    CheckDonCheckSeven = 1
                    check = check + 1
            else:
                ZeroQuoteLocked = 0
                OneQuoteLocked = 0
                TwoQuoteLocked = 0
                ThreeQuoteLocked = 0
                FourQuoteLocked = 0
                FiveQuoteLocked = 0
                SixQuoteLocked = 0
                SevenQuoteLocked = 0
                EightQuoteLocked = 0
                NineQuoteLocked = 0


            #This makes sure all the different possible numbers for the seventh aren't the same

        #holy lord took three days to edit all 7 if statements, havent checked thoroughly yet 16/4/25 23:30

        #inmsert code to make sure <= 5 code didgits have the same number


        #ThisMakesSureThatAllTheDigetsArentTheExactSame <= 5:
        while check == 7:
            print("work")
            if OneSumOfZero == TwoSumOfZero or OneSumOfZero == ThreeSumOfZero or OneSumOfZero == FourSumOfZero or OneSumOfZero == FiveSumOfZero or OneSumOfZero == SixSumOfZero or OneSumOfZero == SevenSumOfZero or TwoSumOfZero == ThreeSumOfZero or TwoSumOfZero == FourSumOfZero or TwoSumOfZero == FiveSumOfZero or TwoSumOfZero == SixSumOfZero or TwoSumOfZero == SevenSumOfZero or ThreeSumOfZero == FourSumOfZero or ThreeSumOfZero == FiveSumOfZero or ThreeSumOfZero == SixSumOfZero or ThreeSumOfZero == SevenSumOfZero or FourSumOfZero == FiveSumOfZero or FourSumOfZero == SixSumOfZero or FourSumOfZero == SevenSumOfZero or FiveSumOfZero == SixSumOfZero or FiveSumOfZero == SevenSumOfZero or SixSumOfZero == SevenSumOfZero:
                #calcs if any of the zerosa are equal to eachother
                ThisMakesSureThatAllTheDigetsArentTheExactSame = ThisMakesSureThatAllTheDigetsArentTheExactSame + 1

            if OneSumOfOne == TwoSumOfOne or OneSumOfOne == ThreeSumOfOne or OneSumOfOne == FourSumOfOne or OneSumOfOne == FiveSumOfOne or OneSumOfOne == SixSumOfOne or OneSumOfOne == SevenSumOfOne or TwoSumOfOne == ThreeSumOfOne or TwoSumOfOne == FourSumOfOne or TwoSumOfOne == FiveSumOfOne or TwoSumOfOne == SixSumOfOne or TwoSumOfOne == SevenSumOfOne or ThreeSumOfOne == FourSumOfOne or ThreeSumOfOne == FiveSumOfOne or ThreeSumOfOne == SixSumOfOne or ThreeSumOfOne == SevenSumOfOne or FourSumOfOne == FiveSumOfOne or FourSumOfOne == SixSumOfOne or FourSumOfOne == SevenSumOfOne or FiveSumOfOne == SixSumOfOne or FiveSumOfOne == SevenSumOfOne or SixSumOfOne == SevenSumOfOne:
                #calcsif any of le ones are same
                ThisMakesSureThatAllTheDigetsArentTheExactSame = ThisMakesSureThatAllTheDigetsArentTheExactSame + 1

            if OneSumOfTwo == TwoSumOfTwo or OneSumOfTwo == ThreeSumOfTwo or OneSumOfTwo == FourSumOfTwo or OneSumOfTwo == FiveSumOfTwo or OneSumOfTwo == SixSumOfTwo or OneSumOfTwo == SevenSumOfTwo or TwoSumOfTwo == ThreeSumOfTwo or TwoSumOfTwo == FourSumOfTwo or TwoSumOfTwo == FiveSumOfTwo or TwoSumOfTwo == SixSumOfTwo or TwoSumOfTwo == SevenSumOfTwo or ThreeSumOfTwo == FourSumOfTwo or ThreeSumOfTwo == FiveSumOfTwo or ThreeSumOfTwo == SixSumOfTwo or ThreeSumOfTwo == SevenSumOfTwo or FourSumOfTwo ==  FiveSumOfTwo or FourSumOfTwo ==  SixSumOfTwo or FourSumOfTwo ==  SevenSumOfTwo or  FiveSumOfTwo == SixSumOfTwo or FiveSumOfTwo == SevenSumOfTwo or SixSumOfTwo == SevenSumOfTwo:
                #
                ThisMakesSureThatAllTheDigetsArentTheExactSame = ThisMakesSureThatAllTheDigetsArentTheExactSame + 1

            if OneSumOfThree == TwoSumOfThree or OneSumOfThree == ThreeSumOfThree or OneSumOfThree == FourSumOfThree or OneSumOfThree == FiveSumOfThree or OneSumOfThree == SixSumOfThree or OneSumOfThree == SevenSumOfThree or TwoSumOfThree == ThreeSumOfThree or TwoSumOfThree == FourSumOfThree or TwoSumOfThree == FiveSumOfThree or TwoSumOfThree == SixSumOfThree or TwoSumOfThree == SevenSumOfThree or ThreeSumOfThree == FourSumOfThree or ThreeSumOfThree == FiveSumOfThree or ThreeSumOfThree == SixSumOfThree or ThreeSumOfThree == SevenSumOfThree or FourSumOfThree == FiveSumOfThree or FourSumOfThree == SixSumOfThree or FourSumOfThree == SevenSumOfThree or FiveSumOfThree == SixSumOfThree or FiveSumOfThree == SevenSumOfThree or SixSumOfThree ==  SevenSumOfThree:
                #
                ThisMakesSureThatAllTheDigetsArentTheExactSame = ThisMakesSureThatAllTheDigetsArentTheExactSame + 1

            if OneSumOfFour == TwoSumOfFour or OneSumOfFour == ThreeSumOfFour or OneSumOfFour == FourSumOfFour or OneSumOfFour == FiveSumOfFour or OneSumOfFour == SixSumOfFour or OneSumOfFour == SevenSumOfFour or TwoSumOfFour == ThreeSumOfFour or TwoSumOfFour == FourSumOfFour or TwoSumOfFour == FiveSumOfFour or TwoSumOfFour == SixSumOfFour or TwoSumOfFour == SevenSumOfFour or ThreeSumOfFour == FourSumOfFour or ThreeSumOfFour == FiveSumOfFour or ThreeSumOfFour == SixSumOfFour or ThreeSumOfFour == SevenSumOfFour or FourSumOfFour == FiveSumOfFour or FourSumOfFour == SixSumOfFour or FourSumOfFour == SevenSumOfFour or FiveSumOfFour == SixSumOfFour or FiveSumOfFour == SevenSumOfFour or SixSumOfFour ==  SevenSumOfFour:
                #
                ThisMakesSureThatAllTheDigetsArentTheExactSame = ThisMakesSureThatAllTheDigetsArentTheExactSame + 1

            if OneSumOfFive == TwoSumOfFive or OneSumOfFive == ThreeSumOfFive or OneSumOfFive == FourSumOfFive or OneSumOfFive == FiveSumOfFive or OneSumOfFive == SixSumOfFive or OneSumOfFive == SevenSumOfFive or TwoSumOfFive == ThreeSumOfFive or TwoSumOfFive == FourSumOfFive or TwoSumOfFive == FiveSumOfFive or TwoSumOfFive == SixSumOfFive or TwoSumOfFive == SevenSumOfFive or ThreeSumOfFive == FourSumOfFive or ThreeSumOfFive == FiveSumOfFive or ThreeSumOfFive == SixSumOfFive or ThreeSumOfFive == SevenSumOfFive or FourSumOfFive == FiveSumOfFive or FourSumOfFive == SixSumOfFive or FourSumOfFive == SevenSumOfFive or FiveSumOfFive == SixSumOfFive or FiveSumOfFive == SevenSumOfFive or SixSumOfFive ==  SevenSumOfFive:
                #
                ThisMakesSureThatAllTheDigetsArentTheExactSame = ThisMakesSureThatAllTheDigetsArentTheExactSame + 1

            if OneSumOfSix == TwoSumOfSix or OneSumOfSix == ThreeSumOfSix or OneSumOfSix == FourSumOfSix or OneSumOfSix == FiveSumOfSix or OneSumOfSix == SixSumOfSix or OneSumOfSix == SevenSumOfSix or TwoSumOfSix == ThreeSumOfSix or TwoSumOfSix == FourSumOfSix or TwoSumOfSix == FiveSumOfSix or TwoSumOfSix == SixSumOfSix or TwoSumOfSix == SevenSumOfSix or ThreeSumOfSix == FourSumOfSix or ThreeSumOfSix == FiveSumOfSix or ThreeSumOfSix == SixSumOfSix or ThreeSumOfSix == SevenSumOfSix or FourSumOfSix == FiveSumOfSix or FourSumOfSix == SixSumOfSix or FourSumOfSix == SevenSumOfSix or FiveSumOfSix == SixSumOfSix or FiveSumOfSix == SevenSumOfSix or SixSumOfSix == SevenSumOfSix:
                #
                ThisMakesSureThatAllTheDigetsArentTheExactSame = ThisMakesSureThatAllTheDigetsArentTheExactSame + 1

            if OneSumOfSeven == TwoSumOfSeven or OneSumOfSeven == ThreeSumOfSeven or OneSumOfSeven == FourSumOfSeven or OneSumOfSeven == FiveSumOfSeven or OneSumOfSeven == SixSumOfSeven or OneSumOfSeven == SevenSumOfSeven or TwoSumOfSeven == ThreeSumOfSeven or TwoSumOfSeven == FourSumOfSeven or TwoSumOfSeven == FiveSumOfSeven or TwoSumOfSeven == SixSumOfSeven or TwoSumOfSeven == SevenSumOfSeven or ThreeSumOfSeven == FourSumOfSeven or ThreeSumOfSeven == FiveSumOfSeven or ThreeSumOfSeven == SixSumOfSeven or ThreeSumOfSeven == SevenSumOfSeven or FourSumOfSeven == FiveSumOfSeven or FourSumOfSeven == SixSumOfSeven or FourSumOfSeven == SevenSumOfSeven or FiveSumOfSeven == SixSumOfSeven or FiveSumOfSeven == SevenSumOfSeven or SixSumOfSeven == SevenSumOfSeven:
                #
                ThisMakesSureThatAllTheDigetsArentTheExactSame = ThisMakesSureThatAllTheDigetsArentTheExactSame + 1

            if OneSumOfEight == TwoSumOfEight or OneSumOfEight == ThreeSumOfEight or OneSumOfEight == FourSumOfEight or OneSumOfEight == FiveSumOfEight or OneSumOfEight == SixSumOfEight or OneSumOfEight == SevenSumOfEight or TwoSumOfEight == ThreeSumOfEight or TwoSumOfEight == FourSumOfEight or TwoSumOfEight == FiveSumOfEight or TwoSumOfEight == SixSumOfEight or TwoSumOfEight == SevenSumOfEight or ThreeSumOfEight == FourSumOfEight or ThreeSumOfEight == FiveSumOfEight or ThreeSumOfEight == SixSumOfEight or ThreeSumOfEight == SevenSumOfEight or FourSumOfEight == FiveSumOfEight or FourSumOfEight == SixSumOfEight or FourSumOfEight == SevenSumOfEight or FiveSumOfEight == SixSumOfEight or FiveSumOfEight == SevenSumOfEight or SixSumOfEight == SevenSumOfEight:
                #
                ThisMakesSureThatAllTheDigetsArentTheExactSame = ThisMakesSureThatAllTheDigetsArentTheExactSame + 1

            if OneSumOfNine == TwoSumOfNine or OneSumOfNine == ThreeSumOfNine or OneSumOfNine == FourSumOfNine or OneSumOfNine == FiveSumOfNine or OneSumOfNine == SixSumOfNine or OneSumOfNine == SevenSumOfNine or TwoSumOfNine == ThreeSumOfNine or TwoSumOfNine == FourSumOfNine or TwoSumOfNine == FiveSumOfNine or TwoSumOfNine == SixSumOfNine or TwoSumOfNine == SevenSumOfNine or ThreeSumOfNine == FourSumOfNine or ThreeSumOfNine == FiveSumOfNine or ThreeSumOfNine == SixSumOfNine or ThreeSumOfNine == SevenSumOfNine or FourSumOfNine == FiveSumOfNine or FourSumOfNine == SixSumOfNine or FourSumOfNine ==  SevenSumOfNine or FiveSumOfNine == SixSumOfNine or FiveSumOfNine == SevenSumOfNine or SixSumOfNine == SevenSumOfNine:
                #
                ThisMakesSureThatAllTheDigetsArentTheExactSame = ThisMakesSureThatAllTheDigetsArentTheExactSame + 1


            if ThisMakesSureThatAllTheDigetsArentTheExactSame > 5:
                ThisMakesSureThatAllTheDifferentsNumbersForOneDigetArentLikeTheExactSame = 0
                ThisMakesSureThatAllTheDifferentsNumbersForTwoDigetArentLikeTheExactSame = 0
                ThisMakesSureThatAllTheDifferentsNumbersForThreeDigetArentLikeTheExactSame = 0
                ThisMakesSureThatAllTheDifferentsNumbersForFourDigetArentLikeTheExactSame = 0
                ThisMakesSureThatAllTheDifferentsNumbersForFiveDigetArentLikeTheExactSame = 0
                ThisMakesSureThatAllTheDifferentsNumbersForSixDigetArentLikeTheExactSame = 0
                ThisMakesSureThatAllTheDifferentsNumbersForSevenDigetArentLikeTheExactSame = 0
                ThisMakesSureThatAllTheDigetsArentTheExactSame = 0
                ThisIsACounterSoTheCodeWorks = 0
                ThisIsACounterSoTheCodeWorksbutdifferent1 = 0
                ThisIsACounterSoTheCodeWorksbutdifferent2 = 0
                ThisIsACounterSoTheCodeWorksbutdifferent3 = 0
                ThisIsACounterSoTheCodeWorksbutdifferent4 = 0
                ThisIsACounterSoTheCodeWorksbutdifferent5 = 0 
                ThisIsACounterSoTheCodeWorksbutdifferent6 = 0
                ThisIsACounterSoTheCodeWorksbutdifferent7 = 0
                ThisIsACounterSoTheCodeWorksbutdifferent8 = 0
                ThisIsACounterSoTheCodeWorksbutdifferent9 = 0
                ThisIsACounterSoTheCodeWorksbutdifferent10 = 0
                ThisIsACounterSoTheCodeWorksbutdifferent11= 0 
                ThisIsACounterSoTheCodeWorksbutdifferent12= 0
                ThisIsACounterSoTheCodeWorksbutdifferent13= 0
                ThisIsACounterSoTheCodeWorksbutdifferent14= 0
                ThisIsACounterSoTheCodeWorksbutdifferent15= 0
                ThisIsACounterSoTheCodeWorksbutdifferent16= 0
                ThisIsACounterSoTheCodeWorksbutdifferent17= 0 
                ThisIsACounterSoTheCodeWorksbutdifferent18= 0
                ThisIsACounterSoTheCodeWorksbutdifferent19= 0
                ThisIsACounterSoTheCodeWorksbutdifferent20= 0
                ThisIsACounterSoTheCodeWorksbutdifferent21= 0
                ThisIsACounterSoTheCodeWorksbutdifferent22= 0
                ThisIsACounterSoTheCodeWorksbutdifferent23= 0 
                ThisIsACounterSoTheCodeWorksbutdifferent24= 0
                ThisIsACounterSoTheCodeWorksbutdifferent25= 0
                ThisIsACounterSoTheCodeWorksbutdifferent26= 0
                ThisIsACounterSoTheCodeWorksbutdifferent27= 0
                ThisIsACounterSoTheCodeWorksbutdifferent28= 0
                ThisIsACounterSoTheCodeWorksbutdifferent29= 0 
                ThisIsACounterSoTheCodeWorksbutdifferent30= 0
                ThisIsACounterSoTheCodeWorksbutdifferent31= 0
                ThisIsACounterSoTheCodeWorksbutdifferent32= 0
                ThisIsACounterSoTheCodeWorksbutdifferent33= 0
                ThisIsACounterSoTheCodeWorksbutdifferent34= 0
                ThisIsACounterSoTheCodeWorksbutdifferent35= 0 
                ThisIsACounterSoTheCodeWorksbutdifferent36= 0
                ThisIsACounterSoTheCodeWorksbutdifferent37= 0
                ThisIsACounterSoTheCodeWorksbutdifferent38= 0
                ThisIsACounterSoTheCodeWorksbutdifferent39= 0
                ThisIsACounterSoTheCodeWorksbutdifferent40= 0
                ThisIsACounterSoTheCodeWorksbutdifferent41= 0 
                ThisIsACounterSoTheCodeWorksbutdifferent42= 0
                ThisIsACounterSoTheCodeWorksbutdifferent43= 0
                ThisIsACounterSoTheCodeWorksbutdifferent44= 0
                ThisIsACounterSoTheCodeWorksbutdifferent45= 0
                ThisIsACounterSoTheCodeWorksbutdifferent46= 0
                ThisIsACounterSoTheCodeWorksbutdifferent47= 0 
                ThisIsACounterSoTheCodeWorksbutdifferent48= 0
                ThisIsACounterSoTheCodeWorksbutdifferent49= 0
                ThisIsACounterSoTheCodeWorksbutdifferent50= 0
                ThisIsACounterSoTheCodeWorksbutdifferent51= 0
                ThisIsACounterSoTheCodeWorksbutdifferent52= 0
                ThisIsACounterSoTheCodeWorksbutdifferent53= 0 
                ThisIsACounterSoTheCodeWorksbutdifferent54= 0
                ThisIsACounterSoTheCodeWorksbutdifferent55= 0
                ThisIsACounterSoTheCodeWorksbutdifferent56= 0
                ThisIsACounterSoTheCodeWorksbutdifferent57= 0
                ThisIsACounterSoTheCodeWorksbutdifferent58= 0
                ThisIsACounterSoTheCodeWorksbutdifferent59= 0 
                ThisIsACounterSoTheCodeWorksbutdifferent60= 0
                ThisIsACounterSoTheCodeWorksbutdifferent61= 0
                ThisIsACounterSoTheCodeWorksbutdifferent62= 0
                ThisIsACounterSoTheCodeWorksbutdifferent63= 0
                ThisIsACounterSoTheCodeWorksbutdifferent64= 0
                ThisIsACounterSoTheCodeWorksbutdifferent65= 0 
                ThisIsACounterSoTheCodeWorksbutdifferent66= 0
                ThisIsACounterSoTheCodeWorksbutdifferent67= 0
                ThisIsACounterSoTheCodeWorksbutdifferent68= 0
                ThisIsACounterSoTheCodeWorksbutdifferent69= 0
                ThisMakesSureThatAllTheDifferentsNumbersForOneDigetArentLikeTheExactSame = 0
                ThisMakesSureThatAllTheDigetsArentTheExactSame = 0
                ZeroALocked = 0
                OneALocked = 0
                TwoALocked = 0
                ThreeALocked = 0
                FourALocked = 0
                FiveALocked = 0
                SixALocked = 0
                SevenALocked = 0
                EightALocked = 0
                NineALocked = 0
                ZeroFLocked = 0
                OneFLocked = 0
                TwoFLocked = 0
                ThreeFLocked = 0
                FourFLocked = 0
                FiveFLocked = 0
                SixFLocked = 0
                SevenFLocked = 0
                EightFLocked = 0
                NineFLocked = 0
                ZeroKLocked = 0
                OneKLocked = 0
                TwoKLocked = 0
                ThreeKLocked = 0
                FourKLocked = 0
                FiveKLocked = 0
                SixKLocked = 0
                SevenKLocked = 0
                EightKLocked = 0
                NineKLocked = 0
                ZeroPLocked = 0
                OnePLocked = 0
                TwoPLocked = 0
                ThreePLocked = 0
                FourPLocked = 0
                FivePLocked = 0
                SixPLocked = 0
                SevenPLocked = 0
                EightPLocked = 0
                NinePLocked = 0
                ZeroULocked = 0
                OneULocked = 0
                TwoULocked = 0
                ThreeULocked = 0
                FourULocked = 0
                FiveULocked = 0
                SixULocked = 0
                SevenULocked = 0
                EightULocked = 0
                NineULocked = 0
                ZeroZLocked = 0
                OneZLocked = 0
                TwoZLocked = 0
                ThreeZLocked = 0
                FourZLocked = 0
                FiveZLocked = 0
                SixZLocked = 0
                SevenZLocked = 0
                EightZLocked = 0
                NineZLocked = 0
                ZeroQuoteLocked = 0
                OneQuoteLocked = 0
                TwoQuoteLocked = 0
                ThreeQuoteLocked = 0
                FourQuoteLocked = 0
                FiveQuoteLocked = 0
                SixQuoteLocked = 0
                SevenQuoteLocked = 0
                EightQuoteLocked = 0
                NineQuoteLocked = 0
                check = 0
                CheckDonCheckOne = 0
                CheckDonCheckTwo = 0
                CheckDonCheckThree = 0
                CheckDonCheckFour = 0
                CheckDonCheckFive = 0
                CheckDonCheckSix = 0
                CheckDonCheckSeven = 0
                count = 0
            else:
                check = 8
                SystemsGo = 1



    #insert like a thing that makes sure thgat the new code created hasent already been added to the array
    #i didi it


    if len(str(count)) < 7:
        if len(str(count)) == 1:
            code = "0" + "0" + "0" + "0" + "0" + "0" + str(count) 
            one = 0
            two = 0
            three = 0
            four = 0
            five = 0
            six = 0
            seven = count
        elif len(str(count)) == 2:
            code = "0" + "0" + "0" + "0" + "0" + str(count) 
            one = 0
            two = 0
            three = 0
            four = 0
            five = 0
            six = int(code[5])
            seven = int(code[6])
        elif len(str(count)) == 3:
            code = "0" + "0" + "0" + "0" + str(count) 
            one = 0
            two = 0
            three = 0
            four = 0
            five = int(code[4])
            six = int(code[5])
            seven = int(code[6])
        elif len(str(count)) == 4:
            code = "0" + "0" + "0" + str(count) 
            one = 0
            two = 0
            three = 0
            four = int(code[3])
            five = int(code[4])
            six = int(code[5])
            seven = int(code[6])
        elif len(str(count)) == 5:
            code = "0" + "0" + str(count) 
            one = 0
            two = 0
            three = int(code[2])
            four = int(code[3])
            five = int(code[4])
            six = int(code[5])
            seven = int(code[6])
        elif len(str(count)) == 6:
            code = "0" + str(count) 
            one = 0
            two = int(code[1])
            three = int(code[2])
            four = int(code[3])
            five = int(code[4])
            six = int(code[5])
            seven = int(code[6])
    else:
        code = str(count)
        one = int(code[0])
        two = int(code[1])
        three = int(code[2])
        four = int(code[3])
        five = int(code[4])
        six = int(code[5])
        seven = int(code[6])


    #insert code to make csv file here

    ArrayAdder(EncryptionArray, count, 0, code)

    if one == 0:
        ArrayAdder(EncryptionArray, count, 1, ZeroALocked)
        ArrayAdder(EncryptionArray, count, 2, ZeroBLocked)
        ArrayAdder(EncryptionArray, count, 3, ZeroCLocked)
        ArrayAdder(EncryptionArray, count, 4, ZeroDLocked)
        ArrayAdder(EncryptionArray, count, 5, ZeroELocked)
    elif one == 1:
        ArrayAdder(EncryptionArray, count, 1, OneALocked)
        ArrayAdder(EncryptionArray, count, 2, OneBLocked)
        ArrayAdder(EncryptionArray, count, 3, OneCLocked)
        ArrayAdder(EncryptionArray, count, 4, OneDLocked)
        ArrayAdder(EncryptionArray, count, 5, OneELocked)
    elif one == 2:
        ArrayAdder(EncryptionArray, count, 1, TwoALocked)
        ArrayAdder(EncryptionArray, count, 2, TwoBLocked)
        ArrayAdder(EncryptionArray, count, 3, TwoCLocked)
        ArrayAdder(EncryptionArray, count, 4, TwoDLocked)
        ArrayAdder(EncryptionArray, count, 5, TwoELocked)
    elif one == 3:
        ArrayAdder(EncryptionArray, count, 1, ThreeALocked)
        ArrayAdder(EncryptionArray, count, 2, ThreeBLocked)
        ArrayAdder(EncryptionArray, count, 3, ThreeCLocked)
        ArrayAdder(EncryptionArray, count, 4, ThreeDLocked)
        ArrayAdder(EncryptionArray, count, 5, ThreeELocked)
    elif one == 4:
        ArrayAdder(EncryptionArray, count, 1, FourALocked)
        ArrayAdder(EncryptionArray, count, 2, FourBLocked)
        ArrayAdder(EncryptionArray, count, 3, FourCLocked)
        ArrayAdder(EncryptionArray, count, 4, FourDLocked)
        ArrayAdder(EncryptionArray, count, 5, FourELocked)
    elif one == 5:
        ArrayAdder(EncryptionArray, count, 1, FiveALocked)
        ArrayAdder(EncryptionArray, count, 2, FiveBLocked)
        ArrayAdder(EncryptionArray, count, 3, FiveCLocked)
        ArrayAdder(EncryptionArray, count, 4, FiveDLocked)
        ArrayAdder(EncryptionArray, count, 5, FiveELocked)
    elif one == 6:
        ArrayAdder(EncryptionArray, count, 1, SixALocked)
        ArrayAdder(EncryptionArray, count, 2, SixBLocked)
        ArrayAdder(EncryptionArray, count, 3, SixCLocked)
        ArrayAdder(EncryptionArray, count, 4, SixDLocked)
        ArrayAdder(EncryptionArray, count, 5, SixELocked)
    elif one == 7:
        ArrayAdder(EncryptionArray, count, 1, SevenALocked)
        ArrayAdder(EncryptionArray, count, 2, SevenBLocked)
        ArrayAdder(EncryptionArray, count, 3, SevenCLocked)
        ArrayAdder(EncryptionArray, count, 4, SevenDLocked)
        ArrayAdder(EncryptionArray, count, 5, SevenELocked)
    elif one == 8:
        ArrayAdder(EncryptionArray, count, 1, EightALocked)
        ArrayAdder(EncryptionArray, count, 2, EightBLocked)
        ArrayAdder(EncryptionArray, count, 3, EightCLocked)
        ArrayAdder(EncryptionArray, count, 4, EightDLocked)
        ArrayAdder(EncryptionArray, count, 5, EightELocked)
    elif one == 9:
        ArrayAdder(EncryptionArray, count, 1, NineALocked)
        ArrayAdder(EncryptionArray, count, 2, NineBLocked)
        ArrayAdder(EncryptionArray, count, 3, NineCLocked)
        ArrayAdder(EncryptionArray, count, 4, NineDLocked)
        ArrayAdder(EncryptionArray, count, 5, NineELocked)


    #Adds fghij to the array
    if two == 0:
        ArrayAdder(EncryptionArray, count, 6, ZeroFLocked)
        ArrayAdder(EncryptionArray, count, 7, ZeroGLocked)
        ArrayAdder(EncryptionArray, count, 8, ZeroHLocked)
        ArrayAdder(EncryptionArray, count, 9, ZeroILocked)
        ArrayAdder(EncryptionArray, count, 10, ZeroJLocked)
    elif two == 1:
        ArrayAdder(EncryptionArray, count, 6, OneFLocked)
        ArrayAdder(EncryptionArray, count, 7, OneGLocked)
        ArrayAdder(EncryptionArray, count, 8, OneHLocked)
        ArrayAdder(EncryptionArray, count, 9, OneILocked)
        ArrayAdder(EncryptionArray, count, 10, OneJLocked)
    elif two == 2:
        ArrayAdder(EncryptionArray, count, 6, TwoFLocked)
        ArrayAdder(EncryptionArray, count, 7, TwoGLocked)
        ArrayAdder(EncryptionArray, count, 8, TwoHLocked)
        ArrayAdder(EncryptionArray, count, 9, TwoILocked)
        ArrayAdder(EncryptionArray, count, 10, TwoJLocked)
    elif two == 3:
        ArrayAdder(EncryptionArray, count, 6, ThreeFLocked)
        ArrayAdder(EncryptionArray, count, 7, ThreeGLocked)
        ArrayAdder(EncryptionArray, count, 8, ThreeHLocked)
        ArrayAdder(EncryptionArray, count, 9, ThreeILocked)
        ArrayAdder(EncryptionArray, count, 10, ThreeJLocked)
    elif two == 4:
        ArrayAdder(EncryptionArray, count, 6, FourFLocked)
        ArrayAdder(EncryptionArray, count, 7, FourGLocked)
        ArrayAdder(EncryptionArray, count, 8, FourHLocked)
        ArrayAdder(EncryptionArray, count, 9, FourILocked)
        ArrayAdder(EncryptionArray, count, 10, FourJLocked)
    elif two == 5:
        ArrayAdder(EncryptionArray, count, 6, FiveFLocked)
        ArrayAdder(EncryptionArray, count, 7, FiveGLocked)
        ArrayAdder(EncryptionArray, count, 8, FiveHLocked)
        ArrayAdder(EncryptionArray, count, 9, FiveILocked)
        ArrayAdder(EncryptionArray, count, 10, FiveJLocked)
    elif two == 6:
        ArrayAdder(EncryptionArray, count, 6, SixFLocked)
        ArrayAdder(EncryptionArray, count, 7, SixGLocked)
        ArrayAdder(EncryptionArray, count, 8, SixHLocked)
        ArrayAdder(EncryptionArray, count, 9, SixILocked)
        ArrayAdder(EncryptionArray, count, 10, SixJLocked)
    elif two == 7:
        ArrayAdder(EncryptionArray, count, 6, SevenFLocked)
        ArrayAdder(EncryptionArray, count, 7, SevenGLocked)
        ArrayAdder(EncryptionArray, count, 8, SevenHLocked)
        ArrayAdder(EncryptionArray, count, 9, SevenILocked)
        ArrayAdder(EncryptionArray, count, 10, SevenJLocked)
    elif two == 8:
        ArrayAdder(EncryptionArray, count, 6, EightFLocked)
        ArrayAdder(EncryptionArray, count, 7, EightGLocked)
        ArrayAdder(EncryptionArray, count, 8, EightHLocked)
        ArrayAdder(EncryptionArray, count, 9, EightILocked)
        ArrayAdder(EncryptionArray, count, 10, EightJLocked)
    elif two == 9:
        ArrayAdder(EncryptionArray, count, 6, NineFLocked)
        ArrayAdder(EncryptionArray, count, 7, NineGLocked)
        ArrayAdder(EncryptionArray, count, 8, NineHLocked)
        ArrayAdder(EncryptionArray, count, 9, NineILocked)
        ArrayAdder(EncryptionArray, count, 10, NineJLocked)


    #adds klmno tto le array
    if three == 0:
        ArrayAdder(EncryptionArray, count, 11, ZeroKLocked)
        ArrayAdder(EncryptionArray, count, 12, ZeroLLocked)
        ArrayAdder(EncryptionArray, count, 13, ZeroMLocked)
        ArrayAdder(EncryptionArray, count, 14, ZeroNLocked)
        ArrayAdder(EncryptionArray, count, 15, ZeroOLocked)
    elif three == 1:
        ArrayAdder(EncryptionArray, count, 11, OneKLocked)
        ArrayAdder(EncryptionArray, count, 12, OneLLocked)
        ArrayAdder(EncryptionArray, count, 13, OneMLocked)
        ArrayAdder(EncryptionArray, count, 14, OneNLocked)
        ArrayAdder(EncryptionArray, count, 15, OneOLocked)
    elif three == 2:
        ArrayAdder(EncryptionArray, count, 11, TwoKLocked)
        ArrayAdder(EncryptionArray, count, 12, TwoLLocked)
        ArrayAdder(EncryptionArray, count, 13, TwoMLocked)
        ArrayAdder(EncryptionArray, count, 14, TwoNLocked)
        ArrayAdder(EncryptionArray, count, 15, TwoOLocked)
    elif three == 3:
        ArrayAdder(EncryptionArray, count, 11, ThreeKLocked)
        ArrayAdder(EncryptionArray, count, 12, ThreeLLocked)
        ArrayAdder(EncryptionArray, count, 13, ThreeMLocked)
        ArrayAdder(EncryptionArray, count, 14, ThreeNLocked)
        ArrayAdder(EncryptionArray, count, 15, ThreeOLocked)
    elif three == 4:
        ArrayAdder(EncryptionArray, count, 11, FourKLocked)
        ArrayAdder(EncryptionArray, count, 12, FourLLocked)
        ArrayAdder(EncryptionArray, count, 13, FourMLocked)
        ArrayAdder(EncryptionArray, count, 14, FourNLocked)
        ArrayAdder(EncryptionArray, count, 15, FourOLocked)
    elif three == 5:
        ArrayAdder(EncryptionArray, count, 11, FiveKLocked)
        ArrayAdder(EncryptionArray, count, 12, FiveLLocked)
        ArrayAdder(EncryptionArray, count, 13, FiveMLocked)
        ArrayAdder(EncryptionArray, count, 14, FiveNLocked)
        ArrayAdder(EncryptionArray, count, 15, FiveOLocked)
    elif three == 6:
        ArrayAdder(EncryptionArray, count, 11, SixKLocked)
        ArrayAdder(EncryptionArray, count, 12, SixLLocked)
        ArrayAdder(EncryptionArray, count, 13, SixMLocked)
        ArrayAdder(EncryptionArray, count, 14, SixNLocked)
        ArrayAdder(EncryptionArray, count, 15, SixOLocked)
    elif three == 7:
        ArrayAdder(EncryptionArray, count, 11, SevenKLocked)
        ArrayAdder(EncryptionArray, count, 12, SevenLLocked)
        ArrayAdder(EncryptionArray, count, 13, SevenMLocked)
        ArrayAdder(EncryptionArray, count, 14, SevenNLocked)
        ArrayAdder(EncryptionArray, count, 15, SevenOLocked)
    elif three == 8:
        ArrayAdder(EncryptionArray, count, 11, EightKLocked)
        ArrayAdder(EncryptionArray, count, 12, EightLLocked)
        ArrayAdder(EncryptionArray, count, 13, EightMLocked)
        ArrayAdder(EncryptionArray, count, 14, EightNLocked)
        ArrayAdder(EncryptionArray, count, 15, EightOLocked)
    elif three == 9:
        ArrayAdder(EncryptionArray, count, 11, NineKLocked)
        ArrayAdder(EncryptionArray, count, 12, NineLLocked)
        ArrayAdder(EncryptionArray, count, 13, NineMLocked)
        ArrayAdder(EncryptionArray, count, 14, NineNLocked)
        ArrayAdder(EncryptionArray, count, 15, NineOLocked)



    #pqrst
    if four == 0:
        ArrayAdder(EncryptionArray, count, 16, ZeroPLocked)
        ArrayAdder(EncryptionArray, count, 17, ZeroQLocked)
        ArrayAdder(EncryptionArray, count, 18, ZeroRLocked)
        ArrayAdder(EncryptionArray, count, 19, ZeroSLocked)
        ArrayAdder(EncryptionArray, count, 20, ZeroTLocked)
    elif four == 1:
        ArrayAdder(EncryptionArray, count, 16, OnePLocked)
        ArrayAdder(EncryptionArray, count, 17, OneQLocked)
        ArrayAdder(EncryptionArray, count, 18, OneRLocked)
        ArrayAdder(EncryptionArray, count, 19, OneSLocked)
        ArrayAdder(EncryptionArray, count, 20, OneTLocked)
    elif four == 2:
        ArrayAdder(EncryptionArray, count, 16, TwoPLocked)
        ArrayAdder(EncryptionArray, count, 17, TwoQLocked)
        ArrayAdder(EncryptionArray, count, 18, TwoRLocked)
        ArrayAdder(EncryptionArray, count, 19, TwoSLocked)
        ArrayAdder(EncryptionArray, count, 20, TwoTLocked)
    elif four == 3:
        ArrayAdder(EncryptionArray, count, 16, ThreePLocked)
        ArrayAdder(EncryptionArray, count, 17, ThreeQLocked)
        ArrayAdder(EncryptionArray, count, 18, ThreeRLocked)
        ArrayAdder(EncryptionArray, count, 19, ThreeSLocked)
        ArrayAdder(EncryptionArray, count, 20, ThreeTLocked)
    elif four == 4:
        ArrayAdder(EncryptionArray, count, 16, FourPLocked)
        ArrayAdder(EncryptionArray, count, 17, FourQLocked)
        ArrayAdder(EncryptionArray, count, 18, FourRLocked)
        ArrayAdder(EncryptionArray, count, 19, FourSLocked)
        ArrayAdder(EncryptionArray, count, 20, FourTLocked)
    elif four == 5:
        ArrayAdder(EncryptionArray, count, 16, FivePLocked)
        ArrayAdder(EncryptionArray, count, 17, FiveQLocked)
        ArrayAdder(EncryptionArray, count, 18, FiveRLocked)
        ArrayAdder(EncryptionArray, count, 19, FiveSLocked)
        ArrayAdder(EncryptionArray, count, 20, FiveTLocked)
    elif four == 6:
        ArrayAdder(EncryptionArray, count, 16, SixPLocked)
        ArrayAdder(EncryptionArray, count, 17, SixQLocked)
        ArrayAdder(EncryptionArray, count, 18, SixRLocked)
        ArrayAdder(EncryptionArray, count, 19, SixSLocked)
        ArrayAdder(EncryptionArray, count, 20, SixTLocked)
    elif four == 7:
        ArrayAdder(EncryptionArray, count, 16, SevenPLocked)
        ArrayAdder(EncryptionArray, count, 17, SevenQLocked)
        ArrayAdder(EncryptionArray, count, 18, SevenRLocked)
        ArrayAdder(EncryptionArray, count, 19, SevenSLocked)
        ArrayAdder(EncryptionArray, count, 20, SevenTLocked)
    elif four == 8:
        ArrayAdder(EncryptionArray, count, 16, EightPLocked)
        ArrayAdder(EncryptionArray, count, 17, EightQLocked)
        ArrayAdder(EncryptionArray, count, 18, EightRLocked)
        ArrayAdder(EncryptionArray, count, 19, EightSLocked)
        ArrayAdder(EncryptionArray, count, 20, EightTLocked)
    elif four == 9:
        ArrayAdder(EncryptionArray, count, 16, NinePLocked)
        ArrayAdder(EncryptionArray, count, 17, NineQLocked)
        ArrayAdder(EncryptionArray, count, 18, NineRLocked)
        ArrayAdder(EncryptionArray, count, 19, NineSLocked)
        ArrayAdder(EncryptionArray, count, 20, NineTLocked)


    #uvwxy
    if five == 0:
        ArrayAdder(EncryptionArray, count, 21, ZeroULocked)
        ArrayAdder(EncryptionArray, count, 22, ZeroVLocked)
        ArrayAdder(EncryptionArray, count, 23, ZeroWLocked)
        ArrayAdder(EncryptionArray, count, 24, ZeroXLocked)
        ArrayAdder(EncryptionArray, count, 25, ZeroYLocked)
    elif five == 1:
        ArrayAdder(EncryptionArray, count, 21, OneULocked)
        ArrayAdder(EncryptionArray, count, 22, OneVLocked)
        ArrayAdder(EncryptionArray, count, 23, OneWLocked)
        ArrayAdder(EncryptionArray, count, 24, OneXLocked)
        ArrayAdder(EncryptionArray, count, 25, OneYLocked)
    elif five == 2:
        ArrayAdder(EncryptionArray, count, 21, TwoULocked)
        ArrayAdder(EncryptionArray, count, 22, TwoVLocked)
        ArrayAdder(EncryptionArray, count, 23, TwoWLocked)
        ArrayAdder(EncryptionArray, count, 24, TwoXLocked)
        ArrayAdder(EncryptionArray, count, 25, TwoYLocked)
    elif five == 3:
        ArrayAdder(EncryptionArray, count, 21, ThreeULocked)
        ArrayAdder(EncryptionArray, count, 22, ThreeVLocked)
        ArrayAdder(EncryptionArray, count, 23, ThreeWLocked)
        ArrayAdder(EncryptionArray, count, 24, ThreeXLocked)
        ArrayAdder(EncryptionArray, count, 25, ThreeYLocked)
    elif five == 4:
        ArrayAdder(EncryptionArray, count, 21, FourULocked)
        ArrayAdder(EncryptionArray, count, 22, FourVLocked)
        ArrayAdder(EncryptionArray, count, 23, FourWLocked)
        ArrayAdder(EncryptionArray, count, 24, FourXLocked)
        ArrayAdder(EncryptionArray, count, 25, FourYLocked)
    elif five == 5:
        ArrayAdder(EncryptionArray, count, 21, FiveULocked)
        ArrayAdder(EncryptionArray, count, 22, FiveVLocked)
        ArrayAdder(EncryptionArray, count, 23, FiveWLocked)
        ArrayAdder(EncryptionArray, count, 24, FiveXLocked)
        ArrayAdder(EncryptionArray, count, 25, FiveYLocked)
    elif five == 6:
        ArrayAdder(EncryptionArray, count, 21, SixULocked)
        ArrayAdder(EncryptionArray, count, 22, SixVLocked)
        ArrayAdder(EncryptionArray, count, 23, SixWLocked)
        ArrayAdder(EncryptionArray, count, 24, SixXLocked)
        ArrayAdder(EncryptionArray, count, 25, SixYLocked)
    elif five == 7:
        ArrayAdder(EncryptionArray, count, 21, SevenULocked)
        ArrayAdder(EncryptionArray, count, 22, SevenVLocked)
        ArrayAdder(EncryptionArray, count, 23, SevenWLocked)
        ArrayAdder(EncryptionArray, count, 24, SevenXLocked)
        ArrayAdder(EncryptionArray, count, 25, SevenYLocked)
    elif five == 8:
        ArrayAdder(EncryptionArray, count, 21, EightULocked)
        ArrayAdder(EncryptionArray, count, 22, EightVLocked)
        ArrayAdder(EncryptionArray, count, 23, EightWLocked)
        ArrayAdder(EncryptionArray, count, 24, EightXLocked)
        ArrayAdder(EncryptionArray, count, 25, EightYLocked)
    elif five == 9:
        ArrayAdder(EncryptionArray, count, 21, NineULocked)
        ArrayAdder(EncryptionArray, count, 22, NineVLocked)
        ArrayAdder(EncryptionArray, count, 23, NineWLocked)
        ArrayAdder(EncryptionArray, count, 24, NineXLocked)
        ArrayAdder(EncryptionArray, count, 25, NineYLocked)



    #z.,?!
    if six == 0:
        ArrayAdder(EncryptionArray, count, 26, ZeroZLocked)
        ArrayAdder(EncryptionArray, count, 27, ZeroFullstopLocked)
        ArrayAdder(EncryptionArray, count, 28, ZeroCommaLocked)
        ArrayAdder(EncryptionArray, count, 29, ZeroQuestionMarkLocked)
        ArrayAdder(EncryptionArray, count, 30, ZeroExclimationPointLocked)
    elif six == 1:
        ArrayAdder(EncryptionArray, count, 26, OneZLocked)
        ArrayAdder(EncryptionArray, count, 27, OneFullstopLocked)
        ArrayAdder(EncryptionArray, count, 28, OneCommaLocked)
        ArrayAdder(EncryptionArray, count, 29, OneQuestionMarkLocked)
        ArrayAdder(EncryptionArray, count, 30, OneExclimationPointLocked)
    elif six == 2:
        ArrayAdder(EncryptionArray, count, 26, TwoZLocked)
        ArrayAdder(EncryptionArray, count, 27, TwoFullstopLocked)
        ArrayAdder(EncryptionArray, count, 28, TwoCommaLocked)
        ArrayAdder(EncryptionArray, count, 29, TwoQuestionMarkLocked)
        ArrayAdder(EncryptionArray, count, 30, TwoExclimationPointLocked)
    elif six == 3:
        ArrayAdder(EncryptionArray, count, 26, ThreeZLocked)
        ArrayAdder(EncryptionArray, count, 27, ThreeFullstopLocked)
        ArrayAdder(EncryptionArray, count, 28, ThreeCommaLocked)
        ArrayAdder(EncryptionArray, count, 29, ThreeQuestionMarkLocked)
        ArrayAdder(EncryptionArray, count, 30, ThreeExclimationPointLocked)
    elif six == 4:
        ArrayAdder(EncryptionArray, count, 26, FourZLocked)
        ArrayAdder(EncryptionArray, count, 27, FourFullstopLocked)
        ArrayAdder(EncryptionArray, count, 28, FourCommaLocked)
        ArrayAdder(EncryptionArray, count, 29, FourQuestionMarkLocked)
        ArrayAdder(EncryptionArray, count, 30, FourExclimationPointLocked)
    elif six == 5:
        ArrayAdder(EncryptionArray, count, 26, FiveZLocked)
        ArrayAdder(EncryptionArray, count, 27, FiveFullstopLocked)
        ArrayAdder(EncryptionArray, count, 28, FiveCommaLocked)
        ArrayAdder(EncryptionArray, count, 29, FiveQuestionMarkLocked)
        ArrayAdder(EncryptionArray, count, 30, FiveExclimationPointLocked)
    elif six == 6:
        ArrayAdder(EncryptionArray, count, 26, SixZLocked)
        ArrayAdder(EncryptionArray, count, 27, SixFullstopLocked)
        ArrayAdder(EncryptionArray, count, 28, SixCommaLocked)
        ArrayAdder(EncryptionArray, count, 29, SixQuestionMarkLocked)
        ArrayAdder(EncryptionArray, count, 30, SixExclimationPointLocked)
    elif six == 7:
        ArrayAdder(EncryptionArray, count, 26, SevenZLocked)
        ArrayAdder(EncryptionArray, count, 27, SevenFullstopLocked)
        ArrayAdder(EncryptionArray, count, 28, SevenCommaLocked)
        ArrayAdder(EncryptionArray, count, 29, SevenQuestionMarkLocked)
        ArrayAdder(EncryptionArray, count, 30, SevenExclimationPointLocked)
    elif six == 8:
        ArrayAdder(EncryptionArray, count, 26, EightZLocked)
        ArrayAdder(EncryptionArray, count, 27, EightFullstopLocked)
        ArrayAdder(EncryptionArray, count, 28, EightCommaLocked)
        ArrayAdder(EncryptionArray, count, 29, EightQuestionMarkLocked)
        ArrayAdder(EncryptionArray, count, 30, EightExclimationPointLocked)
    elif six == 9:
        ArrayAdder(EncryptionArray, count, 26, NineZLocked)
        ArrayAdder(EncryptionArray, count, 27, NineFullstopLocked)
        ArrayAdder(EncryptionArray, count, 28, NineCommaLocked)
        ArrayAdder(EncryptionArray, count, 29, NineQuestionMarkLocked)
        ArrayAdder(EncryptionArray, count, 30, NineExclimationPointLocked)


    #"';: 
    if seven == 0:
        ArrayAdder(EncryptionArray, count, 31, ZeroQuoteLocked)
        ArrayAdder(EncryptionArray, count, 32, ZeroAphostropheLocked)
        ArrayAdder(EncryptionArray, count, 33, ZeroSemicolonLocked)
        ArrayAdder(EncryptionArray, count, 34, ZeroColonLocked)
        ArrayAdder(EncryptionArray, count, 35, ZeroSpaceLocked)
    elif seven == 1:
        ArrayAdder(EncryptionArray, count, 31, OneQuoteLocked)
        ArrayAdder(EncryptionArray, count, 32, OneAphostropheLocked)
        ArrayAdder(EncryptionArray, count, 33, OneSemicolonLocked)
        ArrayAdder(EncryptionArray, count, 34, OneColonLocked)
        ArrayAdder(EncryptionArray, count, 35, OneSpaceLocked)
    elif seven == 2:
        ArrayAdder(EncryptionArray, count, 31, TwoQuoteLocked)
        ArrayAdder(EncryptionArray, count, 32, TwoAphostropheLocked)
        ArrayAdder(EncryptionArray, count, 33, TwoSemicolonLocked)
        ArrayAdder(EncryptionArray, count, 34, TwoColonLocked)
        ArrayAdder(EncryptionArray, count, 35, TwoSpaceLocked)
    elif seven == 3:
        ArrayAdder(EncryptionArray, count, 31, ThreeQuoteLocked)
        ArrayAdder(EncryptionArray, count, 32, ThreeAphostropheLocked)
        ArrayAdder(EncryptionArray, count, 33, ThreeSemicolonLocked)
        ArrayAdder(EncryptionArray, count, 34, ThreeColonLocked)
        ArrayAdder(EncryptionArray, count, 35, ThreeSpaceLocked)
    elif seven == 4:
        ArrayAdder(EncryptionArray, count, 31, FourQuoteLocked)
        ArrayAdder(EncryptionArray, count, 32, FourAphostropheLocked)
        ArrayAdder(EncryptionArray, count, 33, FourSemicolonLocked)
        ArrayAdder(EncryptionArray, count, 34, FourColonLocked)
        ArrayAdder(EncryptionArray, count, 35, FourSpaceLocked)
    elif seven == 5:
        ArrayAdder(EncryptionArray, count, 31, FiveQuoteLocked)
        ArrayAdder(EncryptionArray, count, 32, FiveAphostropheLocked)
        ArrayAdder(EncryptionArray, count, 33, FiveSemicolonLocked)
        ArrayAdder(EncryptionArray, count, 34, FiveColonLocked)
        ArrayAdder(EncryptionArray, count, 35, FiveSpaceLocked)
    elif seven == 6:
        ArrayAdder(EncryptionArray, count, 31, SixQuoteLocked)
        ArrayAdder(EncryptionArray, count, 32, SixAphostropheLocked)
        ArrayAdder(EncryptionArray, count, 33, SixSemicolonLocked)
        ArrayAdder(EncryptionArray, count, 34, SixColonLocked)
        ArrayAdder(EncryptionArray, count, 35, SixSpaceLocked)
    elif seven == 7:
        ArrayAdder(EncryptionArray, count, 31, SevenQuoteLocked)
        ArrayAdder(EncryptionArray, count, 32, SevenAphostropheLocked)
        ArrayAdder(EncryptionArray, count, 33, SevenSemicolonLocked)
        ArrayAdder(EncryptionArray, count, 34, SevenColonLocked)
        ArrayAdder(EncryptionArray, count, 35, SevenSpaceLocked)
    elif seven == 8:
        ArrayAdder(EncryptionArray, count, 31, EightQuoteLocked)
        ArrayAdder(EncryptionArray, count, 32, EightAphostropheLocked)
        ArrayAdder(EncryptionArray, count, 33, EightSemicolonLocked)
        ArrayAdder(EncryptionArray, count, 34, EightColonLocked)
        ArrayAdder(EncryptionArray, count, 35, EightSpaceLocked)
    elif seven == 9:
        ArrayAdder(EncryptionArray, count, 31, NineQuoteLocked)
        ArrayAdder(EncryptionArray, count, 32, NineAphostropheLocked)
        ArrayAdder(EncryptionArray, count, 33, NineSemicolonLocked)
        ArrayAdder(EncryptionArray, count, 34, NineColonLocked)
        ArrayAdder(EncryptionArray, count, 35, NineSpaceLocked)



    count = count + 1



y = 0
file = open("EncryptionKey.csv","w")
while y != 10000000:
    data = str(EncryptionArray[y])
    RawData = data.replace('[','')
    RawData = RawData.replace(' ','')
    RawData = RawData.replace(']','')
    RawData = RawData.replace("'",'')        
    newRec = RawData + '\n'
    file.write(newRec)
    y = y + 1


'''
    EncryptionArray[count][1] = LetterFinder(one,two,three,four,five,six,seven,code,letter)    
    EncryptionArray[count][2] = code
    EncryptionArray[count][3] = code
    EncryptionArray[count][4] = code
    EncryptionArray[count][5] = code
    EncryptionArray[count][6] = code
    EncryptionArray[count][7] = code
    EncryptionArray[count][8] = code
    EncryptionArray[count][9] = code
    EncryptionArray[count][10] = code
    EncryptionArray[count][11] = code
    EncryptionArray[count][12] = code
    EncryptionArray[count][13] = code
    EncryptionArray[count][14] = code
    EncryptionArray[count][15] = code
    EncryptionArray[count][16] = code
    EncryptionArray[count][17] = code
    EncryptionArray[count][18] = code
    EncryptionArray[count][19] = code
    EncryptionArray[count][20] = code
    EncryptionArray[count][21] = code
    EncryptionArray[count][22] = code
    EncryptionArray[count][23] = code
    EncryptionArray[count][24] = code
    EncryptionArray[count][25] = code
    EncryptionArray[count][26] = code
    EncryptionArray[count][27] = code
    EncryptionArray[count][28] = code
    EncryptionArray[count][29] = code
    EncryptionArray[count][30] = code
    EncryptionArray[count][31] = code
    EncryptionArray[count][32] = code
    EncryptionArray[count][33] = code
    EncryptionArray[count][34] = code
    EncryptionArray[count][35] = code

'''


