# La modification d'un champ de obligatoire à non obligatoire ne fonctionne pas

**URL:** https://community.simplicite.io/t/3267

## Question
Bonjour,

La modification de configuration de plusieurs champs n'est pas prise en compte.

J'ai réessayé plusieurs fois la manip et vider le cache à chaque fois mais il y a un pb entre le caractère obligatoire des champs 'exemple le nom qui est indiqué dans la page,
![image|690x171](upload://hmZBL8tbsTaDBvREvcqB94W55Fe.png) 

et l'attribut (en cliquant dessus) ou c'est indiqué que le champ n'est pas obligatoire.
![image|690x183](upload://l1E3DKnc3KXIKc8i1OuCnLOsjMb.png) 

J'ai mis à jour le champ depuis le template sans succès, puis depuis les propriétés d'attributs sans succès non plus.

J'ajoute une copie attribut et attribut d'objet d'un des champs (Nom)

![image|690x136](upload://JK12YjjzBaqSUAR2wc9CObvZvD.png) 

![image|690x192](upload://ybFMvApnLfh0C5LwE4V8rsCaodr.png) 

image ou l'on voit dans le template le caractère non obligatoire 

![image|690x183](upload://wZiQcFimvlf5oL5yfIr5gG5L7h3.png) 

Version
[Platform]
Status=OK
Version=5.0.33
BuiltOn=2021-03-29 14:25
Git=release/41b919e90f91560284f40f620adc7e31c83149d8
Encoding=UTF-8
EndpointIP=172.18.0.2
EndpointURL=http://e241eaeed345:8080
TimeZone=UTC
SystemDate=2021-05-05 12:07:06

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=http://localhost:81
ActiveSessions=2
TotalUsers=11
EnabledUsers=10
LastLoginDate=2021-05-05 11:55:08

[Server]
ServerInfo=Apache Tomcat/9.0.44
ServerType=WEB
User=root

[OS]
Name=Linux
Architecture=amd64
Version=5.10.25-linuxkit
SystemEncoding=UTF-8

## Answer
OK. Mettez vous quand même à jour car il vous manque près de 70 commits, essentiellement du correctif. Cf la [release note](https://docs.simplicite.io/5/releasenote/releasenote-5.0.md#version-5.0.33)
