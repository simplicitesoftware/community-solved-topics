# Question chiffrement des données via la méthode EncryptionTool.encrypt

**URL:** https://community.simplicite.io/t/9056

## Question
### Description

Bonjour,

Quel algorithme de chiffrement est appliqué par la méthode EncryptionTool.encrypt ?
On comprend que l'on utilise l'algorithme spécifié dans le paramètre DEFAULT_ENCRYPTION_ALGORITHM  donc ça serait de l'AES.
Est ce bien cela ?

En complément, quel est l'encoding utilisé ? base64 ?

Cordialement,

## Answer
PS: La méthode `public static String encrypt(final String value, final String key)` renvoie une chaine de caractères contenant le `byte[]` crypté encodé en Base 64, et la méthode `public static String decrypt(final String value, final String key)`  prend bien en argument une telle chaine de caractères encodée en Base 64

On va le préciser dans la Javadoc
