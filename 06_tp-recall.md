# TP

## Vue conceptuelle

![](./tp.png)

## Description détaillée

L'objectif est de fournir un environnement stable de travail accessible en SSH depuis un pod éphémère.

L'environnement de travail doit être scalable (horizontalement). Les données créés par l'utilisateur doivent être conservées et récupérables quelque soit le nombre d'environnements.

Pour compléter l'environnement, 2 solutions de supervision accompagnent l'environnement de travail :
* le couple prometheus/grafana lié à un client personnalisé écrit en Python
* un client gRPC capable de lister le contenu du dossier de travail de l'utilisateur

## Vue technique



## Livrables

* Image Docker qui permet de créer un serveur SSH basé sur une debian : **Dockerfile**
* Image Docker qui permet de démarrer un serveur gRPC dont la fonction est de lister le contenu d'un dossier : **Dockerfile**
* Image Docker qui permet d'exposer une métrique au format prometheus qui compte le nombre de connexions tracées dans un fichier de log SSH : **Dockerfile**
* Image Docker qui permet d'utiliser un client SSH : **Dockerfile**
* Image Docker qui permet de faire appel a gRPC server : **Dockerfile**
* Images déjà construites :
  * **Grafana**
  * **Prometheus**
* Dossier kustomization qui permet de construire les ressources suivantes via des fichiers yaml :
  * volumes
    * grafana
    * prometheus
    * ssh_user
  * statefulset
    * prometheus
    * grafana
  * déploiement
    * sshmachine
  * services
    * prometheus (ClusterIP)
    * grafana (NodePort)
    * sshmachine (ClusterIP ssh)
    * sshmachine (ClusterIP http prom)
    * sshmachine (ClusterIP proto grpc)

## Liste de tâches

* [ ] todo 1
