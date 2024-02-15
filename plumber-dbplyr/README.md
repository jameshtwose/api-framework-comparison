### Plumber + dbplyr
#### R
- `brew install libsodium`
- `R -e "install.packages(c('sodium', 'plumber', 'dbplyr', 'RPostgres'), repos='https://cloud.r-project.org/')"`
- `Rscript main.R`

#### Docker
- `docker build -t plumber-dbplyr .`
- `docker run -d -p 8083:8083 plumber-dbplyr`