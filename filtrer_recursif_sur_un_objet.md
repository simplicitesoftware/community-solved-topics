# Filtrer recursif sur un objet

**URL:** https://community.simplicite.io/t/6949

## Question
### Request description

Dans le but de transférer les information d'un dossier vers un autre, on souhaiterai ajouter un filtre, afin 
de retirer l'objet de la vue (celui qui est chargée via le init update) de la recherche pour éviter de faire un transfert vers lui même

### Technical information
On a essayé de passer par un tmpObject dans le init update qui est ensuite regardé dans le presearch avec un test associé sur le isRefInstance.

Mais cela cause deux problème le premier étant que la première visualisation le filtre ne s'applique pas, il faut quitter et revenir, le tmp object étant mis en fin du initUpdate qu'est-ce qui pourrait poser problème ?
Le second étant que le filtre reste présent dans les autre recherche avec des loupes, depuis d'autre objet ayant une recherche sur un dossier.

Auriez-vous des solutions à me proposer ?

On est en 5.3.15

Merci de votre attention.

## Answer
Bonjour,

Pour résumer si j'ai bien compris, vous souhaitez pouvoir sélectionner une référence de dossier qui n'est pas lui-même dans un écran particulier, mais pas pour toutes les références vers un dossier.

Il y a un hook `initRefSelect` qui permet d'agir sur l'instance isRefInstance utilisée par le popup de sélection directement.

Exemple à mettre dans l'objet sélectionné, pour ne pas sélectionner le même row_id :

```java
@Override
public void initRefSelect(ObjectDB parent) {
	if (parent!=null && "MyObject".equals(parent.getName())) {
		setSearchSpec("t.row_id <> " + parent.getRowId());
	}
	super.initRefSelect(parent);
}
```

MyObject pouvant être l'objet Dossier lui-même dans le cas d'un lien réflexif, ou un objet pointant sur la même table de dossier (même row_id), sinon il faut revoir le filtre sur la clé fonctionnelle du dossier et non son row_id technique.

Sans modèle logique sur vos objets/relations, il est difficile de vous aider plus précisément.

A noter : on peut aussi spécialiser ce hook, en fonction de la foreign-key en testant la valeur de `getParentObjectRefField()`, quand plusieurs liens mènent au même objet et le nom de l'objet parent seul est ambigu.
