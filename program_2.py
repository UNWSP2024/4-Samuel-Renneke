#Movie Tix
#Samuel Renneke, 2/12/2026
def main():
    tickets = int(input("How many tickets would you like for Titanic? "))
    tickets = tickets + int(input("How many tickets would you like for Saving Private Ryan? "))
    tickets = tickets + int(input("How many tickets would you like for Despicable Me? "))
    for i in range(tickets):
        print("Ticket " + str(i + 1))
if __name__ == '__main__':
    main()
