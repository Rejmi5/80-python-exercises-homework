#-------------------------------------------------------------------------------
#Python Data Type: List - zadania

#1. Write a Python program to sum all the items in a list.
"""
def sum_items(lst):  # Definiuje funkcje przyjmujaca liste
    return sum(lst)  # Zwraca sume elementow listy
print(sum_items([1, 2, 3, 4]))
"""

#3. Write a Python program to get the largest number from a list.
"""
def max_number(lst):  # Definiuje funkcje z lista jako argument
    return max(lst)  # Zwraca najwieksza liczbe z listy
print(max_number([1, 2, 3, 4, 5]))
"""

#7. Write a Python program to remove duplicates from a list.
"""
def remove_duplicates(lst):  # Funkcja przyjmuje liste
    return list(set(lst))  # Konwertuje liste na set i z powrotem na liste
print(remove_duplicates([1, 2, 2, 3, 3, 4]))
"""

#9. Write a Python program to clone or copy a list.
"""
def clone_list(lst):  # Tworzy funkcje klonujaca liste
    return lst[:]  # Zwraca kopie listy
original_list = [1, 2, 3]
cloned_list = clone_list(original_list)
print(cloned_list)
"""

#8. Write a Python program to check if a list is empty or not.
"""
def is_list_empty(lst):  # Definicja funkcji sprawdzajacej pustosc listy
    return not lst  # Zwraca True, jesli lista jest pusta
print(is_list_empty([]))
print(is_list_empty([1]))
"""

#5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
#Sample List : ['abc', 'xyz', 'aba', '1221']
#Expected Result : 2
"""
def count_special_strings(lst):  # Funkcja liczy specjalne stringi
    return sum(1 for s in lst if len(s) >= 2 and s[0] == s[-1])  # Liczy stringi zgodnie z kryteriami
print(count_special_strings(['aba', 'abc', 'xyz', '111']))
"""

#37. Write a Python program to find common items in two lists.
"""
def find_common(lst1, lst2):  # Definiuje funkcje znajdujaca wspolne elementy
    return list(set(lst1) & set(lst2))  # Zwraca przeciecie dwoch zbiorow
print(find_common([1, 2, 3], [2, 3, 4]))
"""

#26. Write a Python program to check whether two lists are circularly identical.
"""
def are_circularly_identical(lst1, lst2):  # Sprawdza identycznosc cykliczna
    return ' '.join(map(str, lst1)) in ' '.join(map(str, lst2 * 2))  # Porownuje rozszerzona lista
print(are_circularly_identical([1, 2, 3], [3, 1, 2]))
"""

#19. Write a Python program to calculate the difference between the two lists.
"""
def difference(lst1, lst2):  # Funkcja oblicza roznice miedzy listami
    return list(set(lst1) - set(lst2))  # Zwraca roznice zbiorow
print(difference([1, 2, 3, 4], [2, 4]))
"""

#28. Write a Python program to find the second largest number in a list.
"""
def second_largest(lst):  # Znajduje druga najwieksza liczbe
    return sorted(set(lst), reverse=True)[1]  # Sortuje unikalne liczby i zwraca druga
print(second_largest([1, 3, 4, 5]))
"""

#6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""
def sort_by_last(lst):  # Sortuje liste krotek
    return sorted(lst, key=lambda x: x[-1])  # Uzywa ostatniego elementu jako klucza
print(sort_by_last([(1, 3), (3, 1), (2, 2)]))
"""

#13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
"""
def generate_3d_array():  # Tworzy 3D tablice
    return [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]  # Uzywa zagniezdzonych petli
print(generate_3d_array())
"""

#31. Write a Python program to count the number of elements in a list within a specified range.
"""
def count_in_range(lst, start, end):  # Liczy elementy w zakresie
    return sum(start <= x <= end for x in lst)  # Uzywa generatora
print(count_in_range([1, 2, 3, 4, 5, 6], 2, 4))
"""

#42. Write a Python program to find missing and additional values in two lists.
#Sample data : Missing values in second list: b,a,c
#Additional values in second list: g,h
"""
def find_differences(lst1, lst2):  # Znajduje roznice miedzy listami
    return list(set(lst1) - set(lst2)), list(set(lst2) - set(lst1))  # Zwraca brakujace i dodatkowe wartosci
print(find_differences([1, 2, 3], [2, 3, 4, 5]))
"""

#20. Write a Python program to access the index of a list.
"""
def index_of_item(lst, item):  # Zwraca indeks elementu
    return lst.index(item)  # Uzywa metody index
print(index_of_item(['apple', 'banana', 'cherry'], 'banana'))
"""

#12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']
"""
def remove_elements(lst):  # Usuwa elementy z listy
    return [x for i, x in enumerate(lst) if i not in (0, 4, 5)]  # Tworzy liste bez wybranych indeksow
print(remove_elements(['red', 'green', 'blue', 'yellow', 'pink', 'black']))
"""

#18. Write a Python program to generate all permutations of a list in Python.
"""
from itertools import permutations  # Importuje permutations
def all_permutations(lst):  # Generuje wszystkie permutacje
    return list(permutations(lst))  # Zwraca permutacje jako liste
print(all_permutations([1, 2, 3]))
"""

#15. Write a Python program to shuffle and print a specified list.
"""
import random  # Importuje modul random
def shuffle_list(lst):  # Tasuje liste
    random.shuffle(lst)  # Uzywa funkcji shuffle
    return lst  # Zwraca potasowana liste
print(shuffle_list([1, 2, 3, 4, 5]))  # Wynik: [2, 4, 1, 5, 3] (przykładowy)
"""

#21. Write a Python program to convert a list of characters into a string.
"""
def list_to_string(lst):  # Konwertuje liste na string
    return ''.join(lst)  # Łączy elementy listy w string
print(list_to_string(['h', 'e', 'l', 'l', 'o']))  # Wynik: 'hello'
"""

#44. Write a Python program to generate groups of five consecutive numbers in a list.
"""
def generate_groups():  # Tworzy grupy liczb
    return [list(range(i, i+5)) for i in range(1, 21, 5)]  # Generuje grupy po piec liczb
"""