import sys

def main():
	if sys.argv[-1] == 'hello.py':
		print('Hello World!')
	else:	
		for arg in sys.argv: 1
		print("Hello "+arg+"!")
if __name__ == "__main__":
    main()
