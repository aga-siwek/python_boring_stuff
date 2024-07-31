a = 1 
print(type(a))
b = 1.0
print(type(b))
c = "cool"
print(type(c))
d = True
print(type(d))


f = c.endswith("ol")
print(f) and print(type(f))

#operations 

# floor division example
g = 10
h = 3
i = g // h
print(i)
j = g % h
print(j)

age = input("podaj swój wiek")
print(type(age.isdecimal))

#isdecimal() to metoda dostępna dla obiektów typu string w języku Python. Służy ona do sprawdzania, czy wszystkie znaki w danym stringu są cyframi dziesiętnymi (0-9). Metoda zwraca True, jeśli wszystkie znaki w stringu są cyframi dziesiętnymi, w przeciwnym razie zwraca False.


#pizza zadanie
#pizza zadanie

while True:
    pizza = input("podaj średnice pizzy: ")
    pizza_valid = pizza.isdecimal()
    print(pizza_valid)
    if pizza_valid:
        pizza_promien=(float(pizza)) / 2
        pole_pizzy = (pizza_promien**2)*3.14
        print("Twoja pizza ma " + str(pole_pizzy) + " smacznego")
        break
    else:
        print("podaj tylko cyfry")

#randomowa liczba ze zbioru, tutaj bedzie od 1 do 19 (nigdy nie dochodzimy do oststniej liczby)

import random
secretNumber = random.randint(1,20)
print(secretNumber)

#moge zrobic liczbe juz w zapytaniu
guess_number = int(input("take a guess: "))



#imput, zmniejszeniem weryskikacja do boom
is_raining = input("is raining? (yes or no): ").lower() == 'yes'




import sys
sys.exit("buuuuuuu")