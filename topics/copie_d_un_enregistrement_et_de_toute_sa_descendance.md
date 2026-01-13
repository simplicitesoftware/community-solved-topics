# Copie d’un enregistrement et de toute sa descendance

**URL:** https://community.simplicite.io/t/11182

## Question
### Request description

Bonjour,

Je souhaiterais savoir s’il existe une fonctionnalité standard permettant de copier un enregistrement **ainsi que toute sa descendance**.

Exemple : lorsqu’on copie le processus `4`, nous voudrions également copier automatiquement :

* ses enfants directs (`4.1`, `4.2`),

* ainsi que les niveaux inférieurs (`4.1.1`, `4.1.2`, `4.2.1`, `4.2.2`, etc.).

En d’autres termes, l’objectif est de dupliquer un morceau de l’arboresence rattachée à un objet.

![image|597x500](upload://7gWhy7IOk2c1U4g6VjjSW71AAIu.png)

Pourriez-vous me dire :

1. Si ce comportement existe en standard dans Simplicité,

2. Si non, quelles sont vos recommandations et bonnes pratiques pour le mettre en place (hooks, cascade copy, action personnalisée, etc.) ?

Merci d’avance pour vos retours et conseils,
Cordialement.

### Technical information

[details="Instance /health"]
```text
---paste the content of your-instance.com/health---
```

[/details]

[details="Simplicité logs" open]
```text
Version=6.2.15
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
Non, les N,N sont également recopiables. 
Une relation N,N à forcement un lien identifiant vers le parent, par contre le parcours récursif s'arrête vers les enfants.

Exemple : quand on copie un User, on recopie bien ses responsabilités qui sont une N,N entre User et Group, par contre on ne duplique pas les groupes :

`User <--- Resp N,N ---> Group `

Aucun code n'est requis pour faire ça.

Il faut regarder votre modèle pour voir pourquoi l'algo ne comprend pas que c'est une N,N recopiable (souvent un pb de clé fonctionnelle ou de relation).

Pour les autres cas complexes, il faut effectivement coder certaines recopie par `postCreate/isCopied` (pour calculer une clé fonctionnelle, associer d'autres objets, remettre d'autres valeurs par défaut...)
