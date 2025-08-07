# java.lang.NullPointerException: Cannot invoke "org.json.JSONObject.getString(String)" because "this.m_creds" is null

**URL:** https://community.simplicite.io/t/3891

## Question
Bonjour,

NPE / m_creds is null sur une instance "front" v4.0-P25 instanciant un ObjectServiceSimplicite hébergé sur une instance "back" v5.1.4:

* front : Version=4.0.P25 BuiltOn=2021-09-28 22:59 (revision 680201342705438284ecf4de6c17600177b839b1)
* back : Version=5.1.4 BuiltOn=2021-09-28 23:05 Git=release/50bf90c0522a87f35dbfed9b3880d279f8a30dc7

```
2021-09-30 14:17:52,023 ERROR [com.simplicite.util.ObjectDirect] SIMPLICITE|http://ad549ae0e704:8080||ECORED0001|system|com.simplicite.util.ObjectDirect|search||Erreur IT4ITProduct
    java.lang.NullPointerException: Cannot invoke "org.json.JSONObject.getString(String)" because "this.m_creds" is null
     at com.simplicite.util.ObjectServiceSimplicite.getAPI(ObjectServiceSimplicite.java:47)

```

## Answer
Je veux dire au moment où on accède la première fois à l'objet après un clear cache, le `postLoad` est appelé, c'est lui qui parse la configuration et ça catche les exceptions pour les tracer dans les logs

Donc ma question est y-a-t-il des traces d'erreur à ce moment ?

Si le `postLoad` ne s'est pas bien passé alors le NPE en question peut effectivement se produire, on va rendre ça plus propre en évitant le NPE et en mettant une erreur plus explicite mais ça ne résoudra pas ton pb qui est ailleurs.

PS: par hasard as-tu surchargé le hook `postLoad` de ton objet ? Si oui il faut impérativement appeler le `super.postLoad()` pour ce genre d'objets service
