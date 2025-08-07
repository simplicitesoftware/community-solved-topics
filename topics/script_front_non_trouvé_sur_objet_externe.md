# Script front non trouvé sur objet externe

**URL:** https://community.simplicite.io/t/9132

## Question
### Request description

Bonjour, 

J'ai un objet externe avec une ressource SCRIPT, mais elle n'est pas trouvée quand j'affiche mon objet externe.

![image|690x106](upload://ipq10WCnN8Y0GlkFjB0PokGZ9p6.png)

J'ai essayé de debugger un peu, je vois que script = void(0)
```
try {
                        let reader = new FileReader();
                        reader.onload = evt => {
                            let r, result = evt.target.result;
                            result = result ? result.replace(/^[\t\n\r ]*/, "") : "";
                            try {
                                r = JSON.parse(result);
                            } catch (e) {}
                            if (r && r.type == "topredirect" || result.length > 12 && result.substring(0, 12).toUpperCase() == "TOPREDIRECT:")
                                self.loadURL(ctn, r && r.url ? r.url : result.substring(12), {
                                    target: "_top"
                                });
                            else if (r && r.type == "redirect" || result.length > 9 && result.substring(0, 9).toUpperCase() == "REDIRECT:")
                                self.loadURL(ctn, r && r.url ? r.url : result.substring(9));
                            else if (r && r.type == "javascript" || result.length > 11 && result.substring(0, 11).toLowerCase() == "javascript:") {
                                external(r ? r.script : result.substring(11), r);
                                return;
                            } else if (r && ext == "json")
                                download(res, ext, filename);
                            else {
                                content(result);
                                return;
                            }
                            cbk && cbk();
                        }
                        ;
                        reader.onerror = evt => {
                            throw "Reader error = " + evt.target.error.message;
                        }
                        ;
                        reader.readAsText(res);
                    } catch (e) {
                        $app.error("Error reading " + url + " response as text: " + e.message);
                    }
```

Dans Network
![image|690x306](upload://n4KVIWtKqpvlhuXlaczSnR2HPYR.png)

Y a-t-il un changement avec la 6.1 ?
J'ai essayé aussi avec la ressource CLASS mais j'obtiens le même résultat.

Merci d'avance pour votre aide

[Platform]
Status=OK
Version=6.1.15
BuiltOn=2024-11-22 11:40

## Answer
PS: il y a eu un changement sur le typage des objets externes quand le user connecté est `SYSTEM_ADMIN=yes` (ex: `designer`). On est revenu en arrière car ça posait pb. Ce retour arrière sera poussé dans la prochaine révision 6.1

En attendant il faut s'assurer que les objet externe de type UI sont configurés comme suit:

![image|611x500](upload://mCmqwnnXfOokFuTqj1w8rIJ7IHL.png)
