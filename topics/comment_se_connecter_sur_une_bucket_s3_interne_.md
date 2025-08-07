# Comment se connecter sur une bucket S3 interne?

**URL:** https://community.simplicite.io/t/3260

## Question
Bonjour,
ma question est posée dans un contexte de v4 - Version=4.0.P25 BuiltOn=2021-04-23 19:51 (revision 3addcb9b49a1c3b8d3cfe4fd9e06a69e2d4b9681) mais se pose aussi potentiellement sur la v5.

Comment puis-je **initialiser un CloudStorageTool sur une bucket S3 interne** (cf. illustration "use Amazon S3 compatible storage" ci-dessous) ?

à la lecture de la documentation disponible, je crois comprendre qu'il faudrait pouvoir surcharger (override) la propriété [AtrifactID].endpoint (aws-s3.endpoint?) avec l'URL de notre conteneur privé...

Est-ce possible avec l'intégration actuelle sachant que le bloc JSON de configuration proposé dans la doc n'explicite pas ce cas ?
```
{
    "provider": "aws-s3",
    "accessKeyId": "<your access key ID>",
    "secretAccessKey": "<your access key secret>",
    "bucket": "<your bucket name>"
}
```

![image|606x119](upload://o9JxdYzBH6YP6P2NTkkOiH5nJQA.png)

## Answer
Tu as pu tester avec la nouvelle version de `CloudStorageTool` car ça gère désormais le provider "s3" et le paramètre `endpoint`
