def main():
	numbers=[1,2,56,32,51,2,8,92,15]
	print(numbers)
	
	for i in range(1, len(numbers)):
		for j in range(len(numbers)-1):
			if numbers[j] > numbers[j+1]:
				temp = numbers[j+1]
				numbers[j+1] = numbers[j]
				numbers[j] = temp

	print(numbers)

if __name__ == "__main__":
	main()

