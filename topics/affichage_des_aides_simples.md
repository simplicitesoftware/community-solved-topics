# Affichage des aides simples

**URL:** https://community.simplicite.io/t/6928

## Question
Bonjour,

Les aides simples ne s’affichent pas pour certains écrans et s’affichent bien pour d’autres.
Exemple sur le module « démo » :
Elles s’affichent sur l’écran Attribut 
 
![image|690x311](upload://lytn1JCMr0ErPwnyU3S4SCT8Y1P.png)

Mais ne s’affichent pas sur l’’écran Traduction d’attribut : 
 
![image|690x278](upload://cUx4UcVgcE7O8t1eGnDtPD0m03u.png)

Merci d’avance pour votre aide.
Abed

[Platform]
Status=OK
Version=5.3.15
BuiltOn=2023-09-22 16:53
Git=5.3/662de91d19355d80e24aa899086313aba4159d89
Encoding=UTF-8
EndpointIP=149.202.173.228
EndpointURL=https://e3m.simplicite.io:10203
TimeZone=Europe/Paris
SystemDate=2023-09-25 12:56:18

## Answer
Il y avait un problème aléatoire d'initialisation des popovers, ils fonctionnent globalement mais parfois le "focus" ne le déclenche pas, avant on gérait le toggle par code mais on avait d'autre soucis, on a dû revenir à une ouverture par "focus" sur l'icone d'aide (accessibilité RGAA).

On a forcé l'init de ces aides par javascript lorsque le formulaire est chargé :

`$('[data-bs-toggle="popover"]').popover();`
