FROM rstudio/r-base:4.0-xenial

# install R packages
RUN R -e "install.packages(c('plumber', 'dbplyr', 'RPostgres'), repos='https://cloud.r-project.org/')"

COPY api.R /api.R
COPY main.R /main.R

CMD ["Rscript", "main.R"]