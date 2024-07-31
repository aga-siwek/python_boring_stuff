def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        if text[3] != "-":
            return False
        for i in range (4,7):
            if not text[i].isdecimal():
                return False
        if text[7] != "-":
            return False
        for i in range (8, 12):
            if not text[i].isdecimal():
                return False
        return True
    
# print("is 415-555-4242 a phone number?")
# print(is_phone_number("415-555-4242"))
# print("is Moshi moshi a phone number?")
# print(is_phone_number("Moshi Moshi"))
 
message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office 515-555-9999"

for i in range(len(message)):
    chunk = message[i:i+12]
    if is_phone_number(chunk):
        print("Phone number found: " + chunk)
print("Done")


import re
phone_number = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phone_number.search("My number is 666-555-4242,  call me back")
print("Phone number found: " + mo.group())

#group way
phone_number = re.compile(r"\d{3}-\d{3}-\d{4}")
mo = phone_number.search("My number is 666-555-4242,  call me back")
print("Phone number found: " + mo.group())


#2 groups 
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phone_num_regex.search("My number is 666-555-4242,  call me back")
print(mo.group(1)) #first part
print(mo.group())


phone_num_regex_2 = re.compile(r'(\(\d\d\d\))-(\d\d\d)-(\d\d\d\d)') #if we have brackets we have to use (\( )
mo = phone_num_regex_2.search("My number is (666)-555-4242,  call me back")
print(mo.group(1))


