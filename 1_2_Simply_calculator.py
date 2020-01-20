import sys
import os

def main():
	try:
		first_num = int(input('Enter a number (or a letter  to exit): '))
	except:
		sys.exit()
	operation = input('Enter an operation: ')
	secound_num = int(input('Enter a secound number: '))
	if operation == '+':
		print(first_num+secound_num)
	if operation == '*':
		print(first_num*secound_num)
	if operation == '/':
		print(first_num/secound_num)
	if operation == '-':
		print(first_num-secound_num)
if __name__ == "__main__":
    main()
