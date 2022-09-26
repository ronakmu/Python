print("Application to demonstrate industrial programming Using Module")

import AdditionModule

def main():
	
	print("Value of __name__ from Main function is :",__name__)
	print("Enter First Number")	
	no1 = input()
	print("Enter Second Number")
	no2 = input()
	
	Ret = AdditionModule.Add(no1,no2)
	print("Addition is",Ret)

if __name__ == "__main__":
	main()
