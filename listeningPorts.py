# Import the 'socket' module to provide access to networking functionality
import socket
# Import the 'threading' module to enable multi-threading capabilities
import threading


def tcpConnect(ip, portNumber, delay, output):
    # Create a TCP socket and set its options
    tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set the socket option SO_REUSEADDR to allow reusing the local address, avoiding "Address already in use" errors
    tcpSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Set the timeout for the socket operations to the specified delay value
    tcpSock.settimeout(delay)

    try:
        # Attempt to connect to the IP and port
        tcpSock.connect((ip, portNumber))
        output[portNumber] = 'Listening'
    except:
        # If connection fails, mark the port as empty
        output[portNumber] = ''


def scanPorts(hostIP, delay):
    # To run tcpConnect simultaneously
    threads = []
    # For printing purposes
    output = {}

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

    #Prompt
    print('\nThe following ports are listening:')
    # Printing listening ports from 1 to 10000
    for i in range(10000):
        
        # If the port's status is 'Listening'
        if output[i] == 'Listening':
            
            # Print the port number
            print(str(i), end = ' ')


def main():
    #Get the target ip address
    hostIP = input("Enter target IP address: ")
    
    # Prompt for target IP address
    scanPorts(hostIP, 1)

# Run main
if __name__ == "__main__":
    main()