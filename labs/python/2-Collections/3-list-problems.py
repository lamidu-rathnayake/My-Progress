# Exercises: Level 1
my_list = []

# declaring another list 
my_other_list = ["item1","item2","item3","item4","item5","item6","item7"]
print(len(my_other_list)) # 6

# getting 1st middle last items from my_ther_list
first_item = my_other_list[0]
middle_item = my_other_list[len(my_other_list)//2]
last_item = my_other_list[-1]
print(first_item)
print(middle_item)
print(last_item)

mixed_data_types = ["lamidu",24,6,False,"kalaeliya"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[len(it_companies)//2])
print(it_companies[-1])

# modifing the list
it_companies[it_companies.index("Apple")] = "Meta"
print(it_companies)

it_companies.insert(len(it_companies)//2, "Nvidia")

it_companies[it_companies.index("Google")] = it_companies[it_companies.index("Google")].upper()
joined_companies = "#; ".join(it_companies)
print(joined_companies)

print("Apple" in it_companies)

print(it_companies)
it_companies.sort()
print(it_companies)

it_companies.reverse()







