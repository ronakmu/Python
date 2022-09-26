print("Application to demonstrate industrial programming ")

def Add(value1,value2):

		Ans = int(value1) + int(value2)
		return Ans
		

def main():
	
	print("Enter First Number")	
	no1 = input()
	print("Enter Second Number")
	no2 = input()
	
	Ret = Add(no1,no2)

	print("Addition is",Ret)
	
	
if __name__ == "__main__":
	main()
