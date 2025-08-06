# Contrainte champ obligatoire sur un multi-Doc

**URL:** https://community.simplicite.io/t/4854

## Question
### Problem description

Bonjour, 
Nous essayons de rendre obligatoire un champ de type multidoc lors d'une transition d'état

### Steps to reproduce

Nous avons testé deux solutions : 
A. Par le code 
 En utilisant le hook pre-update, et en vérifiant la condition suivante : 
```
if ((getOldStatus().equals("INIT") && getStatus().equals("COMPLETED")) ||(getOldStatus().equals("LACK_INFOS") && getStatus().equals("COMPLETED")) ){
			//si au moins un doc n'est pas chargé, alerte
                        //vérification de ce que ressort la méthode "getDocuments"
			AppLog.info("===================doc="+	getField("evlValReporting").getDocuments(this, getRowId()), Grant.getSystemAdmin());
			if(getField("evlValReporting").getDocuments(this, getRowId())==null ) {
				 return Message.formatError("EVL_ERROR_COMPLETION", "Merci de compléter le Compte de résultat.", "evlValReporting");
```

La partie AppLog.info ressort ceci, bien qu'un doc a été chargé. La contrainte par le "if" n'est donc pas appliquée

> `===================doc={"size":0,"contenttype":""}`

B. Par les contraintes
1. Nous avons créé une contrainte BackEnd
![image|690x316](upload://slCLLXn0LKEVGs44mSx5zazTS3l.png)

2. Lorsqu'on teste la contrainte elle fonctionne, seulement le message d'erreur est le suivant :
![image|569x500](upload://5ry4ymUu43KLgfLvUsyNYlFL4A1.png)

On perd la fonctionnalité qui nous indique quel champ nécessite d'être renseigné + son emplacement. 

Nous avons fait le test pour un doc simple, cela fonctionne parfaitement. 

On détecte donc deux problématiques sur l'utilisation des multidoc : 
1. La méthode getDocuments ne retournent rien, même si au moins un document est renseigné. Elle n'est donc pas exploitable. D'ailleurs cette méthode n'est pas dans la javadoc, bien qu'elle apparaisse ici : [Doc simplicité](https://docs.simplicite.io/documentation/01-core/documents-code-examples.md)

1. L'utilisation des contraintes sur des champs multidoc ne reproduit pas le même comportement que pour des champ "simple" document. 

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.2.2
BuiltOn=2022-04-29 15:38
Git=5.2/a2c69b2ee78658770a248e617730e607252990ca
Encoding=UTF-8
EndpointIP=10.201.58.66
EndpointURL=http://siparex-simplicite-dev-777bcd4cfc-dqxdr:8080
TimeZone=Europe/Paris
SystemDate=2022-05-13 12:00:17
```
[/details]

[details="Simplicité logs"]
```text
> `===================doc={"size":0,"contenttype":""}`
```
[/details]

[details="Browser logs"]
```text
RAS
```
[/details]

[details="Other relevant information"]
RAS
[/details]

## Answer
Les changements ont été faits et seront poussés au prochain build 5.2.4

- Fixed: required multi-doc message displayed on field
- New methods: 
    - **`ObjectField.loadDocuments`** : confusing `ObjectField.getDocuments` is deprecated and replaced by `loadDocuments`
    - **`ObjectField.getListOfDocuments`** : return a list of documents if field is multi-doc (or null)

et le `toString` d'un document multiple retournera un tableau JSON.
