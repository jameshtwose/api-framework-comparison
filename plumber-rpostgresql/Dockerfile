# FROM rstudio/r-base:4.0-xenial
FROM rocker/tidyverse:latest

# install R packages
# RUN R -e "install.packages(c('plumber', 'DBI', 'RPostgres'), repos='https://cloud.r-project.org/')"

RUN install2.r --error plumber DBI RPostgres

COPY api.R /api.R
COPY main.R /main.R

EXPOSE 8084

CMD ["Rscript", "main.R"]