def get_range():
          
    x = int(input("Please enter your first value: "))
    y = int(input("Please enter your second value: "))
    value_check(x, y)


def value_check(x, y):

    if x < 0 :

        if y < x :

            print("\nInvalid input. Please try again")
            get_range()

        else:

            find_disarium(x, y)

    else:

        if y < x :

            print("Invalid input. Please try again")
            get_range()

        else:

            find_disarium(x, y)

def find_disarium(x, y):

    dString = ""

    while (x <= y):

        numberString = str(x)
        stringLength = len(numberString)

        i = 0
        k = 0
        sum = 0

        for i in range (0, stringLength):
            
            sum += int(numberString[k])**(i + 1)
            i += 1
            k += 1

        if x == sum :

            dString += str(numberString) + " | "

        x += 1

    print(dString)

print("This program checks for disarium numbers." +
        "\nYou will be asked to enter a range of numbers." +
        "\nYour first number should not be greater than your second." +
        "\nNeither number your enter should be a negative.")

get_range()
