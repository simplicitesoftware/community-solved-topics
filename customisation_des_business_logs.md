# Customisation des business logs

**URL:** https://community.simplicite.io/t/4605

## Question
Bonjour,

  par défaut sur la plateforme Simplicite, il existe déjà des logs event et des logs activable et paramétrable à notre convenance.

est ce qu'il est possible de créer nos propres logs events et si oui comment les appeler via AppLog

Cordialement,
Olivier Migliorini

## Answer
[quote="Benoit, post:15, topic:4605"]
quel est l’impact du setting “Targets” suivant
[/quote]

* **Logger** => envoie le log à Log4j pour inscription dans le `simplicite.log`
* **Database** => envoie le log dans la table m_log de l'objet Logs (Operation > Logs)
