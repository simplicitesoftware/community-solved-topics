# Page surnuméraire export graphe sans le tableau croisé

**URL:** https://community.simplicite.io/t/3620

## Question
Bonjour,

Un client nous remonte le point suivant :

Lorsque j'ai un tableau croisé affiché sans le graphe, ou un graphe sans le tableau croisé, et que je clique sur "Publier" afin de l'exporter en PDF, le document possède une page surnuméraire vierge (qui correspond au TC/graphe masqué ?).

**Graphe masqué :**
Le graphe du TC est masqué :
![image|690x164](upload://rq3V7JVNYTXR03h97W4jt1ItPQw.png)

Puis, une fois que l'on clique sur "Publier" :
![image|690x454](upload://XpmhkTDf35T5s8ZDNtQLr31i5j.png)


**TC masqué :**
Depuis un objet externe, via le paramétrage que l'on peut passer dans l'URL, on masque le TC et on affiche le graphe, mais quand on clique sur Publier, on a :
![image|690x454](upload://zvwhDHrWG32YNigRa3KQy3tFvR2.png)

Y-a-t-il un moyen de supprimer cette page vierge ?

Merci d'avance pour votre aide,

Alexandre

![image|690x72](upload://CyTTEMLKE6o8dvQ4s9lglAtdMg.png)

## Answer
Merci Simon pour votre aide. 

Je ne m'étais pas rendu compte qu'on avait accès au HTML de la preview. Après analyse, c'est la hauteur de 100% imposée au body et au html dans le css qui crée une nouvelle page sur certains navigateurs. 

Du coup, j'ai "corrigé" le "problème" en rajoutant un mediaquery dans le css de notre thème :

```
@media print {
   html, body {
      height: auto;
   }
}
```
Merci encore !

Alexandre
