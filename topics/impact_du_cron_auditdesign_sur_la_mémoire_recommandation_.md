# Impact du cron AuditDesign sur la mémoire : recommandation?

**URL:** https://community.simplicite.io/t/11034

## Question
Bonjour,

Nous avons constaté que le cron job **AuditDesign**, exécuté quotidiennement, consomme une quantité importante de ressources serveur pendant environ **2 heures**. Lorsque cette exécution coïncide avec une période de forte activité (nombreux appels API provenant de systèmes connexes), la mémoire n’est quasiment pas libérée : elle continue de monter jusqu’à atteindre la limite de heap max, ce qui entraîne ensuite des lenteurs, et à fortiori un crash du serveur.

*Cette surcharge génère également un volume important de logs relatifs.*
Ceci dit, nous n’exploitons pas (encore) les rapports quotidiens de cet audit.

Dans ce contexte, serait-il judicieux — ou au moins acceptable — de **réduire sa fréquence à une exécution hebdomadaire**, par exemple le dimanche, afin d’obtenir un état global de la semaine tout en limitant la charge serveur ?

Merci d’avance pour votre retour.

*Version Simplicité : 5.3.52*

## Answer
En production vous pouvez inhiber l'audit via les paramètres systèmes ad hoc car son intérêt est plutôt en phase de développement/recette (autrement dit, ce que vous livrez en production est sensé avoir déjà été dument audité donc il ne sert à priori à rien de le ré-auditer en production):

![image|690x181](upload://jiQUypIR5ZxQUO5SFl6IBjxhcon.png)
