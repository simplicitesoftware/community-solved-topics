# L'export de module XML ne fonctionne pas en 5.2

**URL:** https://community.simplicite.io/t/5753

## Question
### Request description

Bonjour,

L'export de module ne fonctionne plus depuis que nous avons migré en 5.2.
Quand je clique sur "Export XML", j'ai un message "Document saved:" mais le fichier XML ne se met pas à jour.

![image|690x216](upload://3ex5yXT7BV5egsNLE9PnjL0CNlL.png)

Je n'ai pas d'erreurs dans les logs.
Y a-t-il des adaptations à faire après montée de version ?
Merci !



### Technical information

[details="Instance /health"]
[Platform]
Status=OK
Version=5.2.26
BuiltOn=2022-12-20 22:00
```
[/details]

## Answer
Bonjour @Emmanuelle !

Cette erreur sur le PDF est suspecte, avez-vous un bookshelf lié au champ fichier du module (`mdl_xml`) ? Ça ne devrait pas être le cas. Pouvez-vous transmettre un screenshot équivalent à celui-ci? 

![booksheld|690x370](upload://dWpjZOisCTNAAh5N9LAq2TokYyN.jpeg)
