# Ajout d'un ascenseur vertical sur les listes de valeurs

**URL:** https://community.simplicite.io/t/8036

## Question
Bonjour,

Serait-il possible d’avoir un ascenseur vertical dans le cas où une LOV possède des valeurs qui dépassent le champ de l’écran ?

Exemple :
![image|264x466](upload://8jIJBuHRYHBN6vfsByEGwoQjzAV.png)


Quand j'agrandie l'écran :
![image|231x475](upload://nOq9ohTjT7et7QY4JV7r33ymRnC.png)


il y a aussi le même souci avec l'auto completion quand on commence à saisir dans un champs et qu'on est en bas de l'écran :
![image|244x256](upload://b503ntqODtcGUaJOLBBxt2YJhxi.png)

![image|249x263](upload://4c0k6m48KNXMM0wTyN6Y9dFgvs2.png)


Merci d’avance,

Abed.

[Health check](https://ear-poc.k8s-stage.grouperci.com/ui)

[Platform]

Status=OK

Version=5.3.34

BuiltOn=2024-04-05 09:39

Git=5.3/b3f09e666713dbd92264307a6dc851f97e255130

Encoding=UTF-8

EndpointIP=10.42.105.44

EndpointURL=http://simplicite-poc-cd7bdff46-gblsl:8080

TimeZone=UTC

SystemDate=2024-04-08 10:14:57

## Answer
Après analyse seul Chrome est capable d'utiliser la bonne hauteur restante via le CSS suivant sur le dropdown-menu :

```css
max-height: -webkit-fill-available;
````

Sur Firefox, l'équivalent ne fonctionne pas :

```css
max-height: -moz-available;
```

On a donc dû résoudre le problème par du code javascript qui (re)calcule la hauteur maximale du dropdown, comme la hauteur de l'écran moins sa position verticale, et ce à chaque scroll de la liste ou de la page.


Ce sera livré en 5.3.35.
