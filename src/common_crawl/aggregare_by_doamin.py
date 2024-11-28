from urllib.parse import urlparse
import pandas as pd

# Step 1: Parse domain and path
def extract_domain_and_path(url):
    parsed = urlparse(url)
    return parsed.netloc, parsed.path

def aggregate_by_domain(df: pd.DataFrame):

    # Apply parsing function to extract domain and path
    df[["domain", "paths"]] = df["link"].apply(lambda url: pd.Series(extract_domain_and_path(url)))

    # Step 2: Aggregate paths into a set for each domain
    aggregated = df.groupby("domain").agg(
        domain_frequency=("domain", "size"),  # Count the number of occurrences for each domain
        paths=("paths", lambda x: set(x))     # Aggregate paths into a set
    ).reset_index()

    # Display the result
    print(aggregated)
    return aggregated


