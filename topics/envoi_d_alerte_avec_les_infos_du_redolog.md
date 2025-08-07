# Envoi d'alerte avec les infos du RedoLog

**URL:** https://community.simplicite.io/t/4443

## Question
Version : 5.1.29

Bonjour,

Je souhaite intégrer la log de modification de l'objet dans l'alerte (je récupère le dernier enregistrement de table m_redolog lié à mon objet).
Mon souci, c'est que je n'arrive pas à récupérer la log de la modif en cours mais celle d'avant.

Pouvez-vous svp me dire comment je veux faire ?

Ps : 
  - La log est récupérée avec une requête SQL dans le hook preAlert.
  - Le send est asynchrone.

## Answer
On parle d'une alerte déclenchée sur transition d'état ?

Si oui je pense que l'alerte est envoyée avant que le redo log ne soit constitué.

Vous pouvez, je pense, facilement refabriquer le delta dans le `preAlert` en itérant sur les fields et en comparant la value et la oldvalue

```java
StringBuilder delta = new StringBuilder();
for (ObjectField f : getFields()) {
  if (!f.getValue().equals(f.getOldValue())
    delta.append(f.getDisplay() + " changed from [" + f.getOldValue() + "] to [" +f.getValue() + ]");
}
```
