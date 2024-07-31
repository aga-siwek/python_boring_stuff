import pyinputplus as pyip

def add_up_to_the_max_10(numbers):
    number_list = list(numbers)
    number_list = [int(num) for num in number_list]
    sum_num = 0
    for num in number_list:
        sum_num += num
    
    if sum_num <= 10:
        print(f"this is correct answer, num sum is {sum_num} so is smaller then 10")
        return True
    else: 
        print("Sum of number have to be smaller or equel to 10, your ie equal {sum_num}")
        return False
    

def add_up_to_the_10(numbers):
    numbers_list = list(numbers)
    for i, digit in enumerate (numbers_list):
        numbers_list[i] = int(digit)
    if sum(numbers_list) != 10:
        raise Exception(f"The digits must add up to 10, not {sum(numbers_list)}.")
    return int(numbers) #return an int from of numbers

    
    
response = pyip.inputCustom(add_up_to_the_10)