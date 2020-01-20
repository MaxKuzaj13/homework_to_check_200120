import sys
import os

def main():
	list_fib=[]

	for i in range(30):
		if i == 0:
			list_fib.append(0)
			fib = 0
		elif i<2:
			fib = i
			list_fib.append(i)

		else:
			fib=list_fib[-2]+list_fib[-1]
			list_fib.append(fib)


		print(str(i+1) +'. ' + str(fib))


if __name__ == "__main__":
	main()
