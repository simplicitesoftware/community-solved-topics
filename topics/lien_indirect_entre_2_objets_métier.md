# Lien indirect entre 2 objets métier

**URL:** https://community.simplicite.io/t/6385

## Question
### Lien indirect entre 2 objets métiers via l'éditeur de code

Bonjour, je débute sur simplicité avec une application de logistique. J'essaye d'implémenter la fonction d'ajout de stock du tutoriel à mon cas mais mes objets métiers ne sont pas directement liés. 

Voici l'extrait de mon modèle de données concerné. Mon code se situe sur l'objet "SeccoEntree" qui est l'équivalent de ma commande et je veux impacter le stock de mon objet "SeccoStockReferent" en conséquences.

![extrait_modele_donnees|459x499](upload://1D4hLeQILk0kcWZqPCiGFEkoFvE.jpeg)

Et voici mon code :
![code_Entree_increaseStock|690x294](upload://yzzMx1Jweg3bvlMddpxPcf5ypQF.jpeg)

Je n'arrive pas à trouver le bon code à écrire, peu importe ce que je tente, j'ai énormément d'erreurs qui apparaissent m'indiquant un "unknown field" que je n'arrive pas à identifier. Je pense que mes liens entre objets ne sont pas les bons mais je ne saurais dire pourquoi.

Merci d'avance pour votre aide.
Cordialement,
Manon

## Answer
Suite à notre entretien téléphonique, voici la correction "au plus propre" (vs le "plus pédagogique" que nous avons réalisé ensemble)

```java
package com.simplicite.objects.SECCo;

import java.util.*;

import com.simplicite.util.*;
import com.simplicite.util.exceptions.*;
import com.simplicite.util.tools.*;

/**
 * Business object SeccoEntree
 */
public class SeccoEntree extends ObjectDB {
	private static final long serialVersionUID = 1L;
	
	@Override
	public String postUpdate() {
		// pour chacune des SeccoEntreeProd de ce SeccoEntree (rechercher au préalable)
			// charger le SeccoStockReferent correspondant à 1) l'entrepot de l'entrée, 2) au produit 
			// augmenter la quantité d'autant qu'indiqué dans SeccoEntreeProd
			// sauvegarder
		
		if(this.getOldStatus().equals("EN_COURS") && this.getStatus().equals("VALIDEE")){
			ObjectDB entreePrd = getGrant().getTmpObject("SeccoEntreeProd");
			ObjectDB stockRef = getGrant().getTmpObject("SeccoStockReferent");
			
			synchronized(entreePrd.getLock()){
				for(String[] row : entreePrd.getTool().search(Map.of("seccoEntreeprodEntreeId", getRowId()))){
					entreePrd.setValues(row);
					synchronized(stockRef.getLock()){
						try{
							stockRef.getTool().get(Map.of(
								"seccoStockrefEntrefId", this.getFieldValue("seccoEntreeEntrefId"),
								"seccoStockrefProdId", entreePrd.getFieldValue("seccoEntreeprodProdId")
							));
							stockRef.setFieldValue("seccoStockRefQuantite", 
								stockRef.getField("seccoStockRefQuantite").getInt(0)
								+
								entreePrd.getField("seccoEntreeprodQuantite").getInt(0)
							);
							stockRef.getTool().validateAndSave();
						}
						catch(Exception e){
							AppLog.error("error updating stock", e, getGrant());
						}
					}
				}
			}
		}
		return null;
	}
}

```
