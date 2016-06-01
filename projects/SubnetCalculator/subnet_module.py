# Writing code here to put in to main app when developed
#
# Writing as a function because functions are cool

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
            
        else:
            return subnet_octets
    


print subnet_check()
