# Créer une Custom action qui invoque l'action standard "copy"

**URL:** https://community.simplicite.io/t/5155

## Question
Bonjour,
je souhaiterai créer une "custom action" basée sur la fonction "copy" mais qui spécialise le comportement. Pour ce faire j'ai créé une action :que j'ai liée dans l'ui : 
![image|283x412](upload://by30FZl7H9wQs9lLgX8nvvQ5SFa.png)
j'ai créé une méthode qui positionne un paramètre de session exploitée dans la méthode initCopy pour différentier les comportements lors d'une copie. 
Enfin dans la custom action j'essai d'"invoker" l'action "copy" de la platefome. Cette approche ne semble pas fonctionner...., je vous partage le code  :


	public String newMinorRelease() {
		getGrant().setParameter("TYPE_OF_RELEASE", "Minor");
		ObjectDB obj = getGrant().getTmpObject("AS0ArchitectureStudy");
		obj.select(getRowId());
	
		try {
			 AppLog.warning("newMinorRelease:try ", null, getGrant());
			 String res = obj.invokeAction("copy");
                        return res;
            } 
         catch(Exception e) {
               return "Something went wrong";
            } 
         finally {
            
         }

	}

Merci pour votre aide
Frédéric

## Answer
Une action exposée via les APIs REST est nécessairement une action "serveur" (implémentée en Java)

Pour réaliser une copie il faut faire quelquechose du genre:

```java
try {
  obj.getTool().getForCopy(myRowId);
  (...)
  obj.getTool().validateAndSave();
} catch (Exception e) {
  (...)
}
```
