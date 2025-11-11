# create three characters with attack and defense attributes
character1 = input("Digite o nome do personagem 1: "), (int(input("Digite o valor de ataque do personagem 1: ")), int(input("Digite o valor de defesa do personagem 1: ")))
character2 = input("Digite o nome do personagem 2: "), (int(input("Digite o valor de ataque do personagem 2: ")), int(input("Digite o valor de defesa do personagem 2: ")))
character3 = input("Digite o nome do personagem 3: "), (int(input("Digite o valor de ataque do personagem 3: ")), int(input("Digite o valor de defesa do personagem 3: ")))

# print characters names and attack and defense values
print(character1[0])
print(str(character1[1][0]))
print(str(character1[1][1]))
print(character2[0])
print(str(character2[1][0]))
print(str(character2[1][1]))
print(character3[0])
print(str(character3[1][0]))
print(str(character3[1][1]))

# print full character tuples
characters = [
    [character1[0], character1[1]],
    [character2[0], character2[1]],
    [character3[0], character3[1]]
]

print(characters)
# print which character has the highest attack value
for atk in characters:
    if atk [1][0] == max(character1[1][0], character2[1][0], character3[1][0]):
        highest_attack = atk
print("Ataque " + highest_attack[0] + " " + str(highest_attack[1][0]))

# print which character has the highest defense value
for df in characters:
    if df [1][1] == max(character1[1][1], character2[1][1], character3[1][1]):
        highest_defense = df
print("Defesa " + highest_defense[0] + " " + str(highest_defense[1][1]))