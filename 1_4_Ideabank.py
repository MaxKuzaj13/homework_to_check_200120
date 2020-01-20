import sys
import os

def main(*args):
	if sys.argv[-1] == 'list':
		g=open("ideabank.txt", "r")
		print(g.read())
		sys.exit()
	idea = input('What is your new idea: ')
	try:
		f = open("ideabank.txt", "a+")
		num_lines = sum(1 for line in open("ideabank.txt", "r"))
	except:
		f = open("ideabank.txt", "w+")
		num_lines=1
	line_add=str(num_lines+1)+'. '+idea+ '\n'
	f.write(line_add)
	f.close()
	g=open("ideabank.txt", "r")
	print(g.read())


if __name__ == "__main__":
	main()
