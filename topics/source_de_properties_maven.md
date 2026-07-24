# Source de properties maven

**URL:** https://community.simplicite.io/t/12778

## Question
Bonjour,

Dans le cadre de mon AI workflow, j'utilise un agent "orchestrateur" qui sollicite des  "coding" agents selon la version de Simplicité ciblée. Notre mapping est le suivant :

* **Simplicité 6.2** => Java 17
* **Simplicité 6.3** => Java 21

**Mon problème :** Bien que mon instance Simplicité 6.3 tourne sous Java 21, le fichier `pom.xml` (généré automatiquement ) de nos modules contient toujours les propriétés de compilation Maven fixées à **Java 17**. 
``` xml
<simplicite.version>6.3-SNAPSHOT</simplicite.version>
<maven.compiler.source>17</maven.compiler.source>
<maven.compiler.target>17</maven.compiler.target>
```
Ce qui "pertube" mon agent, il consomme du token à comprendre cette incohérence entre mes instructions et ce qu'il observe. 

**Questions :**

1. Est-ce "normal"/standard ?
2. Est-elle générée par défaut par la plateforme Simplicité (par exemple, via un template interne propre à la version de la plateforme) ?
3. Est-il possible de modifier/forcer cette version de compilateur (pour passer à Java 21 en v6.3) via la configuration du module, comme évoqué dans la documentation sur les **Maven settings** ?

Merci d'avance pour votre aide et vos éclaircissements !

## Answer
_No answer provided._
