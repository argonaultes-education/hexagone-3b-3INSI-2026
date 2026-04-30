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
docker run --network todoapi_network --rm -t -v ./performance/:/performance/ grafana/k6 run --vus 10 --duration 30s /performance/script.js
```