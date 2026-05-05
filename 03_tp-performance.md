# Tests de performance


## Outils

Les outils à tester

* k6 : JavaScript
* Apache JMeter : XML (GUI)
* Locust : Python
* (Postman) : GUI

* LoadRunner (HP) : C

## Préparer environnement de test

Récupérer les sources du projet todo-api

```bash
git clone https://github.com/argonaultes-education/todos-api.git
```

Construire en l'image en ayant effectué les modificaitons nécessaires

```bash
docker build -t todo-api-hexagone:2026 .
```

Créer le sous-réseau

```bash
docker network create todoapi_network
```

Démarrer le conteneur

```bash
docker run -d --network todoapi_network --network-alias todoapi --name todo-api --rm -p 3002:3002 --cpus 2 --memory 4G --memory-swap 4G argonaulteshexagone/todo-api-hexagone:2026
```

## k6

![](./images/perf-1-k6.png))

Démarrer k6 et créer un nouveau fichier en se basant sur la [documentation](https://grafana.com/docs/k6/latest/using-k6/http-requests/).


```javascript
import http from 'k6/http';

export default function () {
  http.get('http://localhost:3002');
}
```

Récupérer l'image

```bash
docker pull grafana/k6
```

Démarrer notre script

```bash
docker run --network todoapi_network --rm -t -v ./performance/:/performance/ grafana/k6 run /performance/script.js
```

Augmenter la durée du test et le nombre d'utilisateurs

```bash
docker run --network todoapi_network --rm -t -v "${pwd}/performance/:/performance/" grafana/k6 run --vus 10 --duration 30s /performance/script.js
```

Ajouter les variables d'environnement pour augmenter le nombre de boucles et exporter les résultats ous forme de tableau de bord

```bash
docker run -e NB_LOOPS=2 -e K6_WEB_DASHBOARD=true -e K6_WEB_DASHBOARD_EXPORT=/performance/output/html-report.html --network todoapi_network --rm -t -v ./performance/:/performance/ grafana/k6 run --vus 10 --duration 30s /performance/script.js
```

## Apache JMeter

### Prérequis

Vérifier que Java 8+ est disponible

```bash
java -version
```

### Installation

Télécharger et extraire les composantes de l'archive

```bash
wget https://dlcdn.apache.org//jmeter/binaries/apache-jmeter-5.6.3.tgz
```

Extraire le composants

```bash
tar -xzf apache-jmeter-5.6.3.tgz
```

Aller dans le dossier `./apache-jmeter-5.6.3/bin/` et lancer le script

```bash
./jmeter
```

Rendre accessible depuis le PATH les scripts jmeter

```bash
export PATH=/datadisk/apache-jmeter-5.6.3/bin:$PATH
```


Lancer le script avec la commande

```bash
jmeter -n -t performance/testplan.jmx -l performance/output/testplan.log -e
```

Attention, cette commande crée les ressources suivantes :

* `report-output/statistics.json`
* `performance/output/testplan.log`
* `jmeter.log`

## Nouveau système soumis à des tests

Application avec une page qui présentera un formulaire demandant un titre de jeu.

L'application présentera le nombre de fois que ce jeu a été renseigné.

### Marche à suivre pour la création du projet

Initialiser le projet

```bash
uv init --bare .
```

Ajouter le module flask au projet

```bash
uv add flask
```

Modifier les scripts, etc...

Démarrer le serveur en utilisant comme script d'entrée le fichier `main.py`

```bash
uv run flask --app main run --debug
```

Si besoin, pour extraire la liste des dépendances au format requirements

```bash
uv export --format requirements-txt > requirements.txt
```


### Exercice 1

Créer 1 script, au format XML (JMX), avec JMeter qui suit le scénario :

1. afficher la page contenant l'input
2. envoyer une valeur de jeu prise au hasard parmi une liste prédéfinie
3. vérifier que la réponse contient la valeur envoyée ainsi que la valeur de `count` > 0

Une fois le script réalisée, lancer le test avec 10 utilisateurs pour 10 itérations et 2 itérations par thread

```bash
jmeter -n -t performance/testplan-sut.jmx -Jthreads=10 -Jrampup=10 -Jloopcount_thread=10 -Jloopid=2 -l performance/output/testplan-sut.log -e
```

Rajouter dans la sortie du script jmeter le label utilisé pour le jeu

Aprè avoir créé l'image format dev de l'application,

```bash
docker build -t hexagone-sut:2026 .
```

Créer un conteneur avec des ressources limités

```bash
docker run -p 5000:5000 --rm --cpus 4 --memory 2G --memory-swap 2G hexagone-sut:2026
```

Faire le même script avec k6

#TODO prochaine séance pour révision

### Exercice 2

Récréer la stack complète des 3 bases avec adminer et nginxlb (sur compose).

Réaliser un scénario de test de performance qui reprend les actions suivantes :

1. affichage de la page de connexion de adminer
2. saisie des identifiants de connexion à la base erp
3. affichage de la page de saisie de requête sql
4. envoie d'une requête sql de création de tables `create table if not exists test_table_$threadid(id serial primary key)`
5. envoie d'une requête sql d'insertion de données  `insert into test_table_$threadid default values`
6. déconnexion
7. reconnexion
8. affichage de la saisie sql
9. envoie d'une requête sql de sélection des lignes existantes dans la table : `select * from test_table_$threadid` : vérifier que le nombre de lignes renvoyées est strictement supérieur à 1
10. déconnexion

Rendre le script dynamique pour permettre la navigation sur les 3 bases de données avec différents utilisateurs.

Initialiser les bases de données avec dix utilisateurs allant de `user1` à `user10` et le mot de passe `password1` à `password10`.

Consulter la [documentation Postgres](https://www.postgresql.org/docs/18/sql-createrole.html) pour la création de nouveaux utilisateurs.

```sql
CREATE ROLE user1 WITH LOGIN CONNECTION LIMIT 2 PASSWORD 'password1';
GRANT CREATE ON SCHEMA public TO user1;
```

Relancer via la commande suivante un smoke test 

```bash
jmeter -n -t performance/testplan-adminer.jmx -Jthreads=10 -Jrampup=10 -Jloopcount_thread=10 -l performance/output/testplan-adminer.log -e
```