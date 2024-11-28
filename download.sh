#!/bin/bash

# Set the base URL for the crawl index
CRAWL_INDEX="CC-MAIN-2024-46"
BASE_URL="https://data.commoncrawl.org/crawl-data/$CRAWL_INDEX/warc.paths.gz"
# Get the list of segment IDs
wget $BASE_URL
# Select the first 3 segments 
gunzip -f warc.paths.gz
head -n 3 warc.paths  > selected_warc_files.txt

mkdir -p commoncrawl_segments
while read -r WARC_PATH; do
    wget "https://data.commoncrawl.org/$WARC_PATH" -P commoncrawl_segments/
done < selected_warc_files.txt
