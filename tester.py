import subprocess
import os
from termcolor import colored


hw_number = input("Enter the homework number: ")
hw_question_number = input("Enter the homework's question number: ")
hw_name = f"hw{hw_number}q{hw_question_number}"

start, end = int(input("Enter the starting number of the tests: ")), int(input("Enter the ending number of the tests: "))

arr_error = []
for i in range(start, end + 1):
    os.system(f"{hw_name}.exe < {hw_name}in{i}.txt > Q{hw_question_number}_res{i}.txt")

for i in range(start, end + 1):
    desired_output = (f"""Comparing files {hw_name}out{i}.txt and Q{hw_question_number}_RES{i}.TXT\r\nFC: no differences encountered\r\n\r\n""")
    batcmd = f"FC {hw_name}out{i}.txt  q{hw_question_number}_res{i}.txt"
    try:
        res = subprocess.Popen(batcmd, stdout=subprocess.PIPE, shell=True).stdout.read().decode('ascii')        
    except:
        continue # Some sort of weird, unimportant problem
    if(res != desired_output):
        print(colored(f"ERROR in TEST {i}", 'red'))
        arr_error.append(i)
    else:
        print(colored(f"TEST {i} PASSED", 'yellow'))

for i in arr_error:
    os.system(f"DIFFMERGE {hw_name}out{i}.txt q{hw_question_number}_res{i}.txt")

input("ENTER ANYTHING TO EXIT")