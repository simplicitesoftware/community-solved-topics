# Items de list non initialisés sur displayList en mode Edit

**URL:** https://community.simplicite.io/t/7951

## Question
### Request description

Bonjour,

J'ai sur un formulaire une action qui ouvre une liste en édition

![image|690x312](upload://wC2GvNfdi6Ko0m5ss3EzjpaIpRR.png)

![image|690x346](upload://ymmsdITdRuzIAneTzYVjz04WOm9.png)

Sur l'objet affiché, j'ai une liste de valeurs qui à l'ouverture via ce bouton n'est pas correctement initialisée.

![image|690x91](upload://j3QTc39CxKeT0pSwVgxXi2TeD7B.png)

Si je fais Close puis Edit list, j'ai cette fois les bonnes valeurs.

![image|690x93](upload://fC0d9a0hUH8DFBiadW12j9rHEEF.png)

Dans le code du bundle UI, je vois que le problème se situe au niveau de la méthode mergeRowMeta

```
this.mergeRowMeta = function(obj, p) {
        let fs = obj.item.meta.fields;
        obj.item.meta.fields = obj.getFields().map(f=>{
            let x = fs.find(x=>x.name == f.name);
            return x ? $.extend({}, f, x) : $.extend({}, f);
        }
        );
        obj.item.meta = $.extend({}, obj.metadata, obj.item.meta);
        if (obj.item._index !== undefined)
            p.index = obj.item._index;
    }
```
J'ai bien les bonnes valeurs au niveau de obj.Field.listOfValues mais dans obj.item.metadata je n'en ai qu'une (celle qui a été enregistrée pour l'instance).

Est-ce un problème au niveau de mon URL d'action ?

Merci d'avance pour votre aide
Emmanuelle

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.3.31
BuiltOn=2024-03-15 13:56
```
[/details]

## Answer
J'ai fini par trouver en comparant les url de mon action et du bouton Edit list au moment du call. Mon action envoie un contexte LIST alors que le bouton envoie UPDATE.

Avec cette URL j'ai bien ma liste de valeurs complète 
```javascript:$ui.displayList(null, "RciDomFctApp",{nav:'add', fixedFilters: {"rciDomfctappAppId": rowId}, edit: "rows", inst: "panel_ajax_RciDomFctApp_rciDomfctappDomId", context: "5"}, null)```
