
listofMacs = []

with open("C:\\Users\\lukeman.adio\\OneDrive - Vodafone Group\\Desktop\\ExampleOnPyth.txt", "r") as reader:  # r means to read
    for aline in reader.readlines():
        listofMacs.append(aline)


# print(listofMacs)
# print('\n' * 2)

RemoveItem = []
for mac in listofMacs:
    NewOne = mac.replace("\n", "")
    RemoveItem.append(NewOne)

# print(RemoveItem)
# print('\n' * 2)

RemoveItem1 = []
for mac in RemoveItem:
    NewOne = mac.replace("@", "&")
    RemoveItem1.append(NewOne)

# print(RemoveItem1)
# print('\n' * 2)

RemoveItem2 = []
for mac in RemoveItem1:
    NewOne = mac.lower()     #return all to local case
    RemoveItem2.append(NewOne)

# print(RemoveItem2)
# print('\n' * 2)

RemoveItem3 = []
for mac in RemoveItem2:
    NewOne = mac.upper()     #return all to upper case
    RemoveItem3.append(NewOne)


# print(RemoveItem3)
# print('\n' * 2)

with open("C:\\Users\\lukeman.adio\\OneDrive - Vodafone Group\\Desktop\\Empty_python.txt", "w") as writer:     # w means to write |  a means to append
    for new in RemoveItem3:
        writer.write(new)
        writer.write('\n')
