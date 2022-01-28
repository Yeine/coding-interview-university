# Algorithmic complexity / Big-O / Asymptotic analysis


# Constant O(1)
"""
The simplest Big O notation we can think of is the constant. 
we can define big O of constant as no matter how big our input is, 
it always takes the same amount of time to compute things.
"""
def big_o_constant(values):
    """
    Print first item in a list of values.
    """
    print(values[0])

# Linear = O(n)
"""
This above function runs in O(n) (linear time).
This means that the number of operations taking place scales linearly with n,
so we can see here that an input list of 100 values will print 100 times, a list of 10,000 values
 will print 10,000 times, and a list of n values will print n times.
"""
def linear_function(input_lists):
    """
     Takes in list and prints out all values
    """
    for values in input_lists:
        print(values)

# O(n²) Quadratic
"""
In the below python code we have two loops, one nested inside another. 
This means that for a list of n items, we will have to perform n operations for every item in the list! 
This means in total, we will perform n times n assignments, or n². So a list of 10 items will have 10², or 100 operations. 
You can see how dangerous this can get for very large inputs! This is why Big-O is so important to be aware of!
"""
def linear_quadratic_function(input_lists):
    """
    Prints pair for every item in list.
    """
    for values in input_lists:
        for inner_values in input_lists:
            print(values, inner_values)

