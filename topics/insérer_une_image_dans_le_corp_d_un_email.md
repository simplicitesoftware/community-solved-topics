# Insérer une image dans le corp d'un email

**URL:** https://community.simplicite.io/t/4424

## Question
Bonjour,

J'ai créé une ressource de type **Image** comme ci-dessous:
![image|690x280](upload://x1DDA5klINlLbOWmCufG29SnO9c.png)

J'aimerais dans le code, pouvoir insérer une image dans le corps d'un email à l'intérieur de la balise HTML "img", dans la propriété src : `<img src="mon_url" />`.

Je suis actuellement dans la capacité d'insérer du contenu à l'intérieur de la propriété src, mais je ne sais pas comment récupérer l'URL de ma ressource image.

Auriez-vous une idée ?

## Answer
Pour insérer une image dans un email, dans Simplicité ou ailleurs... il faut obligatoirement le passer en attachement simple ou avec sa référence content-id :

- Il est impossible de faire autrement car tous les clients de messagerie modernes filtrent les contenus inlinés dynamiquement de type : `<img src="data:image/png...">`

- Il faut forcement utiliser un `<img src="cid:...">` vers un attachment  = attribué par les API (mail.addImage ou équivalent).
