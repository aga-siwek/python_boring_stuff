def print_picnic(items_dict, left_width, right_width):
    print("PICNIC ITEAMS".center(left_width + right_width, "-"))
    for k,v in items_dict.items():
        print(k.ljust(left_width, ".") + str(v).rjust(right_width))



picnic_iteams = {"sandwiches":4, "apples": 12, "cups": 4, "cookies": 8000}

print_picnic(picnic_iteams, 12, 5)
print_picnic(picnic_iteams, 15, 20)