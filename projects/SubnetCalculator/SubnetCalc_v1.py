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

def ip_address_valid(ip):
    
    ''' This function carries out a number of tests to check that the IP is 
    valid. '''
    octets = ip.split('.')
    def four_octets():
        '''Check that there are four octets in the input.'''
        return len(octets) == 4
    def reserved_local():
        return octets[0] == "127"
    def multicast():
        return octets[0] == "224"
    def windows_default():
        return octets[0] == "169" and octets[1] == "254"
    def valid_octets():
        return 1 <= int(octets[0]) <= 223 \
        and 0 <= int(octets[1]) <= 255 \
        and 0 <= int(octets[2]) <= 255 \
        and 0 <= int(octets[3]) <= 255

    if four_octets() == False:
        print "The input needs to be four octets, for example 10.10.10.10, where the '.' seperates each octet."
    elif reserved_local() == True:
        print "Addresses beginning in '127' are reserved local IPs and not valid."
    elif multicast() == True:
        print "Addresses beginning in '224' are multicast addresses and not valid."
    elif windows_default() == True:
        print "Addresses beginning in '169.254' are Microsoft default addresses and not valid."
    elif valid_octets() == False:
        print "One or more octets is out of range. Please check and re-input."
    else:
        return octets




def user_input_ip():

    ''' The purpose of this function is to get an IP address form the user
    and check that the IP is valid. '''

    user_input = raw_input("Enter an IP address in the form of a.b.c.d: ")
    return ip_address_valid(user_input)

ip_address = user_input_ip()
print ip_address
