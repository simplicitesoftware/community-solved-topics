# Compteur dans une page d'accueil

**URL:** https://community.simplicite.io/t/11453

## Question
Bonjour,

Je me permets de vous contacter pour deux petites questions, sûrement très naïves.
J’ai cherché sur le forum ainsi que dans la documentation, mais je n’ai pas trouvé de solution à mon problème.

**Postulat de départ :**

Je souhaite créer les mêmes compteurs que ceux que l’on trouve dans l’application « Demo » sur la page d’accueil (Produits, Clients, etc.).
Cela ne me pose pas réellement de problème, et j’arrive à reproduire le même fonctionnement.

**Première question :**

Sommes-nous limités à **quatre compteurs par ligne** ?
J’ai actuellement cinq compteurs, et le cinquième se retrouve sur la ligne en dessous.

Est-il possible de les afficher tous sur une seule ligne ?
J’ai essayé de modifier la largeur via du CSS, mais cela ne fonctionne pas.

Voici le code que j’ai tenté :

```
/* Ajuste les cartes de compteurs pour afficher cinq éléments sur une ligne */
div.counters > div {
  flex: 0 0 20%;
  max-width: 20%;
}

div.counters .counter-card {
  white-space: normal;
  font-size: 0.85rem; /* Réduire la taille du texte si nécessaire */
}

```

**Deuxième question :**

Mes compteurs sont tous relatifs au même objet métier.
Je souhaiterais que, lorsque je clique sur l’un d’eux, cela ouvre cet objet en appliquant **le filtre correspondant au compteur sélectionné**.

Les compteurs fonctionnent très bien et affichent le bon nombre, mais lorsque je clique dessus, le filtre appliqué est toujours identique : il correspond systématiquement au **dernier compteur**.

Voici le code que j’ai mis en place :

```
{
  "objects": [
    {
      "color": "violet",
      "name": "NovaPitch",
      "icon": "fas/user-plus",
      "filters": {
        "novaPitchSuiviDossierPitch": "= '1' or = '7'"
      },
      "labels": {
        "FRA": "Prendre liaison / Attente date",
        "ANY": "Contact / Date pending"
      }
    },
    {
      "color": "blue",
      "name": "NovaPitch",
      "icon": "fas/clock",
      "filters": {
        "novaPitchSuiviDossierPitch": "= '2'"
      },
      "labels": {
        "FRA": "Attente réponse société",
        "ANY": "Waiting for reply"
      }
    },
    {
      "color": "green",
      "name": "NovaPitch",
      "icon": "fas/calendar-check",
      "filters": {
        "novaPitchSuiviDossierPitch": "= '3'"
      },
      "labels": {
        "FRA": "Préparation entretien",
        "ANY": "Preparing interview"
      }
    },
    {
      "color": "orange",
      "name": "NovaPitch",
      "icon": "fas/file-alt",
      "filters": {
        "novaPitchSuiviDossierPitch": "= '4'"
      },
      "labels": {
        "FRA": "Rédiger compte-rendu",
        "ANY": "Write report"
      }
    },
    {
      "color": "red",
      "name": "NovaPitch",
      "icon": "fas/reply",
      "filters": {
        "novaPitchSuiviDossierPitch": "= '5'"
      },
      "labels": {
        "FRA": "Retour vers société",
        "ANY": "Reply to company"
      }
    }
  ]
}

```

---

Merci d’avance pour votre compréhension et votre aide.

cdt

### Technical information

[details="Instance /health" open]
```text
ERSION Simplicité version 6.2.18;
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

Effectivement en l'état il n'est pas possible d'avoir plus de 4 colonnes. Nous allons corriger ça. 

Concernant les filtres, par défaut la même instance d'objet : `counter_MyObject` est utilisée et donc les filtres s'écrasent.
Vous pouvez ajouter un attribut `instance` spécifique à chaque objet dans le JSON, par exemple : 
```json
{
  "objects": [
    {
      "color": "violet",
      "name": "NovaPitch",
      "instance": "counter1_NovaPitch",
      [...]
    },
    {
      "color": "blue",
      "name": "NovaPitch",
      "instance": "counter2_NovaPitch",
      [...]
    },
    [...]
  ]
}
```
