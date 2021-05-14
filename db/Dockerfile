# Create from official postgress image
FROM postgres:9.4

# Add a database
ENV POSTGRES_DB testdb

# Initial db scripts
COPY ./init-scripts /docker-entrypoint-initdb.d/