# Contraintes et affichage dynamique dans un processus métier

**URL:** https://community.simplicite.io/t/9361

## Question
Bonjour,

Nous souhaitons dans un use case, afficher une description associée à un attribut "produit" dans une étape d'un processus métier.

Actuellement, cela fonctionne correctement dans le formulaire de l'objet associé (les contraintes mettent bien à jour la description en fonction du produit sélectionné, affichage aussi si l'attribut à un produit ), nous avons 2 impact un de visibilité front-end et un autre de valeur de champ :

![ezgif-2-f4558ba1c3|690x257, 75%](upload://waeZyKLHQqX7dAcSdKtUtosdaRl.gif)


mais dans le contexte du processus métier, la description ne se met pas à jour dynamiquement au cours de l'activité.
Elle apparaît uniquement dans la synthèse, mais sans changer en fonction du produit choisi( dans le cas ou l'utilisateur change de produit).

![image|690x226, 75%](upload://8BenaILeiUrjkeaqWlhuGUmXPPQ.png)
![image|690x204, 75%](upload://lIDNIzIr6NDhOOLeCWJE4azvWr9.png)


Est-ce qu’il est prévu que les contraintes et impacts puissent s’appliquer nativement dans les processus métiers associé à un objet ? Ou bien devons-nous passer par un script JavaScript pour refaire cet affichage dynamique ? ( dans ce cas là passer par une ressource lié au processus métier ou la Responsive5 ? )

Je me posais aussi la question concernant les ressources lié à un processus métier :

Pour les ressources liées à un processus métier (JS et CSS), il n’est pas encore possible d’associer directement ces ressources à un processus spécifique. Nous les plaçons pour le moment dans `Responsive5`. Est-il prévu qu'à l'avenir, on puisse utiliser directement ces ressources dans le cadre d’un processus métier pour le personnalisé ? ( ou bien une mauvaise utilisation/compréhension de ma part).

Merci pour votre retour 

### Technical information

[details="Instance /health"]
```text
---Status=OK
Version=6.1.19
BuiltOn=2025-01-06 14:36
Git=6.1/793315cef5dfab9cb2ccefaaf0b870ed3a24e05d
Encoding=UTF-8
EndpointIP=100.88.206.228
EndpointURL=http://lbc-77449-app-5584889c69-bm52g:8080
TimeZone=Europe/Paris
SystemDate=2025-01-09 15:51:37---
```
[/details]

[details="Simplicité logs"]
```text
---paste the content of the **relevant** server-side logs---
```
[/details]

[details="Browser logs"]
```text
---paste content of the **relevant** browser-side logs---
```
[/details]

[details="Other relevant information"]
*----E.g. type of deployment, browser vendor and version, etc.----*
[/details]

## Answer
Bonjour,

Problème reproduit, en fait il manquait des évènements "change" sur les champs lié à des contraintes qui ne pouvaient donc pas être dynamiques. 

De mémoire cela avait été initialement voulu pour pouvoir différencier les règles de gestion dans un formulaire seul ou dans un workflow, mais cela n'a jamais été implémenté.

Ce sera corrigé dans la prochaine livraison 6.1.20 pour appliquer les mêmes règles sous contraintes au sein du workflow.
