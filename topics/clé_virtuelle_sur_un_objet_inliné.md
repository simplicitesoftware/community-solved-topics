# Clé virtuelle sur un objet inliné

**URL:** https://community.simplicite.io/t/11381

## Question
### Request description

Bonjour,

Me revoilà avec un cas aux limites sur les objets inlinés : j'ai un objet A avec un lien classique vers un objet B et un lien inliné vers un objet C.

![image|690x267, 75%](upload://AeDKrKWeefp9PYiLPDEupUd3y5L.png)

![image|690x255, 75%](upload://rLhCfJ6qqd6BtkD1mme8gYrFUlY.png)

J'ai créé une clé virtuelle (B -> A -> C) entre B et C et l'ai mise en inliné aussi.

![image|690x259, 75%](upload://768oHxSNvGSPAIvDpPENoXtVsWq.png)


Mon souci est que quand j'affiche B, l'objet ramené est le premier de la liste et non celui correspondant à la clé virtuelle.

![image|690x457, 75%](upload://g5YViQehiXWHgj6MQyU68iFvfBO.png)
*Onglet C sur le form de A, row_id = 9 (correct)*


![image|690x294](upload://qyNOger9pkqBW5n0rwpfHmOCbq1.png)
*Onglet C sur le form de B, row_id = 11, c'est à dire le premier ramené par le search*

Dans *network*, je vois que le search des objets inlinés avec clé physique ramène bien une seule ligne, mais celui avec clé virtuelle ramène toute la table.
J'ai aussi testé la clé virtuelle sans l'option inliné et j'ai bien la bonne ligne.

![image|679x475, 50%](upload://2tfFpg1VQIiNE3VfWIxHzUOa0b3.png)
*Search avec clé virtuelle inlinée : renvoie une ligne*

![image|506x500, 50%](upload://xJhtIm4uT4GsOEs23El0qKYSrcm.png)
*Search avec clé virtuelle non inlinée : renvoie une ligne*

![image|690x470, 50%](upload://tw8XBLnbM0Q70JaxHSkliOq5lWy.png)
*Search avec clé physique inlinée : renvoie toute la table*

Est-ce que ce paramétrage virtuel + inliné est possible ?
Sinon, je peux persister la clé en champ calculé.

Merci d'avance pour votre aide !
Emmanuelle

[Platform]
Status=OK
Version=6.2.20
BuiltOn=2026-01-02 22:59

## Answer
Il manquait le parent lors du search de l'objet inliné, ce qui explique les différences de payload entre les deux requêtes.

Dans le module Demo, j'ai paramétré un lien virtuel entre DemoSupplier et DemoOrder :
![image|690x319](upload://tWianoCKtSLfciKQxLuwqoV9ZeI.png)

Sur le formulaire d'un Fournisseur : 
![image|690x439](upload://2rVCSxQAbfvhJ8hJPpTyGgBntbd.png)

La commande 2 (row_id=2) correspond bien au ROWID du Fournisseur parent.

Ça sera corrigé en [6.2.21](https://docs.simplicite.io/versions/release-notes/v6-2/#version-6.2.21)
