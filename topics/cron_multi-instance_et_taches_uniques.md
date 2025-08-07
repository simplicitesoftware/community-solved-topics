# CRON multi-instance et taches uniques

**URL:** https://community.simplicite.io/t/5011

## Question
Simplicité 5.1.44

Bonjour,

On constate qu'en environnement multi instance la modification de paramètrage de CRON n'est pas propagée. Y'a-t-il une configuration supplémentaire à faire pour que ces changements soient propagés à chaud sur les autres instances simplicité ?

Aussi, comment s'assurer que le CRON ne se lance qu'une seule fois et pas sur chaque instance ?

Merci d'avance.

## Answer
J'ai fait un rechargement des logs hier soir. Effectivement, je n'avais pas vu qu'il affichait le planning dans les logs.
On constate bien que les 4 concernées sont aux abonnés absents.

Je vais recharger les CRON de ce pas et voir si la liste est complète pour cette nuit.

Merci pour votre piste.
