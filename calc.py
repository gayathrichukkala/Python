def calculator():
    try:
        num1=float(input("enter frst number"))
        num2=float(input("enter secnd number"))
        operation=input("enter operation(+,-,*,/):")

        if operation =="+":
                result=num1+num2
        elif operation == "-":
                result=num1+num2
        elif operation =="*":
                result=num1*num2
        elif operation == "/":
                result=num1/num2
        else:
            print("invalid operation")
            return
        print("result:", result)
    except ValueError:
        print("invalid input. please enter numeric value")
    except ZeroDivisionError:
       print("cannot divide by zero!")
calculator()