# Attribut d'action conditionné dans une transition d'état

**URL:** https://community.simplicite.io/t/9830

## Question
### Request description
Bonjour,

Je rencontre un problème sur une transition d’état dedans mon objet. J’ai associé à cette transition à une action dans laquelle je contrôle un champ date (attribut de l’action).

Dans cette action, je récupère un attribut de type date, et je vérifie côté back que la date saisie est **strictement supérieure à la date du jour**.

Si ce n’est pas le cas, je retourne un `return "Impossible : Choisissez une date supérieure à la date du jour"` pour **empêcher la transition**.

---

###  Comportement observé

* Le message d'erreur s’affiche bien côté front.
* **Mais la transition d’état se fait quand même**, et l’objet passe à l’état `VALIDATED`.

![image|690x233, 75%](upload://7uoh8pvrD4uK9buRxR6sDDZkQOZ.png)

---

### Indice que j’ai trouvé

Il semblerait que la **transition d’état soit effectuée avant même que l’action ne se termine**, ce qui expliquerait pourquoi elle passe malgré le `return` d’erreur.( Je le vois dans mes logs de début d'action lié à la transition). 

J'ai vu que plusieurs configurations peuvent être faites depuis la transition d'état qui réglerait mon problème mais je n'ai rien trouvé dans la Doc comment faire ses conditions de transitions sur une date par exemple( condition en RHINO ou autre ?)
 
![image|690x365, 75%](upload://rGH5ZONrybde2GJUStUnRhBYQhQ.png)


Merci d’avance pour vos retours !



### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=6.2.7
BuiltOn=2025-04-11 11:49
Git=6.2/5f5b1cec41cb5a57bc7fc607a1090ae50e325df4
Encoding=UTF-8
EndpointIP=100.88.227.11
EndpointURL=http://lbc-77449-app-76c78ff45f-kbz79:8080
TimeZone=Europe/Paris
SystemDate=2025-04-18 12:00:55```
[/details]

[details="Simplicité logs"]
```text
---paste the content of the **relevant** server-side logs---
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
Bonjour,

[quote="Hamza, post:1, topic:9830"]
je retourne un `return "Impossible`
[/quote]

C'est à dire dans quel hook ?

Ce genre de règle est a mettre au niveau du pre ou postValidate de l'objet.
Cela bloquera la mise à jour, le bouton d'action n'est qu'un moyen de faire une mise à jour du statut. Si la mise à jour était faite par API ou par code, ou directement depuis le champ statut... il faudrait avoir le même contrôle de date.

Si c'est une action de transition, on peut accéder aux paramètres de l'action depuis les hooks comme suit :

```java
FieldStateTransition tran = getCurrentTransition();
Action action = tran!=null ? tran.getAction() : null;
if (action!=null) {
	String param = action.getConfirmField("myField").getValue();
	if ... return error
}
```

https://docs.simplicite.io/docs/core/custom-actions-examples#state-transition-with-parameters
