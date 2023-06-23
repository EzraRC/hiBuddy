#Import the ping module to be able to use ICMP echo requests.
from ping3 import ping, verbose_ping
# Import the 'threading' module to enable multi-threading capabilities
import threading


#checkHost method
def checkHost(host):

    # Save the delay from the ping method
    delay = ping(host)

    # If there is no delay, then IP is alive
    if delay is not None:
        print(f"{host:>15} - alive")
    
    # Else the IP address does not have a live host
    else:
        print(f"{host:>15} - not reachable")


def main():
    print('\n=========================== LIVE HOST ===========================')
    print('                   IP Address Format: x.x.x.x')
    print('where x can be a one (1), two (11), or three (111) digit number')
    print('  NOTE: x cannot be less than 0 AND cannot be more than 255\n\n')

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

                #Increment the last octet
                host = f"{startOctets[0]}.{startOctets[1]}.{startOctets[2]}.{i}"

                # Create a new thread to execute the 'checkHost' function with the specified 'host' argument
                thread = threading.Thread(target=checkHost, args=(host,))

                # Start the thread, initiating the execution of the 'checkHost' function
                thread.start()

                # Add the thread to the 'threads' list for tracking and potential synchronization purposes
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
