from ping3 import ping, verbose_ping
import threading


def checkHost(host):
    delay = ping(host)
    if delay is not None:
        print(f"{host:>15} - alive")
    else:
        print(f"{host:>15} - not reachable")


def main():
    print('\n=========================== LIVE HOST ===========================')
    print('                   IP Address Format: x.x.x.x')
    print('where x can be a one (1), two (11), or three (111) digit number\n')

    while True:
        # Get the target IP address range
        startIP = input("Enter starting IP address: ")
        endIP = input("Enter ending IP address: ")

        # If start and end IP addresses format is valid
        startOctets = startIP.split(".")
        endOctets = endIP.split(".")
        if len(startOctets) == 4 and all(o.isdigit() and 0 <= int(o) <= 255 for o in startOctets) and len(endOctets) == 4 and all(o.isdigit() and 0 <= int(o) <= 255 for o in endOctets):
            # Let the user know the program is loading
            print("\nChecking hosts, please wait.....\n")

            threads = []
            # Iterate over the IP range and check each host
            for i in range(int(startOctets[3]), int(endOctets[3]) + 1):
                host = f"{startOctets[0]}.{startOctets[1]}.{startOctets[2]}.{i}"
                thread = threading.Thread(target=checkHost, args=(host,))
                thread.start()
                threads.append(thread)

            # Wait for all threads to finish
            for thread in threads:
                thread.join()

            break

        # Else IP address entered is invalid
        else:
            yesOrNo = input("\nAn invalid IP address was entered, would you like to re-enter? (y/n): ")

            # Restart for user to re-enter IP address
            if yesOrNo.lower() == "y":
                print()
                continue

            # Else just end the program
            else:
                break


# Run main
if __name__ == "__main__":
    main()
