#For loops start
#import OS because we will make python use operating system to send ICMP packets.
import os


#create a variable to be entered by user. and it should be a string because we will enter IP addresses.
ip = str(input("please enter the IP address of your test:"))

#creating a for loop that will be counting to 5 times to re-occur for whatever is inside the loop body
for try_ping in range(5):
    print("ICMP packet is ", try_ping)
#below is how we send ping command using the windows cmd with the variable value acquired from the user input for the IP.    
    pinging= os.popen(f"ping -n 1 {ip}").read()
#this is a condition to see the output from the ping and if the text recevied = 1 was in the ping output then print destination is fine, 
# otherwise print destination is not reachable.
#note if you want to change the number of packets sent in the pinging line then you need to change the received = 1 to something else matching the other number.
    if "Received = 1" in pinging:
        print ("pinging destination is fine")
    else:
        print ("Destination is not reachable")