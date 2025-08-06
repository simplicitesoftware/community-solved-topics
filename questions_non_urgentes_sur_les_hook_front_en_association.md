# Questions non urgentes sur les hook front en association

**URL:** https://community.simplicite.io/t/8078

## Question
### Request description

Bonjour,

En travaillant sur du code front, j'ai noté quelques questions concernant les hook :

1 - j'ai l'impression que form.beforeload se déclenche avant que le code front ait été valorisé, c'est possible ? Dans le script ci-dessous, même si j'ai du code dans le hook, p.beforeload est null

```
function get(o) {
            obj = o;
            ui.monitor(ctn, "timesheet");
            try {
                p.beforeload && p.beforeload(ctn, obj, p);
            } catch (e) {
                console.error("Hook error timesheet.beforeload of " + obj.getName(), e);
            }
            $.extend(true, p, $.extend(true, {}, obj.locals.ui.timesheet, p));
            obj.timesheet({
                name: ts,
                resId: rowId,
                start: p.start,
                end: p.end
            }).then(init).catch(ui.isServiceLost);
        }
```
Ce n'est pas le cas pour preload et onload qui sont bien pris en compte

2 - Les hooks sur association
En association, j'ai l'impression que je n'ai pas beaucoup de choix de hook pour travailler sur le formulaire qui s'affiche après sélection des objets à associer. J'aurais eu besoin d'un aftersave ou onunload pour ajouter des traitements après association. Est-ce que j'ai raté quelque chose, sinon, serait-il possible éventuellement d'en ajouter dans une version ultérieure ?

Merci d'avance
Emmanuelle

[Platform]
Status=OK
Version=5.3.34
BuiltOn=2024-04-05 09:39

## Answer
Bonjour,

1) effectivement il y avait une inversion du code pour que ce hook soit visible.
on va corriger, c'est la même chose à d'autres endroits.

2) ce point a déjà été discuté sur d'autres forums privés.
2 nouveaux hooks back `pre/postAssociate` ont été créés à cet effet, appelés en début/fin d'associations à partir de la V6 (qui implémente le service Ajax `associate`) Donc inexistant en V5 qui fait les associations depuis le front et ne permettait pas d'avoir des hooks "sandwich" en back.

```java
/**
 * Hook called after associate
 * @param parent Parent object to associate
 * @param parentFk Foreign key to parent
 * @param child Optional child in case of N,N association
 * @param childFk Optional foreign key to child
 * @return Message or null
 */
public String postAssociate(
   ObjectDB parent, String parentFk, 
   ObjectDB child, String childFk);
```

Il n'est pas prévu de hooks front.
