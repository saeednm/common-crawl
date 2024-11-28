
from db_config import db_config_map
from add_flag import add_is_homepage_flag
from ingest_warc import extract_and_save_external_links
from insert_db import read_and_insert_links_to_db
from read_table import read_table_into_df
from aggregare_by_doamin import aggregate_by_domain
from add_country import add_country_column
from categorize_domains import add_category_to_df
from save_aggregate_table import save_df_to_table
from save_results import save_df_to_parquet

def main():
    """Entry point for the application script"""
    #extract_and_save_external_links()
    #read_and_insert_links_to_db(db_config_map)
    raw_table_df = read_table_into_df(db_config_map, 'external_links', "link")
    #add_is_homepage_flag(raw_table_df)
    aggregated = aggregate_by_domain(raw_table_df)
    add_country_column(aggregated)
    save_df_to_table(aggregated, db_config_map)
    categorized = add_category_to_df(aggregated)
    save_df_to_parquet(categorized)
    
    print("success exit")

main()