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
print("List number 3, Python Built in Functions")
#Calculate min, max,len, sum, average, set, sorted, sorted, using reverse true

min=min(listA)
print(f"min is:{min}")

max=max(listA)
print(f"max is:{max}")

len=len(listA)
print(f"len is:{len}")

sum=(sum(listA))
print(f"sum is:{sum}")

avg=sum/len
print(f"avg is: {avg: .3f}")

sorted=sorted(listA)
print(f"sorted: {sorted}")

print(f"List 4, project 3,Methods")
#append,extend, insert, remove,count,sort, sort with reverse, copy, pop first, pop last

lst= [10,7,3,1]
print(f"New short list is: {lst}")
print("Append a single value to the list:")
lst.append(8)
print(lst)
print("Extend with a new list:")
lst.extend([6,5,9])
print(lst)

lst.insert(11,14)
print(f"Lst with insert: {lst}")

remove_item=5
lst.remove(remove_item)
print(lst)

print("count how many times there is a 2 in the list")
count_of_two=lst.count(2)
print(count_of_two)

asc_list= lst.sort()
print(asc_list)

print("This is the list sorted in descending order)")
descending_sorted= lst.sort(reverse=True)
print(descending_sorted)

print("This is a copy of the list")
lst_1=lst.copy()
print(lst_1)

print("List with the first item removed")
first_item=lst_1.pop(0)
print(lst_1)

print("List with the last item removed")
last_item=lst_1.pop(-1)
print(lst_1)

print("List Transformations")
#filter function
over_five=list(filter(lambda x: x> 5, listA))
print(f"Over five: {over_five}")

#map function
print("Map cuberoot")
cuberoot_listA=list(map(lambda x: math.cbrt(x),listA))
print(f"The cubed root is : {cuberoot_listA}")

#map to caluclate volume
print("Calculate volume")
cube_vol=list(map(lambda x: (x*x*x), listA))

#Task 6 Transformations
print("List Transformations- List Comprehension")

above_eight=[number for number in listA if number >8]
print(f"This is the list with ages over 8: {above_eight}")

#triple value
listA_tripled=[round(number*3, 2) for number in listA]
print(f"These are the tripled ages: {listA_tripled}")

#my choice
listA_add_six= [round(number+6,2) if number < 7 else number for number in listA]
print(f"The new agesl list is: {listA_add_six}")
