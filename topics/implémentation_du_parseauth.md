# Implémentation du parseAuth

**URL:** https://community.simplicite.io/t/11635

## Question
Demande de support reçue par mail:

> Peux-tu nous indiquer où doit-on placer le parseAuth ?

`parseAuth` est un **platform hook** => ça se met dans une classe "shared code" dont le nom doit être ou commencer par `PlatformHooks`, ex:

```java
package com.simplicite.commons.MyModule;

import com.simplicite.util.AppLog;
import com.simplicite.util.Grant;
import com.simplicite.util.SessionInfo;

public class PlatformHooks extends com.simplicite.util.engine.PlatformHooksInterface {
	@Override
	public String parseAuth(Grant sys, SessionInfo info) {
		try {
			String login = info.getLogin();
			// Do something with login
			return login;
		} catch (Exception e) {
			AppLog.error(e, sys);
			return super.parseAuth(sys, info);
		}
	}
}
```

## Answer
[quote="JJB, post:10, topic:11635"]
`"sync": true,`
[/quote]

Il n'est pas impossible que la synchro et le `parseAuth` ne fassent pas bon ménage, dans un contexte où les users sont pré-créés la synchro n'a pas de raison d'être activée

Pouvez vous mettre `"sync": false` (ou ne pas le mettre du tout la valeur par défaut étant `false`) et retester

Merci de préciser la version exacte x.y.z de Simplicité que vous utilisez
