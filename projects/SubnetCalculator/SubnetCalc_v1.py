#   Learning code for Pything for Network Engineering.


#   On taking an IP address and a subnet mask:

#   Outuput:
#       Network Address
#       Broadcast Address
#       Number of Valid hosts per subnet
#       Wildcard Mask
#       Mask bits

#   Offer to generate random IP address for subnet? [y/n]
#   Output Random IP address

#   <continue>

#   Refer application1.png for logical flow

###############################################################################################

import sys
import random

def user_input_ip():

    ''' This function carries out a number of tests to check that the IP is 
    valid.
    
    A vadlid IP address has four octets, deliminated by '.'
    
    The following addresses are not considered valid:
        224.x.x.x - multicast addresses
        127.x.x.x - reserved addresses
        169.254 - windows default adddresses when no DHCP is found '''

    while True:
        user_input = raw_input("Enter an IP address in the form of a.b.c.d: ")
        octets = user_input.split('.')
        print len(octets)

        if len(octets) != 4:
            print "The input needs to be four octets, for example 10.10.10.10, where the '.' seperates each octet."
            continue
        elif octets[0] == "127":
            print "Addresses beginning in '127' are reserved local IPs and not valid."
            continue
        elif octets[0] == "224":
            print "Addresses beginning in '224' are multicast addresses and not valid."
            continue
        elif octets[0] == "169" and octets[1] == "254":
            print "Addresses beginning in '169.254' are Microsoft default addresses and not valid."
            continue
        elif not (1 <= int(octets[0]) <= 223 \
            and 0 <= int(octets[1]) <= 255 \
            and 0 <= int(octets[2]) <= 255 \
            and 0 <= int(octets[3]) <= 255):
            print "One or more octets is out of range. Please check and re-input."
            continue
        else:
            return octets
            break

def subnet_check():

    # We need a list of valid subnet mask octets for later
    valid_octets = ['0', '128','192','224','240','248','252','254','255' ]
 
    while True:

        user_subnet = raw_input("Please enter subnet: ")
        subnet_octets = user_subnet.split('.')
        if len(subnet_octets) != 4:
            print "Subnet needs to be entered as x.x.x.x, three '.' seperating the four octets."

        elif subnet_octets[0] not in valid_octets or\
             subnet_octets[1] not in valid_octets or\
             subnet_octets[2] not in valid_octets or\
             subnet_octets[3] not in valid_octets:
            print "One or more octets is not valid. Valid octets are: "
            for octet in valid_octets:
                print octet
            continue

        elif subnet_octets[0] <= subnet_octets[1] <= subnet_octets[2] \
            <= subnet_octets[3]:
            print "Each subsequent subnet octet from the first must be equal to or lesser than the previous"
            continue 
            
        else:
            return subnet_octets
    


ip_address = user_input_ip()
print ip_address

subnet_octets = subnet_check()
print subnet_octets

