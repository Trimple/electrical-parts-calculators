# resistor dividers calculator

import sys
import os
import getopt

typicalValues = [1, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2, 2.2, 2.4, 2.7, 3, 3.3, 3.6, 3.9, 4.3, 4.7,
            5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1, 10]

searchValues = [0.1, 0.11, 0.12, 0.13, 0.15, 0.16, 0.18, 0.2, 0.22, 0.24, 0.27, 0.3, 0.33, 0.36, 0.39, 0.43, 0.47, 0.51, 0.56,
                0.62, 0.68, 0.75, 0.82, 0.91, 1, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2, 2.2, 2.4, 2.7, 3, 3.3, 3.6, 3.9, 4.3, 4.7,
                5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1, 11, 12, 13, 15, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39, 43, 47, 51, 56,
                62, 68, 75, 82, 91 ]

inputVoltage = None
outputVoltage = None
resistance1 = None
resistance2 = None
accuracyR1 = 0.01
accuracyR2 = 0.01

def calculateResistors(inVoltage, outVoltage, acc1, acc2):
    biggerR1 = 1000;
    biggerR2 = 1;
    smallerR1 = -1000;
    smallerR2 = 1;

    dividingCoef = (inVoltage - outVoltage)/outVoltage
    for res1 in searchValues:
        for res2 in searchValues:
            if (res2 > res1):
                break
            if (abs(res1/res2 - dividingCoef) < 0.0001): #found exact value
                print("Exact dividing coefficient have been found!\nDivider parameters:")
                calculateDividerParams(inVoltage, res1*10000, res2*10000, acc1, acc2)
                return 1
            if((res1/res2 - dividingCoef) < (biggerR1/biggerR2 - dividingCoef) and (res1/res2 - dividingCoef) > 0):
                biggerR1 = res1
                biggerR2 = res2
            if((res1/res2 - dividingCoef) > (smallerR1/smallerR2 - dividingCoef) and (res1/res2 - dividingCoef) < 0):
                smallerR1 = res1
                smallerR2 = res2
    print("Couldn't find exact dividing coefficient.\nDivider parameters for closest bigger coefficient:")
    calculateDividerParams(inVoltage, biggerR1*10000, biggerR2*10000, acc1, acc2)
    print("Divider parameters for closest smaller coefficient:")
    calculateDividerParams(inVoltage, smallerR1*10000, smallerR2*10000, acc1, acc2)

def calculateR1(inVoltage, outVoltage, res2, acc1, acc2):
    LowerResistance = 0
    exactValue = res2*(inVoltage - outVoltage)/outVoltage
    resistanceFactor = 0
    while(exactValue / 10 > 1):
        resistanceFactor = resistanceFactor + 1
        exactValue = exactValue / 10
    for value in typicalValues:
        if (abs(value - exactValue) < 0.001):       #Way to compare float numbers
            print("\nResistor R1 value is\033[92m %.1f Ohm \033[0m" % (exactValue*pow(10, resistanceFactor)))
            print("divider parameters:")
            calculateDividerParams(inVoltage, value*pow(10, resistanceFactor), res2, acc1, acc2)
            break

        elif (value > exactValue):
            print("\nResistor exact value is\033[91m %.1f Ohm\033[0m, but it is not standart. \nClosest standart value lower than exact one is %.1f Ohm. Parameters of divider:" % (exactValue*pow(10, resistanceFactor), LowerResistance*pow(10, resistanceFactor)))
            calculateDividerParams(inVoltage, LowerResistance*pow(10, resistanceFactor), res2, acc1, acc2)
            print("Closest standart value higher than exact one is %.1f Ohm. Parameters of divider:" % (value*pow(10, resistanceFactor)))
            calculateDividerParams(inVoltage, value*pow(10, resistanceFactor), res2, acc1, acc2)
            break

        else:
            LowerResistance = value

def calculateR2(inVoltage, outVoltage, res1, acc1, acc2):
        LowerResistance = 0
        exactValue = res1*outVoltage/(inVoltage - outVoltage)
        resistanceFactor = 0
        while(exactValue / 10 > 1):
            resistanceFactor = resistanceFactor + 1
            exactValue = exactValue / 10
        for value in typicalValues:
            if (abs(value - exactValue) < 0.001):       #Way to compare float numbers
                print("\nResistor R1 value is\033[92m %.1f Ohm \033[0m" % (exactValue*pow(10, resistanceFactor)))
                print("divider parameters:")
                calculateDividerParams(inVoltage, res1, value*pow(10, resistanceFactor), acc1, acc2)
                break

            elif (value > exactValue):
                print("\nResistor exact value is\033[91m %.1f Ohm\033[0m, but it is not standart. \nClosest standart value lower than exact one is %.1f Ohm. Parameters of divider:" % (exactValue*pow(10, resistanceFactor), LowerResistance*pow(10, resistanceFactor)))
                calculateDividerParams(inVoltage, res1, LowerResistance*pow(10, resistanceFactor), acc1, acc2)
                print("Closest standart value higher than exact one is %.1f Ohm. Parameters of divider:" % (value*pow(10, resistanceFactor)))
                calculateDividerParams(inVoltage, res1, value*pow(10, resistanceFactor), acc1, acc2)
                break

            else:
                LowerResistance = value

def calculateDividerParams(inVoltage, res1, res2, acc1, acc2):
    outVoltage = inVoltage*res2/(res1 + res2)
    floatingCurrent = inVoltage/(res1 + res2)*1000
    powerDissipation = floatingCurrent*inVoltage
    outputError = (inVoltage/outVoltage*(res2*(1 + acc2))/(res1*(1 - acc1) + res2*(1 + acc2)) - 1)*100
    print("\nInput voltage: %.2f V" % (inVoltage))
    print("Resistance of R1: " + str(res1) + " Ohm")
    print("Resistance of R2: " + str(res2) + " Ohm")
    print("Accuracy: R1 - " + str(acc1) + ", R2 - " + str(acc2))
    print("=====================================")
    print("Output voltage: %.2f V" % (outVoltage))
    print("Floating current: %.2f mA" % (floatingCurrent))
    print("Power dissipation: %.2f mW" % (powerDissipation))
    print("Max output error: %.2f" % (outputError) + " %\n")


if __name__ == '__main__':
    os.system("cls")
    try:
        opts, args = getopt.getopt(sys.argv[1:],"",["ov=", "iv=", "r1=", "r2=", "a1=", "a2="])
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--ov':
            try:
                outputVoltage = float(arg)
            except:
                print("ov argument is not a number")
                sys.exit(10)
            if(outputVoltage < 0):
                print("Output voltage can't be negative!")
                sys.exit(30)

        elif opt == '--iv':
            try:
                inputVoltage = float(arg)
            except:
                print("iv argument is not a number")
                sys.exit(11)
            if(inputVoltage < 0):
                print("Input voltage can't be negative!")
                sys.exit(31)

        elif opt == '--r1':
            try:
                resistance1 = float(arg)
            except:
                print("r1 argument is not a number")
                sys.exit(12)
            if(resistance1 < 0):
                print("Resistance can't be negative!")
                sys.exit(32)

        elif opt == '--r2':
            try:
                resistance2 = float(arg)
            except:
                print("r2 argument is not a number")
                sys.exit(13)
            if(resistance2 < 0):
                print("Resistance can't be negative!")
                sys.exit(33)

        elif opt == '--a1':
            try:
                accuracyR1 = float(arg)
            except:
                print("a1 argument is not a number!")
                sys.exit(14)
            if(accuracyR1 > 0.5):
                print("Accuracy of R1 is too poor!")
                sys.exit(20)
            elif(accuracyR1 < 0):
                print("Accuracy can't be negative!")
                sys.exit(34)

        elif opt == '--a2':
            try:
                accuracyR2 = float(arg)
            except:
                print("a2 argument is not a number!")
                sys.exit(15)
            if(accuracyR2 > 0.5):
                print("Accuracy of R2 is too poor!")
                sys.exit(21)
            elif(accuracyR2 < 0):
                print("Accuracy can't be negative!")
                sys.exit(35)

    if(inputVoltage != None and outputVoltage != None):
        if(outputVoltage >= inputVoltage):
            print("input voltage can't be bigger than output one!")
            sys.exit(40)
        if(resistance1 != None and resistance2 != None):
            print("Wrong set of parameters!")
            sys.exit(41)

        elif(resistance1 == None and resistance2 == None):
            calculateResistors(inputVoltage, outputVoltage, accuracyR1, accuracyR2)

        elif(resistance1 == None and resistance2 != None):
            calculateR1(inputVoltage, outputVoltage, resistance2, accuracyR1, accuracyR2)

        elif(resistance1 != None and resistance2 == None):
            calculateR2(inputVoltage, outputVoltage, resistance1, accuracyR1, accuracyR2)

    elif(inputVoltage != None and outputVoltage == None and resistance1 != None and resistance2 != None):
        calculateDividerParams(inputVoltage, resistance1, resistance2, accuracyR1, accuracyR2)

    elif(inputVoltage == None and outputVoltage != None and resistance1 != None and resistance2 != None):
        calculateDividerParams(outputVoltage*(resistance1 + resistance2)/resistance2, resistance1, resistance2, accuracyR1, accuracyR2)

    else:
        print("Wrong set of parameters!")
        sys.exit(41)
