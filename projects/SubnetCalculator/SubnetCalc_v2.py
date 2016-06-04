# A re-write of SubnetCalculator using the NetAddr module. The logic and the
# flow will not be altered, just the code. I'm not implmenting the random 
# addreess function.

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

def user_input(message):

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
        return(check,)

def get_ip():

    ''' This function gets the host IP, returns netaddr.IPaddress object.'''
    while True:
        ip_host = user_input("Please enter host IP in the form of a.b.c.d: ")
        check = ip_host_check(ip_host)
        if not check[0]:
            print check[1]
            continue
        else:
            return(ip_host)
            break

def get_subnet():

    '''This function gets the host subnet, returns netaddr.IPAddress object.'''

    while True:
        ip_subnet = user_input("Please enter mask in the form of a.b.c.d: ")
        check = ip_subnet_check(ip_subnet)
        if not ip_subnet_check(ip_subnet)[0]:
            print check[1]
            continue
        else:
            return(ip_subnet)
            break
    
def main():

    ''' Sets host_ip and host_subnet to netaddr.IPAddress objecta. Uses objects to create
    netaddr.IPNetwork object, host_network.
    
    From host_network:

        Network Address
        Broadcast Address
        Number of Valid hosts per subnet
        Wildcard Mask
    
    From host_subnet:

        Mask bits

    are obtained.'''

    host_ip = get_ip()
    host_subnet = get_subnet()
    host_network = netaddr.IPNetwork('/'.join([str(host_ip), str(host_subnet.netmask_bits())]))
    print "The Network Address is: " + str(host_network.network)
    print "The Broadcast Address is: " + str(host_network.broadcast)
    print "The hostmask is: " + str(host_network.hostmask)
    print "The mask bits  are: " + str(host_subnet.bits())
    if int(host_network.size) == 1:
        print "The number of hosts is 1."
    elif int(host_network.size) == 2:
        print "The number of hosts is 1 with a broadcat address."
    else:
        print "The number of hosts is " + str(int(host_network.size) - 2)


if __name__ == "__main__":
    main()
