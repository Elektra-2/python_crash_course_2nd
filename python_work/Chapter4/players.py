#  Slicing a list
players = ['john', 'ana', 'augusto', 'jeff']
print(players[0:2])
print(players[-2])  # imprime do fim da lista pro inicio

print("Here are the first three players on my team:")
for player in players[:2]:
    print(player.title())

# Copying Lists
foods = ['pizza', 'hamburger', 'falafel', 'cake']
friends_food = foods[:]
print(foods)
print(friends_food)

friends_food.append('ice-cream')
print(friends_food)


# Tuples - are immutable
dimensions = (200, 2)
print(dimensions[0], dimensions[1])
