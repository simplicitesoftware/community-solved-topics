# Migration de 5.3.76 vers 6.2.15

**URL:** https://community.simplicite.io/t/10620

## Question
Bonjour,

Suite à la fermeture de ce topic [https://community.simplicite.io/t/migration-de-5-3-71-vers-6-script-rhino/10361/22](https://community.simplicite.io/t/migration-de-5-3-71-vers-6-script-rhino/10361/22) je rouvre celui car :

La migration de 5.3.71 vers 6.0.12 ne pose pas de problème en supprimant tout les script rhino de la table m_script_usage et l’applicatif tourne correctement aucun problème. Néanmoins si j’essaye de faire la même chose en passant de la 5.3.76 vers la 6.2.15 en java 21 je rencontre d’énorme problème.

Globalement l’applicatif ce lance correctement néanmoins aucune donné n’est accessible, c’est à dire que tout les menus s’affiche correctement mais que toute les listes sont vides alors qu’en bdd il y a de la donnée. Avec comme message d’erreur pour tout les objet non natifs simplicité :

```
WARN|designer|com.simplicite.util.engine.ObjectLoader|getClone||Evénement: Unable to clone the object MonObjet: read it from repository (slow access)
java.lang.NullPointerException: Cannot invoke "com.simplicite.util.ObjectDB.setData(com.simplicite.util.engine.ObjectData)" because "o" is null

```

De plus en designer je n’ai plus aucun bouton pour pouvoir créer des éléments dans ces listes.

Quelle est la conduite à tenir ?

Merci d’avance

## Answer
Indépendamment des tests d'import/upgrade que je n'ai malheureusement pas encore eu le temps de faire, j'ai fait le test de compilation de votre module en 6.2 et il y a bien des points à revoir:

![image|690x183](upload://nEF9cQk6nQyqfgobCpKzUQOofAP.png)

Ces erreurs correspondent au "breaking change" concernant la lib tierce PDFBox (passée de v2 à v3) intervenu en 6.1 (cf.  [release note de la 6.1](https://docs.simplicite.io/versions/release-notes/v6-1#compatibility-breaking-changes))

Il y a aussi le platform hook `isMenuEnable` qui a été supprimé en 6.1 (cf. la [release note de la 6.1](https://docs.simplicite.io/versions/release-notes/v6-1/#compatibility-breaking-changes)) qu'il faut donc refactorer

Vous devez résoudre ces points pour que votre module fonctionne en 6.2

Pour information, pour faire ce test préalable de compilation il faut modifier 2 choses dans le `pom.xml`:
![image|690x430](upload://vYAiIldVEYQ289RAnsFKU2ZF8fk.png)
![image|690x473](upload://bxxoACLKTfDZyqeYZuE1HG8KrcK.png)
et faire un `mvn -U clean compile` ou son équivalent dans un IDE Java.

Si vous n'avez pas accès à internet et donc pas aux repos Maven publics vous pouvez aussi faire pointer l'URL du repo Maven sur le `/maven` d'une instance 6.2 interne
