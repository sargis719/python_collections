from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import ChainMap
from collections import namedtuple

# Counter Example 1
def letter_count(str):
    """
    This function gets a string and prints
    count of each element.
    """
    set1 = set(str)
    lst = list(str)
    cnt = Counter(lst)
    for i in set1:
        print("Number of {} in {} is {}".format(i, str, cnt[i]))

# Counter Example 2
def common(str):
    """
    This function gets a string and prints the most
    common element in the string.
    """
    lst = list(str)
    cnt = Counter(lst)
    print("The most common element in {} is {}".format(str, cnt.most_common()[0][0]))
    for i in range(1, len(cnt.most_common()), 1):
        if cnt.most_common()[i][1] == cnt.most_common()[0][1]:
            print("and {}".format(cnt.most_common()[i][0]))


# Counter Example 3
def atm_withraw():
    """
    This function asks the user to withraw some amount
    from an ATM machine, and shows the number of each bill
    left in the ATM after the withrawal:
    """
    atm = Counter({100:10, 50:10, 20:5, 10:5, 5:5, 1:4})
    print("The ATM before withrawal: ", dict(atm))
    total = 0
    for i in atm:
        total += i * atm[i]
    withraw = int(input("Please enter amount to withraw: "))
    if withraw <= total:
        for i in atm:
            if withraw >= i:
                temp = withraw // i
                if temp > atm[i]:
                    temp = atm[i]
                deduct = {i:temp}
                atm.subtract(deduct)
                withraw -= temp * i
                total -= temp * i
        print("The ATM after withrawal: ", dict(atm))
    else:
        print("Entered amount is greater than the available amount in the ATM")

# defaultdict Example 1
def a_count(word):
    """
    This function gets a word, and returns
    the number of 'a' in the word.
    """
    lst = list(word)
    letters = defaultdict(int)
    for i in lst:
        letters[i] += 1
    if 'a' not in letters:
        letters['a'] = 0
    return letters['a']

# defaultdict Example 2
def dic_update(dic1, list1):
    """
    This function gets a dictionary of numbers and a list of numbers,
    and updates the dictionary according to the count of each number
    in the list.
    """
    new_dict = defaultdict(int)
    for i in dic1:
        new_dict[i] +=1
    for i in list1:
        new_dict[i] += 1
    dic1 = dict(new_dict)
    return dic1

# defaultdict Example 3
def atm_deposit():
    """
    This function prints the number of each bill in an ATM as a dictionary,
    asks the user for the amount to be deposited, and prints the updated ATM
    according to the amount of money deposited.
    """
    atm = {100: 10, 50: 10, 20: 5, 10: 5,  1: 4}
    print("ATM before deposit: ", atm)
    print("Please make your deposit in the following format: bill-count")
    new_dict = defaultdict(int)
    for i in atm:
        new_dict[i] = atm[i]
    deposit = ""
    while deposit != "done":
        deposit = input("After you done type 'done': ")
        if deposit == 'done':
            break
        lst = deposit.split("-")
        new_dict[int(lst[0])] += int(lst[1])
    atm = dict(new_dict)
    print("ATM after deposit: ", atm)

# OrderDict Example 1
def atm_order(dict1):
    """
    This function gets a dictionary as an ATM and arranges the bills
    by order(largest to smallest).
    """
    # dict1 = {1:50, 20:25, 50:25, 5:40}
    od = OrderedDict()
    lst = (100, 50, 20, 10, 5, 1)
    for i in lst:
        if i in dict1:
            od[i] = dict1[i]
        else:
            od[i] = 0
    for key, value in od.items():
        print(key, value)

# OrderDict Example 2
def letter_count(word):
    """
    This function gets a word and displays the count of
    each letter in alphabetical order using OrderDict.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    od = OrderedDict()
    for i in alphabet:
        if i in word:
            od[i] = word.count(i)
    for value, key in od.items():
        print(value, key)

# deque Example 1
def deque_example1():
    """
    This example shows adding elements to the list according to their priority.
    Hight priority added to the begginng of the list, low priority added to the
    end of the list.
    """
    print("Please enter tasks to the list followed by their priority l/h: ")
    task = ""
    lst = []
    deq = deque(lst)
    while task != "done":
        task = input("Enter the task or 'done' to finish: ")
        if task == "done":
            break
        priority = input("Enter the priority l/h: ")
        if priority == 'h':
            deq.appendleft(task)
            print(deq)
        else:
            deq.append(task)
            print(deq)
    print(deq)

# deque Example 2
def deque_example2(lst, el):
    """
    Given a list, this function returns the count of the element
    by using deque.
    """
    deq = deque(lst)
    return deq.count(el)


def deque_example3():
    """
    This example shows First in First Out waiting list
    through the use of deque.
    """
    deq = deque([])
    deq.append("First")
    print(deq[0], " is in")
    deq.append("Second")
    print(deq[1], " is is")
    deq.append("Third")
    print(deq[2], " is in")
    print(deq[0], " is out")
    deq.popleft()
    deq.append("Fourth")
    print(deq[2], " is in")
    print(deq[0], " is out")
    deq.popleft()
    print(deq[0], " is out")
    deq.popleft()
    deq.append("Fifth")
    print(deq[1], " is in")
    print(deq[0], " is out")
    deq.popleft()
    print(deq[0], " is out")
    deq.popleft()

def chainmap_example1():
    # Adding two dictionaries using ChainMap
    dict1 = {"Apples": 5, "Bananas": 10, "Peaches": 12}
    dict2 = {"Potatoes": 4, "Carrots": 9}
    new_dict = ChainMap(dict1, dict2)
    print(dict(new_dict))

def chainmap_example2():
    # Adding new dictionary to a ChainMap
    dict1 = {"Apples": 5, "Bananas": 10, "Peaches": 12}
    dict2 = {"Potatoes": 4, "Carrots": 9}
    new_dict = ChainMap(dict1, dict2)
    dict3 = {3:10, 4:20}
    new_new_dict = new_dict.new_child(dict3)
    print(dict(new_new_dict))

def chainmap_example3():
    # Removin Element from a ChainMap
    dict1 = {"Apples": 5, "Bananas": 10, "Peaches": 12}
    dict2 = {"Potatoes": 4, "Carrots": 9}
    new_dict = ChainMap(dict1, dict2)
    print(dict(new_dict))
    new_dict.pop("Apples")
    print(dict(new_dict))


def chainmap_example4():
    # Accessing Elements in ChainMap
    dict1 = {"Apples": 5, "Bananas": 10, "Peaches": 12}
    dict2 = {"Potatoes": 4, "Carrots": 9}
    new_dict = ChainMap(dict1, dict2)
    for key, value in new_dict.items():
        print(key, ": ", value)

def nameddtuple_example1():
    # Creating namedtuple and accesing it's elements
    user = namedtuple('user', 'name, age, sex')
    user1 = user(name="John", age=24, sex="M")
    user2 = user(name="Adam", age=22, sex="M")

    print("{} and {} are friends.".format(user1.name, user2.name))
    print("{} is {} and {} is {}.".format(user1.name, user1.age, user2.name, user2.age))

def namedtuple_example2():
    # Creating a new namedtuple by using _replace() function
    user = namedtuple('user', 'name, age, sex')
    user1 = user(name="John", age=24, sex="M")
    user2 = user1._replace(age="88")
    print(user1)
    print(user2)
