text = input("Enter to english message to translate to Pig Latin: ")

def text_change_to_the_list(text):
    list_with_text_pig_latin = []
    if "." in text: 
        text = text.replace(".", " .")
    if "," in text:
        text = text.replace(",", " ,")
    list_with_text = text.split(" ")
    return(list_with_text)

   

    list_with_text = text.split(" ")
    list_with_text_pig_latin = []

def pig_latin_list_replacer (list_with_text):

    import copy
    VOWELS = ("a", "e", "i", "o", "u", "y")

    for index, words in enumerate(list_with_text):
        if words.isalpha(): #only for words
            upper = words.isupper()
            title = words.istitle()
            words = words.lower()
            
            if words[0] in VOWELS:
            # if words.startswith("a") or words.startswith("e") or words.startswith("h") or words.startswith("i") or words.startswith("y") or words.startswith("o"):
                words = words + "yay"
            if words[0] not in VOWELS:
                    while words[0] not in VOWELS:
                        words = words[1:] + words[0]
                    words += "ay"
            if upper:
                words = words.upper()
            if title:
                words = words.title()
            list_with_text[index] = words

    return list_with_text



def list_change_to_the_text(pig_latin_list):
    pig_latin_text = " ".join(pig_latin_list)

    if " ." in pig_latin_text: 
        pig_latin_text = pig_latin_text.replace(" .", ".")
    if " ," in pig_latin_text:
        pig_latin_text = pig_latin_text.replace(" ,", ",")
    return pig_latin_text



list_with_text = text_change_to_the_list(text)
pig_latin_list = pig_latin_list_replacer(list_with_text)
pig_latin_text = list_change_to_the_text(pig_latin_list)
print(pig_latin_text)

