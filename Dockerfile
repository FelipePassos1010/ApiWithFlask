FROM mysql:5.7

COPY ./db/ /docker-enterypoint-initdb.d/