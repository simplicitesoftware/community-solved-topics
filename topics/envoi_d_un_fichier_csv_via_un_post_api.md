# Envoi d'un fichier CSV via un post API

**URL:** https://community.simplicite.io/t/6324

## Question
### Request description

*Bonjour, je souhaite réaliser une requête POST via une API externe à Renault comportant 2 champs: Currency_Exchange_Rates_Accrued (fichier CSV) et jwt (token sous forme de string). J'ai crée une méthode en rajoutant l'utilisation de proxy (que je collerai plus bas dans le poste), mais je tombe systématiquement sur une erreur 404: {"code":404,"message":"Not Found"}. Néanmoins, sur Postman, le post fonctionne normalement.*

### Steps to reproduce

```
public static JSONObject postCsvJSON(Grant grant, String url, String filePath, String jwtToken) {
  setLogLevel(grant, Level.INFO);
  Unirest.config().clientCertificateStore(CERTIFICATE_PATH, CERTIFICATE_PASSWORD);
  HttpRequestWithBody request = Unirest.post(url);
  boolean needProxy = !url.startsWith(Grant.getSystemAdmin().getContextURL()) && !Grant.getSystemAdmin().getContextURL().endsWith("simplicite.io");
  if (needProxy) {
    String proxyData = Grant.getSystemAdmin().getParameter("RENAULT_PROXY");
    String proxyHost = null;
    String proxyPort = null;
    if (StringUtils.isNotBlank(proxyData)) {
      String[] proxyDataPart = proxyData.split(",");
      proxyHost = proxyDataPart[0].trim();
      proxyPort = proxyDataPart[1].trim();
    } else {
      if (url.startsWith("https")) {
        proxyHost = System.getProperty("https.proxyHost");
        proxyPort = System.getProperty("https.proxyPort");
      } else {
        proxyHost = System.getProperty("http.proxyHost");
        proxyPort = System.getProperty("http.proxyPort");
      }
    }
    request.proxy(proxyHost, Integer.parseInt(proxyPort));
  }

  final kong.unirest.HttpResponse < String > response;

  File file = new File(filePath);
  response = request.header(HttpHeaders.CONTENT_TYPE, "multipart/form-data")
    .field("Currency_Exchange_Rates_Accrued", file)
    .field("jwt", jwtToken)
    .asString();

  if (response.isSuccess()) {
    return new JSONObject(response.getBody());
  } else {
    return new JSONObject().put("code", response.getStatus()).put("message", response.getStatusText());
  }
}
```

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.2.38
BuiltOn=2023-04-20 10:56
Git=5.2/66dd3f848850f0ba670a5f92674282285b3d3341
Encoding=UTF-8
EndpointIP=172.17.0.6
EndpointURL=http://902b2556b6d5:8080
TimeZone=Europe/Paris
SystemDate=2023-05-03 11:24:52
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
C'est la réflexion que j'ai eu en voyant l'erreur, je vais regarder cela de plus près avec un DevOps. 
Je vous en remercie.
