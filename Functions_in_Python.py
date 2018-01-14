# File: Functions_in_Python.py
# Description: Creating functions in Python
# Environment: Spyder IDE in Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Creating functions in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Functions_in_Python (date of access: XX.XX.XXXX)

"""
Created on Thu Jan 11 16:16:24 2018

@author: Valentyn
"""
import os
import psutil
import shutil
import sys

def sys_info():
    print("Current directory: ", os.getcwd())
    print("Number of CPU: ", os.cpu_count())
    print("Operation System: ", sys.platform)
    print("File system encoding: ", sys.getfilesystemencoding())

def file_duplicating(filename):
    if os.path.isfile(filename): # Checking if the file_name[i] is a file and isn't folder
        new_file = filename + '.duplication'
        shutil.copy(filename, new_file) # Copying the file into another file
        if os.path.exists(new_file):
            print("The file - ", new_file, " - was successfully created!")
        else:
            print("Something went wrong!")
    else:
        print("Something went wrong!")

def file_deleting(filename):
    if os.path.isfile(filename): # Checking if the file_name[i] is a file and isn't folder           
        if filename.endswith('.duplication'): # Checking if the file has the ending 'duplication'
            os.remove(filename) # Removing the file                 
            print("The file - ", filename, " - was successfully deleted!")
        else:
            pass

print("This is a Great Python Program!")
print("Hello there, programmer!")

name = input("What is your name? ")
print(name, ", Welcome!")

answer = ''

while answer != 'Q' and answer != 'N' and answer != 'q' and answer != 'n':   
    answer = input("Let's work? (Y/N/Q)")    
    if answer == 'Y' or answer == 'y':
        print("Great choice!") # type "pass" for the empty construction
        print("I can do for you:")
        print("[1] - show list of files and folders in current directory")
        print("[2] - show information about System")
        print("[3] - show list of running tasks in the System")
        print("[4] - duplication of all files in the current directory")
        print("[5] - change the current directory")
        print("[6] - duplication of specific file in the specific directory")
        print("[7] - deleting all files with endings '.duplication' in the specific directory")
        todo = int(input("Make your choice: "))    
        if todo == 1:
            print(os.listdir())
        elif todo == 2:
            sys_info()
        elif todo == 3:
            print("List of current running PIDs: ", psutil.pids())
        elif todo == 4:
            print("All files in the current directory are duplicated now!")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                file_duplicating(file_list[i])
                i += 1
        elif todo == 5:
            print("Type the name of the derictory you want to change in.")
            current_directory = input("Input name of the directory: ")
            os.chdir(current_directory)
            file_list = os.listdir()
            print("List of files in chosen directory:")
            for file_name in file_list:
                print(file_name)
        elif todo == 6:
            print("Type the name of the derictory you want to work with")
            specific_directory = input("Input name of the directory or type '.' for current directory: ")
            file_list = os.listdir(specific_directory)
            print("Type the name of the file you want to duplicate")
            file_to_duplicate = input("Input name of the file: ")
            fullname_of_file_to_duplicate = os.path.join(specific_directory, file_to_duplicate) # function to join full path to the file with the name of the file
            file_duplicating(fullname_of_file_to_duplicate)
        elif todo == 7:
            print("Type the name of the derictory you want to delete duplactes in")
            specific_directory = input("Input name of the directory: ")
            file_list = os.listdir(specific_directory)
            i = 0
            while i < len(file_list):
                file_deleting(file_list[i])
                i += 1
            print(i, " files were checked now!")
        else: pass # for the empty construction        
    elif answer == 'N' or answer == 'n':
        print("Good by, see you next time!")
    elif answer == 'Q' or answer == 'q':
        print("You successfully finished the work, see you soon!")
    else:
        print("Unknown input, try again")
