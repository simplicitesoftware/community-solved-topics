# Clear Cache sur instances multiples

**URL:** https://community.simplicite.io/t/4970

## Question
Simplicité 5.1.44

Bonjour, ce ticket fait suite à celui ci : 
https://community.simplicite.io/t/modification-de-parametre-applicatif/4402

On se rendait  compte que les clearcache n'était pas forcément pris en compte et la cause est simple : nous avons plusieurs instances Simplicité sur une même base de données. Quand on fait le clearcache serveur sur l'instance A suite à la modification d'un paramètre, comment propager le clearcache sur les instance B, C ... ?

## Answer
Oui `set/getParameter` = en mémoire dans le cache et `set/getSystemParam` = directement en base

Mais vous pouvez aussi simplement utiliser votre objet métier qui hérite de `SystemParam` pour faire les appel en base

Un pattern qui vous oblige à faire un clear cache pour répondre à un besoin métier n'est clairement pas une bonne approche, un clear cache est une opération d'exploitation ou de maintenance ponctuelle.
