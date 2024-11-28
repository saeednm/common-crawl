import pandas as pd
import requests
import time
import aggregare_by_doamin
import save_aggregate_table


# API configuration
API_URL = "https://website-categorization.whoisxmlapi.com/api/v2"
API_KEY = "your_api_key_here"  # Replace with your API key

def categorize_website(domain):
    """
    Queries the API to categorize a website based on its domain.

    Args:
        domain (str): The domain to categorize.

    Returns:
        str: The category of the website, or 'Unknown' if unavailable.
    """
    try:
        response = requests.get(API_URL, params={"apiKey": API_KEY, "domainName": domain})
        response.raise_for_status()
        data = response.json()
        # Parse category from API response (adjust based on the API used)
        categories = data.get("categories", [])
        return ", ".join(categories) if categories else "Unknown"
    except Exception as e:
        print(f"Error categorizing {domain}: {e}")
        return "Unknown"

def add_category_to_df(df: pd.DataFrame):

    # Add the 'category' column to the DataFrame
    categories = []
    for domain in df["domain"]:
        categories.append(categorize_website(domain))
        time.sleep(1)  # To handle API rate limits, if necessary

    df["category"] = categories

    # Display the result
    print(df)
    return df

categorized_domains =  add_category_to_df(aggregare_by_doamin.aggregated)
save_aggregate_table.save_df_to_table(categorized_domains)
