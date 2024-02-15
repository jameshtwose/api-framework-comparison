library(dbplyr)
library(DBI)
library(RPostgres)
library(tibble)

# get postgres connection
con <- DBI::dbConnect(RPostgres::Postgres(), 
                      dbname = "postgres",
                      host = "localhost",
                      port = 5432,
                        user = "postgres",
                        password = "changeme")

# get first 10 complaints
complaints_table <- dplyr::tbl(con, "complaints_table")
complaints <- dplyr::collect(complaints_table)
complaints <- head(complaints, 10)
# print(complaints)
# get complaints as named list
print(as.list(tibble::deframe(complaints)))