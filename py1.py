import string
import random
import time

print("////////////////////Welcome to password generator v1.0.0////////////////////")

rules = ['digits', 'uppercase letters', 'lowercase letters', 'punctuation']
length = int(input("Please enter your password length: "))


# what is this password for?
name = input("what is this password for: ")

# letter generator


def p0():
    return random.randint(0, 9)


def p1():
    return random.choice(string.ascii_uppercase)


def p2():
    return random.choice(string.ascii_lowercase)


def p3():
    return random.choice(string.punctuation)


fns = []

# functions
print('starting...')
time.sleep(2)

print("set password rules with yes(1), No(0)")

j = 0
for i in range(4):
    print('Do you want your password have', rules[i], '?')
    x = input()
    if i == 0 and (x == 'Yes' or x == 'yes'):
        fns.append(p0)
    elif i == 1 and (x == 'Yes' or x == 'yes'):
        fns.append(p1)
    elif i == 2 and (x == 'Yes' or x == 'yes'):
        fns.append(p2)
    elif i == 3 and (x == 'Yes' or x == 'yes'):
        fns.append(p3)

# generator
password = []
for i in range(length):
    word = random.choice(fns)()
    password.append(word)
print(password, len(password))
