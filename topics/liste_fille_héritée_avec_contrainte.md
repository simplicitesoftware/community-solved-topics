# Liste fille héritée avec contrainte

**URL:** https://community.simplicite.io/t/9677

## Question
### Request description

Bonjour,

Nous rencontrons un problème en plusieurs couches sur la V6 que nous ne reproduisons pas en V5.
Dans le cas très particulier d'une liste fille 
- héritée
- avec contrainte
les données du panel ne s'affichent pas au premier chargement.

![image|690x191](upload://nIlnqaI1UpATVYAzOQe1KQz35Kr.png)

Après un reload du formulaire, elles s'affichent correctement. 
Si je recharge toute la page (F5) le problème apparaît de nouveau.
Il semble que la durée de chargement de la contrainte crée une confusion au moment de l'affichage de la liste.

![image|690x95](upload://vSFVuMIzdesjRFFi5uh7cs4RnZw.png)

Je mets ci-dessous les steps et mon analyse.

### Steps to reproduce

1.Créer un objet B hérité d'un objet A
2.Créer un lien d'un objet C en liste fille sur l'objet A
3.Créer une contrainte sur l'objet C
4. Dans le template de l'objet B, ajouter cette liste fille dans les onglets bas
5. Afficher l'objet B : l'onglet C reste sur le vue "skeleton"
6. Faire un reload de B : l'onglet C s'affiche correctement

Analyse :
Il semble qu'en raison du chargement un peu long de la contrainte, on entre dans 

``` function display() obj.hook(p.display, [ctn, obj, p, _ => {``` 

 **avant** l'appel à ```s.display = s.display || o.displaySearch;``` dans bindHooks.

```p.display``` qui est sensé afficher la liste est donc undefined.

Je vois qu'on passe une 2ème fois dans le display **après** le bindHooks, mais le display semble se faire cette fois sur l'onglet du père qui est dans une area inherited cachée.

HTML de ma liste fille sur C, hidden avec les data
![image|690x35](upload://z7oII5dBqcTZnR7l6L7KwgKz0c0.png)

HTML de ma liste fille sur B, toujours en skeleton
![image|690x24](upload://xRrrY2PIfW56A28CuRKe5tiDtiD.png)

J'espère avoir donné toutes les informations utiles,
Merci de votre aide,
Emmanuelle

### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=6.2.3
BuiltOn=2025-03-07 12:29
Git=6.2/de139c86150da2a84599aa6c14b51d1e06a2e118
```
[/details]

## Answer
[quote="Emmanuelle, post:3, topic:9677"]
mais l’affichage de la liste s’effectue sur la version mère (onglet caché hérité) du formulaire.
[/quote]

Je ne comprends pas, mais ça doit venir de là.
