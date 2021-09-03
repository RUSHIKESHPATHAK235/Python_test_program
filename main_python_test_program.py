import colorama
import time
from colorama import Fore, Back, Style
colorama.init()

print(Fore.LIGHTGREEN_EX)
print("Total marks test: 30")

print(Fore.WHITE)
a=(input("Test 1 what if you want to show any name in your code in python: "))

if a=="print":
    print(Fore.GREEN)
    time.sleep(0.5)
    print("✔ Test passed 1")
    print("Marks 10")


elif a=="PRINT":
    print(Fore.GREEN)
    time.sleep(0.5)
    print("✔ Test passed 1")
    print("Marks 10")

elif a=="Print":
    print(Fore.GREEN)
    time.sleep(0.5)
    print("✔ Test passed 1")
    print("Marks 10")

else:
    print(Fore.RED)
    time.sleep(0.5)
    print("✘ Test failed 1")
    print("Marks 0")

print(Fore.WHITE)
b=(input("Test 2 what if you want to import colors in text what is the command in python: "))

if b=="colorama":
    print(Fore.GREEN)
    time.sleep(0.5)
    print("✔ Test passed 2")
    print("Marks 10")

elif b=="COLORAMA":
    print(Fore.GREEN)
    time.sleep(0.5)
    print("✔ Test passed 2")
    print("Marks 10")

elif b=="Colorama":
    print(Fore.GREEN)
    time.sleep(0.5)
    print("✔ Test passed 2")
    print("Marks 10")

else:
    print(Fore.RED)
    time.sleep(0.5)
    print("✘ Test failed 2")
    print("Marks 0")

print(Fore.WHITE)
c=(input("Test 3 what if you want to write text in text what you want to write in python: "))

if c=="input":
    print(Fore.GREEN)
    time.sleep(0.5)
    print("✔ Test passed 3")
    print("Marks 10")

elif c=="Input":
    print(Fore.GREEN)
    time.sleep(0.5)
    print("✔ Test passed 3")
    print("Marks 10")

elif c=="INPUT":
    print(Fore.GREEN)
    time.sleep(0.5)
    print("✔ Test passed 3")
    print("Marks 10")
else:
    print(Fore.RED)
    time.sleep(0.5)
    print("✘ Test failed 3")
    print("Marks 0")
