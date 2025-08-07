# getForCopy(myRowId); sur un objet avec un copie en cascade

**URL:** https://community.simplicite.io/t/5240

## Question
Bonjour,
j'ai un object ayant une relation vers un autre objet et un paramètre copie en cascade 
![image|690x129](upload://roGakociXOhJJDvsXcuUaEgya2p.png)

j'ai implémenté une copie spécifique pouvant être appelé via une action et une api.
voici un extrait du code :

		try {
		  obj.getTool().getForCopy(myRowId);
                  // 
                  obj.getTool().validateAndSave();
  	       } catch (Exception e) {
			return "Something went wrong"+e;
		}
l'opération échoue suite à un doublon de clef sur l'object copié  lié : om.simplicite.util.exceptions.ValidateException: ERR_USERKEY: STUDY-dev-998 0.00
alors que la copie via l'UI se déroule correctement. Y a t'il un moyen d'éviter ce doublon de clef engendré par une copie brutte de tous les champs sans repositionner de nouvelle clef sur la copie de l'objet liée ?
Frédéric

## Answer
Bonjour
merci pour votre aide, je viens de trouver la solution grâce à vous, j'avais un bout de code dans le try qui faisait un erase de la clef fonctionnelle, j'ai déplacé cette init dans le prevalidate et je confirme les copies en cascade fonctionnent correctement.
Merci encore pour votre aide
Frédéric
