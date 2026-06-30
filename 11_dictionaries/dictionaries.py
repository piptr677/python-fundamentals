#phonebook = {}
#phonebook["John"] = 938477566
#phonebook["Jack"] = 676767676
#phonebook["Jill"] = 123456789
#print(phonebook)

#or

phonebook = {
    "John" : 938477566,
    "Jack" : 676767676,
    "Jill" : 123456789
}
#print(phonebook)

#for name, number in phonebook.items():
#    print("Phone number of %s is %d" % (name, number))

del phonebook["John"]
phonebook.pop("Jack")

print(phonebook)