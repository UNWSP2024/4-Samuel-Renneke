#Bank Balance
#Samuel Renneke, 2/12/2026

def main():
    budget = float(input("What's your budget? "))
    spent = 1.0
    total = 0
    difference = 0


    while True:
        spent = float(input("How much money did you spend? \n Enter 0 to see final budget: "))

        if spent == 0:
            break

        total += spent
        difference = budget - total

    if difference > 0:
            print("You have " + str(difference) + " more dollars to spend.")
    else:
            print("You are " + str(difference * -1) + " over budget.")




if __name__ == '__main__':
    main()
