# escape keys

print("Days\tTopics\tExerciess")
print("Days\nTopics\nExerciess")
print("Days\Topics\Exerciess")
print("Days\\TopicsExerciess")
print("Days\'Topics\"Exerciess")


# string formatting tehnique 1  ->      " %s " %(subtitutions,..)

# %s = string
# %d = integers
# %f = floating point numbers
# %.number of digintsf = fixed posistion (ex: %.2f)

print("i am %s. i teach %s." %("lamidu", "math"))
print("the area of circle with a radius %d is %.2f." %(23, 23.328543)) # we can assign variables aswell

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
print("the following are python libraries: %s" % (python_libraries))


# string formatting technique 2 ->    "{} {} {}".format(a, b, c)  
print("{} + {} = {}".format(2, 4, (2+4)))
print("the value is {:.2f}".format(23.343))


# stirng formatting technique 3 ->    f"{variable or the value} {} {} {}..]"
print(f"the following are python libraries: {python_libraries}")
# formatting floating point numbers
print(f"the price is {23.3424:.2f}")


