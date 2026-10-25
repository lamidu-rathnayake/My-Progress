#  lets master lists and explore iter


# adding items

# append()
# extend(iterable)
# insert(location, item)

scanners = ["canon", "borroughs"]
scanners.append("epson")
print(scanners)

scanners.extend(["kodak","canonX"])
print(scanners)

# insert to front of the list
scanners.insert(0, "digital cheque")
print(scanners)


fruits = ['banana', 'orange', 'mango', 'lemon' ,"orange"]
fruits.remove("orange")
print(fruits)

# get key and list item at the same time
for index, fruit in enumerate(fruits):
    print(index, fruit)

# get items from two list at the same time
items = ["mac", "phone"]
counts = [4, 5]
for item, count in zip(items, counts):
    print(item, count) 




