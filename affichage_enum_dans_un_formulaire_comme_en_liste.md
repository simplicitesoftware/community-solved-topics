# Affichage Enum dans un formulaire comme en liste

**URL:** https://community.simplicite.io/t/9167

## Question
### Request description

Bonjour,

Nous avons un formulaire d'objet ou des champs comme **Nom du produit ou service** et **Type de document légal** sont actuellement affichés sous forme de listes déroulantes avec des choix possibles :
![image|189x500, 50%](upload://vM09BJdnrR2yOCpmbrDMZsveXIw.png)

Tous ses champs sont en read-only dans le formulaire et non modifiable, c'est pour ca qu'on aimerait avoir le meme affichage qu'en liste pour que l'utilisateur ne voit que la valeur de sorti et non les autres choix disponible.

![image|205x138, 75%](upload://sUPQfFnftXdq6h76RQPg9wLIxCQ.png)


Voici le rendu voulu par l'équipe design :

![image|358x500, 50%](upload://eC14yRjVBbUGas2UfvjfTNZwHL2.png)

En brief, on aimerait avoir l'affichage en tag de la liste en formulaire lorsque l'attribut en en read only :slight_smile: 




### Technical information

[details="Instance /health"]
```text
---[Platform]
Status=OK
Version=6.1.14
BuiltOn=2024-11-13 12:35
Git=6.1/34709826975d46845d2c518ac5815bd118d09709
Encoding=UTF-8
EndpointIP=100.88.65.123
EndpointURL=http://lbc-77449-app-8566f9479c-pk7l9:8080
TimeZone=Europe/Paris
SystemDate=2024-12-02 11:19:12

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://lbc-app.ext.gke2.int.gcp.renault.com
ActiveSessions=1
TotalUsers=28
EnabledUsers=25
LastLoginDate=2024-12-02 09:50:37---
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

Dans une formulaire, il faut avoir l'ensemble des options/valeurs du `<select>` même dans le cas de la lecture seule pour l'utilisateur :

- Champ ramené/sélectionnable via Object picker (une référence ou un datamap)
- Contrainte sur le champ (par exemple pour changer sa valeur en fonction d'un autre)
- Code / Hook front qui changerait la valeur

Pour ne pas faire régresser les fonctionnalités de sélection dynamique (autre que par l'utilisateur), il faudrait plutôt passer par du CSS pour changer l'aspect du contrôle.

coins arrondis + masquer le bouton arrow/caret:

```css
.field[data-field=myFieldName] .field-enum.readonly {
	.select2 {
		width: fit-content !important
	}
	.select2-selection, .enum-item {
		border-radius: 1rem !important;
	}
	.select2-selection__arrow {
		display: none !important;
	}
}
```

on va voir pour intégrer ça en standard à un rendering en "tag" + read-only.
