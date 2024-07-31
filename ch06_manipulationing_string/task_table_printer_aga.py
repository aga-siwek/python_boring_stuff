
# well organize table with 3 column, the width like the longer part text)

table_data = [["apples", "oranges", "cherries", "banana", "carroten", "mango", "cherry"],
              ["Alice", "Bob", "Carol", "David", "aga"],
              ["dog", "cats", "moose", "goose", "rat", "elephant","bear"]]


def list_len(table_data):
    max_len_list = 0
    for index, list in enumerate (table_data):
        len_list = len(table_data[index])
        if len_list > max_len_list:
            max_len_list = len_list
    return max_len_list


def the_same_column_number(table_data, max_len_list):
    for index, list in enumerate(table_data):
        diffrent_files = max_len_list - len(list)
        while diffrent_files > 0:
            table_data[index].append(" ")
            diffrent_files -= 1


def len_words(table_data):
    table_len = []
    for index, list in enumerate(table_data):
        table_len.append([])
        for i, iteams in enumerate(list):
            word_width = len(iteams)
            table_len[index].append(word_width)
    return table_len




def max_wight_for_the_column(table_len):
    num = len(table_len[0])-1
    max_column = []

    while num >= 0: #we selected the number in column.
        column_width = [list[num] for list in table_len]
        max_column.insert(0, max(column_width)) #becouse we use number from the bigger value to the 0, we add new value on the beggining on the list
        num -= 1

    return max_column



def print_with_column_wight(table_data, max_column):
    for index, list in enumerate(table_data):
        print()
        for i, iteams in enumerate(list):
            print(iteams.ljust(max_column[i]).title(), end=" | ")

            
    

max_len_list = list_len(table_data)
the_same_column_number(table_data, max_len_list)
table_len = len_words(table_data)
max_column = max_wight_for_the_column(table_len)
print_with_column_wight(table_data, max_column)



