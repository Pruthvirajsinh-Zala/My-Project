
a = 5
b = 2


try:
    print("resource Open")
    print(a/b)
    k = int(input("Enter a Number"))
    print(k)

except ZeroDivisionError as e:
    print("Hey, You cannot divide a Number by Zero", e)

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Somthing went Wrong...")

finally:
    print("resource Closed")
    