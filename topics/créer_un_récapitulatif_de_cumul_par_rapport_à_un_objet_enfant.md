# Créer un récapitulatif de cumul par rapport à un objet enfant

**URL:** https://community.simplicite.io/t/5114

## Question
### Request description
Bonjour,
Est-il possible de sommer les points de la liste enfant "Mon parcours d'intégration" pour les actions au statut "Réalisé" pour caculer un % de réalisation sur l'objet principal ?

![image|690x233](upload://aX78H0FfCs8GjHRQOLxvuQlpQRA.png)


### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and those are the steps to reproduce it:*

1. Lorsqu'on met à jour une tâche, si elle passe au statut "Réalisé" alors le scoring d'onboarding s'implémente des points indiqués dans la colonne "Points associés"


### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=5.2.5
BuiltOn=2022-05-25 15:54
Git=5.2/ecae3b828f4cb7eda5e0e6f6e018fca9b12483d7
Encoding=UTF-8
EndpointIP=10.201.117.37
EndpointURL=http://siparex-simplicite-dev-5475d8459-t98qm:8080
TimeZone=Europe/Paris
SystemDate=2022-08-02 15:18:06
```
[/details]

[details="Simplicité logs"]
```text
N/A
```
[/details]

[details="Browser logs"]
```text
N/A
```
[/details]

[details="Other relevant information"]
N/A
[/details]

Merci et Bel été !

## Answer
Bonjour Ophélie, 

Tu peux implémenter ce besoin dans un hook `postUpdate()` de l'objet "Mon parcours d'intégration" pour que ça mette à jour la valeur du champ de l'objet parent.
