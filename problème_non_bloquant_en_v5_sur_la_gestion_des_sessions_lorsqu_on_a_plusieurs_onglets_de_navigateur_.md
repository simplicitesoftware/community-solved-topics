# Problème non bloquant en v5 sur la gestion des sessions lorsqu'on a plusieurs onglets de navigateur ouverts en parallèle

**URL:** https://community.simplicite.io/t/4112

## Question
Bonjour,

en v4, il était possible de travailler avec plusieurs onglets ouverts (un pour l'éditeur de code, d'autres pour la configuration des objets, d'autres pour les tests, etc.), de faire un clear cache - y compris global - puis de simplement se reconnecter sur un des onglets, les autres récupéraient la nouvelle session et le contexte de travail de chaque onglet n'était pas perdu (il suffisait de recharger le formulaire ou la liste courante).

en v5, les autres onglets deviennent inutilisables (moulinent dans le vide) et il faut recharger complètement la page dans le navigateur puis recharger le contexte initial (éditeur de code, configuration d'objet, etc.).

Est-ce lié à un changement structurant dans la gestion du cache ou des sessions ?
C'était très pratique et permettait de gagner un temps certain.

## Answer
Ca fonctionne :

- il n'y a pas de dégradation de perfs d'accéder au local storage à chaque call pour récupérer la bonne clé
- si le navigateur n'a pas de local storage, on reste sur l'ancien fonctionnement, mais c'est par sécurité car tous les navigateurs modernes en ont un.

On backporte pour la prochaine 5.1.
