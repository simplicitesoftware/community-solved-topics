# Redirection sur le formulaire parent lors du changement de statut d'un enfant

**URL:** https://community.simplicite.io/t/11492

## Question
*Bonjour,*

J’ai un objet parent qui a plusieurs objets enfants.

Lorsque je suis sur le formulaire enfant et que je valide le formulaire, j’aimerais que mon action (qui change le statut de l’enfant) me redirige vers le formulaire parent.

Merci pour votre aide.

###

## Answer
Bonjour et merci pour votre réponse.

Ca fonctionne parfaitement en adaptant ce code dans ma fonction postUpdate lorsque je vérifie un changement de statut avec la methode hasChanged() de mon statut field.
