### Plumber + RPostgres
#### R
- `brew install libsodium`
- `R -e "install.packages(c('sodium', 'plumber', 'RPostgres'), repos='https://cloud.r-project.org/')"`
- `Rscript main.R`

#### Docker
- `docker build -t plumber-rpostgresql .`
- `docker run -d -p 8084:8084 plumber-rpostgresql`