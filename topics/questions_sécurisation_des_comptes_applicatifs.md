# Questions sécurisation des comptes applicatifs

**URL:** https://community.simplicite.io/t/4662

## Question
Bonjour,

j'ai quelques questions concernant la sécurisation des comptes :

**1 - Robustesse des mots de passe**
Est-il possible de définir la longueur du mot de passe attendu par paramétrage ? et donc une modification de message d'erreur lors du renouvellement de mot de passe

**2 - Renouvellement de mot de passe**
Peut-on contraindre le renouvellement de mot de passe ? exemple : mot de passe à changer tous les 6 mois via une tâche planifiée du socle ?

**3 - Blocage de compte après tentatives infructueuses**
Peut-on bloquer un compte après N tentative de connexion ou N est un paramètre système ?

**4 - Blocage de compte pour absence d’usage**
Est-il possible de désactiver les comptes utilisateurs après une absence d’usage de N mois , N paramétrable via une tâche planifiée du socle ?

Merci

PS : Je pense que les points 2,3,4 sont gérables en spécifique et en paramétrage. Concernant le point, j'ai un doute

## Answer
1) oui on peut mettre toutes les règles relatives au format de password que l'on souhaite dans le platform hook [validatePassword](https://docs.simplicite.io/5/javadoc/com/simplicite/util/ScriptedPlatformHooks.html#validatePassword(com.simplicite.util.Grant,java.lang.String))
Ce hook permet de remonter N messages d'erreur pour expliciter la non vérification des règles

2) oui il suffit de forcer le param utilisateur `FORCE_CHANGE_PASSWORD` à `yes` par tâche planifiée ou autre

3) oui ça peut facilement s'implémenter dans le platform hook [preAuth](https://docs.simplicite.io/5/javadoc/com/simplicite/util/ScriptedPlatformHooks.html#parseAuth(com.simplicite.util.Grant,com.simplicite.util.SessionInfo)), cf. https://docs.simplicite.io/documentation/91-authentication/internal-auth.md#antibruteforce

4) oui la date de dernière connexion est stockée donc une tâche planifiée peut désactiver les users non connectés depuis une durée paramétrable

Pour aller plus loin, à partir de la 5.1 il est aussi possible de gérer une authent à 2 facteurs. Ca a été amélioré en 5.2 où c'est devenu paramétrable pour les différents types (OTP par mail/SMS ou TOTP par application d'authentification type Google/Microsoft Authenticator, ou 2FA custom) cf. https://docs.simplicite.io/documentation/91-authentication/internal-auth.md#2fahttps://docs.simplicite.io/documentation/91-authentication/internal-auth.md

La question n'a pas été posée mais l'algorithme de hashage du password est configurable (y compris avec un mécanisme de "salage" si besoin)

Cela étant dit, à nouveau, si on a des besoins très pointus en termes d'ident/authent, il vaut toujours mieux s'appuyer sur un produit externe 100% dédié à la gestion d'identité plutôt que l'ident/authent interne.

Pour mémoire Simplicité peut gérer par paramétrage des IdP SAML, OpenIdConnect (avec des fonctions avancées pour le cas KeyCloak), Crowd et gérer tout mode de connexion déléguée spécifique via les platforms hooks appropriés (LDAP, SSO, ...)
