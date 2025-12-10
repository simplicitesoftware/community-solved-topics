# LOG trop volumineuse pour faire une analyse : occurences de lignes à supprimer

**URL:** https://community.simplicite.io/t/11045

## Question
Bonjour,

Nous rencontrons actuellement un incident bloquant sur Vision360 concernant le fichier de log, qui est devenu extrêmement volumineux et difficile à analyser.

Une très grande quantité de lignes (environ 150 000) proviennent de messages internes Simplicité liés à l’objet de traduction **m_translate** :

```
delete from m_translate where row_id=
-- dead link detected m_translate.tsl_id /
```

Ces messages semblent issus d’un traitement interne Simplicité (cleanup / tâches planifiées / gestion des liens orphelins sur m_translate).

Pouvez-vous svp vérifier de votre coté?

On parle de l’instance de **PROD** de Vision36O.

Merci pour votre support.

Cordialement,
Safae

## Answer
[quote="Safae_Safari, post:4, topic:11045"]
Version=5.3.66
[/quote]

Vous n'êtes donc pas à jour. Comme déjà indiqué ce pb de log a été corrigé (pas de bol en 67).

cf release note :

### 5.3.67 (2025-04-11) - maintenance revision {#version-5.3.67}
- Inhibited "dead links" design audit checks on the translation table to avoid potential false positives

Il faut donc vous mettre à jour, pour éviter de nous remonter des pb déjà corrigés. 
- Toute demande de support sur une branche en LTS nécessite forcement d'être à jour puisqu'un éventuel correctif sera fait sur la branche à jour 
- Inhiber la cron n'est qu'un contournement.
