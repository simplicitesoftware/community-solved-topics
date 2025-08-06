# Hook preSearch perd le contexte du parent/grand-parent dans le cas d'une relation n-n présentée en Pillbox

**URL:** https://community.simplicite.io/t/6328

## Question
Continuing the discussion from [Hook initRefSelect pas exécuté dans le cas d&#x27;une relation n-n présentée en PillBox](https://community.simplicite.io/t/hook-initrefselect-pas-execute-dans-le-cas-dune-relation-n-n-presentee-en-pillbox/1489/6):

### Version

*5.2.36 [EDIT] reproduit en 5.2.39*

### Description

*Bonsoir, je ne sais pas s'il s'agit d'un bug ou d'une feature request mais je pense rencontrer un problème similaire à celui traité dans le post cité plus haut. Je classe le post en support dans le doute...*

Dans le cas présent, je dois pouvoir filtrer les éléments dans la pillbox en fonction du rowId de l'objet courant qui présente la pillbox. Hors je n'arrive pas à remonter à ce contexte depuis le hook preSearch de l'objet présenté dans la pillbox:
- getParentObject(), getParentRefField(), etc. renvoient tous null
- getInstanceName() renvoie un nom d'instance tmp_xxx mais pas panel_xxx ou pillbox_panel_xxx

Du coup, impossible d'une part d'identifier le contexte du filtre et d'autre part de récupérer le rowId de l'objet parent qui présente la pillbox...

## Answer
Merci pour les explications.
Effectivement, si le besoin est de filtrer les NN accessibles en fonction du parent, on est comme dans le cas d'une vue en panel sur laquelle on voudrait ajouter un filtre/search spec.

`initList` : en général on utilise ce hook pour préparer la liste avant son affichage UI
`preSearch` : toujours appelé avant tout "select" en base pour le count, une liste paginée, un select(id) qui est search sur le row_id...

Si on change le rendering, il faudrait que le filtre par code s'applique aussi.
Du coup pour être plus homogène sur les nommages des instances / API, il faudrait utiliser un nom d'instance panel ou équivalent comme `panel_pillbox_<obj>_<fk>`, pour que le isPanelInstance() renvoit true + qu'on sache aussi identifier l'instance pillbox.
