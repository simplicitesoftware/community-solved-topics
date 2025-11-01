# Erreur de compilation hookBegin

**URL:** https://community.simplicite.io/t/10942

## Question
### Request description

*Bonjour,*

j’ai une erreur de compilation lorsque j’essaye d’implémenter le hook de la documentation dans un objet du module Démo : 

![image|690x205](upload://yv3a8pdAV9L89jcA8culdOru9gN.png)

Message de la pop-in du code editor : 

```
Java compilation error (status 1)
/usr/local/tomcat/webapps/ROOT/WEB-INF/src/com/simplicite/objects/Demo/DemoProduct.java:40: error: method does not override or implement a method from a supertype
  @Override
  ^
/usr/local/tomcat/webapps/ROOT/WEB-INF/src/com/simplicite/objects/Demo/DemoProduct.java:47: error: reference to hookBegin is ambiguous
    super.hookBegin(hook, maxTime, maxStack);
         ^
  both method hookBegin(String,int,int,Object...) in ObjectCore and method hookBegin(String,Object...) in ObjectCore match
2 errors
```

PS: je ne retrouve plus le tableau avec l’ordre des hooks dans la documentation. Il me semblait qu’elle était dans la partie Tutoriel

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=6.2.15
BuiltOn=2025-08-15 11:39
Git=6.2/309efbdf46b217e3145711d1c47c3e5ad5459aa5
Encoding=UTF-8
EndpointIP=100.88.242.57
EndpointURL=http://lbc-77449-app-7bbc4db5bc-9dbht:8080
TimeZone=Europe/Paris
SystemDate=2025-10-31 09:41:50

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://ldm-app.ext.gke2.dev.gcp.renault.com
ActiveSessions=1
LastLoginDate=2025-10-31 09:19:06

[Server]
ServerActiveSessions=9
ServerSessionTimeout=30
CronStarted=true

[JavaVM]
HeapFree=202654
HeapSize=573440
HeapMaxSize=3758080
TotalFreeSize=3387294

[Cache]
ObjectCache=213
ObjectCacheMax=10000
ObjectCacheRatio=2
ProcessCache=0
ProcessCacheMax=10000
ProcessCacheRatio=0
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Healthcheck]
Date=2025-10-31 09:41:50
ElapsedTime=8
```

[/details]

[details="Simplicité logs"]
```text
Java compilation error (status 1)
/usr/local/tomcat/webapps/ROOT/WEB-INF/src/com/simplicite/objects/Demo/DemoProduct.java:40: error: method does not override or implement a method from a supertype
  @Override
  ^
/usr/local/tomcat/webapps/ROOT/WEB-INF/src/com/simplicite/objects/Demo/DemoProduct.java:47: error: reference to hookBegin is ambiguous
    super.hookBegin(hook, maxTime, maxStack);
         ^
  both method hookBegin(String,int,int,Object...) in ObjectCore and method hookBegin(String,Object...) in ObjectCore match
2 errors
```

[/details]

[details="Browser logs"]
```text
---paste content of the **relevant** browser-side logs---
```

[/details]

[details="Other relevant information"]
*----E.g. type of deployment, browser vendor and version, etc.----*

[/details]

## Answer
La documentation (et le snippet de l'éditeur de code) n'était pas à jour, la signature de cette méthode est:

```java
@Override
protected void hookBegin(
    String hook,
    int maxTime,
    int maxStack,
    Object... args)
  throws HookException
{
    // ...		
}
```

C'est corrigé au niveau de la doc. Ce le sera au niveau du snippet dans la prochaine révision 6.2.18 qui sera releasée aujourd'hui.
