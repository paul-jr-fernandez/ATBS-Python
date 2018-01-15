# Chapter 3: Functions - The Collatz Sequence
# Author: Paul Jr Fernandez
# Changelog:
# 16 Jan 2017 v1.0: Added changelog and some comments to increase readability

# Import necessary modules
import sys

# Function to return the collatz sequence for a number
def collatz(num):
    if num % 2 == 0: # Even number
        return num // 2
    else: # Odd number
        return (num * 3 + 1)

# Main
print("Collatz Sequence Generator")
print("Enter the number:",end='')
try: # Ensure input is an integer
    seq_num = input_number = int(input())
except ValueError:
    print('Value entered is not an integer!\nPlease enter an integer value.')
    sys.exit(2) # Error: Non-integer value entered
if input_number <= 0: # Collatz sequence is for positive integers only
    print("The collatz sequence can be only generated for numbers greater than 0")
    sys.exit(1) # Warning: Integer value less than 1 entered
else:
    while seq_num != 1:
        print(seq_num, end=',')
        seq_num = collatz(seq_num)
print(seq_num)
sys.exit(0) # If all goes well
