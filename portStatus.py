# Import the 'socket' module to provide access to networking functionality
import socket
# Import the 'threading' module to enable multi-threading capabilities
import threading


#tcpConnect method
def tcpConnect(ip, portNumber, delay, output):
    # Create a TCP socket and set its options
    tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set the socket option SO_REUSEADDR to allow reusing the local address, avoiding "Address already in use" errors
    tcpSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Set the timeout for the socket operations to the specified delay value
    tcpSock.settimeout(delay)

    # Attempt to connect to the IP and port

    # If the connection is made, mark the port as Open
    try:
        tcpSock.connect((ip, portNumber))
        output[portNumber] = 'Open'
    # If the connection times out, mark the port as filtered
    except socket.timeout:
        output[portNumber] = 'Filtered'
    except:
        # If connection fails, mark the port as empty
        output[portNumber] = ''


#scanPorts Method
def scanPorts(hostIP, delay):
    # To run tcpConnect simultaneously
    threads = []
    # For printing purposes
    output = {port: '' for port in range(10000)}

    # Spawning threads to scan ports
    for i in range(10000):
        # Create a thread for each port to be scanned
        t = threading.Thread(target=tcpConnect, args=(hostIP, i, delay, output))
        threads.append(t)

    # Starting threads
    for i in range(10000):
        # Start each thread
        threads[i].start()

    # Locking the main thread until all threads complete
    for i in range(10000):
        # Wait for each thread to finish execution
        threads[i].join()

    # Prompt
    print('\n====== RESULTS ======')

    # Printing listening ports from 1 to 10000
    for port, status in output.items():

        #If not closed then print the port and it's status
        if status != '':
            print(f"Port {port}: {status}")

    # Print note
    print('\nNB: Ports not listed can be assumed to be in a \'CLOSED\' state')


#Main method - Conducts the port scan and prints the statuses
def main():
    #Get the target ip address
    hostIP = input("Enter target IP address: ")
    
    # Let user know the program is loading
    print("Scanning ports, please wait.....\n")

    # Prompt for target IP address
    scanPorts(hostIP, 1)

# Run main
if __name__ == "__main__":
    main()
