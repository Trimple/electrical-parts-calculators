# resistor deviders calculator

import sys
import getopt

inputVoltage = None
outputVoltage = None
resistance1 = None
resistance2 = None
resistanceFactor = None
accuracyR1 = 0.01
accuracyR2 = 0.01


def calculateDeviderParams(inVoltage, res1, res2, acc1, acc2):
    outVoltage = inVoltage*res2/(res1 + res2)
    floatingCurrent = inVoltage/(res1 + res2)*1000
    powerDissipation = floatingCurrent*inVoltage
    outputError = (inputVoltage/outVoltage*(res2*(1 + acc2))/(res1*(1 - acc1) + res2*(1 + acc2)) - 1)*100
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
    try:
        opts, args = getopt.getopt(sys.argv[1:],"",["ov=", "iv=", "r1=", "r2=", "a1=", "a2="])
        print(opts)
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
            print("input voltage can't be bigger then output one!")
            sys.exit(40)
        if(resistance1 != None and resistance2 != None):
            print("Wrong set of parameters!")
            sys.exit(41)

        elif(resistance1 == None and resistance2 == None):
            print("Calculating resistors values")

        elif(resistance1 == None and resistance2 != None):
            print("Calculating resistor 1 value")

        elif(resistance1 != None and resistance2 == None):
            print("Calculating resistor 2 value")

    elif(inputVoltage != None and outputVoltage == None and resistance1 != None and resistance2 != None):
        calculateDeviderParams(inputVoltage, resistance1, resistance2, accuracyR1, accuracyR2)

    elif(inputVoltage == None and outputVoltage != None and resistance1 != None and resistance2 != None):
        print("Calculating input voltage")

    else:
        print("Wrong set of parameters!")
        sys.exit(41)

    #print("i'm here")
