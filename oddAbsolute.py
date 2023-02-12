def calculateAbsolute():   
    in_num  = int(input("Enter a number: "))
    standard_num = 21
    if in_num > 21:
        absval = abs(standard_num - in_num)*2
    else:
        absval = abs(standard_num - in_num)
    print("Result:",absval)
## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
