# Ajouter une contrainte de visibilité sur un attribut d'action

**URL:** https://community.simplicite.io/t/5236

## Question
Bonjour,

Serait-il possible d'ajouter une contrainte de visibilité sur un attribut d'action (non persistant) en fonction d'un autre attribut d'action (non persistant) ?

Exemple, Dans l'action suivante, je souhaite afficher le 2ième attribut (texte à saisir) uniquement si l'utilisateur choisi "Oui" :
![image|667x277](upload://9rhqHX3875e16m1V6MJb7lliAMl.png)

Merci d'avance.
Abed.
[Platform]
Status=OK
Version=5.2.13
BuiltOn=2022-09-01 16:16
Git=5.2/ceeaa2a4f4995109f7c051724c9f36c1eac003f7
Encoding=UTF-8
EndpointIP=149.202.173.228
EndpointURL=http://e3m.simplicite.io:10118
TimeZone=Europe/Paris
SystemDate=2022-09-05 22:24:24

## Answer
Bonjour,

Les contraintes s'appliquent aux objets, pas aux actions dont les champs sont en général de simples compléments obligatoires ou facultatifs de l'action sans logique métier particulière.

On peut surcharger les champs via le hook `initAction` en back avant affichage.

https://docs.simplicite.io/documentation/01-core/businessobject-code-hooks.md

```java
@Override
public void initAction(Action action) {
    ObjectField f = action.getConfirmField(getGrant().getLang(), "myFieldName");
    f.setDefaultValue("aValue");
    f.setRequired(true);
}
```

En front, pour ajouter du code dynamique dans ce formulaire, il faut ajouter du code javascript dans le champ **UI template** HTML de l'onglet confirmation de l'action qui permet avant tout de positionner les champs autrement que les uns en dessous des autres, mettre des zones de texte, etc. 

Exemple myField2 visible si myField1 vaut abc, affichage en 2 colonnes :

```html
<div class="row">
  <div class="field col-sm-6" data-field="myField1"></div>
  <div class="field col-sm-6" data-field="myField2"></div>
</div>

<script type="text/javascript">
// input du champ myField1
$('#field_myField1_idACTIONNAME').change(function() { 
   // label + input du champ myField2
   let fg = $('.form-group[data-group=myField2]');
   $(this).val() == "abc" ? fg.show() : fg.hide();
});
</script>
```
