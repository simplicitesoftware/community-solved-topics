# Format des nombres

**URL:** https://community.simplicite.io/t/11388

## Question
### Request description

Bonjour,

Pour une application en anglais, j'essaie de formater les décimaux au format DC
- point pour les milliers
- virgule pour les décimales

Et j'ai des questions :slight_smile: 

- est-il possible de le configurer au niveau de la langue, et pas par utilisateur ? Sinon comment forcer ce format par défaut pour tous ? Par code peut-être ?
- pour l'instant j'ai tenté le choix "DC" au niveau utilisateur et j'ai un comportement étrange sur un pourcentage : si je saisis mon pourcentage avec une virgule, la virgule disparaît quand je sors du champ - mais si je le saisis avec un point, il se transforme en virgule. 

[EDIT]
Je vois que la langue est celle par défaut (EN) à la saisie, et celle surchargée sur le user au chargement du form

*Load*
![image|690x70](upload://ctSQgfY9FR85V6eFlwrGjAoYRxO.png)

*Click sur le champ*
![image|690x56](upload://uP532Cqx9IGxjOet9FCRkNZ9kmD.png)


J'ai vu qu'il y avait une [évolution](https://community.simplicite.io/t/separateur-decimal-en-anglais/6154/6) en 5.3, mais je ne sais pas trop comment l'utiliser.

Merci d'avance pour votre aide !
Emmanuelle

[Platform]
Status=OK
Version=6.2.20
BuiltOn=2026-01-02 22:59

## Answer
Ok donc revient à un décimal flottant simple, un `big-décimal` doit mal gérer le formatage.
on va essayer de l'améliorer mais ici je ne pense pas que ce soit ton besoin.
Un `double` gère très bien une précision de (10,4) suffisant pour un pourcentage ?

Attention l'ALTER risque de ne pas marcher (varchar => double)
