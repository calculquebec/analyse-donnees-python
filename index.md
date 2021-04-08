---
layout: default

title: Accueil
---

## À propos

Cet atelier est une adaptation du tutoriel
[Data Carpentry - Data Analysis and Visualization in Python for Ecologists](https://datacarpentry.org/python-ecology-lesson/).

Les notebooks Jupyter et les données associées sont [disponibles sur GitHub](https://github.com/calculquebec{{ site.baseurl }}).

### Les données utilisées

Pour le présent atelier, nous utiliserons un sous-ensemble des données du [*Portal Project Teaching Database*](https://figshare.com/articles/Portal_Project_Teaching_Database/1314459).
* Entre autres, le fichier `data/surveys.csv` est une version simplifiée du [fichier original](https://ndownloader.figshare.com/files/2292172).
* **Référence** : Ernst *et al*, [Long-term monitoring and experimental manipulation of a Chihuahuan Desert ecosystem near Portal, Arizona, USA](https://esapubs.org/archive/ecol/E090/118/)

Avec ce fichier de données, nous allons étudier les caractéristiques de
différentes espèces animales vues dans différents sites de la zone de recherche.
Chaque enregistrement dans ce fichier CSV contient l'information d'un seul animal observé.
Voici les différentes informations recueillies qui correspondent aux colonnes d'une table de données :

 Colonne          || Description
----------------- || -----------
`record_id`       || Identifiant unique de l'enregistrement
`month`           || Mois de l'enregistrement
`day`             || Jour de l'enregistrement
`year`            || Année de l'enregistrement
`plot_id`         || Identifiant du site
`species_id`      || Identifiant de l'espèce, encodé avec deux lettres
`sex`             || Sexe de l'animal ("F", "M")
`hindfoot_length` || Longueur de l'arrière-pied (mm)
`weight`          || Poids de l'animal (g)

<hr />

Les premières lignes du fichier CSV ressemblent donc à ceci :

```
record_id,month,day,year,plot_id,species_id,sex,hindfoot_length,weight
1,7,16,1977,2,NL,M,32,
2,7,16,1977,3,NL,M,33,
3,7,16,1977,2,DM,F,37,
4,7,16,1977,7,DM,M,36,
5,7,16,1977,3,DM,M,35,
6,7,16,1977,1,PF,M,14,
7,7,16,1977,2,PE,F,,
8,7,16,1977,1,DM,M,37,
9,7,16,1977,1,DM,F,34,
```

## Autres liens utiles
* Module Python [`pandas`](https://pandas.pydata.org/docs/reference/index.html)
  * Fonction [`melt()`](https://pandas.pydata.org/docs/reference/api/pandas.melt.html)
* Module Python [`plotnine`](https://plotnine.readthedocs.io/en/stable/) :
  * [Galerie (exemples)](https://plotnine.readthedocs.io/en/stable/gallery.html)
  * Constructeurs d'éléments géométriques [`geom_*()`](https://plotnine.readthedocs.io/en/stable/api.html#geoms)
  * Constructeurs de thèmes [`theme*()`](https://plotnine.readthedocs.io/en/stable/api.html#themes)
  * Constructeurs de facettes [`facet_*()`](https://plotnine.readthedocs.io/en/stable/api.html#facets)
* Module Python [`plotly`](https://plotly.com/python/) pour des graphes interactifs
* Outils d'édition de code Python :
  * Via [JupyterLab](https://docs.computecanada.ca/wiki/JupyterLab) sur les grappes de calcul
  * Via un [Jupyter Notebook](https://docs.computecanada.ca/wiki/JupyterNotebook/fr), lancé localement
  * L'éditeur [Spyder](https://www.spyder-ide.org)
  * [Visual Studio Code](https://code.visualstudio.com)
* Les prochains ateliers à [Calcul Québec](https://www.eventbrite.ca/o/calcul-quebec-8295332683)
  et [Calcul Canada](https://www.computecanada.ca/research-portal/technical-support/training/)
* Tutoriels en ligne [Software Carpentry](https://software-carpentry.org/lessons/)
  et [Data Carpentry](https://datacarpentry.org/lessons/) :
  * [Introduction à la ligne de commande Bash](https://swcarpentry.github.io/shell-novice/)
  * [Introduction à la programmation en Python](https://swcarpentry.github.io/python-novice-inflammation/)
  * [Nettoyage des données avec OpenRefine](https://datacarpentry.org/OpenRefine-ecology-lesson/)
  * [Gestion de données avec SQL](https://datacarpentry.org/sql-ecology-lesson/)
  * [Analyse de données et visualisation en R](https://datacarpentry.org/R-ecology-lesson/)
