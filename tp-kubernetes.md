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