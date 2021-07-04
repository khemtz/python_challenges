#!/usr/bin/python3


import re,sys
#save the value of the first argv and save on var1, this will help us to validate with the diferents regular expressions
print (str(len(sys.argv)))
var1 = sys.argv[1]

#we need to verify that ipv4 has values between 0 to 255 with the regexp taken from logstash grok patterns, make some modifications:
#us_ipv4 = "(?<![0-9])(?:(?:[0-1]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])[.](?:[0-1]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])[.](?:[0-1]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])[.](?:[0-1]?[0-9]{1,2}|2[0-4][0-9]|25[0-5]))(?![0-9])"
us_ipv4 = "^(?:(?:([0-1]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])(\.)){3}(?:([0-1]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])))$"

#for IPv6 we need to verify is a valid HEX format. 

us_ipv6 = "((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?$"

#for the next regexp i assume that for binary the size of 8 bits separate by \. this for ipv4

us_ipv4binary = "^(?:[01]{8}(\.|\s)){3}[01]{8}$"
us_ipv6binary = "^(?:[01]{16}(:|\.|\s)){7}[01]{16}$"

if re.match(us_ipv4,var1):
    print("is a valid IPv4 IP: " + var1)
elif re.match(us_ipv6,var1):
    print("is a valid IPv6 IP: " + var1)
elif re.match(us_ipv4binary,var1):
    print("is a valid IPv4 Binary IP: " + var1)
elif re.match(us_ipv6binary,var1):
    print("is a valid IPv6 Binary IP: " + var1)
else:
    print("is not valid IP")
