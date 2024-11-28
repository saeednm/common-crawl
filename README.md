# common-crawl

the goal of this project is to ingest and analyze sample data from internet crawled public data prepared by common-crawl. 

### download WARC files

execute ```download.sh``` bash file to go to commoncrawl.org and download 3 segments of the most recent data to local

``` sh download.sh ```

### initialize docker environment

run the following command to start a postgres db instance and our dockerized python project

``` docker compose up ```

#### steps 

1. for each downloaded WARC file extract every external link you can find and save them in txt file line by line(```ingest_warc.py```)
2. Load the data into a single column postgres table on docker (```insert_db.py```)
3. read from table into pandas dataframe for next step aggregations(```read_table.py```)
4. add a column to df as a flag that indicates if the link redirects to a home page or a subsection (```add_flag.py```)
5. Aggregate dataframe by primary links and compute their frequency by also keeping track of subsections(```aggregare_by_doamin.py```)
6. add a column to df to indicate country of the url (```add_country.py```)
7. Add a column that categorizes the type of content hosted by the website by using an external api (```categorize_domains.py```)
8. save aggregated dataframe into postgre db (```save_aggregate_table.py```)
9. The final aggregation result dataframe saved in columnar (arrow) files following a
partition schema on county name (```save_results.py```)

