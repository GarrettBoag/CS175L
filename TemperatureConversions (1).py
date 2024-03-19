def main():
    controlLoop()

def convertToKelvin(f):
    kelvin = ((5/9)*f) + 459.67
    return kelvin
    pass

def convertToCentigrade(fahren):
    #Take in the fahrenheit temp as an argument
    cent = (fahren - 32) * (5/9)
    return cent
    pass

def doConversion():
    fahren = getFahrenheit()# get back Fahrenheit
    kelvin = convertToKelvin(fahren)# send Fahrenheit get back Kelvin
    cent = convertToCentigrade(fahren)# sends Fahrenheit gets back Centigrade
    print(f'Fahrenheit: {fahren:.2f} Kelvin {kelvin:.2f} Centigrade: {cent:.2f}')
    print()
    pass

def repeat():
    conv_num = input("How many conversions would you like to do this time?")
    for x in range(int(conv_num)):
        doConversion()
    pass

def controlLoop():
    y_n = input('Do you want to do some conversions(Yes or No)?')
    if y_n == 'yes':
        repeat()
    pass

def getFahrenheit():
    fahren = int(input('Enter Fahrenheit temperature (must be -50 to 130):'))
    while fahren > 130 or fahren < -30:
        fahren = int(input("--Error--\nEnter a value from -50 to 130"))
    return int(fahren)
    pass

# This code will call the 'main' function if the entire program was run.
if __name__ == '__main__':
    main()
