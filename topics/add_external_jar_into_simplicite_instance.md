# ADD external jar into simplicite instance

**URL:** https://community.simplicite.io/t/11414

## Question
Hello Team,

I need to add external jar file or maven dependency into simplicite instance, so could you please guide me how to add external jar into instance?

## Answer
You can do this without needing to integrate any additional JAR:

```java
bytes[] pdf = HTMLToPDFTool.markdownToPDF("My title", "Hello _Markdown_ **world**!");
```

See [the `HTMLToPDFTool` helper class Javadoc](https://platform.simplicite.io/6.3/javadoc/com/simplicite/util/tools/HTMLToPDFTool.html#markdownToPDF(java.lang.String,java.lang.String))

When you request our support please always start by explaining us what is your **functional/business requirement**. On a rich LowCode platform such as Simplicite adding custom JARs and/or writing "heavy" custom code is often not the right approach.
