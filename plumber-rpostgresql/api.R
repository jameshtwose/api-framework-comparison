# api.R

library(DBI)
library(RPostgres)

# get postgres connection
con <- DBI::dbConnect(RPostgres::Postgres(), 
                      dbname = "postgres",
                      # localhost if running from command line
                      # host = "localhost",
                      # docker container name (postgres) if running from docker
                      host = "postgres",
                      port = 5432,
                        user = "postgres",
                        password = "changeme")

#* Get a welcome message
#* @serializer json
#* @get /
function() {
  list(hello = "Welcome to the plumber-rpostgresql API!")
}

#* Get complaints
#* @serializer json
#* @param limit The number of complaints to return
#* @get /complaints
function(limit=10) {
  # get first X complaints
    complaints <- dbGetQuery(con, "SELECT * FROM complaints_table", n=as.numeric(limit))
    complaints_list <- split(complaints, seq(nrow(complaints)))
    # complaints_list <- setNames(split(complaints, seq(nrow(complaints))), rownames(complaints))
    complaints_list
}
