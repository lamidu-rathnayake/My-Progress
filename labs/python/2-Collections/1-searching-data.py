# problem: FieldSync has a collection of scanners, and you need to find all scanners assigned to a particular branch.

scanners = [
    {"id": 1, "model": "Canon", "branch": "Colombo"},
    {"id": 2, "model": "Panini", "branch": "Kandy"},
    {"id": 3, "model": "Epson", "branch": "Colombo"},
    {"id": 4, "model": "Canon", "branch": "Galle"},
]

# implement this function
def get_scanners_by_branch(scanners, branch):
    matching_scanners = []

    for scanner in scanners:
        if scanner["branch"].casefold() == branch.casefold():
            matching_scanners.append(scanner)

    return matching_scanners

result = get_scanners_by_branch(scanners, "Colombo")
print(result)


# result
# [
#     {"id": 1, "model": "Canon", "branch": "Colombo"},
#     {"id": 3, "model": "Epson", "branch": "Colombo"}
# ]