r'''
                            Assginment-1.1
                            --------------
                (Done by Abhijit Venkatesh - @Abjt03)

1. Practice Comparison and Assignment Operators (4 sets of operators)

    Run this program and choose Option 1

2. If and Else statement for :
    a. If it snows I will go out Else I will not
    b. If it rains frogs I will dance

    Run this program and choose Option 2

'''
# Choose Opt 1 or Opt 2
choice = int(input("Options :\n1. Comparison and Assignment Operators\n2. If-Else\nEnter Choice : "))

# Comparison and Assignment Operators
if choice == 1:

    a, b = 2, 4
    print("a =", a, "b =", b)
    print("Greater than :", a > b)
    print("Lesser than :", a < b)
    print("Greater than or equal to :", a >= b)
    print("Lesser than or equal to :", a <= b)
    print("Equal to :", a == b)
    print("Not equal to :", a != b, '\n')

    a, b = 3, 3
    print("a =", a, "b =", b)
    print("Greater than :", a > b)
    print("Lesser than :", a < b)
    print("Greater than or equal to :", a >= b)
    print("Lesser than or equal to :", a <= b)
    print("Equal to :", a == b)
    print("Not equal to :", a != b, '\n')

    a, b = 4, 2
    print("a =", a, "b =", b)
    print("Greater than :", a > b)
    print("Lesser than :", a < b)
    print("Greater than or equal to :", a >= b)
    print("Lesser than or equal to :", a <= b)
    print("Equal to :", a == b)
    print("Not equal to :", a != b, '\n')

    a, b = 'x', 'y'
    print("a =", a, "b =", b)
    print("Greater than :", a > b)
    print("Lesser than :", a < b)
    print("Greater than or equal to :", a >= b)
    print("Lesser than or equal to :", a <= b)
    print("Equal to :", a == b)
    print("Not equal to :", a != b, '\n')

# If-Else
if choice == 2:

    # First statement
    snows = int(input("Enter '1' If Snowing Else Enter '0' : "))
    if snows == 1:
        print("I will go out")
    else:
        print("I will not go out")

    # Second statement
    frog_rain = int(input("Enter '1' If Raining Frogs Else Enter '0' : "))
    if frog_rain == 1:
        print("I will dance")
    else:
        print("Inconclusive")
