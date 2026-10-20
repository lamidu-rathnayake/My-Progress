# problem: FieldSync has a collection of scanners, and you need to find all scanners assigned to a particular branch.


scanners = [
    {"id": 1, "model": "Canon", "branch": "Colombo"},
    {"id": 2, "model": "Panini", "branch": "Kandy"},
    {"id": 3, "model": "Epson", "branch": "Colombo"},
    {"id": 4, "model": "Canon", "branch": "Galle"},
]

# implement this function
def get_scanners_by_branch(scanners, branch):
    # Your solution
    pass

result = get_scanners_by_branch(scanners, "Colombo")
print(result)


# result
# [
#     {"id": 1, "model": "Canon", "branch": "Colombo"},
#     {"id": 3, "model": "Epson", "branch": "Colombo"}
# ]