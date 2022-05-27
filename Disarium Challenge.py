def get_range():
    firstPage = int(input("Please enter your first value: "))
    lastPage = int(input("Please enter your second value: "))
    value_check(firstPage, lastPage)

def value_check(firstPage, lastPage):
    if firstPage < 0 :
        if lastPage < firstPage :
            print("\nInvalid input. Please try again")
            get_range()

        else:
            disariumPrint = find_disarium(firstPage, lastPage)
            disariumPrint = disariumPrint[:-3]
            print(disariumPrint)
            
    else:
        if lastPage < firstPage :
            print("Invalid input. Please try again")
            get_range()

        else:
            disariumPrint = find_disarium(firstPage, lastPage)
            disariumPrint = disariumPrint[:-3]
            print(disariumPrint)
            

def find_disarium(firstPage, lastPage):

    disariumString = ""

    while (firstPage <= lastPage):
        numberString = str(firstPage)
        stringLength = len(numberString)
        exponent = 0
        index = 0
        sum = 0

        for exponent in range (0, stringLength):
            sum += int(numberString[index])**(exponent + 1)
            exponent += 1
            index += 1

        if firstPage == sum :
            disariumString += str(numberString) + " | "

        firstPage += 1

    return disariumString

print("This program checks for disarium numbers." +
        "\nYou will be asked to enter a range of numbers." +
        "\nYour first number should not be greater than your second." +
        "\nNeither number your enter should be a negative.")

get_range()
