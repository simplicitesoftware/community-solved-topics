# [CI/CD] Automatic module imports at startup

**URL:** https://community.simplicite.io/t/3982

## Question
Bonjour @scampano,

J'adore la feature de déploiement automatique. Avec docker-compose ça marche très bien également.

Est-il possible de spécifier la branche du repo git ?

Merci d'avance.

## Answer
Je veux dire : si c'est une spec d'import de ce type que vous utilisez:

```yaml
modules:
- name: "<Module name>"
  version: "<Module version>"
  git: "<Git repo URI>"
- ...
```

alors on ne peut pas préciser la branche.

Il faut utiliser une spec d'import du type: 

```yaml
modules:
- name: "<Module name>"
  version: "<Module version>"
  git:
    uri: "<Git repo URI>"
    branch: "<Branch>"
    ...
- ...
```
