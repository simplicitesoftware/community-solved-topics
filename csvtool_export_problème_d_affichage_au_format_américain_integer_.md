# CSVTool.export : problème d'affichage au format américain (Integer)

**URL:** https://community.simplicite.io/t/6870

## Question
### Request description

Bonjour,

Nous avons remarqué une régression concernant l'affichage des Integer depuis le passage en version 5.3.

Avant l'update, un attribut de type int, valeur 1200 sort bien au format "**1200**" dans un export .csv.
Après l'update, un attribut de type int, valeur 1200 sort au format américain "**1,200**" dans un export  .csv.

Pareil pour les nombres plus important de type 1000000 devient 1,000,000 etc etc

Le problème apparait lors de l'utilisation de cette méthode d'action :

	public String generateExportUnitFile(Action action){
        try {
            String nameObject = "MlaRefinedTripletExport";
            ObjectDB obj = getGrant().getProcessObject(nameObject);
            obj.resetFilters();
            obj.resetValues();                           
            File f = new File(getGrant().getTmpDir() + "/" + "generateExportunitFile_" + nameObject + ".csv");
            PrintWriter out = new PrintWriter(f);
            CSVTool.export(obj, null, "list", ";", false, out);
            saveFile("csv", "generateExportunitFile_" + nameObject, "UPDATED", f);
        } catch (Exception e) {
            AppLog.error(getClass(), "display", null, e, getGrant());
        }
        return "OK";
    }

La méthode saveFile, sauvegarde le fichier au format DocumentDB.

Le problème n'est présent qu'avec un export "par code", je ne le reproduis pas avec l'export par UI :

![image|429x500](upload://h292CDYmMeJomZavXlU86Kj6kZe.png)

Merci d'avance,

Benoît

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.3.11
BuiltOn=2023-08-07 15:27
Git=5.3/015368bc51913a479e8d682d65ea405c12b45951
Encoding=UTF-8
EndpointIP=xxx
EndpointURL=xxx
TimeZone=Europe/Paris
SystemDate=2023-09-13 09:51:19
```
[/details]

## Answer
[quote="Benoit, post:1, topic:6870"]
`CSVTool.export(obj, null, "list", ";", false, out);`
[/quote]

```
public static void export(ObjectDB obj, List<String[]> rows, String mode, String sep, boolean techfields, PrintWriter out)
```

L'export est désormais formatté s'il n'est pas technique : nombre dans la préférence du user, libellé yes/no au lieu de 1/0, format des dates...

- Mettez le flag `techfields= true` pour récupérer les données en format "raw"
- Ou changez la préférence du user qui exporte 

![image|327x191](upload://3Cgt64LZusm653eQ539FMFONZSF.png)

- Ou encore le rendering du champ comme "simple" non monétaire (exemple pour une année pour la laisser "2023" et pas "2 023")

![image|343x223](upload://goRNjLc7eQZgTE61j20wonuo1BS.png)
