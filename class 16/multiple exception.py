try:
    n1,n2 = eval(input("Enter the number seperated by commas"))
    result=n1/n2
    print(result)
except SyntaxError as ex:
    print("an exception occured",ex)
except ZeroDivisionError as ex:
    print(ex)
except:
    print("an error occured")
else:
        print("no error")
finally:
    print("I will be there always")
