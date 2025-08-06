# Erreur à la création d'un objet SELECT

**URL:** https://community.simplicite.io/t/6244

## Question
### Request description

Bonjour,

Je ne parviens plus à créer d'objet de type SELECT. 
Je tombe sur l'erreur suivante

![image|690x279](upload://1qUlwrcdaQWGEMdQTHvnKnXhVlL.png)

Pouvez vous m'aider à débugger ?
Merci d'avance

Emmanuelle

### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and these are the steps to reproduce it:*

1.Go to Administration > Business Object
2.Create
3. Fill any logical name and select as physical name
4. Save

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.2.37
BuiltOn=2023-04-14 19:00
```
[/details]

## Answer
Oui c'est "récent", les objets select ont pas mal évolué ces derniers mois.

Pour résoudre le pb il suffit de mettre `select 1` dans le paramétrage. Dans les révisions prochaines ce sera un warning
