"""
Module 3. Task 3
Christine Martinez, Domain: cats
"""

# import some modules first - how many can you make use of?

import math
import statistics


# define some functions




# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("your code here")


# Why? Why only print if this the module called?
# Because when you write good functions, you may want to
# import this module into another script - just like you did
# math or statistics.
# Build a library of resuable functions to support your domain.

# For example, if your domain:
# Is sports, create functions to provide a list of teams.
# Is pets, create functions to calculate adoption prices.
# Is music, create functions to return a list of your favorite artists.


# When you write reusable functions for your domain, you can
# import the module with your utility functions into other modules
# and use them there.  This is a very common practice.
# Anything you write can be imported into later projects.

print("List 1 Project 3")
#listA is contains ages of cats

listA= [21,19,18,17,16,15,14,13,12,11,10,9,8.5,8,7.5,7,6.5,6,4,2,1]

#Here calculate the mean, mode and median for listA

mean=statistics.mean(listA)
mode=statistics.mode(listA)
median=statistics.median(listA)

print(f"mean:{mean}")
print(f"mode:{mode}")
print(f"median:{median}")

#standard deviation and variance
variance=statistics.variance(listA)
stdev=statistics.stdev(listA)

print(f"stdev:{stdev}")
print(f"variance:{variance}")

print("List 2 Project 3")

#List representing 10 integer Items

orange_cat_ages_list=[
    10,
    9,
    8,
    7,
    6,
    4,
    2,
    1,
    17,
    18,
    19,
] 


#list y representing price of adoption for orange cats

orange_cats_price=[
    20.5,
    19.5,
    18,
    25.5,
    30.5,
    22.5,
    32.5,
    31.5,
    28.5,
    45.5,
    15.9,
]

print(f"List of ages for all orange cats in the shelter: {orange_cat_ages_list}")
print()
print(f"List of adoption prices of the orange cats in the shelter: {orange_cats_price}")

#Corelation, slope and intercept

correlationxy=statistics.correlation(orange_cat_ages_list,orange_cats_price)
slope, intercept=statistics.linear_regression(orange_cat_ages_list,orange_cats_price)

#y=mx+b

x_max=25
y_new=slope*x_max+intercept

print(f"With linear regression if a cat is 25 years old, it will cost {y_new:.3f}")

#list 3 project 3