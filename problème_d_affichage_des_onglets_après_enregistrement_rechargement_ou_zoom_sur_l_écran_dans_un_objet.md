# Problème d'affichage des onglets après enregistrement, rechargement ou zoom sur l’écran dans un objet avec sous-objets intégrés

**URL:** https://community.simplicite.io/t/9406

## Question
### Request description

Bonjour,

Je rencontre un problème d’affichage des onglets dans un objet lorsque  certaines actions sont effectuées. Voici les détails :

### Steps to reproduce
### *Contexte*

* Mon objet principal contient plusieurs onglets pour organiser les données.
* Certains onglets intègrent des **sous-objets**.

*This request concerns an **up-to-date** Simplicité instance
and these are the steps to reproduce it:*

### *Problème observé*
1. **Après un rechargement ou un enregistrement** :

Si je navigue sur un onglet (par exemple, **"Description du traitement"**) puis que je clique sur **"Recharger"** ou **"Enregistrer"**, alors :
![image|690x195](upload://A75WacxSbVxyQsqRqCVGDb0BS4h.png)

  * L’onglet **"Informations générales"** devient actif, ce qui n’est **pas le comportement attendu** (seul l’onglet actif avant le rechargement devrait rester affiché).
  * L’onglet **"Description du traitement"** reste **en surbrillance** et est toujours actif.

![image|690x275](upload://kGvtDyiDkuGGk7KWpCwQS9UP73U.png)

  * Les contenus des deux onglets (**"Informations générales"** et **"Description du traitement"**) apparaissent **l'un au-dessus de l'autre sur le même écran**, créant une confusion visuelle.
![image|690x348](upload://qqUwJFHI4YjRRpU0WPVycBtXdeC.png)

2. **Après un zoom ou dézoom de l’écran** :

* Le problème survient également lorsque je change le niveau de zoom (CTRL + molette de souris ou CTRL + "+/-").
* Les deux onglets sont alors **simultanément en surbrillance**, et leurs contenus respectifs s'affichent à la suite.

3. Lorsque je retire les onglets contenant des sous-objets, le problème disparaît totalement, ce qui suggère probablement que le bug est lié à ces intégrations.

Voici les onglets contenant des sous-objets (Suivi de conformité et Notifications) : 
![image|690x343](upload://5ngIvt5hI4P13u30vCtm5JTMOQK.png)
![image|690x282](upload://eFhbqXXzdfeTfGV0xNjMmtBW7JF.png)

### **Questions**

1. Avez-vous déjà rencontré ce type de comportement avec des sous-objets intégrés dans des onglets ?
3. Existe-t-il une configuration ou un paramétrage natif pour forcer la gestion correcte des onglets après un rechargement ou un enregistrement ?
4. Y a-t-il des préconisations spécifiques pour intégrer des sous-objets dans des onglets sans perturber le comportement standard ?

Merci d’avance pour vos retours et vos suggestions !

Cordialement,
Elyass

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=6.1.18
BuiltOn=2024-12-17 12:35
Git=6.1/835d2f827019bc362da1d12d58775e0744609213
Encoding=UTF-8
EndpointIP=100.88.11.45
EndpointURL=http://bca-71077-app-98d6b5d4b-9t6n5:8080
TimeZone=Europe/Paris
SystemDate=2025-01-20 18:01:24

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://bcsi-legal-app.gke2.ope.gcp.renault.com
ActiveSessions=1
TotalUsers=13021
EnabledUsers=89
LastLoginDate=2025-01-20 17:50:27

[Server]
ServerInfo=Apache Tomcat/9.0.98
ServerType=WEB
ServerActiveSessions=1
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=6.1.112+
DockerImageName=almalinux9
SystemEncoding=UTF-8

[JavaVM]
Version=21.0.5
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=21.0.5+11-LTS
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=314164
HeapSize=481280
HeapMaxSize=2068480
TotalFreeSize=1901364

[Cache]
ObjectCache=115
ObjectCacheMax=10000
ObjectCacheRatio=1
ProcessCache=0
ProcessCacheMax=10000
ProcessCacheRatio=0
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
VendorName=postgresql
ProductName=PostgreSQL
ProductVersion=15.8
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.7.4
DBDate=2025-01-20 18:01:24
DBDateOffset=0
DBPatchLevel=6;P01;c3f2592da7f3cdd9b86409daaf7631f5;18
UsingBLOBs=true

[Healthcheck]
Date=2025-01-20 18:01:25
ElapsedTime=21
```
[/details]

## Answer
Bonjour,

Si vous n'avez pas besoin des listes filles, il faut effectivement les masquer.
On va surement devoir limiter le fonctionnement natif pour ne pas les afficher dans ce cas.

Attention toutefois, il est préférable de masquer la Vue/View qui contient le Link et non le Link lui-même. Car la vue sert à l'affichage uniquement et cela aura uniquement un impact sur la UI. 

Masquer le Link revient potentiellement à ne plus voir du tout la relation en back, y compris par exemple dans un export, ou un delete cascade.

De plus il n'est pas nécessaire de rechercher le lien, il y a des accesseurs par nom. Par exemple :

```java
boolean isPanel = isPanelOf("legalDataprocessAsDC") || isPanelOf("legalDataprocessAsSC");
View view = getView("RedoLog;rlg_object");
if (view!=null) 
  view.setVisible(isPanel);
```
