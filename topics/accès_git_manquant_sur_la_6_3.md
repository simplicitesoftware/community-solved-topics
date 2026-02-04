# Accès GIT manquant sur la 6.3

**URL:** https://community.simplicite.io/t/11518

## Question
### Request description

Bonjour,
Sur un environnement intialisé avec une image 6.3, je n'ai pas d'onglet Module commits visible sur mes modules (que ce soit mon projet ou par exemple Demo)

![image|442x500](upload://wUZbosNu1WYFt5TgJuNR8lAVCV.png)

Sur des environnements 6.2 migrés vers 6.3, nous n'avons pas ce souci.
Mon user a bien les groupes ADMIN et DESIGNER assignés à l'objet ModuleCommit, je ne sais pas que chercher d'autre.

Avez vous des pistes ?
Merci !
Emmanuelle

[Health check]

[Platform] Status=OK Version=6.3.2 BuiltOn=2026-01-30 20:34

## Answer
Merci pour ton retour rapide, je viens de trouver la cause tout simplement en ouvrant les logs car j'ai vu que les erreurs étaient loggées dans le start.sh ...
Et le répertoire git est granté à root et non à simplicite. 

![image|690x84](upload://aHVUiJElMmMpIOeblO63LUr9Joe.png)



Désolée pour le dérangement !
