# Niveau de sécurité : Prévisualisation document Word sur Simplicité V6

**URL:** https://community.simplicite.io/t/8325

## Question
### Description

Bonjour,

Dans le cadre d'un nouveau projet, nous prévoyons d'intégrer la fonctionnalité de prévisualisation de documents. Pour notre développement en cours, nous avons implémenté cette fonctionnalité via Simplicité pour prévisualiser les documents.
![Capture d’écran 2024-06-10 143905|690x51, 75%](upload://ljNJ6gUdFlyggNVPhaOeoE7OBto.png)

Je voudrais savoir :

  * La prévisualisation est-elle sécurisée ? En particulier, les données des documents sont-elles envoyées à des serveurs externes (ex: Microsoft) ?
  * Si oui, comment pouvons-nous bloquer ce partage d'information pour garantir la confidentialité de nos données ? S'il existe une alternative sécurisée.
 * Sinon Désactiver la prévisualisation et demander au User de d'abord télécharger le document. ( fesable via une action ou autre)

Ceci serait important afin de chiffrer ce UseCase et de pas avoir de mauvaise surprise à l'utilisation de cette fonctionnalité au niveau de la sécurisation ( données personnelles).

En attente d'un retour à bientot,

### Version

[Platform]
Status=OK
Version=6.0.12
BuiltOn=2024-05-31 19:02
Git=6.0/540dc0427aeb0f02e2466107874f803e6aef9c75
Encoding=UTF-8
EndpointIP=100.88.201.116

## Answer
La fonctionnalité UI de preview des documents peut être globalement inhibée via le param système `USE_DOC_PREVIEW` (l'utilisateur aura alors toujours la possibilité de télécharger le document pour le visualiser localement)

S'agissant des documents Office la preview s'appuie sur la fonctionnalité web publique de preview d'Office365. Pour ce faire les documents sont rendus temporairement disponible pour Office 365 via un mécanisme d'URL avec un jeton à usage unique (donc pas réutilisable par un tiers ayant intercepté cette URL). Mais ça veut bien dire que le contenu document se retrouve, au moins temporairement, dans des composants Office365.

Il existe plusieurs solutions web/Java de prévisualisation de documents Office "locale" (i.e. coté serveur ou coté client) ou de conversion Office vers PDF mais le résultat est souvent de mauvaise qualité et les conditions d'usage et/ou les coûts de licence et/ou la lourdeur technique de ces produits (en tout cas ceux que nous avions étudiés à l'époque) ne nous ont pas permis d'en intégrer un en marque blanche dans la plateforme.

Si vous envisagez d'acquerir un tel produit tiers répondant à vos besoins et à vos contraintes il faudra qu'on regarde avec vous comment vous pourrez techniquement l'intégrer (ex: via une action client ou serveur ad hoc), voire s'il est possible de le "hooker" au niveau du bouton de preview des documents
