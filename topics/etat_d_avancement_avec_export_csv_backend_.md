# Etat d'avancement avec export CSV (Backend)

**URL:** https://community.simplicite.io/t/6597

## Question
Bonjour,

J'aurais souhaité savoir s'il existe un moyen de récupérer l'état d'avancement lors de l'utilisation de la méthode suivante côté back :

[CSVTool ](https://docs.simplicite.io/5/javadoc/com/simplicite/util/tools/CSVTool.html#export(com.simplicite.util.ObjectDB,java.util.List,java.lang.String,java.lang.String,boolean,java.io.PrintWriter))

L'idéal serait de pouvoir récupérer la valeur lignes exportées / lignes totales, le but étant de pouvoir suivre l'état d'avancement des exports CSV qui sont lancées en parallèle.

Merci d'avance,

Benoît

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.2.42
BuiltOn=2023-06-22 14:55
Git=5.2/0ecad74ae5fa667fbdbd463af6203fbe84c6bd4d
Encoding=UTF-8
EndpointIP=100.88.2.117
EndpointURL=http://mla-api-75b787b778-55lvz:8080
TimeZone=Europe/Paris
SystemDate=2023-06-27 16:16:29
```
[/details]

## Answer
Bonjour Benoit,

Oui, l'export paginé indique au fur et à mesure le nombre de lignes exportées :

```java
String count = obj.getParameter(ImportExportTool.EXPORT_PROGRESS);
```

Si l'export est lancé via un objet dans la file asynchrone, on peut donc l'observer de l'extérieur. C'est ce que fait l'export CSV de la UI.

Launcher
```java
// Launcher, example : Action button
public String myActionMethod() {

	JobQueue.push("myExport123", new Runnable() {
		@Override
		public void run() {
			ObjectDB obj = getGrant().getObject("myExportObject123", "MyObject");
			CSVTool.export(obj...);
		}
	});
```

and observer

```java
// Other tracker thread, example : external object to display the counter
@Override
public String display(Parameters params) {
	// same object instance
	ObjectDB obj = getGrant().getObject("myExportObject123", "MyObject"); 
	return obj.getParameter(ImportExportTool.EXPORT_PROGRESS);
}
```

Pour avoir le total, il suffit de faire un `obj.getCount()`

@scampano
