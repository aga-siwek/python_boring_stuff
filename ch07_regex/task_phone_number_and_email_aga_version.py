#copy from pyperclip and create valiapbes
#use re findall and find a value
#connect
#convert to string
#copy to clipboard



# if we have structure

def past_text_from_clipboard():
    import pyperclip
    copied_text = pyperclip.paste()
    print(copied_text)
    return copied_text

def find_owners_and_convert_to_the_list(copied_text):
    import re
    owner_regex = re.compile(r"\w*:")
    owners = owner_regex.findall(copied_text)
    return owners


def find_email_and_convert_to_the_list(copied_text):
    import re
    mail_regex = re.compile(r"\w*@\w*\.\w*")
    mails = mail_regex.findall(copied_text)
    return mails


def find_phone_and_convert_to_the_list(copied_text):
    import re
    phone_regex = re.compile(r"\d{3}\d{3}\d{3}|\d{3} \d{3} \d{3}|\d{3}-\d{3}-\d{3}|\+\d{2} \d{3} \d{3} \d{3}|\+\d{2}d{3}|\d{3}-\d{3}-\d{3} ")
    phones = phone_regex.findall(copied_text)
    return phones



def created_dictionary_with_contact(owners, mails, phones):
    contact = {}
    for index, owner in enumerate(owners):
        contact[owner] = [mails[index], phones[index]]
    return contact





def convert_dictionary_to_string(contact):
    text_with_contact_list = "Below contact list:\n"
    for k, v in contact.items():
        text_with_contact_list += f"{k} \nemail: {v[0]} \nphone: {v[1]} \n"
    print(text_with_contact_list)
    return text_with_contact_list

def copy_contact_to_clipboard(text_with_contact_list):
    import pyperclip
    pyperclip.copy(text_with_contact_list)
    print()
    print(" Previous text copied to the clipboard")
    

                                  


copied_text = past_text_from_clipboard()
mails = find_email_and_convert_to_the_list(copied_text)
owners = find_owners_and_convert_to_the_list(copied_text)
phones = find_phone_and_convert_to_the_list(copied_text)
contact = created_dictionary_with_contact(owners, mails, phones)
text_with_contact_list = convert_dictionary_to_string(contact)
copy_contact_to_clipboard(text_with_contact_list)


