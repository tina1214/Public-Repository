""""
Tina Hou
August 12 2023
Kaggle Test Prompt 1:
Check if a user given list of numbers have two numbers that add to the user given target number
Prompt 2:
Sort user given list of numbers from small to big
"""
import os
def Menu():
    os.system('clear')
    print("##################################################################")
    print("#               Kaggle Test Prompt Introductions                 #")
    print("# Prompt 1: The user will provide a list of numbers and a target #")
    print("# number. The program will check whether any two numbers from    #")
    print("# the given list adds up to the given target number.             #")
    print("#                                                                #")
    print("# Prompt 2: The user will provide a list of numbers in any order.#")
    print("# The program will sort the list from ascending order.           #")
    print("#                                                                #")
    print("#                     Test the Programs                          #")
    print("# Press 1 to test Prompt 1                                       #")
    print("# Press 2 to test Prompt 2                                       #")
    print("##################################################################")
    choice = input("Enter number to test Prompt: ")
    os.system('clear')
    if '1' in choice:
        prompt1()
    elif '2' in choice:
        prompt2()

def prompt1():
    input1 = input("Enter your list of numbers in format # # # etc.: ")
    list1 = input1.split()
    target = input("Enter target number: ")
    length1 = len(list1)
    for i in range(length1):
        for j in range(i+1,length1):
            sum = int(list1[i]) + int(list1[j])
            if int(target) == sum:
                print("True")
                input("Press enter to return home")
                Menu()
    print("False")
    input("Press enter to return home")
    Menu()

def prompt2():
    input2 = input("Enter your list of numbers in format # # # etc.: ")
    list2 = input2.split()
    length2 = len(list2)
    for i in range(length2):
        for j in range(i+1,length2):
            if int(list2[j]) < int(list2[i]):
                temp = list2[i]
                list2[i] = list2[j]
                list2[j] = temp
    print(list2)
    input("Press enter to return home")
    Menu()

Menu()
