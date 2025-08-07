# Acknowledge d'un import de module OK ou KO dans les logs

**URL:** https://community.simplicite.io/t/6140

## Question
Bonjour,

Sur un serveur Azure, lorsque nous importons un module important dans simplicité, nous rencontrons un message d'erreur 499 ou 504 alors que l'import est en cours.

Ce message vient d'Azure lui-même, qui, au bout d'un certain temps (120s environ), indique que la connexion client-serveur s'est interrompue car faute de réponse d'une des deux parties.

Si l'on quitte la pop-up d'erreur, l'écran n'est plus grisé et la pop-up "Import OK/KO" n'apparait plus.

Existe-il une trace dans les logs qui indiquerait l'état final de l'import, mis à part le déclenchement des CRON toutes les 5 min présumant le fait que le traitement d'import est fini ?

## Answer
Bonjour,

Une erreur 504 est un timeout HTTP qui visiblement est de 2 minutes dans votre environnement.
Ce n'est pas bloquant, c'est juste que le client ne peut plus recevoir la réponse (le popup ok/ko final) en fin de traitement côté back.

Augmenter ce timeout si vous en avez la possibilité.

Sinon vous devez alors aller dans le menu **Opération / Supervision des imports** pour voir les logs et le statut de cet import quand il sera terminé avec son temps.

En 5.4 (version alpha qui sera la V6), l'import et l'export de module seront asynchrones avec un popup qui affichera l'avancement du traitement via la nouvelle fonctionnalité des Actions via le paramètre AsyncTracker.

![image|405x500](upload://bIMy3CUvq6bBkRYD4R8NJ12PB7w.png)
https://docs.simplicite.io/5/releasenote/releasenote-5.4.md
