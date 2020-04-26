#Reading a file API, FILES AND PIP

#Reading from a file

#with open('people.txt, 'r'') as text_file:
   # contents = text_file.read()
   # print(contents)

#Excerise 5:1 - To do list

# new_Item = input('Enter a to-do item: ' )
#
# with open ('todo.txt', 'r') as todo_file:
#     todo = todo_file.read()
# todo = todo + new_Item + '\n'
#
# with open('todo.txt', 'w+') as todo_file:
#     todo_file.write(todo)


milk = input('what milk alternative do you want to add to the recipe?')

with open('ice_coffee_recipie.txt', 'r') as ice_coffee_recipie_file:
    ice_coffee_recipie = ice_coffee_recipie_file.read()
ice_coffee_recipie = ice_coffee_recipie + milk + '\n'

with open('ice_coffee_recipie.txt', 'w') as ice_coffee_recipie_file:
    ice_coffee_recipie_file.write(ice_coffee_recipie)
