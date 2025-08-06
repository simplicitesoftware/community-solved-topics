# Conditionner une transition d'état à partir d'un attribut incorporé

**URL:** https://community.simplicite.io/t/5012

## Question
Bonjour,

Je voudrais conditionner un bouton de transition d'état sur la valeur d'un champ n'appartement pas à l'objet mais à un objet incorporé.
L'objet métier dossier pmfp a différents états et a un lien d'attribut incorporé de l'objet métier souhait/orientation, ce dernier objet a le champ qui devrait conditionner l'affichage de la transition.

J'ai essayé différentes écritures sans succès, en voici un exemple.

Condition sur la transition si le bouton eligibilité est à oui
![image|690x317](upload://auKKkrLq3EIWTiVlAWhGadyaLTz.png)
mais le bouton qui ne nomme accepté est absent
![image|690x199](upload://zglWsHj6nnaleZR4vv5ewTSap6d.png)

Le bouton rejeté n'a pas de condition pour l'instant mais devrait avoir l'opposé.

Merci pour vos retours
Thierry

## Answer
Bonjour Thierry, 

J'utiliserais le hook [isStateTransitionEnable(String fromStatus, String toStatus)​](https://docs.simplicite.io/5/javadoc/com/simplicite/util/ObjectDB.html#isStateTransitionEnable(java.lang.String,java.lang.String)) au niveau de l'objet PMFP, dans lequel j'irais vérifier la valeur du champ "éligibilité" de l'objet Souhait/Orientation lié.
