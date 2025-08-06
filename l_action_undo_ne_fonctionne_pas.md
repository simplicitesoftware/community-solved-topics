# L'action Undo ne fonctionne pas

**URL:** https://community.simplicite.io/t/7010

## Question
### Request description

Bonjour,

Lorsqu'on met à jour un élément et que l'on clique sur le undo, l'écran freeze.

Dans les logs front, j'ai l'erreur suivante

```
ui-bundle.js?_=17:1641 Uncaught TypeError: app._ajaxKey is not a function
    at Simplicite.UI.Engine.undoRedo (ui-bundle.js?_=17:1641:640)
    at HTMLImageElement.<anonymous> (ui-bundle.js?_=17:2442:487)
    at HTMLImageElement.dispatch (jquery.js:2:43184)
    at y.handle (jquery.js:2:41168)
```
et dans le code du bundle ui la fonction app._ajaxKey() est appelée, il semble qu'elle existe mais avec un k minuscule : _ajaxkey()

```
    this.undoRedo = function(ctn, action, num, url) {
        if (action == "undo" || action == "redo") {
            view.showLoading(null);
            $.ajax({
                url: root + "/ui/json/app?action=" + action + "&type=user&num=" + (num || 1) + "&_ajaxkey=" + (app._ajaxKey() || "")
            }).done(r=>{
                let ur = r.response;
                if (ur) {
                    if (url)
                        ur.url = url;
                    $(".js-undoredo").trigger("ui.undoredo", [ur]);
                    ur.url && ui.loadURL(ctn, ur.url);
                }
            }
            ).always(()=>view.hideLoading(null));
        }
        return ui;
    }
    ;
```
Merci d'avance
Emmanuelle

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.3.17
BuiltOn=2023-10-06 15:15
```
[/details]

## Answer
[quote="Emmanuelle, post:1, topic:7010"]
`_ajaxKey`
[/quote]

Tout à fait, le K majuscule c'est pour le local storage.
Il manque aussi le paramètre _tabId qui identifie l'onglet (il y a un buffer undo/redo par onglet du navigateur). on corrige.
