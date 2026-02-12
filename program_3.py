#Average Rainfall
#Samuel Renneke, 2/12/2026
def main():
    years = int(input("How many years would you like to input? "))
    rain = 0

    for i in range(years):
        months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
        for x in range(12):
            month = months[x]
            rain = rain + int(input("How many inches of rain in " + month + "? "))

    print("Rain over " + str(years * 12) + " months:")
    print("Total rain = " + str(rain) + " inches")
    print("Average rain = " + str(rain / (years * 12)) + " inches per month")

if __name__ == '__main__':
    main()main()
