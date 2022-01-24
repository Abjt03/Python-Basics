r'''
                            Assginment-2
                            ------------
                (Done by Abhijit Venkatesh - @Abjt03)

1. All Dictionary methods

    Run this program and choose option 1

2. Create a Set

    Run this program and choose option 2

3. Most frequent charactr program - MyCaptain

    Done in MyCaptain

4. Filename extension program in MyCaptain

    Done in MyCaptain

5. Calculator in Python

    Run this program and choose option 3

'''

# Choice
choice = int(input("Enter Choice :\n1. Dictionary methods\n2. Create a Set\n"))

# Dictionary methods
if choice == 1:

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    print("Copy the dictionary")
    car2 = car.copy()
    print(car2)

    print("Clear the dictionary")
    car2.clear()
    print("No. of Key-value pairs left in the dict is :", len(car2.keys()))

    print("Return a dictionary with the specified keys and the specified value")
    x = ('key1', 'key2', 'key3')
    y = 0
    thisdict = dict.fromkeys(x, y)
    print(thisdict)

    print("Return value of 'brand' key")
    print(car.get("brand"))

    print("Return a list containing a tuple for each key value pair")
    print(car.items())

    print("Return a list containing the dictionary's keys")
    print(car.keys())

    print("Remove 'model' key-pair and return its value")
    print(car.pop("model"))
    print(car)

    print("Remove and return the last item from the dictionary")
    print(car.popitem())
    print(car)

    print("Show value of given key with optional default")
    print(car.setdefault("brand", "BMW"))

    print("Insert key-value pair using update")
    car.update({"color": "White"})
    print(car)

    print("Return a list containing the dictionary's values")
    print(car.values())

# Create a set
elif choice == 2:

    thisset = {"apple", "banana", "cherry"}
    print(thisset)

# If-Else Calculator
elif choice == 3:

    # Calculator choice and input
    ch = int(input("Enter choice :\n1. Add\n2. Subtract\n"))
    a = int(input("a : "))
    b = int(input("b : "))

    # Addition
    if ch == 1:
        print("Sum :", a+b)
    # Subtraction
    elif ch == 2:
        print("Difference :", a-b)
