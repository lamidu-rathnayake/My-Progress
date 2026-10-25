# checking the range function
# ---------------------------
# it creates range of numbers from 0 to target number

for i in range (5): 
    # 0 1 2 3 4 (not 5, it only cares about the count of the numbers from 0) <- this is relavent only if we use "range(one parameter)" function
    print(i)


# checking types
num_one = 3
num_two = 4
total = num_one + num_two

# complex type
print(type(2j))

# join 
branches = ["1", "3", "5"]
result = ",".join(branches)
print(result)

# finding the position of the char set in a string
name = "lamidu rathnayake"
position = name.find("rath")
positionNegative = name.find("ke")
print(position)
print(positionNegative)
startWithCheck = name.startswith("midu") # name is starting with "la.." so the result is false
endWithCheck = name.endswith("ke") # name is starting with "ke" so the result is true (used to identifiy file extensions and naming patterns\)

print(startWithCheck)
print(endWithCheck)


# checking the string is a number it self, not containing any non-numerical charactors
number1 = "12347"
number2 = "dh23452x"
print(number1.isdigit()) # true
print(number2.isdigit()) # false


# removing the leading and trailing
faultystring = " lamidu rathnaYake    "
print(faultystring.strip())
print(faultystring.strip().title()) # make every world's first letter upper , also make other letters lowercase
print(faultystring.strip().lower()) # make all letters lower


