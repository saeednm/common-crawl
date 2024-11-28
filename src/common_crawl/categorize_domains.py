import pandas as pd
import requests
import time


# API configuration
API_URL = "https://website-categorization.whoisxmlapi.com/api/v2"
API_KEY = "your_api_key_here"  # Replace with your API key

def categorize_website(domain):
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
