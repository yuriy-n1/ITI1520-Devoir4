# Iman Baratov et Yuriy Neyra Alvarado
# 2026-11-24
# Ce programme contient nos réponses pour la complétion du «Devoir 4».

# Q1
'''
La fonction "transl" permet de traduire les mots dans le dictionnaire d'anglais au français ou du français à l'anglais.
Si le mot n'éxiste pas dans le dictionnaire, la chaîne de caractères 'Unknown' est retournée.
'''
def transl(d, s): # (dict, str) -> str
    cles = list(d.keys())
    liste = list(d.values())
    for i in range (len(d)):
        if liste[i] == s:
            return cles[i]
    if s in d:
        return d[s]
    else:
        return "Unknown"

# Q2
'''
La fonction 'setOp' enlève les valeurs dupliquées et renvoie une liste avec un ordre different.
(Ordre croissant pour les nombres positifs et envoie les nombres negatives en arrière)
'''
def setOp(list1, list2): # (liste, liste) -> liste
    return set(list1 + list2)

# Q3
'''
'matrixMinMax' nous renvoie les valeurs minimale et maximale d'une matrice.
'''
def matrixMinMax(matrix): # (liste[liste[int]]) -> int, int
    valMin = float("inf")
    valMax = float("-inf")
    for i in range (len(matrix)):
        for j in range (len(matrix[i])):
            if matrix[i][j] < valMin:
                valMin = matrix[i][j]
            if matrix[i][j] > valMax:
                valMax = matrix[i][j]
    return valMin, valMax

'''
# test Q1
d = {"apple": "pomme", "banana": "banane", "pear": "poire", "plum": "prune"}
print(transl(d,"pear"))
print(transl(d,"poire"))
print(transl(d,"appricot"))

# test Q2
print()
print(setOp([1,2,2,3],[2,-6,8,7]))
print(setOp([],[1,4,2,4,6]))
print(setOp([1,1,1,1],[]))
print(setOp([1],[2,3,2,2]))

# test Q3
print()
print(matrixMinMax([[1,5],[2,8]]))
print(matrixMinMax([[1,5,10],[2,8,-1]]))
print(matrixMinMax([[2,8,-1]]))
print(matrixMinMax([[1],[1]]))
'''
