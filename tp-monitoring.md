# Monitoring

## Prometheus

Présentation de l'architecture globale

![](https://prometheus.io/assets/docs/architecture.svg)

### Installation et premiers pas

Démarrer un conteneur docker basé sur l'image `prom/prometheus`

```bash
docker run -p 9090:9090 prom/prometheus
```

Accéder à l'interface web de gestion et de configuration

Voir `http://localhost:9090/`

Accéder au point d'accès qui expose les metrics.

Voir `http://localhost:9090/metrics`

Récupérer le fichier de configuration global

Modifier les valeurs de scrapping :

* scrape_interval: 10s
* scrape_timeout: 20s

Ensuite essayer avec les valeurs suivantes :

* scrape_interval: 10s
* scrape_timeout: 5s
