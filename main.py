import datetime
import os
import sys

# clearScreen method - Clears the screen for cleaner output and improved readability
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


# displayMenu - Provides menu for the user
def displayMenu():
    print("========================= hiBuddy! ========================\n")
    print("1. Port Scan - Identify port states for a given IP address")
    print("0. Exit\n")


# printDisclaimer
def printDisclaimer():
    lines = [
        "hiBuddy is a complete Network Enumeration Tool with a major focus on reconnaissance features",
        "such as Port Scanning, System Information, and much more. The creator of this program, EzraRC,",
        "is not responsible for any misuse or damage done as a result of the program. hiBuddy should be",
        "used to help cybersecurity students learn about reconnaissance and how they can create scripts",
        "and programs to help automate the procedure. Before using this program, PLEASE be aware of your",
        "country or state's cybersecurity and information technology laws. Thank you! :)",
        "\n\"I, the current user, am responsible for all of my actions done while using this program.\"",
        "Date: {}".format(datetime.datetime.now())
    ]

    print("======================= PLEASE READ THIS DISCLAIMER BEFORE CONTINUING =======================\n")
    for line in lines:
        print(line)
    print("\n=============================================================================================")
    input("By pressing ENTER, you agree to the statement above.")


# userChoice - Provides the appropriate output based on the user's choice
def validateInput():
    userChoice = input("Enter the number of your choice: ")

    # Choices

    # 1 - Scan ports and display their states
    if userChoice == "1":
        clearScreen()

        # Run portStatus program
        os.system("python portStatus.py")
        print("====================== OPERATION FINISHED! ======================")
        input("\nPress ENTER to continue...")

    # 0 - Exit the program
    elif userChoice == "0":
        print("\nThanks for using! Bye bye and take care :)")
        sys.exit()

    # Invalid input
    else:
        clearScreen()
        print("================= ERROR // ERROR // ERROR //=================")
        print("\nAn invalid choice was entered")
        print("Please use a choice from the options provided within the menu\n")
        print("Thank you!")
        print("\n=============================================================")
        input("Press ENTER to continue...")


if __name__ == "__main__":
    printDisclaimer()
    while True:
        clearScreen()
        displayMenu()
        validateInput()
