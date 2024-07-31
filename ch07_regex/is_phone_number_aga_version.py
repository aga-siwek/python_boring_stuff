#415-555-4a42
def is_phone_number(text):
    if len(text) != 12:
        return False
    if text[3] and text[7] != "-":
        return False
    if text[0:3].isdecimal() and text[4:7].isdecimal() and text[8:].isdecimal():
        return True
    return False

# text = "455-555-4222"
# text_checker = is_phone_number(text)
# print(text_checker)

message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office"

for i in range(len(message)):
    chunk = message[i:i+12]
    if is_phone_number(chunk):
        print("Phone number found: " + chunk)
print("Done")

