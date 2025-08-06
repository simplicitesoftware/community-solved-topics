# Select sur un BO depuis PlatformHooks

**URL:** https://community.simplicite.io/t/4570

## Question
Bonjour, 
J'ai des difficultées à récuperer un record depuis la BDD dans la class PlatformHooks.

J'ai testé de plusieurs manière mais à chaque fois il ne trouve pas le record a partir de son row_id
Le record en question:
![image|510x113](upload://t8FQX3C1xyzp4Qq2kCU5rWvkqGd.png)

![image|690x184](upload://jUZ3E0eULfsWenF4VnaaNKr7dLD.png)

Le code ( 4 manière différentes): 


```
            String centerId = g.simpleQuery(directorQuery);
            if (centerId != null && !centerId.isBlank()) {
                ObjectDB center = Grant.getSystemAdmin().getTmpObject("NamCentre");

                BusinessObjectTool boToool = new BusinessObjectTool(center);

                boToool.select(centerId);
                // Exception, log ci-joint
                boToool.getObject().setFieldValue("namCntUserDirecteurId", userId);
                boToool.validateAndUpdate();

                center.resetFilters();
                if (center.select(centerId)) {
                    // A priori false à chaque fois
                    center.setFieldValue("namCntUserDirecteurId", userId);
                    center.update();
                }

                ObjectDB namCentre = g.getTmpObject("NamCentre");
                try {
                    // Erreur, log ci-joint
                    namCentre.getTool().select(centerId);
                    namCentre.getTool().getObject().setFieldValue("namCntUserDirecteurId", userId);
                    namCentre.save();
                } catch (GetException e) {
                    AppLog.simpleError(e);
                }
                namCentre.resetFilters();
                namCentre.getField("row_id").setFilter(centerId);

                for (String[] row : namCentre.search(false)) {
                    //Array vide
                    namCentre.setFieldValue("namCntUserDirecteurId", userId);
                    namCentre.update();
                }
```
L'objet en quesiton
![image|380x242](upload://osOv9FMGPWxUV7kVvyKbrej7x3D.png)

Quelle piste ai-je omis ?

## Answer
Bonjour,

1. Le `g.getTmpObject()` *(ligne 19 du code collé)* ne peut pas vous donner un objet fonctionnel puisque vous êtes dans le `preLoadGrant` et que **les droits de l'utilisateur n'ont donc pas encore été chargés**. Cela explique que vous obteniez un `GetException` en utilisant `BusinessObjectTool.select` : l'utilisateur n'a pas les droits.

2. Votre première approche (l.3) est plus pertinente: on utilise en général l'utilisateur system (dont vous utilisez les droits avec `Grant.getSystemAdmin()`) pour les manipulations en amont du chargement du grant. Vous obtenez cependant la même exception, il est donc probable que l'utilisateur `system` n'ait pas les droits sur notre objet `NamCentre`. Vous pouvez essayer d'exclure ce cas de figure :

      - en attribuant manuellement les droits avec [Grant.changeAccess](https://docs.simplicite.io/5/javadoc/com/simplicite/util/GrantCore.html#changeAccess(java.lang.String,boolean%5B%5D))

     - en mettant ajoutant un groupe de droits de type superadministrateur en profil du groupe **ADMIN**


[details="Exemple avec attribution manuelle"]
```java
String centerId = g.simpleQuery(directorQuery);
if (centerId != null && !centerId.isBlank()) {

    Grant sys = Grant.getSystemAdmin();
    boolean[] oldcrud = sys.changeAccess("NamCentre", false,true,true,false); // READ & UPDATE
    try{
        ObjectDB center = sys.getTmpObject("NamCentre");
        synchronized(center){
            center.resetFilters();
            center.resetValues();
            center.getTool().select(centerId);
            center.setFieldValue("namCntUserDirecteurId", userId);
            center.getTool().validateAndUpdate();
        }
    }
    catch(Exception e){
        AppLog.error(e, sys);
    }
    finally{
        // restore original rights
        sys.changeAccess("NamCentre", oldcrud);
    }
}

```
[/details]

Cordialement,
