# Préconisations base de données

**URL:** https://community.simplicite.io/t/6238

## Question
### Request description

Bonjour,

Nous réfléchissons à externaliser la base de données de notre solution dans un cube On premise.
Est-ce que c'est une configuration recommandée, déconseillée, aucun des deux ?

Merci !
Emmanuelle

## Answer
Tout dépend de la qualité de la connexion réseau entre l'instance Simplicité et la base de données... c'est ce que j'entends par "pas trop distante": ex: Si chaque requête SQL prends 500ms de latence réseau parce que ça transite par 10 firewalls et 3 proxies ce sera globalement catastrophique niveau performances.

Sinon aucun pb. C'est comme ça que de nombreux clients déploient Simplicité (par exemple sur un cloud - ex: AWS ECS/EKS - avec Simplicité en container(s) et une base managée "as a service" externe - ex: AWS RDS).

De manière plus générale, la base de données est l'élément clé de l'architecture d'une application Simplicité = elle contient les données et les méta données (le paramétrage et le code). Il faut donc faire en sorte qu'elle soit performante vis à vis de l'usage qui en est fait depuis Simplicité = intrinsèquement performante + accessible avec de bonnes performances, et bien sûr mettre en place les processus de sauvegarde qui vont bien. C'est la base qui est la plus déterminante pour les performances, il ne sert, par exemple, strictement à rien de multiplier les noeuds Simplicité, si ils pointent sur une base de donnée peu performante.
