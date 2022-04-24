my_list = ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
print(my_list)

Instrument_List = ["Trumpet", "Trombone", "Euphonium", "Accordion", "Clarinet", "Tuba", "Guitar", "Drums", "Congas", "Flute"]
print(Instrument_List)

print(Instrument_List[9])

print(my_list[0], my_list[-3], my_list[1])  # fav 3 Cities

first_3_Cities = my_list[0:3]
print(first_3_Cities)


new_list = (my_list[0], my_list[1], Instrument_List[0], Instrument_List[1])
print(new_list)

my_list [1] = "Orlando"  #STEP 5
my_list [0] = "San Francisco"
my_list [2] = "Brooklyn"
my_list [-3] = "Hollywood"
my_list [-5] = "Tampa"
print(my_list)

my_list.append("Oakland")   #STEP 6
my_list.extend(["New York City", "Los Angeles"])
my_list.insert(0, "Miami")
print(my_list)

del my_list[0]
my_list.remove("San Francisco")
my_list.pop(0)
print(my_list)


