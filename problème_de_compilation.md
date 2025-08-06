# Problème de compilation

**URL:** https://community.simplicite.io/t/10446

## Question
Bonjour,

Suite à nos derniers échanges, je travaille actuellement à la mise en place d’un code qui, à terme, devra permettre l’envoi d’un mail. Pour l’instant, je me concentre simplement sur la récupération des données issues de certains champs, afin de les stocker dans des variables qui serviront à construire le contenu du message.

Cependant, lors de la compilation, je rencontre plusieurs messages d’erreur que je ne parviens pas à résoudre. Je vous joins ci-dessous :

* le code que j’ai rédigé,

* ainsi qu’une capture d’écran des messages d’erreur rencontrés à la compilation.

Je suis conscient que ma question peut paraître basique, et je vous remercie par avance pour votre indulgence ainsi que pour le temps que vous prendrez à me répondre. Cela m’aidera à progresser.

Merci encore pour votre aide précieuse.

Bien cordialement,

[details]
![image001-3|690x387](upload://4TRw3LkDQZklO9BL3KxGfBgLMqG.png)

[/details]

[details="Instance /health"]
```java
package com.simplicite.objects.Nova_memoria;

import java.util.*;
import com.simplicite.util.*;
import com.simplicite.util.exceptions.*;
import com.simplicite.util.tools.*;
import com.simplicite.util.annotations.BusinessObjectAction; // Import pour l'annotation

/**
 * Business object Nova_Projet
 */
public class Nova_Projet extends ObjectDB {
    private static final long serialVersionUID = 1L;

    @Override
    public void preLoad() {
        AppLog.info(getClass(), "preLoad", "Classe Nova_Projet chargée - Vérification pour débogage", getGrant());
    }

    @BusinessObjectAction
    public String action_btn_inv_sct(Action a) {
        try {
            String societeId = getFieldValue("novamPjtSctId"); // row_id société
            AppLog.info(getClass(), "action_btn_inv_sct", "ID société (row_id) : " + societeId, getGrant());
            if (Tool.isEmpty(societeId)) {
                return Message.formatSimpleError("Aucune société liée.");
            }

            // Récupérer ID métier société (champ inline)
            String IDsociete = getFieldValue("novamSctIdSociete");
            AppLog.info(getClass(), "action_btn_inv_sct", "ID métier société : " + (IDsociete != null ? IDsociete : "vide"), getGrant());

            // Charger société par clé métier pour obtenir row_id
            ObjectDB societe = getGrant().getTmpObject("Nova_Societe");
            synchronized (societe) {
                societe.resetFilters();
                societe.setFieldFilter("novamSctIdSociete", IDsociete);
                societe.search();
                if (societe.getCount() == 0) {
                    return Message.formatSimpleError("Société non trouvée par clé métier.");
                }
                societe.setValues(societe.getRow(0)); // Charger valeurs (getRow retourne String[])
                String societeRowId = String.valueOf(societe.getRowId()); // Convertir long en String
                AppLog.info(getClass(), "action_btn_inv_sct", "Société chargée - Row ID : " + societeRowId, getGrant());
            }

            // Filtrer contacts sur row_id société
            ObjectDB contact = getGrant().getTmpObject("Nova_Contact_Societe");
            synchronized (contact) {
                contact.resetFilters();
                contact.setFieldFilter("novamCtcsocSctId", String.valueOf(societe.getRowId())); // Utiliser row_id converti
                contact.search();
                if (contact.getCount() == 0) {
                    return Message.formatSimpleError("Aucun contact trouvé.");
                }
                contact.setValues(contact.getRow(0)); // Charger premier contact
                String MailAC = contact.getFieldValue("novamCtcsocMailContactSociete");
                AppLog.info(getClass(), "action_btn_inv_sct", "Email contact (MailAC) : " + (MailAC != null ? MailAC : "vide"), getGrant());
            }

            return Message.formatSimpleInfo("Variables récupérées avec succès.");
        } catch (Exception e) {
            AppLog.error(getClass(), "action_btn_inv_sct", "Erreur variables", e, getGrant());
            return Message.formatSimpleError(e.getMessage());
        }
    }
}
```

[/details]

[details="Simplicité logs"]
```text
---paste the content of the **relevant** server-side logs---
```

[/details]

[details="Browser logs"]
```text
---paste content of the **relevant** browser-side logs---
```

[/details]

[details="Other relevant information"]
*----E.g. type of deployment, browser vendor and version, etc.----*

[/details]

## Answer
Merci beaucoup pour votre réponse, et encore une fois pour le temps que vous m’accordez.

Je comprends bien vos explications. Je vous avoue que, même si la documentation est assez fournie, elle me semble parfois peu intuitive — surtout lorsqu’on cherche quelque chose de précis. Mais cela vient certainement aussi de mon niveau encore très débutant.

Encore merci pour votre aide précieuse.

Bien cordialement,
