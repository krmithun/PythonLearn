from collections import namedtuple
from pprint import pprint
import pytest
import math
import paramiko
import logging
import os
import json
import unittest

logger = logging.getLogger()
hdlr = logging.FileHandler(filename='scratch.log')
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)


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


def test_tuple():
    data_container = namedtuple(
        'data_container', ['scm',
                           'client', 'server',
                           'client_if', 'server_if',
                           'client_gw', 'server_gw',
                           'cgw_shell', 'sgw_shell',
                           'config', 'org_id',
                           'version', 'internal',
                           'snmp_server_shell',
                           'snmp_trap_server',
                           'snmp_server'])
    print("Tuple {0}".format(data_container))


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
    for number in range(1001):
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


def test_tuple():
    # Overwriting a tuple
    dimensions = (800, 600)
    print(dimensions)
    dimensions = (1200, 900)


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


def acceleration(v1, v2, t1, t2):
    a = (v2 - v1) / (t2 - t1)
    return a


def test_acc(r=10, h=2):
    print(acceleration(0, 10, 0, 20))
    liquid_vol = (4 * math.pi * r ** 3) / 3 - (math.pi * h * 2 * (3 * r - h)) / 3
    print(liquid_vol)


def test_func1():
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

    # Using keyword arguments
    def describe_pet(animal, name):
        """Display information about a pet."""
        print("\nI have a " + animal + ".")
        print("Its name is " + name + ".")

    describe_pet(animal='hamster', name='harry')
    describe_pet(name='willie', animal='dog')


def test_func2():
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


def test_kwargs():
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


def test_yield():
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
        if num > 100:
            break
        print(num)


def test_global_var():
    def foo():
        global c
        c = 1
        return c

    foo()
    print(c)


def test_count_words():
    # str = "Life is all about possibilities"
    # l_words = str.split()
    print(len("Life is all about possibilities".split()))


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
    for line in output.split("\n"):
        print("---->" + line)
    # print(output)


def test_exception():
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
    else:
        print("Your tickets are printing.")


def test_oops1():
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

    # remove an element
    # not present in my_set
    # you will get an error.
    # Output: KeyError

    my_set.remove(2)


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


def test_exception1():
    try:
        div = 0
        assert div != 0
        res = 10 / div
    except Exception as e:
        print("Exception {}".format(e))
        # raise Exception("ZeroDivisionError")
        raise ZeroDivisionError
    finally:
        print("div {}".format(div))


def test_exception2():
    def square(x):
        assert x >= 0, 'Only positive numbers are allowed'
        return x * x

    assert 2 < 0
    try:
        square(-2)
    except AssertionError as msg:
        print(msg)


def test_exception3():
    def square(x):
        assert x >= 0, 'Only positive numbers are allowed'
        return x * x

    try:
        # assert 2 <= 0
        square(-2)
    except Exception as msg:
        print(msg)
        raise
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

