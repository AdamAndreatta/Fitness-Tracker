import argparse
import os
import time

print("Welcome to fitness Tracker!\n\nWelcome to fitness tracker your one stop shop for all your fitness needs here,\nyou will generate workouts track your dietary consumption and convert from various weights kg -> lbs\n")

next = input("press 1 to continue to the main menu\n")
os.system('cls')
trackList = dict()

tracker_saved = False

while True:
    print("======Main Menu======\n")
    print("Welcome! below are the solutions for all your needs fitness.\nJump around and enjoy the features and create\nand track all your fitness needs.\n")
    feature = input("1. Convert weight value\n2. Dietary Tracker\n3. Create a workout\n5. Exit Program\n")

    def weightConverter():
        while True:
            print("======Weight Converter======")
            conversion = input("Welcome to weight Conversion!\nPlease select your conversion of choice!\n1. kg to lbs\n2. lbs to kgs\n3. return to main menu\n")

            if conversion == "1":
                kgs = input("Please enter the amount you would like to convert.\n")

                f = open("conversion.txt", "w")
                f.write(f"pounds:{kgs}")
                f.close()

            elif conversion == "2":
                pounds = input("Please enter the amount you would like to convert.\n")

                f = open("conversion.txt", "w")
                f.write(f"kgs:{pounds}")
                f.close()

            elif conversion == "3":
                os.system('cls')
                return

            else:
                print("please select an option that is listed below\n")
                continue

    def dietaryTracker():
        while True:
            print("======Dietary Tracker======")
            print("Welcome to dietary tracker the only tool you need to help you get your diet on right.\nBelow you can add, remove, edit, and search all the items you add to your caloric tracker this will help you\nkeep a good tab on what and when you're eating during the week!\n")

            selection = input("Please select an option\n1. Insert new item\n2. View all current items\n3. Convert table to csv\n4. Edit an item in your table\n5. Remove an item from your table\n6. Search an item from your table\n7. Save table\n8. Return to main menu\n")

            if selection == "1":
                item = input("Please type the name of the item you would like to insert\n")
                calories = input("Please enter the calorie amount of the item\n")
                quantity = input("Please enter the quantity of the item your are adding\n")

                trackList[item] = [f"calories:{calories}", f"quantity:{quantity}"]
                continue

            elif selection == "2":
                for key in trackList:
                    print(f"{key}:")
                    for value in trackList[key]:
                        print(f"{value}")

            elif selection == "4":
                name = input("Please enter the name of the item you wish to edit.\n")
                edited = input("Please select what you would like to edit.\n1. Calories\n2. quantity\n")

                if edited == "1":
                    amount = input("Please input the amount you wish to change it too.\n")
                    trackList[name][0] = f"calories: {amount}"

                if edited == "2":
                    quantity = input("Please input which quantity you wish to insert.\n")
                    trackList[name][1] = f"quantity: {quantity}"

            elif selection == "5":
                name = input("Please enter the name of the item you wish to delete.\n")
                trackList.pop(f"{name}")

            elif selection == "6":
                name = input("Please enter the name of the item you wish to search.\n")

                if name not in trackList:
                    while True:
                        name = input("Name entered is invalid please enter a valid item.\n")
                        if name in trackList:
                            break

                calories = trackList[name][0]
                quantity = trackList[name][1]

                print(f"{name}\n{calories}\n{quantity}")

            elif selection == "7":
                f = open("Tracker.txt", "w")
                for key in trackList:
                    for item in trackList[key]:
                        save = f"{key}: {item}\n"
                        f.write(save)
                f.close()
                print("Your table has been saved!")

            elif selection == "8":
                os.system('cls')
                return

    def workoutGenerator():
        print("======Workout Generator======")
        print("Please select an option to create a workout for your unique situation! This tool makes for a great way to change up\nyour workout plan when youre not sure what you're feeling!\n")
        print("1. Generate a full workout\n2. Generate for 1 body part\n3. Save Workout\n5. Return to main menu\n")

        option = input("Please select an option listed below\n")
        if option == "1":
            os.system('cls')

            f = open("Workout.txt", "w")
            f.write("full")
            f.close()

        elif option == "2":
            os.system('cls')

            bodyPart = input("Please select which body part you would like a workout generated for. (Arms, Legs, Back, Chest)\n")

            f = open("Workout.txt", "w")
            f.write(f"single:{bodyPart}")
            f.close()

        elif option == "3":
            os.system('cls')

            print("micro service not built for this yet")

        elif option == "5":
            os.system('cls')
            return

    if feature == "1":
        os.system('cls')
        weightConverter()

    elif feature == "2":
        os.system('cls')
        dietaryTracker()

    elif feature == "3":
        os.system('cls')
        workoutGenerator()

    elif feature == "5":
        os.system('cls')

        if tracker_saved is False:
            response = input("Your current tracker is not save if you choose to exit the session it will be deleted.\n Are you sure you wish to exit? Press 1. exit wihtout saving\n 2. save and exit\n")

            if response == "1":
                break

            if response == "2":
                f = open("Tracker.txt", "w")
                for key in trackList:
                    for item in trackList[key]:
                        save = f"{key}: {item}\n"
                        f.write(save)
                f.close()
                break
