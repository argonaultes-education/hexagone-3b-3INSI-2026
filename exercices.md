# Docker

## Exercice 1 - Conteneur postgres

Créer un conteneur basé sur l'image Postgres, et faire en sorte de se connecter à l'instance Postgres, sur la base de données tprevision en utilisant un autre conteneur possédant le binaire psql.

Le second conteneur doit être éphèmère - donc détruit à la fin de son exécution.

L'accès depuis le second conteneur au conteneur de l'instance doit se faire via un alias DNS exclusivement.

![](./schema-exo1.png)

### Solution

1. Créer un conteneur correspondant à l'instance postgres avec la base de données par défaut `tprevision`

```bash
docker run --name db -d -e POSTGRES_DB=tprevision -e POSTGRES_PASSWORD=password  postgres:latest
```


2. Créer un nouveau sous réseau `revision_network`

```bash
docker network create revision_network
```


3. Associer le conteneur #1 au sous réseau `revision_network` avec l'alias DNS `db`

```bash
docker network connect revision_network db --alias db
```

4. Créer un conteneur éphèmère interactif rattaché au sous réseau `revision_network` déclenchant l'exécution d'une commande psql

```bash
docker run --rm --network revision_network -it postgres:latest psql -h db -U postgres tprevision
```

## Exercice 2 - Dind


Créer un conteneur basé sur l'image [dind](https://hub.docker.com/_/docker).

Créer un second conteneur capable de créer des conteneurs invisibles pour la machine hôte en utilisant le conteneur #1.

Depuis ce second conteneur, créer une instance postgres comme cela a été fait dans le 1er exercice.
