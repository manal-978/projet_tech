#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def lire_fichier_cnf(nom_fichier):
    with open(nom_fichier, 'r') as f:
        lignes = f.readlines()
    cnf_f = []
    for ligne in lignes:
        if ligne.startswith('p cnf'):
            num_vars = int(ligne.split()[2])
        elif ligne.startswith('c'):
            continue
        else:
            cnf_f.append(list(map(int, ligne.split()[:-1])))
    return cnf_f, num_vars

# Fonction pour générer toutes les combinaisons de True/False pour n variables
def generate_truth_table(n):
    if n == 0:
        return [[]]
    lower_order = generate_truth_table(n-1)
    return [row + [v] for row in lower_order for v in [True, False]]
nom_fichier = 'uf20-01.cnf'
cnf_formula, num_vars = lire_fichier_cnf(nom_fichier)
table_verite = generate_truth_table(num_vars)

est_satisfiable = False
for row in table_verite:
    est_satisfiable_row = all(any(row[abs(literal)-1] == (literal > 0) for literal in clause) for clause in cnf_formula)
    if est_satisfiable_row:
        est_satisfiable = True
    print(row, ":", est_satisfiable_row)

if est_satisfiable:
    print("satisfiable")
else:
    print("non satisfiable")


# In[15]:


import random

def lire_fichier_cnf(nom_fichier):
    with open(nom_fichier, 'r') as f:
        lignes = f.readlines()
    cnf_f = []
    for ligne in lignes:
        if ligne.startswith('p cnf'):
            num_vars = int(ligne.split()[2])
        elif ligne.startswith('c'):
            continue
        else:
            cnf_f.append(list(map(int, ligne.split()[:-1])))
    return cnf_f, num_vars

nom_fichier = 'uf20-01.cnf'

cnf ,num_vars = lire_fichier_cnf(nom_fichier)
solution = {i: random.choice([True, False]) for i in range(1, num_vars+1)}

num_satisfiable = sum(any(solution[abs(literal)] == (literal > 0) for literal in clause) for clause in cnf)
est_satisfiable = any(all(solution[abs(literal)] == (literal > 0) for literal in clause) for clause in cnf)

print("Solution RANDOM :", solution)
print("Nombre de clauses satisfaites :", num_satisfiable)
if est_satisfiable:
    print("La formule CNF est satisfiable")
else:
    print("La formule CNF n'est pas satisfiable")


# In[ ]:





# In[ ]:





# In[ ]:




