# Function to add sleep data
def add_sleep():
    hours = input("Enter today's sleep hours: ")

    file = open("sleep.txt", "a")   # append mode
    file.write(hours + "\n")
    file.close()

    print("Sleep data saved!")

# Function to analyze sleep
def analyze_sleep():
    try:
        file = open("sleep.txt", "r")
        data = file.readlines()
        file.close()

        if len(data) == 0:
            print("No data available!")
            return

        sleep_hours = []

        for line in data:
            sleep_hours.append(float(line.strip()))

        avg = sum(sleep_hours) / len(sleep_hours)

        print("Average Sleep:", avg)

        if avg < 6:
            print("Poor Sleep")
        elif avg <= 8:
            print("Normal Sleep")
        else:
            print("Healthy Sleep")

    except FileNotFoundError:
        print("No data file found!")

# Menu
while True:
    print("\n1. Add Sleep Data")
    print("2. Analyze Sleep")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_sleep()
    elif choice == 2:
        analyze_sleep()
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
