#copy from pyperclip and create valiapbes
#use re findall and find a value
#connect
#convert to string
#copy to clipboard




# if we don't have structure

def past_text_from_clipboard():
    import pyperclip
    copied_text = pyperclip.paste()
    return copied_text



def find_email_and_convert_to_the_list(copied_text):
    import re
    mail_regex = re.compile(r"\w*-\w*@\w*\.\w*\.w*|\w*@\w*\.\w*\.\w*|\w*@\w*\.\w*|\w*-\w*@\w*\.\w*")
    mails = mail_regex.findall(copied_text)
    return mails


def find_phone_and_convert_to_the_list(copied_text):
    import re
    phone_regex = re.compile(r"""(\d{3}\d{3}\d{3}
                             |\d{3} \d{3} \d{3}|\d{3}-\d{3}-\d{3}
                             |\+\d{2} \d{3} \d{3} \d{3}
                             |\+\d{2}d{3}|\d{3}-\d{3}-\d{3})
                             | """, re.VERBOSE)
    phones = phone_regex.findall(copied_text)
    return phones




def convert_list_to_string(mails, phones):
    text_with_contact_list = "Below contact list:\n"
    if mails != None:
        text_with_contact_list += "\nMails: \n"
        for i, mail in enumerate (mails):
            text_with_contact_list += f"{mail}\n"
    else:
        print("The program doesn't find a e-mail")
    text_with_contact_list += "\nPhones: \n"
    if phones != None:
        for j, phone in enumerate (phones):
            text_with_contact_list += f"{phone}\n"
        print(text_with_contact_list)
        return text_with_contact_list
    else:
        print("The program doesn't find a phone")

def copy_contact_to_clipboard(text_with_contact_list):
    import pyperclip
    pyperclip.copy(text_with_contact_list)
    print()
    print(" Previous text copied to the clipboard")
    

                                  


copied_text = past_text_from_clipboard()
mails = find_email_and_convert_to_the_list(copied_text)
# owners = find_owners_and_convert_to_the_list(copied_text)
phones = find_phone_and_convert_to_the_list(copied_text)
# contact = created_dictionary_with_contact(owners, mails, phones)
text_with_contact_list = convert_list_to_string(mails, phones)
copy_contact_to_clipboard(text_with_contact_list)


