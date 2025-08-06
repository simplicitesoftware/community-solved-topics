# JVM indicateurs

**URL:** https://community.simplicite.io/t/5634

## Question
Bonjour,

A quoi correspond la valeur 98% dans l'image jointe  ? Quelle est son utilité ?
De ma vision, que le free memory est important.

![image|690x184](upload://slT81ZlP0TahQajkBY9olzhWhEh.png)

Cordialement,

## Answer
Ca indique que la JVM a alloué 98% de la mémoire max possible = alloc 515Mo / max 524Mo
Ca veut pas dire que les threads n'ont plus de mémoire/saturée car Free heap est encore à 150Mo.
Mais bien que la JVM a réellement bloqué 515Mo niveau OS sur les 524Mo possibles.

il faut activer et regarder le monitoring "heap size" pour plus de précisions.

Il y a 4 courbes : 
- le max imposé à la JVM = constante plafond
- l'allocated qui varie peu / par palier d'après et en prévision des usages : mémoire vraiment réservée niveau OS
- et le réellement utilisé par les threads qui est en dent de scie à chaque passage du GC
- le min imposé à la JVM : quand on sait que la JVM a besoin d'une certaine quantité en régime nominal, on peut lui donner d'office au démarrage, et l'allocated ne pourra pas aller en dessous

L'allocated sert à éviter des appels system couteux pour demander de la mémoire à l'OS / pre-réservations.
