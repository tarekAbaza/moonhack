items = [
"A: 3 litres of water",
"B: Shampoo",
"C: An extra Spacesuit",
"D: A shovel",
"E: A 10 day oxygen supply",
"F: Solar panels",
"G: The seeds for your mission",
"H: The soil for your mission",
"I: A 3 day food supply"
]

print("It is the year 2049. You are on a solo mission to restock the base on the moon with soil and seeds to grow more plants.")
print("You have just landed but you are in trouble. You have landed 300 kilometers from the moon base!")
print("You can get to the base in 3 days on your lunar rover")
print("The lunar rover can only fit you in your spacesuit and 4 other items")
print("Out of the items below, which do you bring? \n")



for objects in items:
    print(objects)
    print("inside forloop")
print("outside forloop")
    
user_choice = input("inter your choice: ")
#print(user_choice)
user_list = list(user_choice.split(','))
#print(user_list )

if "A" not in user_list and "a" not in user_list:
    print("hahaha")
else:
    print("goed")