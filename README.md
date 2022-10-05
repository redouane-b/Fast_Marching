# Implémentation de la méthode Fast Marching
## Description de la méthode

La méthode Fast Marching sert à résoudre les problèmes de valeurs limites de l'équation Eikonal.

L'objectif de la méthode Fast Marching est de calculer numériquement le temps d'arrivée T, solution de l'équation stationnaire:
c(x) |∇xT(x)| = 1

## Implémentation en Python
L’algorithme de la méthode:
* Définition du front initial et initialisation de T
* Définition de la narrow band et initialisation de T sur celle ci
* Recherche de la plus petite valeur de T pour la Narrow Band
* Redéfinition de la Narrow Band en complétant avec les nouveaux voisins
* Recalcul de T pour la Narrow Band et itération du processus jusqu’à visite de tous les points

## Résultats
### Résolution d'un labyrinthe
![image](images/image3.png)

### Planificateur d'itinéraire
![image](images/image4.png)

