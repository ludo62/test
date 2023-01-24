"""name = input("Quel est ton nom ? ")
age = input("Quel est ton âge ? ")


try:
    age_prochain = int(age) + 1
except:
    print("Vous devez rentrer un nombre pour l'age !")
else:
    print("Vous vous appelez " + name, "et vous avez " + str(age), "ans.")
    print("L'an prochain vous aurez " + str(age_prochain) + " ans.")
"""

# boucle while : tant que la condition est vraie, on continue à boucler

n = 0  # creer la variable
print(n)
# n = 1  # reafecte la variable
# print(n)
# n = n + 1  # incremente
# print(n)

# print("Début de la boucle")
# while n < 10:
#     print("Valeur de n: " + str(n))
#     n = n + 1

# print("Fin de la boucle")


mdp = ""
while not mdp == "Ludo":
    mdp = input("Quel est le mot de passe ? ")
print("Mot de passe correct, vous avez accès au compte.")
