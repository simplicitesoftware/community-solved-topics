# Appliquer un filtre sur l'autocomplétion d'un champ lorsqu'on est dans le panneau de recherche

**URL:** https://community.simplicite.io/t/6416

## Question
### Request description

Bonjour,

Sur un objet A j'ai une référence qui pointe vers un autre objet B. 
Dans le formulaire de l'objet A, lorsque l'utilisateur utilise l'autocomplétion ou la loupe il doit avoir accès uniquement aux lignes actives de l'objet B. Pour mettre en place ce filtre j'ai utilisé le hook initRefSelect. Le filtre fonctionne correctement dans les formulaires mais pas dans le paneau de recherche ou ce dernier fonctionne uniquement quand on clique sur la loupe, quand on utilise l'autocomplétion le filtre n'est pas pris en compte.

### Steps to reproduce

1. J'ai installé le module de Démo
2. Au niveau du code Java de l'objet "DemoSupplier" j'ai ajouté le code suivant :

```
package com.simplicite.objects.Demo;

import java.util.*;

import com.simplicite.util.*;
import com.simplicite.util.exceptions.*;
import com.simplicite.util.tools.*;

/**
 * Business object DemoSupplier
 */
public class DemoSupplier extends ObjectDB {
	private static final long serialVersionUID = 1L;
	
	@Override
	public void initRefSelect(ObjectDB parent) {
		
		super.initRefSelect(parent);
		
		AppLog.warning("DEBUG 2305 / initRefSelect / instanceName: " + getInstanceName(), null, null);
		
		setSearchSpec("sup_name = 'actif'");
		
	}
	
	@Override
	public void preSearch() {
		
		super.preSearch();
		
		AppLog.warning("DEBUG 2305 / preSearch / instanceName: " + getInstanceName(), null, null);
		
		//setSearchSpec("sup_name = 'actif'");
		
	}
	
	
}

```

3.  Dans le PlatformHooks j'ai le code suivant :

```
package com.simplicite.commons.Demo;

import java.util.*;

import com.simplicite.util.*;
import com.simplicite.bpm.*;
import com.simplicite.util.exceptions.*;
import com.simplicite.util.tools.*;

/**
 * Platform Hooks
 */
public class PlatformHooks extends com.simplicite.util.engine.PlatformHooksInterface {
	
	@Override
	public String preSearchIndex(Grant g, String search) {
		
		AppLog.warning("DEBUG 2305 / preSearchIndex", null, null);
		
		return search;
		
	}
	
	@Override
	public List<SearchItem> postSearchIndex(Grant g, List<SearchItem> rows) {
		
		AppLog.warning("DEBUG 2305 / postSearchIndex", null, null);
		
		return rows;
		
	}
	
}

```

4. J'ai créé les 3 suppliers suivants, j'utilise le champ "name" pour savoir si le supplier est actif ou non :

![image|690x213](upload://sUO8r22FslKuTGkrrGFXw9KBDlE.png)


5. Quand je crée un produit, au niveau du champ "Supplier code" l'autocomplétion me propose bien que les suppliers "actif" :

![image|690x170](upload://7Rh3XHUWSQZd1rHrC7aMa8QK20R.png)

Idem quand on passe par la loupe :

![image|690x183](upload://hqloqdIj0L7wVW9uNkP9uzWhDzX.png)

6. Je vais sur la liste des produits, je clique sur la loupe pour pouvoir appliquer un filtre, puis sur la loupe au niveau du champ "Supplier code" :

![image|690x241](upload://ynmQRRqLtdPnln4RUD2FcLM2OfA.png)

7. La liste propose bien les suppliers actifs uniquement :

![image|690x188](upload://iyckADmM9vqqCaLfuRas905cqCa.png)

8. Par contre si j'utilise l'autocomplétion, la liste me propose C01 et C02 au lieu de C01 et C03 :

![image|690x156](upload://hSFe79rbBQXQ75D9RJM18dSPEPQ.png)




### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=5.2.40
BuiltOn=2023-05-16 15:59
Git=5.2/86fffedebb118d8596f5e819c02cb176332760d0
Encoding=UTF-8
EndpointIP=
EndpointURL=
TimeZone=UTC
SystemDate=2023-05-23 09:56:01

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=
ActiveSessions=1
TotalUsers=7
EnabledUsers=5
LastLoginDate=2023-05-23 09:46:13

[Server]
ServerInfo=Apache Tomcat/9.0.75
ServerType=WEB
ServerActiveSessions=1
ServerSessionTimeout=30

[OS]
Name=Linux
Architecture=amd64
Version=5.15.90.1-microsoft-standard-WSL2
DockerImageName=centos7
SystemEncoding=UTF-8

[JavaVM]
Version=17.0.7
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.7+7
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=142647
HeapSize=422912
HeapMaxSize=489472
TotalFreeSize=209207

[Cache]
ObjectCache=237
ObjectCacheMax=10000
ObjectCacheRatio=2
ProcessCache=11
ProcessCacheMax=10000
ProcessCacheRatio=0
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
ProductName=PostgreSQL
ProductVersion=13.11 (Debian 13.11-1.pgdg110+1)
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.6.0
DBDate=2023-05-23 09:56:01
DBDateOffset=0
DBPatchLevel=5;P02;03426763fd1f2419a73b6fb3361e94a1
UsingBLOBs=true

[Healthcheck]
Date=2023-05-23 09:56:01
ElapsedTime=157
```
[/details]

## Answer
Ok en fait rien à voir, j'ai confondu.

Cette completion de la recherche fait un "select distinct" en base des valeurs connues en base pour cette colonne ramenée dans l'objet Produit.
Ce n'est pas une recherche de référence qui passe par le hook initRefSelect, mais une aide à la saisie des valeurs qui existent déjà et qu'on peut rechercher = on complete le libellé et non pas une foreign-key caché.

Ca explique pourquoi ça remonte C01 et C02 qui doivent exister dans la table des produits comme fournisseurs référencés.

Par contre la loupe est bien un reference picker.

Pour surcharger/modifier ce que remonte le `fieldCompletion(field,query,context,values)` du produit, il faut utiliser le hook de même nom :
- par défaut s'il renvoit null = ça cherche les valeurs distinctes en base pour cette colonne
- s'il renvoit liste vide = pas de completion
