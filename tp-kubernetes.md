# Kubernetes

## Installation

Minikube

```bash
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
```

## Démarrage

```bash
minikube start --driver docker
```

```bash
minikube kubectl -- get po -A
```

```bash
minikube kubectl -- get namespace
```


```bash
minikube dashboard
```

## Exercice 1 : Créer un déploiement (self-healing)

```bash
kubectl create deployment deploynginx --image=nginx:latest
```

Essayer de supprimer le pod déployé

```bash
kubectl delete pod/deploynginx-
```

Créer une ressource pod simple

```bash
kubectl run podnginx --image=nginx:latest
```

Supprimer le pod podnginx

```bash
kubectl delete pod/podnginx
```


## Exercice 2 : Rollback

Augmenter le nombre de pods dans un déploiement

```bash
kubectl scale deployment deploynginx --replicas=3
```

Afficher plus de détails sur une ressource

```bash
kubectl describe deploy/deploynginx
```


Une fois déployé, intéressons-nous à la nouvelle commande

```bash
kubectl rollout --help
```

Cette commande ne s'applique qu'à 3 types de ressources (deployments, daemonsets, statefulsets).


Pour consulter l'historique de versions

```bash
kubectl rollout history deployment deploynginx
```

Pour afficher le détail de la révision 1

```bash
kubectl rollout history deployment deploynginx --revision=1
```

Pour créer une nouvelle version, nous allons mettre à jour un élément qui est versionné, à savoir l'image par exemple

```bash
kubectl set image deployment deploynginx nginx=nginx:stable-alpine3.18-slim
```

Vérifier qu'une nouvelle version a bien été inscrite

```bash
kubectl rollout history deployment deploynginx
```

Consulter la nouvelle version

```bash
kubectl rollout history deployment deploynginx --revision=2
```

Défaire la dernière action compatible rollout

```bash
kubectl rollout undo deployment deploynginx
```

## Exercice 3 : 

Créer le déploiement hr-deploy avec 1 pod

```bash

```

Créer le déploiement crm-deploy avec 1 pod

```bash

```


Créer le déploiement erp-deploy avec 1 pod

```bash

```


Créer le déploiement admin-deploy avec 3 pods

```bash

```


Accéder aux bases de données en passant par le proxy

```bash

```
