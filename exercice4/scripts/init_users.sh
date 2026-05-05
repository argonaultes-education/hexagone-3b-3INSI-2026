#!/usr/bin/env bash
set -e

for id in $(seq 1 10) ; do
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" -c "CREATE ROLE user${id} WITH LOGIN CONNECTION LIMIT 2 PASSWORD 'password'"
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" -c "GRANT CREATE ON SCHEMA public TO user${id}"
done