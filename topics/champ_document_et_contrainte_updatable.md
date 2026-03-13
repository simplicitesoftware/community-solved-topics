# Champ document et contrainte Updatable

**URL:** https://community.simplicite.io/t/11785

## Question
### Request description

Bonjour,
Encore un souci avec les contraintes :grimacing: cette fois c'est sur une 6.2 mais je reproduis aussi en 6.3.

Avec une contrainte
- front
- qui définit la propriété Updatable d'un champ Document
- le champ dispose d'un document

![image|690x313, 50%](upload://b2PUJPuwKOHY6t2rqkHQVSWJXe5.png)

Je passe le Booleen à No, le document disparaît quand le champ Bocument devient Read only

![image|690x316, 50%](upload://zhQVnQm5ykHqFBqvz0Q7o6XbnBt.png)

Je repasse à Yes, mon champ Document est Updatable mais vide (ainsi que le champ image que j'ai impacté par la contrainte également)

![image|415x465, 50%](upload://pAjv1SrQknS0z6WoPjYd3ONnA6K.png)

Et le Save renvoie une erreur NO_FILE_FORMAT

![image|388x247, 50%](upload://xUxFCscLqDs1d6e08i91kF0k5kw.png)




Le ```updatable``` de la contrainte appelle la fonction ```redraw()``` qui semble via l'appel à ```val()``` (sans paramètre) vouloir chercher le document dans la partie *Choose file* et non le document déjà enregistré. 

```
find() {
            super.find();
            this.file = $("#file_field_" + this.name, this.ctn)[0];
            return this.input;
        }
```

Or dans notre cas, nous n'avons pas changé le document, *Choose file* est hidden et son attribut File est vide.

![image|690x39](upload://41jkpuAU2Jf8YzcdVUnubJpp2Ko.png)

La contrainte 
[DemoSupplier-C1.xml|attachment](upload://4P5TG70vVqNfbfQXg2NmqApl5Lw.xml) (2.1 KB)


[Platform]
Status=OK
Version=6.2.21
BuiltOn=2026-01-15 22:16

## Answer
Correctif livré et à tester en preview/6.3.7 car toucher aux documents est assez sensible.

Le cas qui posait problème :

- Boolean à Vrai : la contrainte passe le document en éditable
- Sélection d'un document
- Booléen à Faux : le champ passe en lecture / l'input file est détruit, il ne reste que le nom du document dans un champ texte en lecture
- Booléen à Vrai : le champ repasse en écriture / l'input file est de nouveau disponible mais vide (on ne peut pas setter un input file avec un File) ! seul le nom du document en lecture reste présent
- Save... miracle le document est sauvegardé !
