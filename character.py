# create three characters with attack and defense attributes
character1 = ('Warrior', [15, 10])
character2 = ('Mage', [20, 5])
character3 = ('Rogue', [12, 8])

# print characters names and attack and defense values
print(character1[0] + " " + str(character1[1][0]) + " " + str(character1[1][1]))
print(character2[0] + " " + str(character2[1][0]) + " " + str(character2[1][1]))
print(character3[0] + " " + str(character3[1][0]) + " " + str(character3[1][1]))

# print which character has the highest attack value
characters = [character1, character2, character3]
for atk in characters:
    if atk [1][0] == max(character1[1][0], character2[1][0], character3[1][0]):
        highest_attack = atk
print("Ataque " + highest_attack[0] + " " + str(highest_attack[1][0]))

# print which character has the highest defense value
for df in characters:
    if df [1][1] == max(character1[1][1], character2[1][1], character3[1][1]):
        highest_defense = df
print("Defesa " + highest_defense[0] + " " + str(highest_defense[1][1]))