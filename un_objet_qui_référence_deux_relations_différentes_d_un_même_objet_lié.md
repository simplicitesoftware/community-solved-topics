# Un objet qui référence deux relations différentes d'un même objet lié

**URL:** https://community.simplicite.io/t/3408

## Question
![Capturea|690x409](upload://vhmAQZphUfTIxSHucLWs1zCOIU4.png)
Bonjour,

Dans le code de l'objet, quand on fait l'initRefSelect pour faire une sélection de la relation A : characBusnObjLinkedId (voir la capture ci-jointe), le getParentObjectRefField nous renvoie characBusnObjId (B), sachant qu'on a pas les mêmes règles métier qui encadrent ces deux relations ...... du coup on est bloqué.

version 4.0.P25.fc264504a796dafe39e855086c681bc359140df6

Merci.
Yacine

## Answer
[quote="yacinekheddache, post:1, topic:3408"]
getParentObjectRefField
[/quote]

Bonjour,

Je ne reproduis pas le problème sur une V4 à jour.

```java
	@Override
	public void initRefSelect(ObjectDB parent)
	{
		String ref = getParentObjectRefField();
		// ...
		super.initRefSelect(parent);
	}
```

Par exemple pour un Profile de Simplicité (N,N entre 2 groupes), si on met ce code dans l'objet Group, la référence est bien le champ :
- prf_profile_id
- ou prf_group_id

suivant le popup Group qu'on ouvre
