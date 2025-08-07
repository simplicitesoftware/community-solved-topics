# Release 5.2.26 absent from docker registry

**URL:** https://community.simplicite.io/t/5679

## Question
### Problem description

The image registry.simplicite.io/platform:5.2.26 is absent from docker registry

### Steps to reproduce

```shell
$ docker pull registry.simplicite.io/platform:5.2.26

Failed to pull image "registry.simplicite.io/platform:5.2.26": rpc error: code = Unknown desc = Error response from daemon: manifest for registry.simplicite.io/platform:5.2.26 not found: manifest unknown: manifest unknown
```

## Answer
Le tag `5.2.26` vient d'être ajouté. 
Vous pouvez désormais bien faire un `docker pull registry.simplicite.io/platform:5.2.26`
