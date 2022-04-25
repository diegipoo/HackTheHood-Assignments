Grocery_List = {"Chicken":1.59, "Beef":1.99, "Cheese":1.00, "Milk": 2.50}

Chicken_price = Grocery_List["Chicken"]
Beef_price = Grocery_List["Beef"]
Cheese_price = Grocery_List["Cheese"]
Milk_price = Grocery_List["Milk"]

print(Grocery_List)
print(Beef_price)

Soccer_Players_Age = {"Lionel Messi": 34, "Cristiano Ronaldo": 37, "Paul Pogba": 29}
Lionel_Age = Soccer_Players_Age["Lionel Messi"]  #STEP V
Cristiano_Age = Soccer_Players_Age["Cristiano Ronaldo"]
Paul_Age = Soccer_Players_Age ["Paul Pogba"]
print(Lionel_Age, Cristiano_Age, Paul_Age)
print( Soccer_Players_Age)

Shoe_Dictionary = {"Jordan": 1, "Yeezy": 8, "Foamposite": 10, "Air Max": 5, "SB Dunk": 20}
Shoe_Dictionary["SB Dunk"] -= 2   #Step 6
Shoe_Dictionary["Yeezy"] += 1

Shoe_Dictionary["Jordan"] +=7
Shoe_Dictionary["Yeezy"] +=7
Shoe_Dictionary["Foamposite"] +=7
Shoe_Dictionary["Air Max"] += 7
Shoe_Dictionary["SB Dunk"] +=7

Shoe_Dictionary["Jordan"] -=3
Shoe_Dictionary["Yeezy"] -=3
Shoe_Dictionary["Foamposite"] -=3
Shoe_Dictionary["Air Max"] -=3
Shoe_Dictionary["SB Dunk"] -=3
print(Shoe_Dictionary)

Soccer_Players_Age["Luka Modric"] = 38  #Changing Value of a Dictionary
Soccer_Players_Age["Neymar"] = 35 #Step 8
Soccer_Players_Age["Kante"] = 31

del Soccer_Players_Age["Kante"]
del Soccer_Players_Age["Neymar"]

print(Soccer_Players_Age)



