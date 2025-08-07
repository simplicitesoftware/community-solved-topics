# Comment empêcher la méthode "preload" de se ré-exécuter lors de l'utilisation de l'Action?

**URL:** https://community.simplicite.io/t/5696

## Question
Bonjour,

Je voudrais vider les champs d'un formulaire lorsque je l'ouvre, pour éviter de devoir le faire manuellement. Pour ce faire, j'ai utilisé la méthode "preload" qui semble fonctionner correctement lors de l'ouverture du formulaire.

Le problème est que lorsque j'utilise l'Action présent sur le formulaire, la méthode "preload" se ré-exécute et vide malheureusement la donnée que j'ai entrée dans les champs. Sauriez-vous comment éviter cela et comment garder la donnée entrée dans les champs lors de l'utilisation de l'Action ?

Merci d'avance pour votre aide !

______ Health Check _______

[Platform]
Status=OK
Version=5.1.54
BuiltOn=2022-10-31 15:49
Git=5.1/06cc2793ebaaa50ddf3f3dee2251b397d7bdc09b
Encoding=UTF-8
EndpointIP=172.20.180.245
EndpointURL=http://mla-api-5858675499-scwrn:8080
TimeZone=Europe/Paris
SystemDate=2023-01-03 16:38:20

## Answer
Bonjour, 

Le hook `preLoad` n'est pas adapté à votre besoin. Il est appelé au chargement de la définition de l'objet et non pas à l'affichage d'un formulaire. 
Utilisez plutôt le hook `initUpdate` dans le cadre d'ouverture d'un formulaire en **update** ou `initCreate` dans le cadre d'ouverture d'un formulaire de **création**.

Lorsque vous parlez de "vider les champs", il s'agit des champs du formulaire ou des attributs de l'action ?
