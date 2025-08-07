# Failed to load - Import d'un module

**URL:** https://community.simplicite.io/t/4276

## Question
Bonjour,
Je n'arrive pas à importer un module (taille 205Mo). 
J'ai modifié le paramètre système MAX_UPLOAD_SIZE à 1024 en valeur remplacée, mais cela ne fonctionne toujours pas. 

Voici ce que je trouve dans la console  (rien de visible dans les logs)
![image|547x119](upload://9kmENd8upa0uWne1g5WnAI093dL.png)


[Platform]
Status=OK
Version=5.1.16
BuiltOn=2021-12-11 19:17

Merci pour votre aide,

## Answer
Ce code retour HTTP : 413 (Payload Too Large) n'est pas renvoyé au niveau Simplicité mais par un composant en amont, à priori votre reverse proxy (donc jouer sur le paramètre système `MAX_UPLOAD_SIZE` n'aura pas d'effet) => à voir avec votre exploitant

Vérifiez aussi que vous avez bien laissé le `maxPostSize` par défaut au niveau Tomcat (par défaut on le livre à `-1` justement pour que ça ne soit pas bloquant à ce niveau).

PS: Je profite de cette réponse pour vous rappeler qu'il y a en ce moment des vulnérabilités majeures détectées sur le composant tiers Log4J qui sont corrigées au fil de l'eau et qu'on met donc à jour immédiatement dans de nouvelles révisions Simplicité cf. https://community.simplicite.io/t/log4j-2-x-vulnerability-updated/4200/13, il est donc en ce moment plus que jamais impératif de vous maintenir très régulièrement à jour => la révision actuelle est la 5.1.22
