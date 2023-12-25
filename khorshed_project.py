for i in range(0,100):
    grade=float(input("What is the grade percentage:"))
    if 80<=grade<100:
        print("You got A+")
    elif 70<=grade<79:
        print("You got A")
    elif 60<=grade<69:
        print("You got A-")
    elif 50<=grade<59:
        print("You got B")
    elif 40<=grade<49:
        print("You got C")
    elif 33<=grade<39:
        print("You got D")
    else:
        print("You got F")