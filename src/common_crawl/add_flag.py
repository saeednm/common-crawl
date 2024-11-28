from urllib.parse import urlparse
import pandas as pd

def check_if_is_homepage(url):
    url_parsed = urlparse(url)
    return  url_parsed.path == "" or url_parsed.path == "/"


def add_is_homepage_flag(df: pd.DataFrame):

    df["is_homepage"] = df.apply(lambda x: check_if_is_homepage(x['link']), axis=1)
    print(df)


