# Lists

clothes = [
    "shorts",
    "shoes",
    "t-shirt",
]

if clothes[0] == 'shorts':
    clothes[0] = 'warm coat'
    print(clothes)

gameScores = [3,4,5,6,7,8,9,200]
print(len(gameScores))
print(max(gameScores))
print(min(gameScores))
print(list(reversed(gameScores)))


shoppingList = [
    'bread',
    'chease',
    'pop tarts',
    'carrots',
]
if 'bread' in shoppingList:
    shoppingList.append('butter')
    print(shoppingList)

if 'milk' not in shoppingList:
    print('you have no milk in the fridge')


costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0

for costs in costs:
    total_cost = total_cost + costs
    print(total_cost)

#Dictionary - key value pairs. 'key':'value'
place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number': '54',
    'location': {
        'longitude': 127,
        'latitude': 63,
    }
}  #