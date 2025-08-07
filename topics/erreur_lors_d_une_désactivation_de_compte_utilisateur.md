# Erreur lors d'une désactivation de compte Utilisateur

**URL:** https://community.simplicite.io/t/4411

## Question
Bonjour,
Nous rencontrons une erreur "étrange" lorsqu'on cherche à suspendre une licence d'utilisateur : 
> 2022-02-15 17:47:02,684|SIMPLICITE|ERROR||http://siparex-simplicite-dev-745fcf686c-b58k5:8080||ECORED0001|designer|com.simplicite.webapp.ObjectDocument|displayFile||Erreur File from input stream
>     java.lang.NullPointerException: Cannot invoke "java.io.InputStream.read(byte[])" because "in" is null
>      at com.simplicite.webapp.tools.ServletTool.writeStream(ServletTool.java:2698)
>      at com.simplicite.webapp.ObjectDocument.displayFile(ObjectDocument.java:337)

Pouvez-vous nous aider, s'il vous plait ? 

[Platform]
Status=OK
Version=5.1.29
BuiltOn=2022-02-11 19:20
Git=release/771ad074cf3bf293da3a66e81b5b92cee875d00d
Encoding=UTF-8
EndpointIP=10.201.117.53
EndpointURL=http://siparex-simplicite-dev-745fcf686c-b58k5:8080
TimeZone=Europe/Paris
SystemDate=2022-02-15 17:51:44

Merci,
Ophélie

## Answer
Après parcours de votre instance, j'ai noté 2 choses :

- Vous avez d'autres objets qui héritent de SimpleUser dans vos modules et ils sont bien codés avec des  `getField("xxx").setVisibility(ObjectField.VIS_HIDDEN);`
donc sans changer la définition du champ xxx directement.

Visiblement vous ne partagez pas vos bonnes pratiques entre modules. 
Le champs usr_active ne doit pas rester en l'état invisible.

@Elcoco 
Merci de répondre quand ce sera fait.

- Il y avait un problème bloquant dans l'export du module "Evaluator"
Le Dataset attaché au module n'était pas exportable (upload d'un ZIP de taille nulle), nous avons dû le supprimer. Vous devez vérifier si votre dataset d'origine était trop gros ou corrompu.
