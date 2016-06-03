# A re-write of SubnetCalculator using the NetAddr modle. The logic and the
# flow will not be altered, just the code.

#   On taking an IP address and a subnet mask:

#   Outuput:
#       Network Address
#       Broadcast Address
#       Number of Valid hosts per subnet
#       Wildcard Mask
#       Mask bits

#   Refer application1.png for logical flow

import sys
import netaddr

def user_input_ip(message):

    ''' This function tests that the user input is in the fomr of a dotted decimal
    IPv4 address. '''
    
    while True:
        try:
            ip = netaddr.IPAddress(raw_input(message))
        except netaddr.AddrFormatError:
            print "Please check the format of your input, that format is not valid."
        else:
            return ip
            break

def ip_host_check(ip_host):


    ''' This function checks that the host is not:
        A hostmask
        224.x.x.x - multicast addresses
        127.x.x.x - reserved addresses
        169.254 - windows default adddresses when no DHCP is found
        
        ip_host requires a nettaddr.IPAddress object'''

    check = True

    if ip_host.is_hostmask():
        check = False
        return (check, "Input is a hostmask, please check and try again")
    elif ip_host.is_loopback():
        check = False
        return (check, "Input is a loopback, please check and try again")
    elif ip_host.is_netmask():
        check = False
        return (check, "Input is a netmask, please check and try again")
    elif ip_host.is_multicast():
        check = False
        return (check, "Input is a multicast, please check and try again")
    elif ip_host.is_link_local():
        check = False
        return (check, "Input is link local, please check and try again")
    else:
        return (check,)

def ip_subnet_check(ip):

    ''' This function checks that the subnet is a valid subnet. ip is required to be a
    netaddr.IPAddress object '''

    check = True

    if not ip.is_netmask():
        check = False
        return(check, "Input is not a valid subnet, please try again")
    else:
        check = True
        return(check)

def get_ip_and_mask():

    while True:
        ip_host = user_input_ip("Please enter host IP in the form of a.b.c.d: ")
        check = ip_host_check(ip_host)
        if not ip_host_check(ip_host)[0]:
            print check[1]
            continue
        else:
            print str(ip_host)
            break
get_ip_and_mask()


    



#        if len(octets) != 4:
#            print "The input needs to be four octets, for example 10.10.10.10, where the '.' seperates each octet."
#            continue
#        elif octets[0] == "127":
#            print "Addresses beginning in '127' are reserved local IPs and not valid."
#            continue
#        elif octets[0] == "224":
#            print "Addresses beginning in '224' are multicast addresses and not valid."
#            continue
#        elif octets[0] == "169" and octets[1] == "254":
#            print "Addresses beginning in '169.254' are Microsoft default addresses and not valid."
#            continue
#        elif not (1 <= int(octets[0]) <= 223 \
#            and 0 <= int(octets[1]) <= 255 \
#            and 0 <= int(octets[2]) <= 255 \
#            and 0 <= int(octets[3]) <= 255):
#            print "One or more octets is out of range. Please check and re-input."
#            continue
#        else:
#            return octets
#            break
