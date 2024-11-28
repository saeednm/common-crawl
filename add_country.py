from urllib.parse import urlparse
import pandas as pd
import add_flag

# Map of TLDs to countries
TLD_TO_COUNTRY = {
    "com": "International",
    "org": "International",
    "net": "International",
    "us": "United States",
    "uk": "United Kingdom",
    "ca": "Canada",
    "au": "Australia",
    "in": "India",
    "cn": "China",
    # Add more TLDs as needed
}

def infer_country_from_url(url):
    """
    Infers the country from the top-level domain (TLD) of a URL.

    Args:
        url (str): The URL to analyze.

    Returns:
        str: The inferred country or 'Unknown'.
    """
    try:
        domain = urlparse(url).netloc.split('.')[-1]  # Extract TLD
        return TLD_TO_COUNTRY.get(domain, "Unknown")
    except Exception as e:
        return "Unknown"

def update_country_column(df: pd.DataFrame):

    df["country"] = df.apply(lambda x: infer_country_from_url(x['link']), axis=1)
    print(df)


update_country_column(add_flag.df)
