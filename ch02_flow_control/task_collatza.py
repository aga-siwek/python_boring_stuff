def collatz(number):
    while True:
        if number % 2 == 0:
            return number // 2
        elif number % 2 == 1:
            return 3 * number + 1
  
        
choosen_number = input("please write a number")
result = collatz(int(choosen_number))
print(result)
while result != 1:
    result = collatz(int(choosen_number))
    print(result)



# def collatz(number):
#     while True:
#         if number % 2 == 0:
#             return number // 2
#         elif number % 2 == 1:
#             return 3 * number + 1
  
        
# result = int(input("please write a number: "))

# while result != 1:
#     result = collatz(result)
#     print(result)