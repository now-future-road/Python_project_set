def operation(number):

    while True:

        result = input(f"What {number} u want to enter: ")

        try:
            result = float(result)
            break
        except Exception as e:
            print(f"{type(e).__name__} {e} ")
    return result
number_1 = operation(1)
number_2 = operation(2)
    
sign = input("What type of oper(+;-;/;*)")
a = 0
if(sign == "+"):
    a = number_1 + number_2
    print(a)
elif sign == "-":
    a = number_1 - number_2
    print(a)
elif sign == "*":
    a = number_1 * number_2
    print(a)

elif sign == "/":
    a = number_1 / number_2
    print(a)
