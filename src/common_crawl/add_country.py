from urllib.parse import urlparse
import pandas as pd

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
        domain = url.split('.')[-1]  # Extract TLD
        return TLD_TO_COUNTRY.get(domain, "Unknown")
    except Exception as e:
        return "Unknown"

def add_country_column(reference , df: pd.DataFrame):

    df["country"] = df.apply(lambda x: infer_country_from_url(x[reference]), axis=1)
    return df



