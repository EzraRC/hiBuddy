# hiBuddy
(WORK IN PROGRESS)

This app is a complete Network Enumeration Tool with a major focus on reconnaissance features. Hopefully, it will feature a GUI for ease of use so users will not have to memorize command lines. I am also using this app to practise my scripting and coding skills for cybersecurity, so feel free to reach out to me for help, or to give me advice on how to improve my program :)

I have also provided a 'references' text file to keep track of all the resources I used and well, just to give em credit for helping me out too.

## Setup

### How to Install
- Navigate into the 'files' folder.
- Run the batch file (setup.bat) and it'll install everything you need.
<br />**(NB: You may need to give it admin privileges to install Python 3)**

### How to Run
- Navigate into the 'src' folder.
- Launch the main.py file using an IDE of your choice.
- Have fun and learn well! :)

### How to Use
- Enter the number for the option that you would like to use.
<br /> **(EXAMPLE: Type '1' if you would like to use the Port Scan option)**
- Follow the on-screen instructions.

## Features
**Port Scan**
<br />Identifies the states of ports ranging from 0 to 9999, listing if they are 'Open' or 'Filtered'. If the port number is not listed, we can assume that the port is closed (granted that the program works correctly).

**Live Hosts**
<br />Given a range of IP Addresses, it will use an ICMP to send echo request messages. If a reply is received, then it will list that the address is 'Alive', otherwise it will note that the IP Address currently tested is not reachable. 
