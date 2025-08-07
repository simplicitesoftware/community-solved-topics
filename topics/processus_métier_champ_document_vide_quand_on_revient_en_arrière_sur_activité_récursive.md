# Processus métier : champ document vide quand on revient en arrière sur activité récursive

**URL:** https://community.simplicite.io/t/7835

## Question
### Request description

Bonjour, 

J'ai un processus métier avec une activité qui posséde une transition d'état récursive. Au niveau de l'activité j'autorise l'utilisateur à revenir en arrière.

Je constate que quand on revient en arrière sur cette activité les champs type document sont vides alors qu'ils ont bien été complétés lorsqu'on est arrivé la première fois sur l'activité. Côté back tout semble ok, le champ document n'est pas vide et le document en question est bien présent dans la table m_document. Ca ressemble un problème côté front.


### Steps to reproduce

1. A partir du module de Démo, j'ai ajouté à l'objet DemoOrder un attribut type document.

![image|690x162](upload://hjgolJb8CXeugcMLfsrzt4W0GSI.png)


2. J'ai modifié le processus DemoOrderCreate afin d'ajouter une transition d'activité récursive sur l'activité OrderCreate.

![image|589x500](upload://xLAuyh8GUNh2q1CxOV3CPpBgKd6.png)

3. Sur l'activité OrderCreate j'ai autorisé le retour en arrière et la transition d'activité récursive appelle la méthode addNewOrderHandler que j'ai créé.

![image|690x275](upload://h8QrNlhgUtkfLY1HhSU0NbXeq8P.png)

4. J'ai ajouté le code suivant au processus DemoOrderCreate afin de gérer la transition récursive.

```
package com.simplicite.workflows.Demo;

import java.util.*;

import com.simplicite.bpm.*;
import com.simplicite.util.*;
import com.simplicite.util.exceptions.*;
import com.simplicite.util.tools.*;

/**
 * Process DemoOrderCreate
 */
public class DemoOrderCreate extends Processus {
	private static final long serialVersionUID = 1L;
	
	private static final String FIELD = "Field";
	private static final String ROW_ID_FIELD_NAME = "row_id";
	private static final String CREATE_ORDER_ACTIVITY_STEP = "ORDC-300";
	
	Stack<String> orderRowIdStack = new Stack<>();
	
	/**
	 * Méthode appelée par la transition d'activité OrderCreate -> OrderCreate.
	 * Permet d'ajouter à la stack orderRowIdStack le row_id 0 afin de forcer
	 * l'affichage du formulaire de l'objet Commande en création. Cf. postLock.
	 */
	public void addNewOrderHandler(ActivityFile pContext) {
		
		orderRowIdStack.push(ObjectField.DEFAULT_ROW_ID);
		
	}
	
	@Override
	public void postInstantiate(Grant g) {
		
		super.postInstantiate(g);
		
		orderRowIdStack = new Stack<>();
		
	}
	
	@Override
	public void postValidate(ActivityFile context) {
		
		super.postValidate(context);
		
		String step = context.getActivity().getStep();
		
		if (CREATE_ORDER_ACTIVITY_STEP.equals(step)) {
		
			String orderRowId = context.getDataValue(FIELD, ROW_ID_FIELD_NAME);
			
			// On ajoute le row_id de la commande créée à la stack pour
			// permettre à l'utilisateur de revenir en arrière avec le bouton
			// précédent. Cf. postLock.
			orderRowIdStack.push(orderRowId);
			
		}
		
	}
	
	@Override
	public void postLock(ActivityFile context){
		
		String step = context.getActivity().getStep();
		
		if (CREATE_ORDER_ACTIVITY_STEP.equals(step)) {
			
			// Si la stack est vide on affiche le formulaire de création
			// d'une commande (cas où on arrive pour la première fois sur
			// l'activité permettant de créer une commande).
			// Sinon on récupére le row_id de la commande que l'on doit
			// afficher pour que l'utilisateur puisse modifier une commande
			// déjà créé (via utilisation du bouton précédent). 
			// Si l'utilisateur crée des commandes en boucle, le row_id en haut
			// de la stack sera 0 (cf. addNewRowHandler).
			String orderRowId = orderRowIdStack.empty() ? ObjectField.DEFAULT_ROW_ID : orderRowIdStack.pop();
			
			context.setDataFile(FIELD, ROW_ID_FIELD_NAME, orderRowId); 
				
		}
		
	}
	
}

```

5. Ensuite j'utilise le processus afin de créer deux commandes. Lorsque je suis sur le formulaire de création d'une commande je mets bien un document dans le champ type document que j'ai ajouté.

6. Une fois la seconde commande créée, j'utilise le bouton précédent pour revenir sur ma première commande afin de la modifier. Je retrouve la commande telle que je l'avais créé mais le champ document est vide alors que je l'ai bien complété lors de la création et que d'après les logs de l'initUpdate le champ n'est pas vide.

Voici un vidéo du comportement que je constate, ça sera surement plus parlant ^^

![Simplicite_53_Processus_champ_doc_vide|video](upload://p0pqDvsThQYrYPuilw6eJz4u5O5.mp4)

Si besoin, voici le module de Démo avec mes modifications :

[Demo-5.1.tar.gz|attachment](upload://fF5OJGJ6aNP8Ue6M4JgvN6B9qq.gz) (1.7 MB)




### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=5.3.29
BuiltOn=2024-02-23 12:48
Git=5.3/9d1719fd313a86364994ba1f8eba3baa6719d2e5
Encoding=UTF-8
EndpointIP=172.24.0.3
EndpointURL=http://c3c8afa1e88d:8080
TimeZone=UTC
SystemDate=2024-02-29 10:58:17

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://10.24.160.176:5380
ActiveSessions=1
TotalUsers=8
EnabledUsers=5
LastLoginDate=2024-02-29 10:56:04

[Server]
ServerInfo=Apache Tomcat/9.0.86
ServerType=WEB
ServerActiveSessions=1
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=3.10.0-1160.108.1.el7.x86_64
DockerImageName=centos7
SystemEncoding=UTF-8

[JavaVM]
Version=17.0.10
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.10+7
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=159324
HeapSize=686080
HeapMaxSize=2007040
TotalFreeSize=1480284

[Cache]
ObjectCache=398
ObjectCacheMax=10000
ObjectCacheRatio=3
ProcessCache=398
ProcessCacheMax=10000
ProcessCacheRatio=3
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
VendorName=postgresql
ProductName=PostgreSQL
ProductVersion=13.14 (Debian 13.14-1.pgdg120+2)
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.7.2
DBDate=2024-02-29 10:58:17
DBDateOffset=0
DBPatchLevel=5;P03;147c106a661029519d5c89f711e6d10c
UsingBLOBs=true

[Healthcheck]
Date=2024-02-29 10:58:17
ElapsedTime=13
```
[/details]

## Answer
Le back n'envoyait que le row_id du document et pas les metadata associées (name, path, object, mime type...) en vue d'une mise à jour via action "back". 

Ce sera corrigé en 5.3.30.
