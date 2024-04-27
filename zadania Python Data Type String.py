#-------------------------------------------------------------------------------
#Python Data Type: String - zadania

#1. Write a Python program to calculate the length of a string.
"""
def string_length(a):           # Funkcja do obliczania dlugosci stringa
    length = 0                  # Definiowanie stringa zmiennej "length" i jej wartosci
    for char in a:              # Petla for, ktora idzie przez kazdy znak w stringu i po kazdym znaku dodaje '1' do wartosci zmiennej "length"
        length += 1
    return length               # Zwraca zmienna length z dlugoscia stringa

a = input()                     # Definiowanie zmiennej "a" i uzupelnianie jej wartosci z klawiatury
print(string_length(a))         # Wywołanie funkcji string_length() i wypisanie wyniku petli
"""

#2. Write a Python program to count the number of characters (character frequency) in a string.
#Sample String : google.com'
#Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
"""
def check_frequency(a):             # Funkcja do obliczania czestotliwosci znakow stringa
    frequency = {}                  # Definiowanie pustego slownika do przechowywania czestotliwosci znakow.
    for n in a:                     # Wykonanie iteracji przez kazdy znak w podanym ciagu znakow.
        znaki = frequency.keys()    # Pobranie kluczy (znakow) ze slownika czestotliwosci.
        if n in znaki:              # Sprawdzenie, czy biezacy znak juz istnieje w slowniku czestotliwosci.
            frequency[n] += 1       # Jesli istenieje, zwieksz licznik wystapien tego znaku o 1.
        else:                       # Jesli znak nie istnieje w slowniku czestotliwosci, ustaw licznik wystapien tego znaku na 1.
            frequency[n] = 1
    return frequency                # Zwraca slownik zawierajacy czestotliwosc wystapien kazdego znaku.

a = input()                         # Pobranie stringa od uzytkownika.
print(check_frequency(a))           # Wywolanie funkcji check_frequency() i wydrukowanie wyniku.
"""

#3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
#Sample String : 'w3resource'
#Expected Result : 'w3ce'
#Sample String : 'w3'
#Expected Result : 'w3w3'
#Sample String : ' w'
#Expected Result : Empty String
"""
def two_first_two_last(string):    # Funkcja, która zwraca stringa z dwoma pierwszymi i dwoma ostatnimi znakami.
    a = string                     # Przypisanie wartosci stringa do zmiennej 'a'.
    string_length = len(string)    # Obliczenie dlugosci stringa.
    if string_length > 2:          # Sprawdzenie, czy dlugosc stringa jest wieksza niz 2.
        first_char = a[0]          # Pierwszy znak lancucha.
        second_char = a[1]         # Drugi znak lancucha.
        penultimate_char = a[string_length - 2]  # Przedostatni znak lancucha.
        last_char = a[string_length - 1]  # Ostatni znak lancucha.
        final_word = first_char + second_char + penultimate_char + last_char  # Laczenie pierwszych dwoch i ostatnich dwoch znakow w nowy lancuch.
        return final_word          # Zwrocenie nowego lancucha.
    else:                           # Jezeli lancuch ma dlugosc mniejsza lub rowna 2.
        final_word = ""             # Zwrocenie pustego lancucha.
        return final_word          # Zwrocenie pustego lancucha.

string = input()                   # Pobranie lancucha znakow od uzytkownika.
print(two_first_two_last(string))  # Wywolanie funkcji i wydrukowanie wyniku.
"""

#4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
#Sample String : 'restart'
#Expected Result : 'resta$t'
"""
def change_occurrences(a):             # Funkcja modyfikująca ciąg poprzez zamianę pozostałych wystąpień pierwszego znaku na "$".
    first_char = a[0]                  # Zapisanie pierwszego znaku ciągu.
    modified_string = first_char + a[1:].replace(first_char, "$")  # Zamiana wszystkich wystąpień pierwszego znaku (poza pierwszym) na "$".
    return modified_string             # Zwrócenie zmodyfikowanego ciągu.

a = input()                            # Pobranie ciągu znaków od użytkownika.
print(change_occurrences(a))           # Wywołanie funkcji 'change_occurrences' i wydrukowanie wyniku.
"""

#8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
#Sample Output:
#Longest word: Exercises
#Length of the longest word: 9
"""
def find_longest_word(list_of_words):           # Funkcja znajdująca najdłuższy wyraz z listy i podająca jego długosc
    longest_word = max(list_of_words, key=len)  # Znajduje slowo o najwiekszej dlugosci
    return longest_word, len(longest_word)      # Zwraca zmienne z najdluzszym slowem i jego dlugoscia

# Przyklad uzycia funkcji
words = ['samochod', 'kolowrotek', 'lusterko', 'szyba']
print(find_longest_word(words))                 # Wywolanie funkcji i wyswietlenie wyniku
"""

#12. Write a Python program to count the occurrences of each word in a given sentence.
"""
def count_words(sentence):                                       # Funkcja zliczająca ilosc wystapien danego slowa
    words_sentence = sentence.split()                            # Podzielenie zdanie na slowa
    return {word: words_sentence.count(word) for word in words_sentence}  # Utworzenie slownika z liczbami wystapien kazdego slowa

sentence = "samochod jedzie bardzo szybko po autostradzie mijajac auta"         # Przyklad zdania wrzuconego do funkcji
print(count_words(sentence))                                     # Wywolanie funkcji i drukowanie wyniku
"""

#14. Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
#Sample Words : red, white, black, red, green, black
#Expected Result : black, green, red, white,red
"""
def sort_words(input_string):                       # Funkcja sortująca wyrazy i usuwająca duplikaty
    words = sorted(set(input_string.split(", ")))   # Sortowanie slow i usuniecie duplikatow
    return ", ".join(words)                         # Laczenie posortowanych slow z powrotem w ciag

input_words = 'czerwony, zielony, bialy, niebieski, czarny, fioletowy, bialy, zielony' # Przykladowe slowa
print(sort_words(input_words))                      # Wywolanie funkcji i wyswietlenie wyniku
"""

#20. Write a Python function to reverse a string if its length is a multiple of 4.
"""
def reverse_string_if_multiple_of_four(a):      # Funkcja odwracajaca ciag znakow jezezli jego dlugosc jest wielokrotnoscia cyfry 4
    return a[::-1] if len(a) % 4 == 0 else a    # Odwrocenie ciagu, jesli jego dlugość jest wielokrotnoscia 4

# Przykład użycia:
string = "Python"
print(reverse_string_if_multiple_of_four(string))
"""

#25. Write a Python program to create a Caesar encryption.
#Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
"""
def caesar_encrypt(text, shift):                        # Funkcja szyfrujaca tekst przy uzyciu szyfru Cezara z okreslonym przesunieciem
    encrypted_text = []                                 # Utworzenie pustej listy dla zaszyfrowanego tekstu
    for char in text:                                   # Iterowanie przez kazdy znak w tekscie
        if char.isalpha():                              # Sprawdzenie czy znak to litera
            shift_base = 65 if char.isupper() else 97   # Ustalenie bazy ASCII dla wielkich lub malych liter
            encrypted_text.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))  # Szyfrowanie znaku i dodanie do listy
        else:
            encrypted_text.append(char)                 # Dodanie znakow niealfabetycznych bez zmian
    return ''.join(encrypted_text)                      # Polaczenie listy w ciag zaszyfrowany i zwrocenie go

print(caesar_encrypt("Hello, World!", 3))               # Przyklad tekstu i przesuniecia
"""

#30. Write a Python program to print the following numbers up to 2 decimal places.
"""
def print_decimal_places(number, places=2):     # Funkcja formatujaca liczbę zmiennoprzecinkową do określonej liczby miejsc dziesiętnych
    format_string = "{:." + str(places) + "f}"  # Utworzenie formatu wyswietlania liczby z ustalona liczba miejsc dziesietnych
    return format_string.format(number)         # Zwrot sformatowanej liczby

print(print_decimal_places(3.14159))            # Przyklad liczby do sformatowania
"""

#38. Write a Python program to count occurrences of a substring in a string.
"""
def count_substring_occurrences(string, substring):             # Funkcja liczaca i zwracajaca liczbe wystapien podciagu w ciagu
    return string.count(substring)

print(count_substring_occurrences("hello hello hello", "lo"))   # Przykladowe ciagi do analizy
"""

#42. Write a Python program to count repeated characters in a string.
#Sample string: 'thequickbrownfoxjumpsoverthelazydog'
#Expected output :
#o 4
#e 3
#u 2
#h 2
#r 2
#t 2
"""
def count_repeated_chars(s):                # Funkcja liczaca i zwracajaca slownik z literami, ktore powtarzaja sie w ciagu wiecej niz raz
    from collections import Counter         # Import modulu do liczenia elementow
    counter = Counter(s)                    # Policzenie wystapienia kazdego znaku
    return {char: count for char, count in counter.items() if count > 1}    # Utworzenie slownika tylko z powtarzajacymi sie znakami i zwrocenie go

print(count_repeated_chars('samochodjedziebardzoszybkopoautostradziemijajacauta')) # Przykladowy ciag do analizy
"""

#46. Write a Python program to convert a given string into a list of words.
#Sample Output:
#['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
#['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
"""
def string_to_word_list(s):         # Funkcja konwertujaca ciag znaków na liste slow
    return s.split()                # Pozzielenie ciagu na liste slow

print(string_to_word_list("Samochod jedzie bardzo szybko po autostradzie mijajac auta."))  # Przykladowy ciag do konwersji
"""

#57. Write a Python program to remove spaces from a given string.
"""
def remove_spaces(s):                   # Funkcja usuwajaca wszystkie spacje z podanego ciągu znaków
    return s.replace(" ", "")           # Usuniecie spacji z ciagu i zwrot nowego ciagu

print(remove_spaces("a b c d e f g"))   # Przykladowy ciag do przetworzenia
"""

#60. Write a Python program to capitalize the first and last letters of each word in a given string.
"""
def capitalize_first_last_letters(a):               # Funkcja kapitalizujaca pierwsza i ostatnia litere kazdego slowa w ciagu
    words = a.split()                               # Podzielenie ciagu na slowa
    capitalized_words = [word[0].upper() + word[1:-1] + word[-1].upper() if len(word) > 1 else word.upper() for word in words]  # Kapitalizowanie pierwszej i ostatniej litery w kazdym slowie
    return " ".join(capitalized_words)              # Polaczenie slow z powrotem w ciag i zwrot

print(capitalize_first_last_letters("hello world")) # Przykladowy ciag do modyfikacji
"""

#67. Write a Python program to remove all consecutive duplicates of a given string.
"""
def remove_consecutive_duplicates(a):   # Funkcja usuwajaca powtarzajace sie, kolejne znaki w ciagu, zwracajajaca nowy ciag ze zmienionymi zbiorami powtarzajacych sie znakow na pojedyncze znaki
    from itertools import groupby       # Importowanie funkcji groupby do grupowania powtarzajacych sie elementow
    return ''.join(char for char, _ in groupby(a))  # Usuniecie powtarzajacych sie znakow i zwrot nowego ciagu

print(remove_consecutive_duplicates("aaabbbccdaaa"))    # Przykladowy ciag do przetworzenia
"""

#84. Write a Python program to swap cases in a given string.
#Sample Output:
#pYTHON eXERCISES
#jAVA
#nUMpY
"""
def swap_case(s):   # Funkcja zmieniajaca wielkosc liter na przeciwna w podanym ciągu
    return s.swapcase() # Zmiana wielkosci kazdej litery na przeciwna

print(swap_case("Python Exercises"))    # Przykladowy ciag do przetworzenia
"""

#90. Write a Python program to remove duplicate words from a given string.
#Sample Output:
#Original String:
#Python Exercises Practice Solution Exercises
#After removing duplicate words from the said string:
#Python Exercises Practice Solution
"""
def remove_duplicate_words(s):  # Funkcja usuwajaca duplikaty slow z podanego ciagu
    words = s.split()           # Dzieli ciag na slowa
    seen = set()                # Tworzy zestaw do sledzenia juz widzianych slow
    return " ".join(word for word in words if not (word in seen or seen.add(word))) # Zwraca ciag bez duplikatow

print(remove_duplicate_words("Python Exercises Practice Solution Exercises"))   # Przykladowy ciag do przetworzenia
"""

#96. Write a Python program to convert a given string to Camelcase.
#Sample Output:
#javascript
#fooBar
#fooBar
#foo.Bar
#fooBar
#foobar
#fooBar
"""
def to_camel_case(text):    #Funkcja konwertujaca podany tekst na notację CamelCase
    words = text.split()    # Dzieli tekst na slowa
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])  # Tworzy CamelCase: pierwsze slowo male, pozostale z duzej litery

print(to_camel_case("python exercises practice solution"))  # Przykladowy tekst do konwersji
"""

#109. Write a Python program that counts the number of leap years within the range of years. Ranges of years should be accepted as strings.
#Sample Data:
#("1981-1991") -> 2
#("2000-2020") -> 6
"""
def count_leap_years(range_string):     # Funkcja zliczajaca lata przestepne w okreslonym zakresie lat
    start_year, end_year = map(int, range_string.split('-'))    # Konwertuje zakres lat na liczby calkowite
    return sum(1 for year in range(start_year, end_year+1) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) # Zwraca liczbe lat przestepnych w zakresie

print(count_leap_years("2000-2020"))    # Przykladowy zakres lat do analizy
"""