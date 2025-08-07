# Export CSV plus long

**URL:** https://community.simplicite.io/t/6452

## Question
Bonjour,

Suite à notre passage en version 5.2 le 09/05, nous avons remarqué une augmentation du temps de traitement concernant la génération de fichier CSV.

La fonctionnalité en cause, utilise massivement cette méthode : [CSVTool](https://docs.simplicite.io/5/javadoc/com/simplicite/util/tools/CSVTool.html#export(com.simplicite.util.ObjectDB,java.util.List,java.lang.String,java.lang.String,boolean,java.io.PrintWriter))

Y a-t-il eu des changements la concernant entre la 5.1 et la 5.2 ? (Le but étant d'évincer une piste si ce n'est pas le cas)

L'utilisation de cette méthode est elle toujours en 5.2 la plus efficace niveau temps de traitement ?

Merci d'avance pour vos retours,

Benoît

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.2.38
BuiltOn=2023-04-20 10:56
Git=5.2/66dd3f848850f0ba670a5f92674282285b3d3341
Encoding=UTF-8
TimeZone=Europe/Paris
SystemDate=2023-05-30 10:47:56
```
[/details]

## Answer
Ok on a trouvé le problème en passant dans le JobQueue.push.

A mon avis c'est lié à un correctif suite à une remontée SonarQube. 

- Avant chaque worker faisait un `run()` du thread/runnable = appel bloquant, mais faire un run ce n'est pas exécuter le cycle de vie du Thread, c'est juste un appel à la méthode run, c'est mal.
- Ca a été remplacé par un `start()` qui lance le thread proprement de manière asynchrone mais du coup ça redonne la main au worker qui continue de dépiler trop vite !

On va ajouter un `join()` pour bloquer le worker et attendre la fin de la tache avant de dépiler la suivante.

![image|368x390](upload://z4oV6ZnIdxcUESbtI7jmR7AS2mr.png)

J'ai utilisé un Thread.sleep(30s)  dans l'exemple à la place de l'export.
On voit bien que les taches sont dépilées 10 par 10.
Ce sera poussé dans une prochaine révision.
