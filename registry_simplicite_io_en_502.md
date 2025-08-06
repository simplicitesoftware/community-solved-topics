# Registry.simplicite.io en 502

**URL:** https://community.simplicite.io/t/9659

## Question
Bonjour,

j'essaye de pull la dernière image 6.1.24 et mon pipeline échoue systématiquement (après plusieurs tentatives) sur l'erreur suivante :

```
echo ${DOCKER_SIMPLICITE_PASSWORD} | docker login -u ${DOCKER_SIMPLICITE_USERNAME} --password-stdin registry.simplicite.io

Error response from daemon: login attempt to https://registry.simplicite.io/v2/ failed with status: 502 Bad Gateway
```

Y-a-t-il un problème avec le service registry.simplicite.io ?

Voici les traces verbeuses d'un test d'accès via curl depuis mon poste (hors contexte de pipeline gitlab) :
```
curl --verbose https://registry.simplicite.io/v2/
* Uses proxy env variable https_proxy == 'http://***:***@cosmos-vip.intra.renault.fr:3128'
*   Trying 138.21.169.26:3128...
* Connected to cosmos-vip.intra.renault.fr (138.21.169.26) port 3128 (#0)
* allocate connect buffer!
* Establish HTTP proxy tunnel to registry.simplicite.io:443
* Proxy auth using Basic with user '***'
> CONNECT registry.simplicite.io:443 HTTP/1.1
> Host: registry.simplicite.io:443
> Proxy-Authorization: Basic ***
> User-Agent: curl/7.71.1
> Proxy-Connection: Keep-Alive
>
< HTTP/1.1 200 Connection established
<
* Proxy replied 200 to CONNECT request
* CONNECT phase completed!
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
  CApath: none
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* CONNECT phase completed!
* CONNECT phase completed!
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=registry.simplicite.io
*  start date: Feb  8 22:05:22 2025 GMT
*  expire date: May  9 22:05:21 2025 GMT
*  subjectAltName: host "registry.simplicite.io" matched cert's "registry.simplicite.io"
*  issuer: C=US; O=Let's Encrypt; CN=R11
*  SSL certificate verify ok.
* Using HTTP2, server supports multi-use
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* Using Stream ID: 1 (easy handle 0x7fffdc8ede20)
> GET /v2/ HTTP/2
> Host: registry.simplicite.io
> user-agent: curl/7.71.1
> accept: */*
>
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* old SSL session ID is stale, removing
* Connection state changed (MAX_CONCURRENT_STREAMS == 128)!
< HTTP/2 502
< server: nginx
< date: Wed, 12 Mar 2025 09:10:30 GMT
< content-type: text/html
< content-length: 166
<
<html>
<head><title>502 Bad Gateway</title></head>
<body bgcolor="white">
<center><h1>502 Bad Gateway</h1></center>
<hr><center>nginx</center>
</body>
</html>
* Connection #0 to host cosmos-vip.intra.renault.fr left intact
```

## Answer
Ca devrait être bon, le reverse proxy en amont du registre était visiblement en vrac...
