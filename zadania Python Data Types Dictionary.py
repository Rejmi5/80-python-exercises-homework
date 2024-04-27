#-------------------------------------------------------------------------------
#20 zadan z dictionary

#14. Write a Python program to sort a given dictionary by key.
"""
# Funkcja sortująca słownik po kluczach i zwracająca nowy posortowany słownik
def sort_dict_by_key(d):
    return {key: d[key] for key in sorted(d.keys())}

# Demonstracja działania funkcji
example_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_dict = sort_dict_by_key(example_dict)
print(sorted_dict)
"""

#2. Write a Python script to add a key to a dictionary.
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}
"""
# Funkcja dodająca klucz i wartość do słownika, zwraca zmodyfikowany słownik
def add_key_to_dict(d, key, value):
    d[key] = value
    return d

# Przykład użycia funkcji do dodania nowego klucza do istniejącego słownika
example_dict = {0: 10, 1: 20}
updated_dict = add_key_to_dict(example_dict, 2, 30)
print(updated_dict)
"""

#8. Write a Python script to merge two Python dictionaries.
"""
# Funkcja łącząca dwa słowniki w jeden
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()  # Tworzenie kopii pierwszego słownika
    merged_dict.update(dict2)   # Aktualizacja słownika wartościami z drugiego
    return merged_dict

# Przykład łączenia dwóch słowników
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
result_dict = merge_dictionaries(dict1, dict2)
print(result_dict)
"""

#20. Write a Python program to print all distinct values in a dictionary.
#Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
#Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""
# Funkcja znajdująca unikatowe wartości w liście słowników
def unique_values_in_dict_list(dict_list):
    unique_values = set(val for d in dict_list for val in d.values())
    return unique_values

# Przykład znajdowania unikatowych wartości
data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}]
unique = unique_values_in_dict_list(data)
print(unique)
"""

#33. Write a Python program to check if multiple keys exist in a dictionary.
"""
# Funkcja sprawdzająca, czy wszystkie podane klucze istnieją w słowniku
def check_keys_exist(d, keys):
    return all(key in d for key in keys)

# Demonstracja sprawdzania istnienia kluczy
example_dict = {'a': 1, 'b': 2, 'c': 3}
keys_to_check = ['a', 'b']
exists = check_keys_exist(example_dict, keys_to_check)
print(exists)
"""

#5. Write a Python program to iterate over dictionaries using for loops.
"""
# Funkcja iterująca po kluczach i wartościach słownika, wypisuje każdą parę
def iterate_dictionary(d):
    for key, value in d.items():
        print(f'Klucz: {key}, Wartość: {value}')

# Przykład iteracji po słowniku
example_dict = {'x': 10, 'y': 20, 'z': 30}
iterate_dictionary(example_dict)  # Wypisze klucze i wartości słownika
"""

#10. Write a Python program to sum all the items in a dictionary.
"""
# Funkcja sumująca wszystkie wartości w słowniku
def sum_dict_values(d):
    return sum(d.values())

# Demonstracja sumowania wartości słownika
example_dict = {'a': 3, 'b': 5, 'c': 8}
total = sum_dict_values(example_dict)
print(total)
"""

#18. Write a Python program to check if a dictionary is empty or not.
"""
# Funkcja sprawdzająca, czy słownik jest pusty
def is_dict_empty(d):
    return not bool(d)

# Przykład użycia funkcji
empty_dict = {}
non_empty_dict = {'a': 1}
print(is_dict_empty(empty_dict))
print(is_dict_empty(non_empty_dict))
"""

#37. Write a Python program to replace dictionary values with their sums.
"""
# Funkcja zamieniająca wartości w słowniku na ich sumy
def replace_values_with_sum(*dicts):
    result = {}
    for dictionary in dicts:
        for key, value in dictionary.items():
            result[key] = result.get(key, 0) + value
    return result

# Przykład sumowania wartości z dwóch słowników
dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 2, 'b': 3, 'c': 5}
combined_dict = replace_values_with_sum(dict1, dict2)
print(combined_dict)
"""

#42. Write a Python program to filter a dictionary based on values.
#Original Dictionary:
#{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
#Marks greater than 170:
#{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
"""
# Funkcja filtrująca słownik, zostawiająca tylko te pary, gdzie wartości przekraczają próg
def filter_dict_by_value(d, threshold):
    return {key: value for key, value in d.items() if value > threshold}

# Przykład użycia funkcji do filtrowania słownika
marks = {'Anna': 55, 'Bob': 75, 'Charlie': 65, 'David': 85}
filtered_marks = filter_dict_by_value(marks, 70)
print(filtered_marks)
"""

#19. Write a Python program to combine two dictionary by adding values for common keys.
#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200, 'd':400}
#Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
"""
# Funkcja łącząca dwa słowniki i sumująca wartości dla wspólnych kluczy
def merge_and_sum_dicts(d1, d2):
    from collections import Counter
    return dict(Counter(d1) + Counter(d2))

# Przykład użycia funkcji do łączenia słowników
dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}
result = merge_and_sum_dicts(dict1, dict2)
print(result)
"""

#24. Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string.
#Sample string : 'w3resource'
#Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
"""
# Funkcja tworząca słownik, gdzie kluczami są znaki, a wartościami liczba ich wystąpień
def create_dict_from_string(s):
    result = {}
    for char in s:
        result[char] = result.get(char, 0) + 1
    return result

# Przykład tworzenia słownika z ciągu znaków
string = 'w3resource'
char_count = create_dict_from_string(string)
print(char_count)
"""

#1. Write a Python script to sort (ascending and descending) a dictionary by value.
# Funkcja sortująca słownik według wartości w porządku rosnącym i malejącym
"""
def sort_dict_by_value(d, descending=False):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=descending))

# Przykład sortowania słownika
dict_to_sort = {'apple': 10, 'orange': 20, 'banana': 5, 'tomato': 1}
sorted_dict_asc = sort_dict_by_value(dict_to_sort)
sorted_dict_desc = sort_dict_by_value(dict_to_sort, True)
print(sorted_dict_asc)
print(sorted_dict_desc)
"""

#56. Write a Python program to convert a dictionary into a list of lists.
#Original Dictionary:
#{1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
#Convert the said dictionary into a list of lists:
#[[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
#Original Dictionary:
#{'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
#Convert the said dictionary into a list of lists:
#[['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]
"""
# Funkcja konwertująca słownik do listy list, gdzie każda lista zawiera klucz i wartość
def dict_to_list_of_lists(d):
    return [[key, value] for key, value in d.items()]

# Przykład konwersji słownika do listy list
dictionary = {'1': 'red', '2': 'green', '3': 'blue'}
result_list = dict_to_list_of_lists(dictionary)
print(result_list)
"""

#13. Write a Python program to map two lists into a dictionary.
"""
# Funkcja mapująca dwie listy do słownika, gdzie pierwsza lista zawiera klucze, a druga wartości
def map_lists_to_dict(keys, values):
    return dict(zip(keys, values))

# Przykład mapowania list do słownika
keys = ['a', 'b', 'c']
values = [1, 2, 3]
mapped_dict = map_lists_to_dict(keys, values)
print(mapped_dict)
"""

#57. Write a Python program to filter even numbers from a dictionary of values.
#Original Dictionary:
#{'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
#Filter even numbers from said dictionary values:
#{'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
#Original Dictionary:
#{'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
#Filter even numbers from said dictionary values:
#{'V': [], 'VI': [], 'VII': [2]}
"""
def filter_even_numbers(d):                             # Funkcja filtrująca parzyste liczby z wartości w słowniku
    return {k: [x for x in v if x % 2 == 0] for k, v in d.items()}

data = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}     # Przykład użycia funkcji
filtered_data = filter_even_numbers(data)
print(filtered_data)
"""

#75. Write a Python program to find all keys in a dictionary that have the given value.
#Sample Output:
#Original dictionary elements:
#{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
#Find all keys in the said dictionary that have the specified value:
#['Roxanne', 'Betty']
"""
def find_keys_with_value(d, value):         # Funkcja zwracająca klucze mające określoną wartość
    return [k for k, v in d.items() if v == value]

my_dict = {'a': 100, 'b': 200, 'c': 100}    # Przykład użycia funkcji
keys_with_100 = find_keys_with_value(my_dict, 100)
print(keys_with_100)
"""

#78. Write a Python program to create a flat list of all the keys in a flat dictionary.
#Sample Output:
#Original dictionary elements:
#{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
#Create a flat list of all the keys of the said flat dictionary:
#['Theodore', 'Roxanne', 'Mathew', 'Betty']
"""
def create_flat_list_of_keys(d):        # Funkcja tworząca listę wszystkich kluczy w słowniku
    return list(d.keys())

flat_dict = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}  # Przykład tworzenia listy kluczy
flat_keys = create_flat_list_of_keys(flat_dict)
print(flat_keys)
"""

#71. Write a Python program to retrieve the value of the nested key indicated by the given selector list from a dictionary or list.
#Sample Output:
#Russell
#2
"""
def get_nested_value(d, keys):      # Funkcja pobierająca wartość dla zagnieżdżonego klucza
    for key in keys:
        d = d[key]
    return d

data = {'info': {'name': {'first': 'John', 'last': 'Doe'}}}     # Przykład użycia funkcji
result = get_nested_value(data, ['info', 'name', 'first'])
print(result)
"""

#6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
#Sample Dictionary ( n = 5) :
#Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""
def generate_squares(n):                # Funkcja generująca słownik z kluczami i ich kwadratami
    return {i: i ** 2 for i in range(1, n+1)}

squares_dict = generate_squares(5)      # Przykład użycia funkcji
print(squares_dict)
"""