r'''
                            Assginment-2.2
                            --------------
                (Done by Abhijit Venkatesh - @Abjt03)

1. For loop function of 'step' counter

    Step counter increments over the range in different values as by default, range
    increments by 1 every iteration of the loop
    Eg.
        for i in range(0,5,2):
            print(i, end=" ")
    Output :
        0 2 4

2. How to make a for loop infinite

    import itertools
        for i in itertools.count(start=1):
        if there_is_a_reason_to_break(i):
            break

    This is necessary because range() has a max limit and doesn't go to infinity

3. How to add values to a tuple

    Steps:
    1. Convert tuple to list using list()
    2. Modify using list methods
    3. Convert back to tuple using tuple()

'''
