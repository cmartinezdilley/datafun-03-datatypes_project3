"""
Christne Martinez
Project 3, Tsak 5

"""
print("This section is all about Tupules")
print()
cat_1=("Black", "Siamese Cat", [15, 25.5])
cat_2=("Orange", "Persian Cat", [1,50])
cat_3= ("White", "Ocelot", [2,100])

cat_ages=(15,1,2)
cat_adoption_prices=(25.5,50,100)
print()
print("The following information gives the ages and adoption prices")
print(f"{cat_ages =}")
print(f"{cat_adoption_prices}")
print()
print("Below, we show the cat color, type, age and price")
print(f"{cat_1 =}")
print(f"{cat_2 =}")
print(f"{cat_3 =}")
print()
combined_sets= cat_ages+cat_adoption_prices
print(combined_sets)
print()
print("Repet of a tupule")
cat_ages_4=cat_ages*4
print(cat_ages_4)
print()
print("Next is sets- Task 5")
female_cat_names={"buttercup", "princess", "luna"}
male_cat_names={"mochi", "Mr. Brown", "Max"}
cat_names_union= female_cat_names | male_cat_names
cat_names_interect=female_cat_names and male_cat_names
print(f"Female Cat Names: {female_cat_names}")
print(f"Male Cat Names: {male_cat_names}")
print()
print("When you make them a union, it looks like")
print(f"{cat_names_union}")
print(f"The intersection from these sets is")
print(f"{cat_names_interect}")
print()
print("Next is the dictionary Task")
print()
with open("text_woodchuck.txt") as file_object:
    word_list=file_object.read().split()
word_ct_dictionary= {}
for word in word_list:
    if word in word_ct_dictionary:
        word_ct_dictionary[word] +=1
    else:
        word_ct_dictionary[word] =1
    word_ct_dictionary={word: word_list.count(word) for word in word_list}

print(word_ct_dictionary)

