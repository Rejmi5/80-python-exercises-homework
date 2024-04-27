#-------------------------------------------------------------------------------
#20 zadan z Python Conditional Statements and loops

#1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).
"""
for number in range(1500, 2701):            # Iterowanie przez liczby od 1500 do 2701
    if number % 7 == 0 and number % 5 == 0: # Sprawdzanie, czy liczba jest podzielna przez 7 i 5
        print(number)                       # Wyświetlanie liczby spełniającej warunki
"""

#5. Write a Python program that accepts a word from the user and reverses it.
"""
word = input("Podaj słowo: ")       # Prosi użytkownika o wprowadzenie słowa
reversed_word = word[::-1]          # Odwraca kolejność znaków w słowie
print(reversed_word)                # Wyświetla odwrócone słowo
"""

#6. Write a Python program to count the number of even and odd numbers in a series of numbers
#Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#Expected Output :
#Number of even numbers : 5
#Number of odd numbers : 4
"""
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)   # Lista liczb do sprawdzenia
even_count, odd_count = 0, 0            # Inicjalizacja liczników dla parzystych i nieparzystych liczb
for number in numbers:                  # Przechodzi przez listę liczb
    if number % 2 == 0:                 # Sprawdza czy liczba jest parzysta
        even_count += 1                 # Inkrementuje licznik parzystych
    else:
        odd_count += 1                  # Inkrementuje licznik nieparzystych
# Wyświetla wyniki
print("Liczba liczb parzystych:", even_count)
print("Liczba liczb nieparzystych:", odd_count)
"""

#8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
#Note : Use 'continue' statement.
#Expected Output : 0 1 2 4 5
"""
# Iteruje przez liczby od 0 do 6
for i in range(7):
    # Pomija 3 i 6
    if i in [3, 6]:
        continue
    # Wyświetla liczby z pominięciem 3 i 6
    print(i, end=' ')
"""

#9. Write a Python program to get the Fibonacci series between 0 and 50.
#Note : The Fibonacci Sequence is the series of numbers :
#0, 1, 1, 2, 3, 5, 8, 13, 21, ....
#Every next number is found by adding up the two numbers before it.
#Expected Output : 1 1 2 3 5 8 13 21 34
"""
# Inicjalizacja pierwszych dwóch liczb serii Fibonacciego
a, b = 0, 1
# Generuje liczby serii Fibonacciego
while b < 50:
    print(b, end=' ')
    # Aktualizuje wartości dla kolejnego kroku
    a, b = b, a + b
"""

#10. Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".
#Sample Output :
#fizzbuzz
#1
#2
#fizz
#4
#buzz
"""
for i in range(1, 51):              # Iteruje przez liczby od 1 do 50
    if i % 3 == 0 and i % 5 == 0:   # Dla wielokrotności trzech i pięciu wydrukuj "FizzBuzz"
        print("FizzBuzz")
    elif i % 3 == 0:                # Dla wielokrotności trzech wydrukuj "Fizz"
        print("Fizz")
    elif i % 5 == 0:                # Dla wielokrotności pięciu wydrukuj "Buzz"
        print("Buzz")
    else:                           # W innym przypadku wydrukuj numer
        print(i)
"""

#14. Write a Python program that accepts a string and calculates the number of digits and letters.
#Sample Data : Python 3.2
#Expected Output :
#Letters 6
#Digits 2
"""
text = input("Wprowadz tekst: ")    # Wprowadzenie danych przez użytkownika
digits = letters = 0                # Inicjalizacja zmiennych do zliczania liter i cyfr
for char in text:                   # Iteracja przez każdy znak w stringu
    if char.isalpha():              # Sprawdzenie, czy znak jest literą
        letters += 1                # Zlicza litery
    elif char.isdigit():            # Sprawdzenie, czy znak jest cyfrą
        digits += 1                 # Zlicza cyfry
# Wyświetlanie wyników
print("Litery:", letters)
print("Cyfry:", digits)
"""

#16. Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.
"""
for num in range(100, 401):                             # Iteracja przez zakres od 100 do 400
    if all(int(digit) % 2 == 0 for digit in str(num)):  # Sprawdzenie czy wszystkie cyfry w liczbie są parzyste
        print(num, end=",")
"""

#18. Write a Python program to print the alphabet pattern 'D'.
#Expected Output:
# ****
# *   *
# *   *
# *   *
# *   *
# *   *
# ****
"""
# Wzór litery D
print("****")
for i in range(5):  # Drukowanie środkowej części litery D
    print("*   *")
print("****")  # Zamknięcie litery D
"""

#20. Write a Python program to print the alphabet pattern 'G'.
#Expected Output:
#  ***
# *   *
# *
# * ***
# *   *
# *   *
#  ***
"""
# Wzór litery G
print(" *** ")
print("*   *")
print("*")
print("* ***")
print("*   *")
print("*   *")
print(" *** ")
"""

#22. Write a Python program to print the alphabet pattern 'M'.
#Expected Output:
#  *       *
#  *       *
#  * *   * *
#  *   *   *
#  *       *
#  *       *
#  *       *
"""
# Wzór litery M
print(" *       *")
print(" *       *")
print(" * *   * *")
print(" *   *   *")
print(" *       *")
print(" *       *")
print(" *       *")
"""

#23. Write a Python program to print the alphabet pattern 'O'.
#Expected Output:
#  ***
# *   *
# *   *
# *   *
# *   *
# *   *
#  ***
"""
# Wzór litery O
print(" *** ")
print("*   *")
for i in range(3):  # Drukowanie środkowej części litery O
    print("*   *")
print(" *** ")
"""

#24. Write a Python program to print the alphabet pattern 'P'.
#Expected Output:
# ****
# *   *
# *   *
# ****
# *
# *
# *
"""
# Wzór litery P
print("****")
print("*   *")
print("*   *")
print("****")
print("*")
print("*")
print("*")
"""

#27. Write a Python program to print the alphabet pattern 'T'.
#Expected Output:
# *****
#   *
#   *
#   *
#   *
#   *
#   *
"""
# Wzór litery T
print("*****")
for _ in range(6):  # Drukowanie pionowej części litery T
    print("  *  ")
"""

#28. Write a Python program to print the alphabet pattern 'U'.
#Expected Output:
# *   *
# *   *
# *   *
# *   *
# *   *
# *   *
#  ***
"""
# Wzór litery U
for i in range(6):  # Drukowanie pionowej części litery U
    print("*   *")
print(" *** ")
"""

#29. Write a Python program to print the alphabet pattern 'X'.
#Expected Output:
# *   *
# *   *
#  * *
#   *
#  * *
# *   *
# *   *
"""
# Wzór litery X
print("*   *")
print(" * * ")
print("  *  ")
print(" * * ")
print("*   *")
"""
#30. Write a Python program to print the alphabet pattern 'Z'.
#Expected Output:
#*******
#     *
#    *
#   *
#  *
# *
#*******
"""
# Wzór litery Z
print("*******")
for i in range(5, 0, -1):  # Drukowanie skośnej części litery Z
    print(" " * i + "*")
print("*******")
"""

#33. Write a Python program to convert a month name to a number of days.
#Expected Output:
#List of months: January, February, March, April, May, June, July, August
#, September, October, November, December
#Input the name of Month: February
#No. of days: 28/29 days
"""
# Słownik zawierający miesiące i liczby dni
month_days = {
    "January": 31, "February": "28/29", "March": 31,
    "April": 30, "May": 31, "June": 30,
    "July": 31, "August": 31, "September": 30,
    "October": 31, "November": 30, "December": 31
}
# Wprowadzenie nazwy miesiąca przez użytkownika
month = input("Wprowadz nazwe miesiaca: ")
# Wydrukowanie liczby dni w miesiącu
print("Liczba dni:", month_days.get(month, "Nieprawidlowa nazwa miesiaca"))
"""

#37. Write a Python program that reads two integers representing a month and day and prints the season for that month and day.
#Expected Output:
#Input the month (e.g. January, February etc.): july
#Input the day: 31
#Season is autumn
"""
# Słownik definiujący pory roku według miesięcy i dni
seasons = {
    (6, 21): "Wiosna", (9, 23): "Lato", (12, 21): "Jesień", (3, 21): "Zima"
}
# Wprowadzenie miesiąca i dnia przez użytkownika
month = int(input("Wprowadz miesiac (1-12): "))
day = int(input("Wprowadz dzien (1-31): "))
# Określenie aktualnej pory roku
for (m, d), season in sorted(seasons.items()):
    if (month, day) < (m, d):
        print("Pora roku:", season)
        break
"""

#41. Write a Python program to get the next day of a given date.
#Expected Output:
#Input a year: 2016
#Input a month [1-12]: 08
#Input a day [1-31]: 23
#The next date is [yyyy-mm-dd] 2016-8-24
"""
# Import modułu daty
from datetime import datetime, timedelta
# Wprowadzenie daty przez użytkownika
year = int(input("Wprowadz rok: "))
month = int(input("Wprowadz miesiac [1-12]: "))
day = int(input("Wprowadz dzien [1-31]: "))
# Utworzenie obiektu daty
date = datetime(year, month, day)
# Dodanie jednego dnia do daty
next_day = date + timedelta(days=1)
# Wydrukowanie następnego dnia
print("Nastepna data [rrrr-mm-dd]:", next_day.strftime("%Y-%m-%d"))
"""