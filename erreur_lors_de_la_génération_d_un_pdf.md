# Erreur lors de la génération d'un PDF

**URL:** https://community.simplicite.io/t/1177

## Question
Bonjour, 

Lorsque j'essaie de générer un document pdf et que le processus rencontre un problème, j'ai le message suivant sur une nouvelle page (message classique pour les docs pdf) :

![erreur%20pdf|690x416](upload://2UNRkMs4uxJgpMySNZ09bYIMslB.png) 

J'aimerai plus tôt qu'en cas d'erreur, avoir un message personnalisé et sur la même page. J'ai essayé avec la code suivant :
```
var somme = som + sommeDM + sommeDpt + sommeCC + sommeQual;
	
	if (somme != 100){
		return Message.formatSimpleInfo("ERROR_OBJ");
	}else{
		console.log(somme);
		PDFTool.close(pdf);
		return bos.toByteArray();
	}
```
mais, je n'ai pas le résultat voulu. Pouvez vous m'apporter votre aide s'il vous plait?

Merci d'avance

## Answer
Si votre PDF est publié via un template de publication il faut utiliser le hook `isPrinttemplateEnable`.

Il y a un exemple dans la démo pour la publication du reçu des commandes qui n'est possible que si l'état est validated ou shipped:
![image|690x373](upload://gAbAxSMUkQ6YC7VIDpnAAGzCADU.png) 

Si c'est par une action il faut utiliser le hook `isActionEnable`
