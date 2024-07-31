import re

def is_passowrd_long(password):
    return len(password) > 7


def is_contains_lower_character(password):
    return any(i.islower() for i in password)

    
def is_contains_upper_character(password):
    return any(i.isupper() for i in password)

        
def is_contains_decimal_character(password):
    return any(i.isdecimal() for i in password)

    
def is_contains_special_characters(password):
    special_char = ['`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|','?']        
    return any(i in special_char for i in password)


def is_strong_password(password):
    return all([is_passowrd_long(password), is_contains_lower_character(password), is_contains_upper_character(password), is_contains_decimal_character(password), is_contains_special_characters(password)])
    

    
if __name__ == '__main__':
    password = input("Give a strong password: ")
    print("Is it a strong passowrd?")
    print(is_strong_password(password))
    

