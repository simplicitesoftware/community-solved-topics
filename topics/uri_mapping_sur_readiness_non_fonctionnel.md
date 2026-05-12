# URI mapping sur readiness non fonctionnel

**URL:** https://community.simplicite.io/t/12143

## Question
### Request description

Bonjour,

Suite au passage à Simplicité 6.3 notre uri_mapping sur /readiness ne fonctionne plus.
Est-ce que readiness est un endpoint réservé pour le fonctionnement de Simplicité à présent ?
Je n'ai pas trouvé de mention de celui-ci dans la doc.

### Steps to reproduce
Sur une instance Simplicité 6.3 vierge avec uniquement le module de Démo :

1. J'ai créé un objet externe en accès public avec le paramétrage suivant :

![image|690x328](upload://sjFzL9KnerqhkKDPhGiCgqlUXwb.png)


Et le code (simplifié) suivant :

```
package com.simplicite.extobjects.Demo;

import java.util.*;

import org.json.*;

import com.simplicite.util.*;
import com.simplicite.util.exceptions.*;
import com.simplicite.util.tools.*;

/**
 * REST service external object DemoObservability
 */
public class DemoObservability extends com.simplicite.webapp.services.RESTServiceExternalObject {
	private static final long serialVersionUID = 1L;
	
	/**
	 * GET method handler (returns bad request by default)
	 * @param params Request parameters
	 * @return Typically JSON object or array
	 * @throws HTTPException
	 */
	@Override
	public Object get(Parameters params) throws HTTPException {
		if (getGrant().getEndpoint() != Globals.ENDPOINT_API) return forbidden(
	      "This service must be called on the API endpoint"
	    );
	
	    List<String> parts = getURIParts();
	    String service = parts.isEmpty() ? null : parts.get(0);
	    if (Tool.isEmpty(service)) return badRequest("Missing service name");
	
	    switch (service) {
	      case "liveness":
	        return liveness();
	      case "readiness":
	        return readiness();
	      default:
	        return badRequest("Unknown service: " + service);
	    }
		
	}
	
	private JSONObject liveness() {
        JSONObject livenessResult = new JSONObject();
        livenessResult.put("status", "test tnr");
        
        return livenessResult;
	}
	
	private JSONObject readiness() {
        JSONObject readinessResult = new JSONObject();
        readinessResult.put("simplicite", "test tnr");
    	readinessResult.put("database", "test tnr");
        
        return readinessResult;
	}
}

```

2. Dans le paramètre système "URI_MAPPINGS" j'ai mis cette configuration dans valeur remplacée :

```
[
    { "source": "^/liveness$", "destination": "/api/ext/DemoObservability/liveness" },
    { "source": "^/readiness$", "destination": "/api/ext/DemoObservability/readiness" },
    { "source": "^/testreadiness$", "destination": "/api/ext/DemoObservability/readiness" }
]
```

3. Un clear cache rouge.
4. Le mapping sur /liveness fonctionne bien :

![image|446x142](upload://5EfcjnjMl3rpldIV7hGtgO6XsUD.png)

5. Celui sur /readiness ne fonctionne pas : 

![image|615x172](upload://eOxp0hQFsOhhxY4fEmpw0FxI4gl.png)

6. Celui sur /testreadiness fonctionne :

![image|690x138](upload://gtyDaVK7zN5kJEA6dGkWPaLass5.png)


### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=6.3.8
Variant=full
BuiltOn=2026-04-24 11:37
Git=6.3/ff85b4c0a17da722a2460b21a0e6c9db3d1edb43
Encoding=UTF-8
EndpointIP=
EndpointURL=http://2b7c790b5098:8080
TimeZone=Europe/Paris
SystemDate=2026-04-28 16:35:31

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=http://localhost:8182
ActiveSessions=1
TotalUsers=7
EnabledUsers=5
LastLoginDate=2026-04-28 16:34:08

[Server]
ServerInfo=Apache Tomcat/9.0.117
ServerType=WEB
ServerDevMode=true
ServerCompiler=true
ServerActiveSessions=1
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=6.12.76-linuxkit
DockerImageName=almalinux9
SystemEncoding=UTF-8

[JavaVM]
Version=21.0.11
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=21.0.11+10-LTS
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=61345
HeapSize=251904
HeapMaxSize=503808
TotalFreeSize=313249

[Cache]
ObjectCache=221
ObjectCacheMax=10000
ObjectCacheRatio=2
ProcessCache=3
ProcessCacheMax=10000
ProcessCacheRatio=0
APIGrantCache=1
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
VendorName=postgresql
ProductName=PostgreSQL
ProductVersion=15.4 (Debian 15.4-2.pgdg120+1)
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.7.10
DBDate=2026-04-28 16:35:31
DBDateOffset=0
DBPatchLevel=6;P03;10095a693389d822b7e0090b69954f38;8
UsingBLOBs=true

[Healthcheck]
Date=2026-04-28 16:35:31
ElapsedTime=173

```
[/details]

## Answer
J'ai corrigé le swallowing abusif de `/r` en mettant une regex starts with `/r\\?`

Ca résout le pb mais la question c'était surtout de savoir si cette syntaxe "tiny" à la racine pour les resources avait un usage réel

A ma connaissance les autres tiny URL ne sont pas des URI racines mais des sous URI de `/ui`

La tendance du marché c'est de vouloir utiliser des URI racines arbitraires en fonction de normes "maison" correspondant plus ou moins à des "standard" de facto, il faut donc limiter au max notre consommation de ces URIs racine
