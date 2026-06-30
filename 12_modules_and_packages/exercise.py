import re
#print(dir(re))

functions = dir(re)
find_members = []

for function in functions:
    if "find" in function:
        find_members.append(function)

print(sorted(find_members))