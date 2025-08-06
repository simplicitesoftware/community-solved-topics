# ActionException: No action

**URL:** https://community.simplicite.io/t/4410

## Question
Bonjour,

J'ai créé une nouvelle tâche Cron qui s'exécute tous les 17 du mois. J'ai associé une action à ma tâche Cron. Cependant, quand je clique sur "Exécuter la tâche immédiatement" dans le but de tester si tout fonctionne, j'obtiens l'erreur suivante:
![image|690x272](upload://svLuI2AZyKvYzUw3Pg9lVNYlOpE.png)

Voici mon Cron :
![image|690x175](upload://tITPsmWSc7KWhK3AXA5A8NiGxqA.png)

Voici mon action :
![image|690x252](upload://glFvFUxCvi4inyj7rq7ycOdYaTn.png)

Auriez-vous une idée de pourquoi ma tâche Cron ne reconnait pas mon action ?

## Answer
Il doit y avoir un pb de droits.

Si vous ne précisez pas explicitement de user "Run as" la tâche cron s'exécutera avec le user `system` (qui a les mêmes droits que `designer`)
