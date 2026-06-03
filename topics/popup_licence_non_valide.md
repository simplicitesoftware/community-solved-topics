# Popup Licence non valide

**URL:** https://community.simplicite.io/t/12403

## Question
Bonjour,
Je rencontre une erreur lors de enregistrement d'une clé de licence officielle : la même clé XML est validée correctement sur une instance en 6.3.6 et rejetée sur une instance en 6.3.9 déployée avec une SIM. Une régression a peut-être eu lieu sur le 'LicenseTool.isValid' ?

Au niveau des logs sur la 6.3.9, j'ai un **FCORELI001|system|com.simplicite.util.tools.LicenseTool|isValid||License error: please contact your support.**.

Conséquence, l'enregistrement de la clé, après avoir vidé le cache, redirige, en l’occurrence le designer vers la page de gestions des licences, qui affiche la la popup "Licence Invalide".
Le scope selector n'est pas accessible ('/ui?scope=Home) et dès que je supprime cette clé, l'instance revient à la licence par défaut et designer retrouve l'accès normal.


[Platform]
Status=OK
Version=6.3.9
Variant=light
BuiltOn=2026-05-08 12:14
Git=6.3/58e3ee3f94cecfc8aaa762e57a41f8e5bdf91454

Merci d'avance pour votre aide

## Answer
Je suppose qu'on parle de la clé "Sesame" sur le SIM du SID

L'instance SIM que vous avez déployée est donc déployée en `/<nom de l'instance>` et pas en root `/` 

Du coup la licence Sesame fournie est invalide car elle est pour `/` (contrairement à la licence par défaut qui, elle, est pour `*`)

@Ornan merci de nous communiquer le `/<nom de l'instance>` que vous avez déployé
@Thomas_Repolt il va falloir générer la clé avec pour ce `/<nom de l'instance>`
