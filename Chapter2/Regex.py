import re

#Email Validation
myString = 'From: readers@packt.com (readers email)'
result = re.search('([\w.-]+)@([\w.-]+)', myString)
if result:
    print (result.group(0))   ## 'alice-b@google.com' (the whole match)
    print (result.group(1))  ## 'alice-b' (the username, group 1)
    print (result.group(2))  ## 'google.com' (the host, group 2)

# IP Address Validation
isIP = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
myString = "Your IP is: 192.168.1.254 "
result = re.findall(isIP,myString)
print(result)
    

#Date Format
myString = raw_input('Enter a valid Date (mm/dd/yy): ')

isDate = re.match('1[0-2]\/3[0-1]\/[1-2][0-9]{3}', myString)
if not isDate:
    isDate = re.match('[0-9]\/[0-2][0-9]\/[1-2][0-9]{3}', myString)
    if not isDate:
        isDate = re.match('1[0-2]\/[0-2][0-9]\/[1-2][0-9]{3}', myString)
        if not isDate:
            isDate = re.match('[0-9]\/3[0-1]\/[1-2][0-9]{3}', myString)

if isDate:
    print("valid")
else:
    print("invalid")
