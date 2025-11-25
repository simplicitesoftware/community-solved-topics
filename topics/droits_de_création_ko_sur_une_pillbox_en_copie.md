# Droits de création KO sur une pillbox en copie

**URL:** https://community.simplicite.io/t/11053

## Question
### Request description

Bonjour,
Les droits de création via pillbox semblent disparaître quand on est sur une copie. 
Je me demande si ce n'est pas lié à la feature récente qui affiche les pillbox temporaires.

En création
![image|607x500](upload://sSBTMZejBMfUNUP1KE5rG8PCZC5.png)


En copie
![image|601x500](upload://4rN4kzbh1Lo1SuXarDGmg4zKa0e.png)

Piste d'analyse :
Le call sur les metadata renvoie bien create = true.
![image|690x260](upload://2IVq5BXrpknGYsn50ItrmlhFqMC.png)

Mais create est à false lors du search des N,N existantes sur l'objet source de la copie.

```
else if (l.cascadeCopy && pobj.metadata.copyId)
                        search(pobj.metadata.copyId, true);
```
![image|690x251](upload://lKml0lMVH8b6kiBz1vBsp9cZdmZ.png)

J'ai l'impression que les metadata de ma N,N à copier sont écrasées par celles de l'objet source, sur lequel je n'ai pas les droits.

```
if (res.meta)
self.metadata = res.meta;
```

Merci d'avance pour votre aide
Emmanuelle

[Platform]
Status=OK
Version=6.2.18
BuiltOn=2025-10-31 21:07

## Answer
Merci pour cette analyse très détaillée.

Effectivement le contexte était remis en LIST PANEL pour aller "recopier" les liens existants en respectant les éventuelles règles de la relation en back (ref instance = init, search-spec sur le link....). Tu devais avoir des règles à ce niveau là pour interdire la création.
Il sera remis en contexte initial une fois terminé.

Ce sera corrigé en 6.2.19 en espérant que ça clôture le sujet compliqué des NN en pillbox :zany_face:
