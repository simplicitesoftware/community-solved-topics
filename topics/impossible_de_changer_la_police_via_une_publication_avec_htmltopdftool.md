# Impossible de changer la police via une publication avec HTMLtoPDFTool

**URL:** https://community.simplicite.io/t/5365

## Question
Bonjour, j'essaie en vain de modifier la police  (avec autre chose que sans-serif) résultant de la fonction
```
HTMLToPDFTool.toPDF(content);
```

Lorsque je modifie la police dans mon html avec plusieurs polices, le seul changement que j'arrive à produire est sur "sans-serif", tout les autres changement de police n'ont aucun impact. Les autres règles css ont pourtant l'air de fonctionner normalement.

```
<style> 
span { font-family: sans-serif; } 
</style>
```

![image|212x192, 75%](upload://1WlNl5kM7YMrUIg7lmBKs1Y4sR6.png)


```
<style> span { font-family: serif; } </style> 
ou 
<style> span { font-family: Times New Roman; } </style> 
ou
<style> span {} </style>
```
![image|217x194, 75%](upload://l8XrxMaXRXIbCJBDDGYI7eYJyOE.png)

Voilà un exemple de mon html:
```
<style> 
span { font-family: sans-serif; } 
</style>
<h3 style='font-size:15px;'><span style="color:#E2000A;"><strong>{Part}</strong>
  <img width="62" src="data:image/png;base64,{Image}" alt="image" style="float: right; 
  "></span>
  <p>&nbsp;</p>
<hr size=1 width=100% color=#FF2D00></h3>
```

## Answer
Voici (simplifiée) la partie "conversion" via la lib OpenHtmlToPDF que fait le wrapper `HTMLToPDFTool`:

```
import org.jsoup.Jsoup;
import org.jsoup.helper.W3CDom;
import org.w3c.dom.Document;
import com.openhtmltopdf.pdfboxout.PdfRendererBuilder;

(...)

try (ByteArrayOutputStream os = new ByteArrayOutputStream())
{
	Document doc = new W3CDom().fromJsoup(Jsoup.parse(html));
	new PdfRendererBuilder().toStream(os).withUri(baseURL).withW3cDocument(doc, null).run();
	return os.toByteArray();
}
```
