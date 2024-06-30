'''
Python learning
https://www.w3schools.com/python/python_strings_modify.asp

Run: pytest -sv scratch.py -k test_assert --pdb
'''
import fnmatch
import re
import subprocess
import sys
from collections import namedtuple
from pprint import pprint
import pytest
import math
import paramiko
import logging
import os
import json
from time import strftime
import unittest
# from Mymath import Basicmath

logger = logging.getLogger()
# timestamp = strftime("%Y%m%d_%H%M%S")
# log_file = __file__.split('.')[0] + '_' + timestamp + '.log'
# hdlr = logging.FileHandler(log_file)
hdlr = logging.FileHandler(filename=__file__.split('.')[0] + '.log')
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)
logger.info('Starting')


'''
Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType
'''

'''
Python Casting

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
'''

'''
Fixtures are functions, which will run before each test function to which it is applied. 
Fixtures are used to feed some data to the tests such as database connections, 
URLs to test and some sort of input data. 
Therefore, instead of running the same code for every test, 
we can attach fixture function to the tests and it will run and 
return the data to the test before executing each test.

A function is marked as a fixture by −

@pytest.fixture
'''


@pytest.fixture(scope="session", autouse=True)
def test_newline():
    print('\nTest prerequisites')
    yield
    print('\nTest cleanup')

# @pytest.fixture
# def test_create_network():
#     print('\nTest prerequisites1')
#     yield
#     print('\nTest cleanup1')

# https://www.geeksforgeeks.org/python-keywords/?ref=lbp
# #
# 1.
# 2.
# 3.
# and
# as
# assert
# break
# class
# continue
# def
# del
# elif
# else
# except
# False
# finally
# for
# from
# global
# if
# import
# in
# is
# lambda
# None
# nonlocal


def test_not_in_1():
    # Python program to illustrate
    # not 'in' operator
    x = 24
    y = 20
    list1 = [10, 20, 30, 40, 50]

    if x not in list1:
        print("x is NOT present in given list")
    else:
        print("x is present in given list")

    if y in list1:
        print("y is present in given list")
    else:
        print("y is NOT present in given list")



'''
>STRINGS in Python: 
A string is a sequence of characters that can be a combination of letters, numbers, 
and special characters. It can be declared in python by using single quotes, 
double quotes, or even triple quotes. These quotes are not a part of a string, 
they define only starting and ending of the string.  Strings are immutable, i.e., 
they cannot be changed. Each element of the string can be accessed using indexing 
or slicing operations.

capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning

'''

def test_string_f():
    async_flag = '--true'
    docker_container = 'containerz'
    cmd = 'pwd'
    cmd = (f"docker exec {async_flag} {docker_container} "
           f"/bin/bash -c 'cd /tmp && {cmd}'")

    cmd1 = f"f string example {async_flag}"
    print (cmd)
    print (cmd1)

def test_string_1():
    # Python Program for
    # Creation of String

    # Creating a String
    # with single Quotes
    String1 = 'Welcome to the "Geeks" World'
    print("String with the use of Single Quotes: ")
    print(String1)
    # String with the use of Single Quotes:
    # Welcome to the "Geeks" World

    # Creating a String
    # with double Quotes
    String1 = "I'm a Geek"
    print("\nString with the use of Double Quotes: ")
    print(String1)
    # String with the use of Double Quotes:
    # I'm a Geek

    # Creating a String
    # with triple Quotes
    String1 = '''I'm a Geek and I live in a world of "Geeks"'''
    print("\nString with the use of Triple Quotes: ")
    print(String1)
    # String with the use of Triple Quotes:
    # I'm a Geek and I live in a world of "Geeks"

    # Creating String with triple
    # Quotes allows multiple lines
    String1 = '''Geeks
    			For
    			Life'''
    print("\nCreating a multiline String: ")
    print(String1)
    # Creating a multiline String:
    # Geeks
    #                         For
    #                         Life

    # Python Program to Access
    # characters of String

    String1 = "GeeksForGeeks"
    print("Initial String: ")
    print(String1)
    # Initial String:
    # GeeksForGeeks

    # Printing First character
    print("\nFirst character of String is: ")
    print(String1[0])
    # First character of String is:
    # G

    # Printing Last character
    print("\nLast character of String is: ")
    print(String1[-1])
    # Last character of String is:
    # s

    # Program to reverse a string
    gfg = "geeksforgeeks"
    print(gfg[::-1])

    # Program to reverse a string

    gfg = "geeksforgeeks"

    # Reverse the string using reversed and join function
    gfg = "".join(reversed(gfg))

    print(gfg)

    # Add a space between each character if the string
    print(' '.join(gfg))


def test_string_2():
    # Python Program to
    # demonstrate String slicing

    # Creating a String
    String1 = "GeeksForGeeks"
    print("Initial String: ")
    print(String1)

    # Printing 3rd to 12th character
    print("\nSlicing characters from 3-12: ")
    print(String1[3:12])

    # Printing characters between
    # 3rd and 2nd last character
    print("\nSlicing characters between " +
          "3rd and 2nd last character: ")
    print(String1[3:-2])

def test_string_replace_1():
    a = "Hello, World!"
    print(a.replace("H", "J"))


'''
>Lists in Python:
Lists are one of the most powerful data structures in python. 
Lists are sequenced data types.  In Python, an empty list is created using list() function. 
They are just like the arrays declared in other languages. 
But the most powerful thing is that list need not be always homogeneous. 
single list can contain strings, integers, as well as other objects. 
Lists can also be used for implementing stacks and queues. Lists are mutable, i.e., 
they can be altered once declared. The elements of list can be accessed using indexing 
and slicing operations.

There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''

'''
Function	Description
Append()	Add an element to the end of the list
Extend()	Add all elements of a list to another list
Insert()	Insert an item at the defined index
Remove()	Removes an item from the list
Pop()	    Removes and returns an element at the given index
Clear()	    Removes all items from the list
Index()	    Returns the index of the first matched item
Count()	    Returns the count of the number of items passed as an argument
Sort()	    Sort items in a list in ascending order
Reverse()	Reverse the order of items in the list
copy()	    Returns a copy of the list
The operations mentioned above modify the list Itself.

Built-in functions with List
Function	Description
reduce()	apply a particular function passed in its argument to all 
            of the list elements stores the intermediate result and 
            only returns the final summation value
sum()	    Sums up the numbers in the list
ord()	    Returns an integer representing the Unicode code point of the given Unicode character
cmp()	    This function returns 1 if the first list is “greater” than the second list
max()	    return maximum element of a given list
min()	    return minimum element of a given list
all()	    Returns true if all element is true or if the list is empty
any()	    return true if any element of the list is true. if the list is empty, return false
len()	    Returns length of the list or size of the list
enumerate()	Returns enumerate object of the list
accumulate()	apply a particular function passed in its argument to all of the list elements returns a list containing the intermediate results
filter()	tests if each element of a list is true or not
map()	    returns a list of the results after applying the given function to each item of a given iterable
lambda()	This function can have any number of arguments but only one expression, which is evaluated and returned.
'''

def test_list_accessing():
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[:4])
    # ['apple', 'banana', 'cherry', 'orange']
    print(thislist[2:])
    # ['cherry', 'orange', 'kiwi', 'melon', 'mango']
    print(thislist[-4:-1])
    # ['orange', 'kiwi', 'melon']
    # [m:n] m always points to correct index start from 0
    #       n is till n-1 index

    thislist = ["apple", "banana", "cherry"]
    if "apple" in thislist:
        print("Yes, 'apple' is in the fruits list")
    # Yes, 'apple' is in the fruits list

def test_list_change_list_items():
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
    thislist[1:3] = ["blackcurrant", "watermelon"]
    print(thislist)
    # ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

    thislist = ["apple", "banana", "cherry"]
    thislist[1:2] = ["blackcurrant", "watermelon"]
    print(thislist)
    # ['apple', 'blackcurrant', 'watermelon', 'cherry']
    # range points to 1 item but its assigned 2 items

# The main difference between append() and extend() is that
# append() takes a single element as an argument,
# while extend() takes an iterable as an argument.
# An iterable is a sequence of elements, such as a list, tuple, or string.
def test_list_append_client_server():
    servers = ['server1', 'server2', 'server3']
    clients = ['client1', 'client2', 'client3', 'client4', 'client5']
    hosts = servers + clients
    cs_pairs = []
    for host in hosts:
        clients = list(hosts)
        clients.remove(host)
        cs_pairs.append((host, clients))

    print (cs_pairs)
    print(type(cs_pairs[0]))
    # [('server1', ['server2', 'server3', 'client1', 'client2', 'client3', 'client4', 'client5']), ('server2', ['server1', 'server3', 'client1', 'clien
    # t2', 'client3', 'client4', 'client5']), ('server3', ['server1', 'server2', 'client1', 'client2', 'client3', 'client4', 'client5']), ('client1', [
    # 'server1', 'server2', 'server3', 'client2', 'client3', 'client4', 'client5']), ('client2', ['server1', 'server2', 'server3', 'client1', 'client3'
    # , 'client4', 'client5']), ('client3', ['server1', 'server2', 'server3', 'client1', 'client2', 'client4', 'client5']), ('client4', ['server1', 'se
    # rver2', 'server3', 'client1', 'client2', 'client3', 'client5']), ('client5', ['server1', 'server2', 'server3', 'client1', 'client2', 'client3', 'client4'])]
    # <class 'tuple'>


def test_list_extend_build_cmd():
    filename = 'file1'
    resolution = None
    start = 'start'
    end = 'end'
    cmd = ["rrdtool", "fetch", filename]
    if resolution is not None:
        cmd.extend(["--resolution", str(resolution)])
    if start is not None:
        cmd.append(["--start", str(start)])
    if end is not None:
        cmd.extend(["--end", str(end)])
    print (cmd)
    # ['rrdtool', 'fetch', 'file1', '--start', 'start', '--end', 'end']
    # ['rrdtool', 'fetch', 'file1', ['--start', 'start'], '--end', 'end'] if we add
    # append instead of extend then the list will be added as a seperate element
    # it won't insert
    cmd = " ".join(cmd)
    print (cmd)
    # rrdtool fetch file1 --start start --end end

def test_list_clear_1():
    thislist = ["apple", "banana", "cherry"]
    thislist.clear()
    print(thislist)
    # []

def test_list_del_1():
    file = "first line \n second line \n third line"
    lines = file.splitlines()
    for line in lines:
        print (line)
    del lines[0]
    # this is another way to loop through list if you want index
    for i in range(len(lines)):
        print (lines[i])

def test_list_pop_line():
    output = "\nfirst line\n# Report timeout (screen): 4 sec.\nthird line"
    outputlines = output.splitlines()

    # Parse to get report interval
    # Report timeout (screen): 4 sec.
    interval_rgx = r'# Report timeout .+:\s+(?P<interval>\d+)\s+sec'
    interval = None
    while len(outputlines) > 0:
        line = outputlines.pop(0)
        match = re.search(interval_rgx, line)
        if match:
            interval = int(match.group('interval'))
            break
    print (interval)

def test_list_comprehension_with_dictionary():
    mapping_dict = {"a": 1, "b":2, "c":3}
    string = " ".join(
        "--net:'{}={}'".format(k, v)
        for (k, v) in list(mapping_dict.items()))
    print (string)

def test_list1():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    print("\nletters[1] = {}".format(letters[1]))
    letters.remove("a")
    del letters[-2]
    print(letters)
    letters.pop()
    letters.pop(0)
    letters.pop(2)
    print(letters)

    users = ['val', 'bob', 'mia', 'ron', 'ned']
    # Sorting a list permanently
    users.sort()
    # Sorting a list permanently in reverse alphabetical order
    users.sort(reverse=True)
    # Sorting a list temporarily
    print(sorted(users))
    print(sorted(users, reverse=True))
    # Reversing the order of a list
    users.reverse()

    # Printing the numbers 0 to 1000
    for number in range(11):
        print(number)
    # Printing the numbers 1 to 1000
    for number in range(1, 11):
        print(number)
    # Making a list of numbers from 1 to a million
    numbers = list(range(1, 11))

    # Finding the minimum value in a list
    ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
    youngest = min(ages)
    # Finding the maximum value
    ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
    oldest = max(ages)
    # Finding the sum of all values
    ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
    total_years = sum(ages)

    # Sequence Slicing
    # d  has an index of 3  here, e  has an index of 4 , and f  has an index of 5,
    # but since the slicing syntax is upper-bound exclusive, we need to pass 6
    # as the upper bound.
    print("letters[3:6] = {}".format(letters[3:6]))
    print("letters[0:3] = {}".format(letters[:3]))
    print("letters[-2] = {}".format(letters[-2]))
    print("letters[-3:] = {}".format(letters[-3:]))

    newlist = []
    for item in range(len(letters)):
        if (item % 2 == 0):
            newlist.append(letters[item])
    print(newlist)

    # The complete syntax of list slicing is [start:end:step] .
    # When you don't pass a step, Python assumes the step is 1. [:]
    # itself means to get everything from start to end. So, [::2]
    # means get everything from start to end at a step of two.
    print("letters[::2] = {}".format(letters[::2]))

    my_list = []
    for i in range(1, 21, 3):
        my_list.append(i)
    print(my_list)
    # import pdb;pdb.set_trace()
    # range()  is a Python built-in function that generates a range of integers.
    # However, range()  creates a Python range object.
    # To get a real list object, you need to use the list() function to convert
    # the range object into a list object.
    my_range = range(1, 21)
    print(list(my_range))

    my_range = range(10, 201, 10)
    print(list(my_range))

    # List comprehension
    print([x * 10 for x in range(1, 21)])
    print([str(x) for x in range(1, 21)])

    duplicate_list = ["1", 1, "1", 2]
    unique_list = []
    for item in duplicate_list:
        if item not in unique_list:
            unique_list.append(item)
    print("Duplicate list {} Unique list {}".format(duplicate_list, unique_list))

    duplicate_list = set(duplicate_list)
    print(list(duplicate_list))

def test_list_1():
    # Declaring a list
    L = [1, "a", "string", 1 + 2]
    print(L)
    # Adding an element in the list
    L.append(6)
    print(L)
    # Deleting last element from a list
    L.pop()
    print(L)
    # Displaying Second element of the list
    print(L[1])

    # Creating a List
    List1 = []
    print('List1 length {}'.format(len(List1)))

    # Creating a List of numbers
    List2 = [10, 20, 14]
    print(len(List2))

    # input size of the list
    n = int(input("Enter the size of list : "))
    # store integrs in a list using map, split and strip functions
    lst = list(map(int, input("Enter the integer elements:\
    ").strip().split()))[:n]
    print('The list is:', lst)  # printing the list


def test_list_append():
    # Python program to demonstrate
    # Addition of elements in a List

    # Creating a List
    List = []
    print("Initial blank List: ")
    print(List)

    # Addition of Elements
    # in the List
    List.append(1)
    List.append(2)
    List.append(4)
    print("\nList after Addition of Three elements: ")
    print(List)

    # Adding elements to the List
    # using Iterator
    for i in range(1, 4):
        List.append(i)
    print("\nList after Addition of elements from 1-3: ")
    print(List)

    # Adding Tuples to the List
    List.append((5, 6))
    print("\nList after Addition of a Tuple: ")
    print(List)

    # Addition of List to a List
    List2 = ['For', 'Geeks']
    List.append(List2)
    print("\nList after Addition of a List: ")
    print(List)


def test_list_insert():
    # Python program to demonstrate
    # Addition of elements in a List

    # Creating a List
    List = [1, 2, 3, 4]
    print("Initial List: ")
    print(List)

    # Addition of Element at
    # specific Position
    # (using Insert Method)
    List.insert(3, 12)
    List.insert(0, 'Geeks')
    print("\nList after performing Insert Operation: ")
    print(List)


def test_list_extend():
    # Python program to demonstrate
    # Addition of elements in a List

    # Creating a List
    List = [1, 2, 3, 4]
    print("Initial List: ")
    print(List)

    # Addition of multiple elements
    # to the List at the end
    # (using Extend Method)
    List.extend([8, 'Geeks', 'Always'])
    print("\nList after performing Extend Operation: ")
    print(List)

    # Output
    # Initial List:
    # [1, 2, 3, 4]
    #
    # List after performing Extend Operation:
    # [1, 2, 3, 4, 8, 'Geeks', 'Always']


def test_list_reverse(test_newline):
    # Reversing a list
    mylist = [1, 2, 3, 4, 5, 'Geek', 'Python']
    mylist.reverse()
    print(mylist)

    # ['Python', 'Geek', 5, 4, 3, 2, 1]


'''
Elements can be removed from the List by using the built-in remove() function 
but an Error arises if the element doesn’t exist in the list. Remove() method 
only removes one element at a time, to remove a range of elements, the iterator is used. 
The remove() method removes the specified item.
'''


def test_list_remove():
    # Python program to demonstrate
    # Removal of elements in a List

    # Creating a List
    List = [1, 2, 3, 7, 8, 9, 10, 11, 12]
    print("Initial List: ")
    print(List)

    # Removing elements from List
    # using Remove() method
    List.remove(8)
    List.remove(12)
    print("\nList after Removal of two elements: ")
    print(List)

    try:
        List.remove(13)
    except ZeroDivisionError:
        print('Divide by 0')
    except ValueError:
        print('Value not in list')
    except Exception as e:
        print('Error {}'.format(e))

    # Initial List:
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    #
    # List after Removal of two elements:
    # [1, 2, 3, 4, 7, 8, 9, 10, 11, 12]


'''
pop() function can also be used to remove and return an element from the list, 
but by default it removes only the last element of the list, to remove an element 
from a specific position of the List, the index of the element is passed 
as an argument to the pop() method.
'''


def test_list_pop():
    List = [1, 2, 3, 4, 5]

    # Removing element from the
    # Set using the pop() method
    List.pop()
    print("\nList after popping an element: ")
    print(List)

    # Removing element at a
    # specific index from the
    # Set using the pop() method
    List.pop(2)
    print("\nList after popping a specific element: ")
    print(List)

    # List after popping an element:
    # [1, 2, 3, 4]
    #
    # List after popping a specific element:
    # [1, 2, 4]


def test_list_slice():
    # Python program to demonstrate
    # Removal of elements in a List

    # Creating a List
    List = ['G', 'E', 'E', 'K', 'S', 'F',
            'O', 'R', 'G', 'E', 'E', 'K', 'S']
    print("Initial List: ")
    print(List)

    # Print elements of a range
    # using Slice operation
    Sliced_List = List[3:8]
    print("\nSlicing elements in a range 3-8: ")
    print(Sliced_List)

    # Print elements from a
    # pre-defined point to end
    Sliced_List = List[5:]
    print("\nElements sliced from 5th "
          "element till the end: ")
    print(Sliced_List)

    # Printing elements from
    # beginning till end
    Sliced_List = List[:]
    print("\nPrinting all elements using slice operation: ")
    print(Sliced_List)

    # Initial List:
    # ['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']
    #
    # Slicing elements in a range 3-8:
    # ['K', 'S', 'F', 'O', 'R']
    #
    # Elements sliced from 5th element till the end:
    # ['F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']
    #
    # Printing all elements using slice operation:
    # ['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']

    # Creating a List
    List = ['G', 'E', 'E', 'K', 'S', 'F',
            'O', 'R', 'G', 'E', 'E', 'K', 'S']
    print("Initial List: ")
    print(List)

    # Print elements from beginning
    # to a pre-defined point using Slice
    Sliced_List = List[:-6]
    print("\nElements sliced till 6th element from last: ")
    print(Sliced_List)

    # Print elements of a range
    # using negative index List slicing
    Sliced_List = List[-6:-1]
    print("\nElements sliced from index -6 to -1")
    print(Sliced_List)

    # Printing elements in reverse
    # using Slice operation
    Sliced_List = List[::-1]
    print("\nPrinting List in reverse: ")
    print(Sliced_List)

    # Initial List:
    # ['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']
    #
    # Elements sliced till 6th element from last:
    # ['G', 'E', 'E', 'K', 'S', 'F', 'O']
    #
    # Elements sliced from index -6 to -1
    # ['R', 'G', 'E', 'E', 'K']
    #
    # Printing List in reverse:
    # ['S', 'K', 'E', 'E', 'G', 'R', 'O', 'F', 'S', 'K', 'E', 'E', 'G']


'''
List comprehensions are used for creating new lists from other iterables like tuples, 
strings, arrays, lists, etc. A list comprehension consists of brackets 
containing the expression, which is executed for each element along with the 
for loop to iterate over each element. 
newList = [ expression(element) for element in oldList if condition ]
newlist = [expression for item in iterable if condition == True]
'''


def test_list_comprehension():
    # Python program to demonstrate list
    # comprehension in Python

    # below list contains square of all
    # odd numbers from range 1 to 10
    odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
    print(odd_square)

    # [1, 9, 25, 49, 81]

    # for understanding, above generation is same as,
    odd_square = []

    for x in range(1, 11):
        if x % 2 == 1:
            odd_square.append(x ** 2)

    print(odd_square)


def test_list_sort_with_function_1():
    num_list = [22, 34, 11, 35, 89, 37, 93, 56, 108]
    print('Original Number:', num_list)  # Original Number: [22, 34, 11, 35, 89, 37, 93, 56, 108]

    def sort_by_second_num(num):
        return num % 10

    num_list.sort(key=sort_by_second_num)
    # num_list.sort(key=lambda n: n%10)
    print('Lambda sorted number:', num_list)  # Lambda sorted number: [11, 22, 93, 34, 35, 56, 37, 108, 89]


def test_list_case_insensitive():
    thislist = ["banana", "Orange", "Kiwi", "cherry"]
    # thislist.sort()
    thislist.sort(key=str.lower)
    print(thislist)
    #['Kiwi', 'Orange', 'banana', 'cherry']
    #by default uppercase sorted first
    #['banana', 'cherry', 'Kiwi', 'Orange']




def test_list_map_1():
    num = ['10', '20', '30']
    print(num)
    numint = list(map(int, num))
    print(numint)
    for i in map(int, num):
        print(i)


'''
>enumerate(iterable, start)
'''
def test_list_enumerate_startat1():
    my_list = ['apple', 'banana', 'cherry']
    for index, value in enumerate(my_list, start=1):
        print(index, value)

def test_list_enumerate_reverse():
    my_list = ['apple', 'banana', 'cherry']
    for index, value in enumerate(reversed(my_list)):
        print(len(my_list) - index -1, value)

def test_list_enumerate_set_staicip():
    uplink_id_list = ['up1', 'up2', 'up3']
    static_ip_list = ['192.168.10.1', '192.168.10.2', '192.168.10.3']
    for indx, uplink_id in enumerate(uplink_id_list):
        ip_info = static_ip_list[indx]
        print("Configuring uplink with static ip %s" % ip_info)


def test_list_enumerate():
    # Python program to illustrate
    # enumerate function
    l1 = ["eat", "sleep", "repeat"]
    s1 = "geek"

    # creating enumerate objects
    obj1 = enumerate(l1)
    obj2 = enumerate(s1)

    print("Return type:", type(obj1))
    print(list(enumerate(l1)))

    # changing start index to 2 from 0
    print(list(enumerate(s1, 2)))

    # Return type:
    # [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
    # [(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]

    # Python program to illustrate
    # enumerate function in loops
    l1 = ["eat", "sleep", "repeat"]

    # printing the tuples in object directly
    for ele in enumerate(l1):
        print(ele)

    # changing index and printing separately
    for count, ele in enumerate(l1, 100):
        print(count, ele)

    # getting desired output from tuple
    for count, ele in enumerate(l1):
        print(count)
        print(ele)

    # (0, 'eat')
    # (1, 'sleep')
    # (2, 'repeat')
    # 100 eat
    # 101 sleep
    # 102 repeat
    # 0
    # eat
    # 1
    # sleep
    # 2
    # repeat

    l2 = list(enumerate(l1))
    print(l2)

'''
>map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

Python map() Function Syntax
Syntax: map(fun, iter)

Parameters:

fun: It is a function to which map passes each element of given iterable.
iter: It is iterable which is to be mapped.
NOTE: You can pass one or more iterable to the map() function.

Returns: Returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)

NOTE : The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) .  
'''

def test_map_split():
    deployment = '100/20'
    # total, iteration = map(int, deployment.split('/'))
    # print (total, iteration)
    iteration = list(map(int, deployment.split('/')))
    print (iteration)

def test_map_with_lambda_tuple():
    # Double all numbers using map and lambda
    numbers = (1, 2, 3, 4)
    result = map(lambda x: x + x, numbers)
    print(list(result))

def test_map_with_lambda_addlists():
    # Double all numbers using map and lambda

    numbers1 = [1, 2, 3, 4]
    numbers2 = [1, 3, 3, 4]
    result = map(lambda x,y: x + y, numbers1, numbers2)
    print(list(result))
    # [2, 5, 6, 8]

def test_map_string_to_list():
    strl = ['hi', 'hello']
    # strl_new = list(map(list,strl))
    # strl_r = list(map(lambda x: list(reversed(x)),strl_new))
    strl_r = list(map(lambda x: list(reversed(x)),list(map(list,strl))))
    print (strl_r)
    # [['i', 'h'], ['o', 'l', 'l', 'e', 'h']]

'''
>Filter
The filter() method filters the given sequence with the help of a 
function that tests each element in the sequence to be true or not. 
'''
def test_filter_find_odd():
    # a list contains both even and odd numbers.
    seq = [0, 1, 2, 3, 5, 8, 13]

    # result contains odd numbers of the list
    result = filter(lambda x: x % 2 != 0, seq)
    print(list(result))
    # [1, 3, 5, 13]

    # result contains even numbers of the list
    result = filter(lambda x: x % 2 == 0, seq)
    print(list(result))
    # [0, 2, 8]

'''
In Python, using filter() with None as the first argument filters 
out elements from an iterable that are considered "falsy" in Python.
'''
def test_filter_none():
    numbers = [0, 1, 2, 3, None, "", False, True]

    filtered = list(filter(None, numbers))
    print(filtered)

'''
>fnmatch
'''
def test_filter_1():
    file_list = []
    for root, dirnames, filenames in os.walk(os.getcwd()):
        for filename in fnmatch.filter(filenames, '*.py'):
            file_list.append(os.path.join(root, filename))
    print (file_list)

def test_list_constructor():
    thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
    print(thislist)

'''
Tuples in Python: A tuple is a sequence of immutable Python objects. 
Tuples are just like lists with the exception that tuples cannot be changed once declared. 
Tuples are usually faster than lists.
Tuple items are ordered, unchangeable, and allow duplicate values.
Since tuples are indexed, they can have items with the same value:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
'''

def test_tuple_namedtuple():
    data_container = namedtuple(
        'data_container', ['scm',
                           'client', 'server'])
    data_container('scm1', 'cl1', 'server1')
    print(data_container[0])

# Namedtuple in Python
# Python supports a type of container dictionaries called “namedtuple()”
# present in the module, “collections“.
# Like dictionaries, they contain keys that are hashed to a particular value.
# But on contrary, it supports both access from key-value and iteration,
# the functionality that dictionaries lack.

def test_namedtuple_1():
    # data_container = namedtuple(
    #     'data_container', ['scm',
    #                        'client', 'server',
    #                        'client_if', 'server_if',
    #                        'client_gw', 'server_gw',
    #                        'cgw_shell', 'sgw_shell',
    #                        'config', 'org_id',
    #                        'version', 'internal',
    #                        'snmp_server_shell',
    #                        'snmp_trap_server',
    #                        'snmp_server'])
    # print("Tuple {0}".format(data_container))

    # Python code to demonstrate namedtuple()

    # from collections import namedtuple

    # Declaring namedtuple()
    Student = namedtuple('Student', ['name', 'age', 'DOB'])

    # Adding values
    S = Student(name='Nandini', age='19', DOB='2541997')

    # Access using index
    print("The Student age using index is : ", end="")
    print(S[1])

    # Access using name
    print("The Student name using keyname is : ", end="")
    print(S.name, S.age, S.DOB)

def test_tuple_accessing_1():
    tup = (1, "a", "string", 1 + 2)
    print(tup)
    print(tup[1])
    print(tup[1:3])
    #(1, 'a', 'string', 3)
    #a
    #('a', 'string')

def test_tuple_loop_1():
    thistuple = ("apple", "banana", "cherry")
    for x in thistuple:
        print(x)


'''
Sets are used to store multiple items in a single variable.
Set items are unordered, unchangeable, and do not allow duplicate values.

Method	Shortcut	Description
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns whether another set contains this set or not
 	<	Returns whether all items in this set is present in other, specified set(s)
issuperset()	>=	Returns whether this set contains another set or not
 	>	Returns whether all items in other, specified set(s) is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others
'''
def test_set1():
    # Difference between discard() and remove()

    # initialize my_set
    my_set = {1, 3, 4, 5, 6}
    print(my_set)

    # discard an element
    # Output: {1, 3, 5, 6}
    my_set.discard(4)
    print(my_set)

    # remove an element
    # Output: {1, 3, 5}
    my_set.remove(6)
    print(my_set)

    # discard an element
    # not present in my_set
    # Output: {1, 3, 5}
    my_set.discard(2)
    print(my_set)

    # add item to set
    my_set.add(7)

    # remove an element
    # not present in my_set
    # you will get an error.
    # Output: KeyError

    my_set.remove(2)

def test_set_add_update():
    thisset = {"apple", "banana", "cherry"}
    tropical = {"pineapple", "mango", "papaya"}

    thisset.update(tropical)

    print(thisset)

    thisset = {"apple", "banana", "cherry"}
    mylist = ["kiwi", "orange"]

    thisset.update(mylist)

    print(thisset)

def test_set2():
    # initialize my_set
    # Output: set of unique elements
    my_set = set("HelloWorld")
    print(my_set)

    # pop an element
    # Output: random element
    print(my_set.pop())

    # pop another element
    my_set.pop()
    print(my_set)

    # clear my_set
    # Output: set()
    my_set.clear()
    print(my_set)

    print(my_set)
    #
    # {'d', 'r', 'l', 'H', 'e', 'o', 'W'}
    # d
    # {'l', 'H', 'e', 'o', 'W'}
    # set()
    # set()

'''
Iterations in Python: Iterations or looping can be performed in python by ‘for’ 
and ‘while’ loops. Apart from iterating upon a particular condition, 
we can also iterate on strings, lists, and tuples.
'''


def test_iteration_1():
    i = 1
    while i < 10:
        print(i)
        i += 1

    s = "Hello World"
    for i in s:
        print(i)

    L = [1, 4, 5, 7, 8, 9]
    for i in L:
        print(i)

    for i in range(0, 10):
        print(i)


# not
# or
# pass
# raise
# return
# True
# try
# while
# with
# yield

def test_is():
    a = 10
    b = 100
    if a is b:
        print('a is b')
    else:
        print('a is not b')


# lambda
def test_lambda_1():
    sum1 = lambda n1, n2: n1 + n2
    print(sum1(10, 20))


# assert
def test_assert_1():
    assert 10 > 20


# except
# try
# finally

def test_except_1():
    try:
        d = 10 / 0
    except Exception as e:
        print('In exception {}'.format(e))
    finally:
        print('{}/{}'.format(10, 0))


def test_calculate_uppercase():
    '''
   Tutorials
   POINT
   '''
    str = "Tutorials POINT"
    upper = 0
    index = 0
    while index < str.__len__():
        if str[index].isupper():
            upper += 1
        index += 1
    print("Upper {0}".format(upper))


def test_sumlist():
    list = [100, 200, 300, 400]
    total = 0
    for n in list:
        total += n
    print("Total of list {0} is {1}".format(list, total))




def test_100_2():
    a = 1
    _a = 2
    _a2 = 3
    # 2a = 4


def test_100_3():
    a = 1
    b = 2
    print(a == b)
    # print(b == c)


def test_100_4():
    a = "1"
    b = 2
    print(int(a) + b)

'''
Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

'''

def test_dict1():
    """
   Test dictionary functionlity.
   :return:
   """
    d1 = {"a": 1, "b": 2}
    d2 = dict(a=1, b=2)
    print(d1)
    print(d2)

    # As you see, accessing dictionary values follows the same syntax
    # as accessing list items. The difference is that lists have indexes,
    # while dictionaries have keys that you create by yourself
    print(d1["b"])

    sum_local = d1["a"] + d1["b"]
    print(sum_local)

    d1["c"] = 3
    print(d1)

    d = {"a": 1, "b": 2, "c": 3}
    print(sum(d.values()))

    mydict = {'A': 71.07884,
              'B': 110,
              'C': 103.14484,
              'D': 115.08864,
              'E': 129.11552,
              'F': 147.1766,
              }

    name = "ABC"

    for key, val in mydict.items():
        print(key, val)

    print(sum(value for key, value in mydict.items() if key in name))

    # dictionary comprehension
    dnew = dict((key, value) for key, value in d.items() if value > 1)
    print(dnew)

    d3 = {"a": list(range(1, 11)),
          "b": list(range(11, 21)),
          "c": list(range(21, 31))}
    # d3["a"] = list(range(1,11))
    # d3["b"] = list(range(11,21))
    # d3["c"] = list(range(21,31))
    #  We're also using the built-in Python pprint  module,
    #  which is used to print out well-formatted views of datatypes in Python.
    pprint(d3)
    pprint(d3["b"][2])
    print("b has value {} \n a has value{}".format(d3["b"], d3["a"]))

    alien_0 = {'color': 'green', 'points': 5}
    print(alien_0)
    del alien_0['points']
    print(alien_0)

    d_profile = {"Profile1": 1, "Profile2": 2, "Profile3": 3}
    d_network = {"Network1": 1, "Network2": 2, "Network3": 3}
    d_master = {"profile": d_profile, "network": d_network}
    print(d_master)
    # {
    # 'profile': {'Profile1': 1, 'Profile2': 2, 'Profile3': 3},
    # 'network': {'Network1': 1, 'Network2': 2, 'Network3': 3}
    # }

def test_dict_update():
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    thisdict.update({"color": "red"})
    print (thisdict)
    # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

def test_dict_del():
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    del thisdict["model"]
    print(thisdict)
    # {'brand': 'Ford', 'year': 1964}

'''
If else loop
'''

def test_ifelse_shorthand():
    a = 2
    b = 330
    print("A") if a > b else print("B")


'''
While loop
'''

def test_while_loop_break_continue():
    i = 0
    while i < 6:
        i += 1
        if i == 3:
            continue
        print(i)
        if i == 5:
            break

'''
for loop
'''

def test_for_loop_with_else():
    for x in range(6):
        # if x == 3: break
        print(x)
    else:
        print("Finally finished!")

'''
Functions
'''

def test_func_arbitrary_arguments():
    '''If you do not know how many arguments that will be passed into your function,
    add a * before the parameter name in the function definition.

    This way the function will receive a tuple of arguments,
    and can access the items accordingly:
    '''
    def func(*args):
        print ("args will be received as tuple {}".format(args))
        if args:
            extra_args = ' '.join(map(str, args))
        else:
            extra_args = ''
        print (extra_args)
    func('arg1', 'arg2', 'arg3')


'''If you do not know how many keyword arguments that will be passed into your function, 
add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, 
and can access the items accordingly:
'''
def test_fun_arbitrary_keyword_arguments():
    def my_function(**kid):
        print("His last name is " + kid["lname"])
        print("His first name is " + kid.get('fname'))

    my_function(fname="Tobias", lname="Refsnes")

def test_recursion_1():
    def tri_recursion(k):
        if (k > 0):
            result = k + tri_recursion(k - 1)
            print(result)
        else:
            result = 0
        return result

    print("\n\nRecursion Example Results")
    tri_recursion(6)


def acceleration(v1, v2, t1, t2):
    a = (v2 - v1) / (t2 - t1)
    return a


def test_fun_default_values(r=10, h=2):
    print(acceleration(0, 10, 0, 20))
    liquid_vol = (4 * math.pi * r ** 3) / 3 - (math.pi * h * 2 * (3 * r - h)) / 3
    print(liquid_vol)


def test_func_positional_keyword_arguments():
    c = 1

    def foo():
        # c is a local variable here
        # python gives priority to local variable
        c = 2
        return c

    c = 3
    print(foo())

    # Using positional arguments
    def describe_pet(animal, name):
        """Display information about a pet."""
        print("\nI have a " + animal + ".")
        print("Its name is " + name + ".")

    describe_pet('hamster', 'harry')
    describe_pet('dog', 'willie')

    # Using keyword arguments, positions does not matter
    def describe_pet(animal, name):
        """Display information about a pet."""
        print("\nI have a " + animal + ".")
        print("Its name is " + name + ".")

    describe_pet(animal='hamster', name='harry')
    describe_pet(name='willie', animal='dog')


def test_func_arbitrary():
    # Collecting an arbitrary number of arguments
    def make_pizza(size, *toppings):
        """Make a pizza."""
        print("\nMaking a " + size + " pizza.")
        print("Toppings:")
        for topping in toppings:
            print("- " + topping)

    # Make three pizzas with different toppings.
    make_pizza('small', 'pepperoni')
    make_pizza('large', 'bacon bits', 'pineapple')
    make_pizza('medium', 'mushrooms', 'peppers',
               'onions', 'extra cheese')


def test_function_kwargs():
    # Collecting an arbitrary number of keyword arguments
    def build_profile(first, last, **user_info):
        """Build a user's profile dictionary."""
        # Build a dict with the required keys.
        profile = {'first': first, 'last': last}
        # Add any other keys and values.
        for key, value in user_info.items():
            profile[key] = value
        return profile

    # Create two users with different kinds
    # of information.
    user_0 = build_profile('albert', 'einstein',
                           location='princeton')
    user_1 = build_profile('marie', 'curie',
                           location='paris', field='chemistry')
    print(user_0)
    print(user_1)


'''
>Python Lambda
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.
lambda arguments : expression
'''

'''
>Python filter
'''

'''
>Python map
'''


'''
>yield
The yield statement suspends a function’s execution and 
sends a value back to the caller, but retains enough state to 
enable the function to resume where it left off. 
When the function resumes, it continues execution immediately 
after the last yield run. This allows its code to produce a series 
of values over time, rather than computing them at once and sending them back like a list.
It is generally used to convert a regular Python function into a generator. 
A generator is a special function in Python that returns a generator object to the caller. 
Since it stores the local variable states, hence overhead of memory allocation is controlled.

'''
def test_yield_infinite_generator():
    # A Python program to generate squares from 1
    # to 100 using yield and therefore generator

    # An infinite generator function that prints
    # next square number. It starts with 1
    def nextSquare():
        i = 1
        # An Infinite loop to generate squares
        while True:
            yield i * i
            i += 1  # Next execution resumes
            # from this point

    # Driver code to test above generator
    # function
    for num in nextSquare():
        if num > 10:
            break
        print(num)


'''
>__call__
'''
'''
>subprocess
Subprocess in Python is used to run new programs and scripts by spawning new processes. And it enables the user to launch new programs right from the current Python program thanks to the subprocess module. 

So, you may use a subprocess in Python to run external applications from a git repository or code from C or C++ programs. 
Using subprocesses in Python, you can also obtain exit codes and input, output, or error streams.
The Subprocess in Python can be useful if you've ever intended to streamline your command-line scripting or utilize Python alongside command-line apps—or any applications, for that matter. The Python subprocess module may help with everything from starting GUI interfaces to executing shell commands and command-line programs.

Why run & Popen ?
In general, you should use run if you just need to run a command and capture its output 
and Popen if you need more control over the process, 
such as interacting with its input and output streams.
The Popen class has several methods that allow you to interact with the process, 
such as communicate(), poll(), wait(), terminate(), and kill().
'''

r"""def test_subprocess_call():
    subprocess.call(['mkdir -p  ' + tgt_dir],
                    cwd='/mnt/project/shplatform/nx/',
                    shell=True)
    subprocess.call(['rm -rf *'],
                    cwd='/mnt/project/shplatform/nx/' + tgt_dir,
                    shell=True)
    subprocess.call(["scp",
                     "root@" + host + ":/var/vm_images/*.tgz",
                     "/mnt/project/shplatform/nx/" + tgt_dir])
    subprocess.call(['ls'],
                    cwd='/mnt/project/shplatform/nx/' + tgt_dir)
"""
def test_subprocess_check_call():
    pass

def test_subprocess_check_output():
    pass

def test_subprocess_run_1():
    # run can be used instead of call or check_output

    # result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
    result = subprocess.run(["python", "Rest.py"], shell=True, capture_output=True, text=True)

    print(result.stdout)

def test_subprocess_check_ouput():
    try:
        ans = subprocess.check_output(["python", "--version"], text=True)
        print(ans)

    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code {e.returncode}")

def test_subprocess_popen_without_text():
    # without text=True the output will be in binary, you need to decode it
    process = subprocess.Popen(["dir"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    print("Output:", output.decode())
    print("Error:", error.decode())

    # above can also be achieved with this
    # os.system('dir')

def test_subprocess_popen_with_text():
    # here output will be str, no need to decode
    process = subprocess.Popen(["dir"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
    output, error = process.communicate()
    # print("Output:", output)
    # print("Error:", error)
    for line in output.splitlines():
        if re.search(r'duplicates.csv', line):
            print ('Found file duplicates.csv')
            break

def test_subprocess_popen_with_text_run_script():
    # here output will be str, no need to decode
    process = subprocess.run(["python", "Rest.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
    # output, error = process.communicate()
    print("Output:", process)
    # print("Error:", error)


def test_subprocess_popen_interprocess():
    # use shell=False otherwise child process will be running in background
    # even after the test exits
    lsProcess = subprocess.Popen(["python"], stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, text=True, shell=False)
    grepProcess = subprocess.Popen(
        ["help"], stdin=lsProcess.stdout,
        stdout=subprocess.PIPE, text=True, shell=False)
    output, error = grepProcess.communicate()
    grepProcess.terminate()
    lsProcess.terminate()

    print(output)
    print(error)

def test_subprocess_popen_ssh():
    host = "test.rebex.net"
    port = 22
    username = "demo"
    password = "password"

    command = "ls"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password, port=port)

    (stdin, stdout, stderr) = ssh.exec_command(command)
    lines = stdout.readlines()
    print(lines)
    # ssh.close()
    #
    # user = 'demo'
    # hostname = 'test.rebex.net'
    # passw = "password"
    # ssh_cmd = \
    #     ["sshpass",
    #      "-p", '{}'.format(passw),
    #      "ssh",
    #      "-T",
    #      "-o", "StrictHostKeyChecking=no",
    #      "-o", "UserKnownHostsFile=/dev/null",
    #      "-o", "ConnectTimeout=120",
    #      "{}@{}".format(user, hostname)]
    # ssh = subprocess.Popen(ssh_cmd,
    #                        stdin=subprocess.PIPE,
    #                        stdout=subprocess.PIPE,
    #                        stderr=subprocess.PIPE,
    #                        shell=True)
    cmds = ['pwd',
            'ls']
    # cmds.extend(cmds_list)
    commands = '\n'.join(cmds)
    commands = commands.encode()
    (output, err) = ssh.communicate(commands)
    if ssh.returncode != 0:
        logger.info(err)
        logger.info(output)
        pytest.fail("ssh error")

    # real life example - call another script and process the output
#     args_str = ("/u/qa/tests/install/rbt-install.t --image=" +
#                 deliverable_info['url'] + " --pxe=" +
#                 deliverable_info['base_path'].replace('/mnt/', '') +
#                 " --appliance=" + vlab_appliance + " --owner=" +
#                 vlab_user + " --vlab=" + vlab_name)
#     if scc_hostname:
#         args_str += " --configuring_scc_hostname=" + scc_hostname
# # Execute the command in shell using subprocess.
#     arguments = shlex.split(args_str)
#     pipe = subprocess.Popen(arguments, stdout=subprocess.PIPE)
#     # Search for success and return True.
#     for line in pipe.stdout:
#         if (re.search(r'\[PASS\]: Successfully installed.*', line)
#                 is not None):
#             return True

r"""
os.waitpid

def create_directory(tested_device):
    ""Create a directory in SH to copy the pload tool.""
    sh_os = OS.get(tested_device)
    if not sh_os.path.exists(DEFAULT_DIR):
        sh_os.shell.exec_command('mkdir ' + DEFAULT_DIR)
    # Copy the pload from testing deivce to the tested device.
    p = subprocess.Popen(["scp", SOURCE_PATH, tested_device.username + '@' +
                         tested_device.hostname + ':' + DEFAULT_DIR])
    os.waitpid(p.pid, 0)
    
    
        
        
            try:
                curl_cmd = ['curl', '-s', '-k', image_url, ]
                curl_process = subprocess.Popen(
                    curl_cmd,
                    stdout=subprocess.PIPE
                )
                tar_cmd = ["tar", "xzf", '-']
                returncode = subprocess.call(
                    tar_cmd,
                    cwd=local_image_dir,
                    stdin=curl_process.stdout
                )
                curl_process.stdout.close()
                if returncode:
                    log.error("Extracting failed. Wrong URL?")
                    raise subprocess.CalledProcessError(
                        returncode=returncode,
                        cmd=' | '. join([' '.join(tar_cmd),
                                         ' '.join(curl_cmd)]))
            except OSError as err:
                log.error("Downloading or extracting image failed")
                if err.errno == errno.ENOENT:
                    log.error("curl or tar not installed")
                raise
                
    def execute_cmd_locally(self, cmd, log_stdout=True):
        log.info('Execute cmd: %s' % cmd)
        out = ''
        err = ''
        ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              close_fds=True)
        for line in ps.stdout.readlines():
            if not line:
                break
            out += line.decode("utf-8")
            if log_stdout:
                log.info(line)
        for line in ps.stderr.readlines():
            if not line:
                break
            err += line.decode("utf-8")
            logging.error(line)
        rc = ps.wait()
        log.info('RC: %s' % rc)
        if log_stdout:
            log.info('Out: %s' % out)
        if err:
            log.info('Error: %s' % err)
        return rc, out, err

    """
def test_subprocess_call():
    import subprocess
    ans = subprocess.call(["python", "--version"])
    # ans = subprocess.call(["pwd"])
    if ans == 0:
        print("Command executed.")
    else:
        print("Command failed.", ans)


def create_directory(tested_device):
    """Create a directory in SH to copy the pload tool."""
    sh_os = OS.get(tested_device)
    if not sh_os.path.exists(DEFAULT_DIR):
        sh_os.shell.exec_command('mkdir ' + DEFAULT_DIR)
    # Copy the pload from testing deivce to the tested device.
    p = subprocess.Popen(["scp", SOURCE_PATH, tested_device.username + '@' +
                         tested_device.hostname + ':' + DEFAULT_DIR])
    os.waitpid(p.pid, 0)

r'''
>pexpect
C:\Users\krmit\PycharmProjects\dist-packages\portfolio_system_tests\legacy_core_infra_nx\openstack\enable_ssh_auth.py

'''
'''
>File handling
'''
def test_count_words_file():
    fileobj = open("words1.txt", "r")
    out = fileobj.readlines()
    count = 0
    for line in out:
        print(line)
        count += len(line.split())
    print("Total words = {}".format(count))
    fileobj.close()

    count = 0
    with open("words1.txt", "r") as file:
        str = file.read()
        # print(str)
        # str_list = str.split()
        # count = count + len(str_list)
        strnew = str.replace(",")
        count += len(strnew.split())
    print("Total words = {}".format(count))

'''
>Class
Note: The __init__() function is called 
automatically every time the class is being used to create a new object.
'''
def test_class1():
    class Employee:
        def __init__(self, name, id_, age):
            self.name = name
            self.id = id_
            self.age = age

        def age(self):
            return self.age

    emp1 = Employee("Mithun", 213525, 38)
    print(emp1.name)


def test_ssh():
    host = "test.rebex.net"
    port = 22
    username = "demo"
    password = "password"

    command = "ls"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password, port=port)

    (stdin, stdout, stderr) = ssh.exec_command(command)
    lines = stdout.readlines()
    print(lines)
    ssh.close()


def test_os_cmd():
    output = os.system('dir')
    for line in output:
        print("---->" + line)
    print(output)


def test_input_1():
    # Python program showing
    # a use of input()

    val = input("Enter your value: ")
    import pdb;
    pdb.set_trace()
    print(val)


def test_input_2():
    # Program to check input
    # type in Python

    num = int(input("Enter number :"))
    print(num)
    name1 = input("Enter name : ")
    print(name1)

    # Printing type of input value
    print("type of number", type(num))
    print("type of name", type(name1))





def test_print_1():
    # This Python program must be run with
    # Python 3 as it won't work with 2.7.

    # ends the output with '@'
    print("Python", end='\n')
    print("GeeksforGeeks")


def test_print_2():
    # Python program showing
    # a use of format() method

    # combining positional and keyword arguments
    print('Number one portal is {0}, {1}, and {other}.'
          .format('Geeks', 'For', other='Geeks'))

    # using format() method with number
    print("Geeks :{0:2d}, Portal :{1:8.2f}".
          format(12, 00.546))

    # Changing positional argument
    print("Second argument: {1:3d}, first one: {0:7.2f}".
          format(47.42, 11))

    print("Geeks: {a:5d}, Portal: {p:8.2f}".
          format(a=453, p=59.058))


'''
Operator	Description	Syntax
+	Addition: adds two operands	x + y
–	Subtraction: subtracts two operands	x – y
*	Multiplication: multiplies two operands	x * y
/	Division (float): divides the first operand by the second	x / y
//	Division (floor): divides the first operand by the second	x // y
%	Modulus: returns the remainder when the first operand is divided by the second	x % y
**	Power: Returns first raised to power second	x ** y


Comparison Operator	Description	Syntax
>	Greater than: True if the left operand is greater than the right	x > y
<	Less than: True if the left operand is less than the right	x < y
==	Equal to: True if both operands are equal	x == y
!=	Not equal to – True if operands are not equal	x != y
>=	Greater than or equal to True if the left operand is greater than or equal to the right	x >= y
<=	Less than or equal to True if the left operand is less than or equal to the right	x <= y
is 	x is the same as y	x is y
is not	x is not the same as y	x is not y


Logical Operator	Description	Syntax
and	Logical AND: True if both the operands are true	x and y
or	Logical OR: True if either of the operands is true 	x or y
not	Logical NOT: True if the operand is false 	not x


Bitwise Operator	Description	Syntax
&	Bitwise AND	x & y
|	Bitwise OR	x | y
~	Bitwise NOT	~x
^	Bitwise XOR	x ^ y
>>	Bitwise right shift	x>>
<<	Bitwise left shift	x<<


Assignment Operator	Description	Syntax
=	Assign value of right side of expression to left side operand 	x = y + z
+=	Add AND: Add right-side operand with left side operand and then assign to left operand	a+=b     a=a+b
-=	Subtract AND: Subtract right operand from left operand and then assign to left operand	a-=b     a=a-b
*=	Multiply AND: Multiply right operand with left operand and then assign to left operand	a*=b     a=a*b
/=	Divide AND: Divide left operand with right operand and then assign to left operand	a/=b     a=a/b
%=	Modulus AND: Takes modulus using left and right operands and assign the result to left operand	a%=b     a=a%b
//=	Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to left operand	a//=b     a=a//b
**=	Exponent AND: Calculate exponent(raise power) value using operands and assign value to left operand	a**=b     a=a**b
&=	Performs Bitwise AND on operands and assign value to left operand	a&=b     a=a&b
|=	Performs Bitwise OR on operands and assign value to left operand	a|=b     a=a|b
^=	Performs Bitwise xOR on operands and assign value to left operand	a^=b     a=a^b
>>=	Performs Bitwise right shift on operands and assign value to left operand	a>>=b     a=a>>b
<<=	Performs Bitwise left shift on operands and assign value to left operand	a <<= b     a= a << b

Identity Operators
is          True if the operands are identical 
is not      True if the operands are not identical 

Membership Operators
in            True if value is found in the sequence
not in        True if value is not found in the sequence

Operator Associativity
If an expression contains two or more operators with the same precedence then Operator Associativity is used to determine. 
It can either be Left to Right or from Right to Left.


Ternary Operator
[on_true] if [expression] else [on_false] 

'''


def test_operator_overloading_1():
    # Python Program illustrate how
    # to overload an binary + operator

    class A:
        def __init__(self, a):
            self.a = a

        # adding two objects
        def __add__(self, o):
            return self.a + o.a

    ob1 = A(1)
    ob2 = A(2)
    ob3 = A("Geeks")
    ob4 = A("For")

    print(ob1 + ob2)
    print(ob3 + ob4)
    # GeeksFor


def test_ternary_operator_1():
    # Program to demonstrate conditional operator
    a, b = 10, 20

    # Copy value of a in min if a < b else copy b
    min = a if a < b else b

    print(min)


def test_operator_associativity():
    # Examples of Operator Associativity

    # Left-right associativity
    # 100 / 10 * 10 is calculated as
    # (100 / 10) * 10 and not
    # as 100 / (10 * 10)
    print(100 / 10 * 10)

    # Left-right associativity
    # 5 - 2 + 3 is calculated as
    # (5 - 2) + 3 and not
    # as 5 - (2 + 3)
    print(5 - 2 + 3)

    # left-right associativity
    print(5 - (2 + 3))

    # right-left associativity
    # 2 ** 3 ** 2 is calculated as
    # 2 ** (3 ** 2) and not
    # as (2 ** 3) ** 2
    print(2 ** 3 ** 2)



'''
>Any

any(iterable)
iterable	An iterable object (list, tuple, dictionary)

Returns true if any of the items is True.
'''

def test_any_1():
    # Since all are false, false is returned
    print(any([False, False, False, False]))

    # Here the method will short-circuit at the
    # second item (True) and will return True.
    print(any([False, True, False, False]))

    # Here the method will short-circuit at the
    # first (True) and will return True.
    print(any([True, False, False, False]))


def test_any_2():
    marks = [0, 50, 100, 0]
    print(any(x > 35 for x in marks))
    assert all(x == 0 for x in marks), "Not all got distinction"

def test_any_dict():
    mydict = {0: "Apple", 1: "Orange"}
    x = any(mydict)
    print(x)

    # Returns True because the second key is True.

    # For dictionaries the any() function checks the keys, not the values.

'''
All
Returns true if all of the items are True (or if the iterable is empty). 
'''


def test_all_2():
    marks = [36, 58, 90, 34]
    if all(x > 35 for x in marks):
        print('PASS')
    else:
        print('FAIL')


'''
Difference between == and is operator in Python
The Equality operator (==) is a comparison operator in Python that compare values of 
both the operands and checks for value equality. 
Whereas the ‘is’ operator is the  identity operator that checks whether 
both the operands refer to the same object or not (present in the same memory location).
'''


def test_is_1():
    # python3 code to
    # illustrate the
    # difference between
    # == and is operator
    # [] is an empty list
    list1 = []
    list2 = []
    list3 = list1

    print(id(list1))
    print(id(list2))
    print(id(list3))

    if (list1 == list2):
        print("True")
    else:
        print("False")

    if (list1 is list2):
        print("True")
    else:
        print("False")

    if (list1 is list3):
        print("True")
    else:
        print("False")

    list3 = list3 + list2

    if (list1 is list3):
        print("True")
    else:
        print("False")


"""
>Inheritance
"""

def test_oops_inheritence_1():
    class Network():
        def __init__(self, name, uri):
            self.name = name
            self.uri = uri

        def get_network_type(self):
            type = "Ethernet"
            return type

    class Network_FC(Network):
        def __init__(self, name, uri, fc_type):
            super().__init__(name, uri)
            self.fc_type = fc_type

        def get_fc_type(self):
            return self.fc_type

        # Overriding parent methods
        def get_network_type(self):
            type = "FC"
            return type

    # net1 = Network("Network1", "uri1")
    # net2 = Network("Network2", "uri2")
    fcnet1 = Network_FC("Network1", "uri1", "fabric attached")
    fcnet2 = Network_FC("Network1", "uri1", "direct attached")

    print(fcnet1.get_fc_type())
    print(fcnet2.get_network_type())

"""
>Polymorphism and Inheritance
>Method Overriding
Like in other programming languages, 
the child classes in Python also inherit methods and attributes from the parent class. 
We can redefine certain methods and attributes specifically to fit the child class, 
which is known as Method Overriding.

"""
def test_oops_polymorphism_inheritance():
    from math import pi

    class Shape:
        def __init__(self, name):
            self.name = name

        def area(self):
            pass

        def fact(self):
            return "I am a two-dimensional shape."

        def __str__(self):
            return self.name

    class Square(Shape):
        def __init__(self, length):
            super().__init__("Square")
            self.length = length

        def area(self):
            return self.length ** 2

        def fact(self):
            return "Squares have each angle equal to 90 degrees."

    class Circle(Shape):
        def __init__(self, radius):
            super().__init__("Circle")
            self.radius = radius

        def area(self):
            return pi * self.radius ** 2

    a = Square(4)
    b = Circle(7)
    print(b)
    print(b.fact())
    print(a.fact())
    print(b.area())

    """
    Circle
    I am a two-dimensional shape.
    Squares have each angle equal to 90 degrees.
    153.93804002589985
    """

def test_file_1():
    with open("hitrate.sh", "r") as fileobj:
        # lines = fileobj.read()
        lines = fileobj.readlines()

    # print(lines)
    with open("hitrate.backup", 'w') as nfileobj:
        for line in lines:
            nfileobj.write(line)

    if os.system('sed -i "s/\'//g" hitrate.backup'):
        print("same")
    for line in lines:
        print(line.rstrip())


def test_json():
    numbers = [2, 3, 5, 7, 11, 13]
    filename = 'numbers.json'
    with open(filename, 'w') as f_obj:
        # f_obj.write(str(numbers))
        json.dump(numbers, f_obj)
    with open(filename) as f_obj:
        numbers = json.load(f_obj)
    print(numbers)


def test_unittest():
    # from full_names import get_full_name
    janis = get_full_name('janis', 'joplin')
    print(janis)
    bob = get_full_name('bob', 'dylan')
    print(bob)


'''
>Exception
'''
def test_exception_1():
    prompt = "How many tickets do you need? "
    num_tickets = input(prompt)
    # num_tickets = int(num_tickets)
    # assert num_tickets < 100
    try:
        num_tickets = int(num_tickets)
        assert num_tickets < 100
    # except ValueError:
    except Exception as e:
        print("Please try again.", e)
        pytest.fail("Test fail")
    finally:
        print("Your tickets are printing.")

def test_exception_finally():
    try:
        div = 1
        assert div != 0
        res = 10 / div
    except Exception as e:
        print("Exception {}".format(e))
        # raise Exception("ZeroDivisionError")
        raise ZeroDivisionError
    finally:
        print("Printed always div {}".format(div))

def test_exception_pytest_fail():
    def square(x):
        assert x >= 0, 'Only positive numbers are allowed'
        return x * x

    try:
        # assert 2 <= 0
        square(-2)
    except Exception as msg:
        print(msg)
        raise  # without this test case will be considered as Pass
        # pytest.fail()


def test_string1():
    x = 'banana'
    x = 10020
    for idx in range(0, 5):
        print(x[idx], "=", id(x[idx]))


def test_zip1():
    a = [1, 2, 3]
    b = [4, 5, 6, 7]
    for x, y in zip(a, b):
        print(x + y)
    # 5
    # 7
    # 9


def test_getattr1():
    class Person:
        age = 23
        name = "Adam"

    # person = Person()
    print('The age is:', getattr(Person, "age"))
    print('The name is:', getattr(Person, "name"))
    print('The id is:', getattr(Person, "id", 20))
    # print('The age is:', person.age)

    print(setattr(Person, 'id', 20))

    print(hasattr(Person, 'id'))

    delattr(Person, 'id')

    if not hasattr(Person, 'id'):
        print("Attribute 'id' is not present")

'''
>assert
Syntax : assert condition, error_message(optional) 

Parameters:

condition : The boolean condition returning true or false. 
error_message : The optional argument to be printed in console in case of AssertionError
Returns: Returns AssertionError, in case the condition evaluates to false 
along with the error message which when provided. 

'''
def test_assert_1():
    assert 5 > 10

def test_assertEqual():
    pass

'''
>Print commands
'''
def test_print_1():
    a = 10
    b = 20
    print("Sum {} + {} = {}".format(a, b, a + b))

def test_print_flush():
    import time

    count_seconds = 3
    for i in reversed(range(count_seconds + 1)):
        if i > 0:
            # print(i, end='\n', flush=True)
            print(i, end='>>>', flush=True)
            time.sleep(1)
        else:
            print('Start')
    #3>>>2>>>1>>>Start


def test_print_sep():
    a = 12
    b = 12
    c = 2022
    # print(a, b, c)
    print(a, b, c, sep="-")
    # 12 - 12 - 2022

def test_print_file():
    import io

    # declare a dummy file
    dummy_file = io.StringIO()

    # add message to the dummy file
    print('Hello Geeks!!', file=dummy_file)

    # get the value from dummy file
    print(dummy_file.getvalue())

def test_print_without_newline():
    # Python 3 code for printing
    # on the same line printing
    # geeks and geeksforgeeks
    # in the same line

    print("geeks", end=" ")
    print("geeksforgeeks")

    # array
    a = [1, 2, 3, 4]

    # printing a element in same
    # line
    for i in range(4):
        print(a[i], end=" ")
    # geeks geeksforgeeks
    # 1 2 3 4 PASSED


'''
Function	Description
abs()	Returns the absolute value of a number
all()	Returns True if all items in an iterable object are true
any()	Returns True if any item in an iterable object is true
ascii()	Returns a readable version of an object. Replaces none-ascii characters with escape character
bin()	Returns the binary version of a number
bool()	Returns the boolean value of the specified object
bytearray()	Returns an array of bytes
bytes()	Returns a bytes object
callable()	Returns True if the specified object is callable, otherwise False
chr()	Returns a character from the specified Unicode code.
classmethod()	Converts a method into a class method
compile()	Returns the specified source as an object, ready to be executed
complex()	Returns a complex number
delattr()	Deletes the specified attribute (property or method) from the specified object
dict()	Returns a dictionary (Array)
dir()	Returns a list of the specified object's properties and methods
divmod()	Returns the quotient and the remainder when argument1 is divided by argument2
enumerate()	Takes a collection (e.g. a tuple) and returns it as an enumerate object
eval()	Evaluates and executes an expression
exec()	Executes the specified code (or object)
filter()	Use a filter function to exclude items in an iterable object
float()	Returns a floating point number
format()	Formats a specified value
frozenset()	Returns a frozenset object
getattr()	Returns the value of the specified attribute (property or method)
globals()	Returns the current global symbol table as a dictionary
hasattr()	Returns True if the specified object has the specified attribute (property/method)
hash()	Returns the hash value of a specified object
help()	Executes the built-in help system
hex()	Converts a number into a hexadecimal value
id()	Returns the id of an object
input()	Allowing user input
int()	Returns an integer number
isinstance()	Returns True if a specified object is an instance of a specified object
issubclass()	Returns True if a specified class is a subclass of a specified object
iter()	Returns an iterator object
len()	Returns the length of an object
list()	Returns a list
locals()	Returns an updated dictionary of the current local symbol table
map()	Returns the specified iterator with the specified function applied to each item
max()	Returns the largest item in an iterable
memoryview()	Returns a memory view object
min()	Returns the smallest item in an iterable
next()	Returns the next item in an iterable
object()	Returns a new object
oct()	Converts a number into an octal
open()	Opens a file and returns a file object
ord()	Convert an integer representing the Unicode of the specified character
pow()	Returns the value of x to the power of y
print()	Prints to the standard output device
property()	Gets, sets, deletes a property
range()	Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
repr()	Returns a readable version of an object
reversed()	Returns a reversed iterator
round()	Rounds a numbers
set()	Returns a new set object
setattr()	Sets an attribute (property/method) of an object
slice()	Returns a slice object
sorted()	Returns a sorted list
staticmethod()	Converts a method into a static method
str()	Returns a string object
sum()	Sums the items of an iterator
super()	Returns an object that represents the parent class
tuple()	Returns a tuple
type()	Returns the type of an object
vars()	Returns the __dict__ property of an object
zip()	Returns an iterator, from two or more iterators
'''


"""
>iter
"""

"""
>next
"""
'''
>eval
eval(expression, globals, locals)
Python eval() function parse the expression argument 
and evaluate it as a Python expression and runs Python expression (code) within the program.
'''
def test_eval_1():
    x = 'print(55)'
    eval(x)
    print(eval('1+2'))
    print(eval("sum([1, 2, 3, 4])"))


"""
>Nonlocal Keyword
The nonlocal keyword is used to work with variables inside nested functions.

The nonlocal keyword makes the variable belong to the outer function.
"""
def test_nonlocal_1():
    # global variable
    a = 15
    b = 10

    # function to perform addition
    def add():
        c = a + b
        print(c)
        a = 100

    # calling a function
    add()
    print (a)

    # nonlocal keyword
    def fun():
        var1 = 10

        def gun():
            # tell python explicitly that it
            # has to access var1 initialized
            # in fun on line 2
            # using the keyword nonlocal

            nonlocal var1
            #this means you need to have var1 in the parent function

            # var1 = 20 #otherwise var1 will be considered as local to gun()

            var1 = var1 + 10
            print(var1)

        gun()

    fun()

"""
>module
"""
def test_module_rename():
    import Rest as rest_module

    a = rest_module.person1["age"]
    print(a)

def test_module_dir():
    import collections

    x = dir(collections)
    print(x)

    if 'namedtuple' in x:
        print ('namedtuple module in collections')

"""
>datetime
A reference of all the legal format codes:

Directive	Description	Example	Try it
%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%C	Century	20	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%	
%G	ISO 8601 year	2018	
%u	ISO 8601 weekday (1-7)	1	
%V	ISO 8601 weeknumber (01-53)	01
"""
def test_datetime_strftime():
    import datetime

    timestamp = strftime("%Y%m%d-%H%M%S")
    print (timestamp)

"""
>json
"""
def test_json_loads_dumps():
    import json

    f = open('compatibility_sets.json', 'r')
    file_content = f.read()
    # json.loads will convert file content to python dictionary
    json_dict = json.loads(file_content)
    f.close()
    print (json_dict)
    print (json_dict[0]['vc']['version'])

    json_dict[0]['vc']['version'] = '6.7.0-11726889'
    with open ('compatibility_sets.json', 'w') as fp:
        fp.write(json.dumps(json_dict))
        # json.dumps will convert python dictionary to json format
    fp.close()

# this is for file reading and writing
def test_json_load_dump():
    #json file read
    with open('compatibility_sets.json', 'r') as fp:
        json_dict = json.load(fp)
        # print (json_dict)
    # json file write
    with open ('compatibility_sets1.json', 'w') as fp1:
        json.dump(json_dict, fp1)

# def run_cmd_as_root(self, login_user, login_password, root_password, cmd,
#                     hostname, timeout=60,
#                     search=None, fail_on_timeout=True, ignore_from_search_list=None):
#     ssh_cmd = CMD_SSH_SDDC_MANAGER % (login_user, hostname)
#     self.args.log.info('Spawning: "%s"' % ssh_cmd)
#     p = pexpect.spawn(ssh_cmd, encoding='utf-8', timeout=timeout)
#     try:
#         if not search:
#             search = ['password', 'Password', pexpect.EOF,
#                       pexpect.TIMEOUT, '#', ']#', ']\$',
#                       'Log Collection completed']
#         if ignore_from_search_list:
#             self.args.log.info('Search list: "%s"' % search)
#             self.args.log.info('Ignored from search: "%s"' % ignore_from_search_list)
#             search = [x for x in search if x not in ignore_from_search_list]
#             self.args.log.info('Filter search list: "%s"' % search)
#         cmd_executed = False
#         vrack_password_sent = False
#         cmd_output = []
#         while True:
#             i = p.expect(search)
#             expect_before = p.before
#             cmd_output.append(expect_before)
#             self.args.log.debug(expect_before)
#             self.args.log.debug(p.after)
#             if not p.isalive():
#                 self.args.log.info('Process exited')
#                 break
#             if search[i] == 'password' or search[i] == 'Password':
#                 if vrack_password_sent:
#                     self.args.log.info(
#                         'Send password: "%s"' % root_password)
#                     p.sendline(root_password)
#                 else:
#                     self.args.log.info(
#                         'Send password: "%s"' % login_password)
#                     p.sendline(login_password)
#                     vrack_password_sent = True
#             elif search[i] == pexpect.TIMEOUT:
#                 self.args.log.info('Timeout on command: "%s"' % cmd)
#                 if fail_on_timeout:
#                     raise AssertionError('Timeout on command: "%s"' % cmd)
#                 else:
#                     break
#             elif search[i] == pexpect.EOF:
#                 self.args.log.info('Command completed')
#                 break
#             elif search[i] == '#' or search[i] == ']#':
#                 if cmd_executed:
#                     self.args.log.info('exit')
#                     p.sendline('exit')
#                     break
#                 else:
#                     self.args.log.info('Send cmd: "%s"' % cmd)
#                     p.sendline(cmd)
#                     cmd_executed = True
#                     time.sleep(3)
#             elif search[i] == ']\$':
#                 if cmd_executed:
#                     self.args.log.info('exit')
#                     p.sendline('exit')
#                     break
#                 else:
#                     self.args.log.info('Send su -')
#                     p.sendline('su -')
#             elif search[i] == 'Log Collection completed':
#                 self.args.log.info('Log Collection completed')
#                 break
#             else:
#                 time.sleep(3)
#         p.close(True)
#         return cmd_output
#     except Exception as ex:
#         trace = traceback.format_exc()
#         self.args.log.error(ex)
#         self.args.log.error(trace)


"""
>rest api
"""
def test_rest_api():
    import requests
    import json

    # header = {'Content-type': 'application/json',
    #           'RBM-Authorization': self.config.rbm_auth_token}
    # # json.dumps encodes the python object into json
    # resp = requests.post(url, data=json.dumps(request_body),
    #                      headers=header)
    #

    # data = {"suite_id": suite_id, "name": run_name}
    # header = {"Content-Type": "application/json"}
    # url = \
    #     "https://testrail.lab.nbttech.com/core/index.php?/api/v2/add_run/" + \
    #     str(project_id)
    # res = requests.post(
    #     url,
    #     data=json.dumps(data),
    #     headers=header,
    #     auth=(
    #         'icebox-users@riverbed.com',
    #         '2top90!'))
    # print(res.json()["id"])

    headers = {'content-type': 'application/json'}

    url = "https://reqres.in/api/users/2"
    # url = 'http://{0}:{1}/api/st_mgmt/1.0/'.format(controller_ip,controller_port)
    # response = requests.request("GET", url, headers=headers)
    response = requests.get(url, headers=headers)

    print("\n" + response.text)
    if response.status_code == 200:
        print("response.status_code {}".format(response.status_code))
        print("response.reason {}".format(response.reason))
        print("response.text {}".format(json.loads(response.text)))
        # print("response.headers {}".format(response.headers))

        d_res = json.loads(response.text)
        print("email {}".format(d_res['data']['email']))

    url = "https://jsonplaceholder.typicode.com/posts"
    # payload = {"email":"krmithun@gmail.com", "first_name":"Mithun", "last_name":"Rajarama"}
    response = requests.request("GET", url, headers=headers)
    print("response.status_code {}".format(response.status_code))
    print("response.reason {}".format(response.reason))
    print("response.text {}".format(json.loads(response.text)))

    url = "https://fakerestapi.azurewebsites.net/api/v1/Users"
    # payload = "{\"id\":100,\"userName\":\"Mithun\",\"password\":\"Rajarama\"}"
    # payload = json.dumps({
    #   "id": 20,
    #   "userName": "string1",
    #   "password": "string1"
    # })
    payload = {
        "id": 20,
        "userName": "string1",
        "password": "string1"
    }
    # response = requests.request("POST", url, data=payload, headers=headers)
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print("response.status_code {}".format(response.status_code))
    print("response.reason {}".format(response.reason))
    print("response.text {}".format(json.loads(response.text)))
    print("response.text {}".format(response.text))
    print("response.text {}".format(str(response.json())))

"""
>main
Write a standalone python script
"""
def test_python_standalone():
    def main():
        print ('In main')

    if __name__ == main():
        main()

"""
>sshpass

to run ssh command in single line we need to install sshpass in linux
sshpass -p “ENTER PASSWORD HERE” ssh testuser@122.153.12.31

For Ubuntu
    sudo apt install sshpass
For RHEL
    yum install epel-release
    yum install sshpass
"""

"""
Other important packages
        'pytest',
        'mock',
        'future',
        # PQ testing and tools dependencies
        'pq-ixia',
        'pq-metrics-plugin',
        'pytest-appliance-artifact-collector-plugin',
        'pytest-appliance-log-collector-plugin',
        'pytest-testrail-plugin',
        # Test report dependancies.
        'Flask==0.10.1',
        'Flask-Mail==0.9.1',
        # 'Jinja2==2.8',  Installed along with Flask
        # 'wsgiref',  Doesn't appear to be used by anything
        'requests',
        'python-cinderclient==4.3.0',
        # environment-templates breakages for cmd2
        'python-openstackclient==3.15.0',
        'cmd2==0.8.5',
        # Test dependencies
        'idna==2.7',
        'cryptography',
        'ipaddress',
        'reschema',
        # 'pytest-blocker',  # does not work with pytest 4+
        'pyaml',
        'parse',
        'pexpect',
        'rpyc',
        # Libraries to read etcd keys
        'python-etcd',
        # Other
        'paramiko',
        'urllib3<1.24,>=1.21.1',
        'uritemplate==0.6',
"""