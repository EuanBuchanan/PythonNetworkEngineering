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
        ip_mask = user_subnet.split('.')
        if len(ip_mask) != 4:
            print "Subnet needs to be entered as x.x.x.x, three '.' seperating the four octets."

        elif ip_mask[0] not in valid_octets or\
             ip_mask[1] not in valid_octets or\
             ip_mask[2] not in valid_octets or\
             ip_mask[3] not in valid_octets:
            print "One or more octets is not valid. Valid octets are: "
            for octet in valid_octets:
                print octet
            continue

        elif ip_mask[0] <= ip_mask[1] <= ip_mask[2] \
            <= ip_mask[3]:
            print "Each subsequent subnet octet from the first must be equal to or lesser than the previous"
            continue 
            
        else:
            return ip_mask
    

def convert_to_binary(octet_list):

    binary_list = [ bin(int(octet) % 256)[2:].zfill(8) for octet in octet_list ]

    return binary_list

def get_network_broadcast(ip_address, ip_mask):
    # This function takes two lists, string representations of the decimal values of the
    # ip address and the subnet mask

    # Using binary operations, the network address, the broacast address, the wildcard mask
    # and the number of hosts are obtained.

    ip_network_address = []
    ip_wildcard_mask =[]
    ip_broadcast_address = []
    ip_mask_binary = convert_to_binary(ip_mask)
    host_bits = 0
    hosts = []


    for octet in range(len(ip_mask)):

        mask = int(ip_mask[octet])

        # a subnet mask always has the rightmost bits as zeros, the number of zeros determines
        # how many hosts there are in the network. The formulae for this is ( n ** 2 -2) where
        # n is the number of zeroes

        host_bits += ip_mask_binary[octet].count('0')
        hosts.append(ip_mask_binary[octet].count('0'))
        print hosts

        # The wildcard mask is the invers of the mask. Each octet is eight bits, therefore the
        # sub of the sum of 256 and the inverse of the mask will give us the mask value.

        wildcard = 256 + ~int(ip_mask[octet])

        # The network address is obtained from a bitwsie and of the host address and the mask

        host = int(ip_address[octet])
        network_add = mask & host

        # The sum of the nework addrss and the wildcard mask gives the broadcast address

        broadcast_add = network_add + wildcard

        ip_network_address.append(str(network_add))
        ip_wildcard_mask.append(str(wildcard))
        ip_broadcast_address.append(str(broadcast_add))


    if host_bits == 1:
        number_of_hosts = '1'
    else:
        number_of_hosts = str( 2 ** host_bits - 2)

    print "The Network Address is: " + ".".join(ip_network_address)
    print "The Wildcard Mask is: " + ".".join(ip_wildcard_mask)
    print "The Broadcast Address is: " + ".".join(ip_broadcast_address)
    print "The number of hosts is: " + str(number_of_hosts)

    return (ip_network_address, ip_wildcard_mask, ip_broadcast_address, number_of_hosts)

def get_random_address(ip_addr, ip_mask):
    pass





# ip_address = user_input_ip()
# ip_address_binary = convert_to_binary(ip_address)
# 
# ip_mask = subnet_check()
# ip_mask_binary = convert_to_binary(ip_mask)

ip_network_address, ip_wildcard_mask, ip_broadcast_address, number_of_hosts \
        = get_network_broadcast(['192','168','2','21'], ['255','255','255','224']) 

ip_random_address = get_random_address(ip_network_address, ip_wildcard_mask)
