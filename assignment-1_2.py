r'''
                            Assginment-1.2
                            --------------
                (Done by Abhijit Venkatesh - @Abjt03)

1. All List methods

    Run this program and Choose option 1

2. All String methods

    Run this program and Choose option 2

3. Usage of Negative Index

      The negative indexing starts from where the array ends.
      The index value of -1 gives the last element, and -2 gives the second last element of an array.

'''

# Choice
choice = int(input("Enter your choice :\n1. List Methods\n2. String Methods\n"))

# List methods
if choice == 1:

    list = [1, 2, 3, 4, 5]

    print("Default List :")
    print(list)

    print("Append 6 to the end of the List")
    list.append(6)
    print(list)

    print("Copy the List")
    x = list.copy()
    print(x)

    print("Clear List elements")
    x.clear()
    print("No. of elements :", len(x))

    print("Count number of 4's in List")
    print(list.count(4))

    print("Extend the list by adding another list at the end")
    list2 = [8, 9, 10]
    list.extend(list2)
    print(list)

    print("Print index of first '4' in the list")
    print(list.index(4))

    print("Insert 7 after 6 in the list")
    list.insert(6, 7)
    print(list)

    print("Remove and print 9 from list")
    # Pops last element if no argument
    print(list.pop(8))

    print("Remove first occurence of 10 in the list")
    list.remove(10)
    print(list)

    print("Reverse the list")
    list.reverse()
    print(list)
    list.reverse()

    print("Reverse sort the list")
    list.sort(reverse=True)
    print(list)

# String methods
if choice == 2:

    str = "myCaptain is awesome"

    print("Default String :")
    print(str)

    print("Capitalize the first letter and make the rest lowercase")
    print(str.capitalize())

    print("Convert in Lowercase")
    print(str.lower())

    print("Convert each word's first character into uppercase")
    print(str.title())

    print("Convert string to lower using casefold - converts more unicode characters")
    print(str.casefold())

    print("Convert string to uppercase")
    print(str.upper())

    print("Count number of a's in the string")
    print(str.count('a'))

    print("Return first occurence of 'a' in the string")
    print(str.find('a'))

    print("Replace alloccurences of 'a' in the string with '1'")
    print(str.replace('a', '1'))

    print("Convert lowercase to uppercase and vice versa")
    print(str.swapcase())

    print("Check out the rest of the string functions at https://www.w3schools.com/python/python_strings_methods.asp")
    print("Don't forget all the boolean returning 'is' functions")
