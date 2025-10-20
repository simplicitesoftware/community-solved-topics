# Problème – Modification de l’ordre des colonnes en liste non prise en compte

**URL:** https://community.simplicite.io/t/10509

## Question
### Request description

Bonjour,

J’ai rencontré un problème concernant l’ordre d’affichage des colonnes dans la vue liste d’un objet.
Voici les étapes que j’ai suivies :

1. Ouverture de la liste de l’objet concerné.

2. Modification de l’ordre des colonnes via le paramétrage des **Préférences**.

3. Enregistrement des modifications.

4. Vidage du cache (**Clear cache**) puis rechargement complet de l’interface.

**Problème constaté :**
L’ordre des colonnes reste inchangé, les préférences enregistrées ne sont pas appliquées.
Aucun log spécifique n’apparaît côté serveur suite à cette manipulation.

Voici la capture d’écran des préférences souhaitées :

![image|600x500](upload://4Dfjc8ivxAxfvfcqodSCADh1WPv.png)

Voici la capture d’écran de l’affichage en liste de cet objet qui ne prend pas en compte les préférences :

![image|690x310](upload://iIbyfW4Nl5WVqTwhYxheKaPhcn8.png)

**Précisions :**

* Il n’y a **aucun code hook** qui manipule les préférences.

* Il n’y a **aucune altération**, manuelle ou par code, du paramètre `LIST_PREFS`.

**Test complémentaire :**
J’ai effectué le même test sur un autre objet, et cette fois l’ordre des colonnes a bien été modifié sans même avoir besoin de vider le cache.

Voici les captures d’écran de la configuration de l’objet concerné par le problème :

![image|690x314](upload://vXrbi657XXOLMr8rZDPOmtm90dp.png)

![image|690x331](upload://17Pl3labmAXx1cUH1RoY9Bt3tQc.png)

Voici la capture d’écran du paramètre système `LIST_PREFS` qui prend bien en compte les changements:

![image|690x240](upload://r2KaJB1a3gnaEserx8MBkupZV6q.png)

Pouvez-vous m’indiquer si d’autres actions sont nécessaires pour que les préférences soient prises en compte dans mon cas ?

Merci d’avance pour votre retour.

Cordialement,

Elyass Boussif

### Technical information

[details="Instance /health" open]
```text
[Platform]
Status=OK
Version=6.2.14
BuiltOn=2025-07-31 15:05
Git=6.2/285e27aae1fe529c1a4afc33b026a6d5f04a3552
Encoding=UTF-8
EndpointIP=100.88.230.244
EndpointURL=http://bca-71077-app-66479b7f4d-mwqd4:8080
TimeZone=Europe/Paris
SystemDate=2025-08-13 18:58:49
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

Il y a effectivement un bug sur la gestion de ces préférences. La plateforme n'en tient compte que si le paramètre "Afficher les zones en liste" de l'objet est à **Oui**

Nous allons corriger.
