library(plumber)
# 'api.R' is the location of the file shown above
pr("api.R") %>%
  pr_run(port=8084)