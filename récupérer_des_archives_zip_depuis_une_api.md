# Récupérer des archives ZIP depuis une API

**URL:** https://community.simplicite.io/t/4604

## Question
Bonjour,

Nous avons une API qui nous fournit des archives ZIP.

![image|690x465](upload://3use4czB0qBVvN9dk0U0o8lY0wC.png)

**Comment récupérer ces archives ZIP sous Simplicité (Quelles classes utilisées ?...) ?**

## Answer
**En général**, le token est transmis par le biais d'un Header HTTP, on utilise donc [readURL byteArray avec header](https://docs.simplicite.io/5/javadoc/com/simplicite/util/Tool.html#readUrlAsByteArray(java.lang.String,java.lang.String,java.lang.String,java.lang.Object,java.lang.Object,java.lang.String))

```java
var headers = new HashMap();
headers.put("Authorization", "Bearer "+token);
byte[] zip = Tool.readUrlAsByteArray(url, null, null, null, headers, Globals.BINARY);
```

Attention, le nom et la forme du header varient d'une API à l'autre.
