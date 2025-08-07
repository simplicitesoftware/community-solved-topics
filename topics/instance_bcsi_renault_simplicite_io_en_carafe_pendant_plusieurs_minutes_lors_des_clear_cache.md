# Instance bcsi.renault.simplicite.io en carafe pendant plusieurs minutes lors des clear cache

**URL:** https://community.simplicite.io/t/3873

## Question
Bonjour,
Je prépare l'upgrade 4->5 de l'instance https://bcsi.renault.simplicite.io (je teste nos modules progressivement sur une nouvelle instance temporaire bcsidev.renault.simplicite.io initialisée en 5.1.2).

Dans notre ancienne configuration il y a(vait) une disposition 'bcsi' configurée initialement sur la 3.2 en 2017 et des paramètres de disposition qui ne passent pas l'import et que j'ai supprimée.

J'ai aussi configuré un thème 'renault' qui porte la nouvelle identité de marque 'Renault Group' (divers SVG associés au thème ou comme Resources).

J'ai l'impression que depuis que j'ai effectué ces ajustements, les clear cache prennent plusieurs minutes... Je n'arrive pas à déterminer pourquoi.

Cela peut-il être lié aux modifications évoquées ci-dessus ?

Voici un extrait des logs système au moment du clear cache:
```
2021-09-27 14:26:42,900 INFO [com.simplicite.webapp.filters.AuthMethodFilter] SIMPLICITE|http://renault.simplicite.io:10028||DAUTHCS001|system|com.simplicite.webapp.filters.AuthMethodFilter|methodOAuth2||Debug authentification: OAuth2 requested URI = [/ui]
2021-09-27 14:26:32,105 INFO [com.simplicite.webapp.filters.AuthMethodFilter] SIMPLICITE|http://renault.simplicite.io:10028||DAUTHCS001|system|com.simplicite.webapp.filters.AuthMethodFilter|methodOAuth2||Debug authentification: OAuth2 requested URI = [/ui/logs]
2021-09-27 14:24:30,735 INFO [com.simplicite.util.engine.CoreCache] SIMPLICITE|http://renault.simplicite.io:10028||INFO|system|com.simplicite.util.engine.CoreCache|initProcessCache||Evénement: PROCESS_CACHE_SIZE=10000
2021-09-27 14:24:30,734 INFO [com.simplicite.util.engine.CoreCache] SIMPLICITE|http://renault.simplicite.io:10028||INFO|system|com.simplicite.util.engine.CoreCache|initObjectCache||Evénement: OBJECT_CACHE_SIZE=10000
2021-09-27 14:24:30,725 INFO [com.simplicite.util.engine.GrantManager] SIMPLICITE|http://renault.simplicite.io:10028||INFO|system|com.simplicite.util.engine.GrantManager|clearCache||Evénement: Reload core cache...
2021-09-27 14:24:21,760 INFO [com.simplicite.util.Grant] SIMPLICITE|http://renault.simplicite.io:10028||ICORED0001|public|com.simplicite.util.Grant|init||Info: public connected, session ID: FCF4D265165680424BAB64C080D78EBB, timeout: 5 min , user agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36
2021-09-27 14:24:21,639 WARN [com.simplicite.util.Grant] SIMPLICITE|http://renault.simplicite.io:10028||WCORED0001|system|com.simplicite.util.Grant|getDisposition||Avertissement: Unable to get disposition empty
2021-09-27 14:24:21,624 WARN [com.simplicite.util.Grant] SIMPLICITE|http://renault.simplicite.io:10028||WCORED0001|system|com.simplicite.util.Grant|getDisposition||Avertissement: Unable to get disposition empty
2021-09-27 14:24:21,605 INFO [com.simplicite.webapp.filters.AuthMethodFilter] SIMPLICITE|http://renault.simplicite.io:10028||DAUTHCS001|system|com.simplicite.webapp.filters.AuthMethodFilter|methodOAuth2||Debug authentification: OAuth2 requested URI = [/ui/logs]
2021-09-27 14:24:18,180 INFO [com.simplicite.util.engine.GrantManager] SIMPLICITE|http://renault.simplicite.io:10028||INFO|system|com.simplicite.util.engine.GrantManager|clearCache||Evénement: Compile resources CSS and JS...
2021-09-27 14:24:18,169 INFO [com.simplicite.util.engine.GrantManager] SIMPLICITE|http://renault.simplicite.io:10028||INFO|system|com.simplicite.util.engine.GrantManager|clearCache||Evénement: Clean ObjectLoader and ObjectManager cache...
```

NB: le message 'Unable to get disposition empty' était je crois déjà présent avant que je n'applique les modifications...

## Answer
Perso je respecte les règles de sizing suivantes et je n'ai pas de pb:

- pour le "header logo" : une image SVG de qques Kb max ou un PNG/JPG rectangulaire de max 400 ou 500px max de large sur 100 ou 150px de haut (la UI l'affiche en la resizant à environ 60px de haut donc plus gros ne sert àç rien)
- pour le "logo scope" : une image SVG de qques Kb max ou un PNG/JPG carré de 128x128 (ou au pire 256x256)
- pour le "favicon " : un PNG de 32x32 (ou un ICO 16x16 ou 32x32)
