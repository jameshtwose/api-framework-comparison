# api-framework-comparison
A comparison of an assortment of popular API frameworks in various languages. The project will be an API that interacts with a postgres database and performs CRUD operations. Everything will be run in the final comparison using docker-compose.

## Data
- data is complaints data taken from kaggle
- https://www.kaggle.com/datasets/anoopjohny/consumer-complaint-database

## Commands
- `docker compose up -d` - Starts the postgres database and the api
- exec into the postgres container and run `psql -U postgres` to connect to the database

## Comparisons
- speed
- ease of use
- size
- documentation
- load testing
- error handling
- security
- community

## Frameworks
### Python
- fastapi + sqlalchemy (ORM) [x]
- fastapi + psycopg2 (SQL) [x]

### Node
- express + sequelize (ORM) [x]
- express + pg (SQL)

### Go
- gin + gorm (ORM)
- gin + sqlx (SQL)

### Rust
- rocket + diesel (ORM)
- rocket + sqlx (SQL)

### Java
- spring + hibernate (ORM)
- spring + jdbc (SQL)

### C#
- asp.net + entity framework (ORM)
- asp.net + ado.net (SQL)

### PHP
- laravel + eloquent (ORM)
- laravel + pdo (SQL)

### Ruby
- rails + active record (ORM)
- rails + pg (SQL)

### Kotlin
- ktor + exposed (ORM)
- ktor + jdbc (SQL)

### Scala
- akka + slick (ORM)
- akka + jdbc (SQL)

### Dart
- aqueduct + aqueduct (ORM)
- aqueduct + postgresql (SQL)

### Elixir
- phoenix + ecto (ORM)
- phoenix + postgresql (SQL)

### Clojure
- compojure + honeysql (ORM)
- compojure + jdbc (SQL)

### Crystal
- kemal + granite (ORM)
- kemal + pg (SQL)

### R
- plumber + dbplyr (ORM)
- plumber + RPostgreSQL (SQL)

### Julia
- Genie + GenieORM (ORM)
- Genie + LibPQ (SQL)