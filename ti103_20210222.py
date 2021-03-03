a = "Bonjour"
b = [2, 3]
l = [1, "4", 6, 9.0, a, b]

print(l[2])
print(l[-2])
print(l[1::2])
print(l[1:])
print(l[:-2])
print(l[:])      # Vous creez une copie integrale de la liste
print(l)         # Vous referencez la liste

ll = list(range(0, 8))   # [0, 8[
print(ll)

# range(0, 12, 3)

l.append(5)
print(l)

print(len(l))
l.pop()
print(l)

var = l.pop()

l.insert(2, "toto")
print(l)

print(l[0:l.index("toto")])
l.remove("toto")
l.pop(0)
print(l)


for i in l:
    print(i)


"""
Une fonction qui accepte en parametre une liste et qui retourne la somme des elements de la liste
"""
def compte(l):
    somme = 0

    for i in l:
        somme = somme + i

    return somme


"""
Une fonction qui donne les x premiers nombres carres et retourne une liste, ou x est un parametre
"""
def puissances(x, y):
    l = []

    # x = 5
    # for i in range(1, 5):
    # i = 1
    # i = 2
    # i = 3
    # i = 4
    # i = 5
    for i in range(1, x + 1):
        l.append(i ** y)

    # i = 0
    # while i <= x:
    #     i += 1
    #     l.append(i ** 2)

    return l

"""
Fonction qui dit si un element est dans la liste
"""
def est_dans_la_liste(l, elem):

    if elem in l:
        return True

    else:
        return False


"""
Fonction qui donne en retour le nombre d'occurrences dans une liste
"""
def compte_dans_liste(l, elem):
    i = 0

    while elem in l:
        i += 1
        l.remove(elem)

    return i

# Fibonacci
# Style: iteratif, recursif
#
# Tour de Hanoi

# print(compte([2, 4, 5, 7.6]))
# print(compte([]))
# print(compte(["ahah"]))

# print(sum([2, 4, 5, 7.6]))

print(puissances(13, 3))

l1 = [1, 2, 4]
l2 = [3, 5]
print(l1 + l2 + [4])

l1.append(4)
# l1 = l1 + [4]
print(l1)
print(est_dans_la_liste(l1, 4))
print(compte_dans_liste(l1, 3))



MEDAILLES = 3  # Index 0: Or, Index 1: Argent, Index 2: Bronze
PAYS = 8

tableau = [
    ["Canada", [38, 24, 12]],
    ["Chine", [1, 5, 8]],
    ["USA", [5, 9, 4]],
    ["Russie", [4, 5, 5]],
    ["Autriche", [27, 25, 11]],
    ["Norvege", [5, 4, 3]],
    ["Finlande", [6, 8, 1]],
    ["Slovenie", [18, 16, 16]]
]

# pays = ["Canada", "Chine", "Etats Unis", "Russie", "Autriche", "Norvege", "Finlande", "Slovenie"]

print("Nombre de types de medailles:", MEDAILLES)
print("Nombre de pays qui ont des medailles:", PAYS)
print()

print("+----------+----------+----------+----------+")
print("|   PAYS   |    OR    |  ARGENT  |  BRONZE  |")
print("+----------+----------+----------+----------+")
# print(tableau[0][0])
for c in tableau:
    pays = c[0]
    medailles = c[1]
    or_ = medailles[0]
    argent = medailles[1]
    bronze = medailles[2]
    print(f"| {pays} |    {or_}    |    {argent}    |    {bronze}    |")   # String formatting (python)
print("+----------+----------+----------+----------+")


# Cle valeur (key, value)
d = {"Canada": [38, 24, 12],
     "Chine": [1, 5, 8],
     "USA": [5, 9, 4],
     "Russie": [4, 5, 5],
     "Autriche": [27, 25, 11],
     "Norvege": [5, 4, 3],
     "Finlande": [6, 8, 1],
     "Slovenie": [18, 16, 16]}

for k in d.keys():
    print(k)

for v in d.values():
    print(v)

for k, v in d.items():
    print(f"{k} ==> {v}")


print(d["Canada"])
if d.get("France") is None:
    d["France"] = [1, 1, 1]

print(d.get("France"))

var = d.pop("France")
print(var)




