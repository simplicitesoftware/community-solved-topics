# Rechargement d'un formulaire inliné en cas d'erreur

**URL:** https://community.simplicite.io/t/11413

## Question
### Request description

Bonjour,

J'ai un souci de rechargement de formulaire inliné :  en cas d'erreur au save, le formulaire réapparaît vide.

Je détaille tout ci-dessous.
Merci d'avance pour votre aide !

Emmanuelle

### Steps to reproduce

1. Avoir un objet A avec un lien inliné vers un objet B 
2. Mettre un champ obligatoire sur B
3. Créer une occurrence de A sans remplir le champ obligatoire de B
4. Sauvegarder
5. -> Le form de B se recharge vide

Piste d'analyse :

Le form est vide car uiTemplate est vide dans les metadata de l'objet B.

```
let tmpl = v.uiTemplate instanceof $ ? v.uiTemplate.clone() : $(v.uiTemplate)
```

Le champ semble vidé au moment du count sur l'objet B

```
if (res.meta)
                            self.metadata = res.meta;
```

Normalement, il y a un getMetadata qui revalorise B correctement, mais en cas d'erreur, il y a une sauvegarde des valeurs de champ de l'objet inliné

```
catch(e => {
                            child.metadata.instance = inst;
                            if (e)
                                errs = errs.concat(e);
                            child.inlineValues = child.getValues();
                            fn();
                        }
```

Ca bypasse le rechargement des metadonnées car p.values n'est pas vide

```
if (p.values)
                        init();
                    else {
                        ui.monitor(ctn, "get");
                        if (creation)
                            obj.getForCreate(param).then(init).catch(getError);
                        else if (p.copy)
                            obj.getForCopy(rowId, param).then(init).catch(getError);
                        else
                            obj.getForUpdate(rowId, param).then(init).catch(getError);
                    }
```



### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=6.2.21
BuiltOn=2026-01-15 22:16
```
[/details]

## Answer
OK j'ai bien reproduit, merci pour l'investigation poussée.

On passe par un count parce que l'onglet est un lien. 
Le contexte du count étant un contexte de liste, c'est normal que uiTemplate soit vide. 

Le comportement sera adapté afin de ne pas passer par un count pour les onglets d'objets inlinés.

Ça sera livré en [6.2.22](https://docs.simplicite.io/versions/release-notes/v6-2/#version-6.2.22)
