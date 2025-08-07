# Navigation dans un objet select après filtrage par favori

**URL:** https://community.simplicite.io/t/9860

## Question
### Request description

Bonjour,

Nous avons identifié une anomalie concernant la navigation dans les documents favoris :

#### 🔍 Contexte :

Depuis la liste `Tous les documents`, nous filtrons les résultats en activant le filtre par **favori**. Nous accédons ensuite à un document favori.
![Capture d'écran 2025-04-25 110912|690x311, 75%](upload://isPmjC3eGZ3BICxUH4vBNd5nYgH.png)


Une fois dans la fiche d’un document mis en favori, il n’est plus possible de naviguer dans un autre document via le **panel latéral (panel 2)** *si l’autre document n’est pas lui aussi dans les favoris*.
![Capture d'écran 2025-04-25 111004|690x451, 50%](upload://evW42UHkE3ccOSvy0BIDvhBG0mw.png)

Un message "Aucun résultat à la recherche" s’affiche (cf. capture jointe), comme si le filtre restait actif au niveau du formulaire.
![Capture d'écran 2025-04-25 111016|690x242, 75%](upload://pxARkx0gfoOLUBDsceoMIcPcJzy.png)


#### ❓ Questions :

1. Est-ce un comportement attendu (lié au fait que l’arborescence est une **vue de type select**) ?
2. Est-ce que cela pourrait être corrigé nativement dans le standard ?
3. À défaut, serait-ce possible de **désactiver les filtres de liste lors du passage dans le formulaire** pour éviter ce blocage ?

Merci d’avance pour vos retours et conseils. 

### Technical information

[details="Instance /health"]
```text
---paste the content of your-instance.com/health---
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

L'instance d'objet en liste (main) est filtrée sur les favoris de l'utilisateur (cf la requete en base qui fait un `where row_id in (liste des faroris)`.

Votre objet "select" contient surement un lien vers le même objet ?

Celui-ci devra soit :
- aller vers une autre instance d'objet non filtrée
- ou vers un héritier de votre objet qui n'aura pas de filtre
- ou retirer le filtre à chaque ouverture du formulaire `initUpdate`
`setBookmarksFilterEnabled(false);`

Est-ce que d'autres filtres sont pris en compte de la même manière ? Par exemple si vous placez un filtre sur un champ, est-ce que votre lien fonctionne vers un "objet en dehors de ce filtre" ?

Il faudrait surement faire une évolution en 6.2 pour que le "select(id)" du formulaire ignore le filtre des favoris, tout comme il ignore les filtres utilisateur des champs (mais pas les search-spec back).
