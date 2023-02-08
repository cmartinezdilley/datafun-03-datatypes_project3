"""
Task 4 from Module 3
Christine Martinez
"""

# imports first
import random

# reusable functions next

# call functions and execute code
# use if __name__ == "__main__":

#Five lists

wild_cats=["Ocelot", "Black Footed Cat", "Sand Cat", "Snow Leopard", "Caracal"]

domestic_cats= ["Siamese", "British Short Hair", "Maine Coon", "Sphynx", "Persian Cat"]

cat_food_types= ["Raw", "Wet", "Dry"]

cat_food_brands= ["Science Diet", "Friskies", "Purina"]

common_fur_colors= ["black", "orange", "white", "Grey", "Black and White"]

print("String Lists 1- Python Built in Functions")
print()
print("Length of the lists are:")
print(f" Wild Cats: {len(wild_cats)}")
print(f" Types of domestic cats: {len(domestic_cats)}")
print(f"Types of cat foods: {len(cat_food_types)}")
print(f"Cat food brands: {len(cat_food_brands)}")
print(f"Commone fur colors: {len(common_fur_colors)}")

print("This is the set")
wild_cats_set= (wild_cats)
print(f"Set of Wild cats: {wild_cats_set}")

print("This is the zip function")
combined_lists= zip(wild_cats,domestic_cats)
print(f"Thhe zipped tuple is: {list(combined_lists)}")



print("Next are the string Lists 2: Random Choice")
print(f"Random selection on {random.choice(common_fur_colors)}")
sentence=(f"I saw a {random.choice(wild_cats)} that likes {random.choice(cat_food_brands)} food that is {random.choice(cat_food_types)}. I wonder what {random.choice(common_fur_colors)} {random.choice(domestic_cats)} cats usually eat")
print(sentence)

print("Next is unique words")
with open("text_zen_of_python.txt", "r") as fileObject:
    text = fileObject.read()
    list_words = text.split()
    unique_words = set(list_words)


print("This text was used to get a list of Unique words")
print(sorted(unique_words)) 
unique_word_ct = len(unique_words)
print(f"There are {unique_word_ct} list unique words retrieved.")
