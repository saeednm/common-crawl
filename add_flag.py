from urllib.parse import urlparse
import pandas as pd
import read_table

def check_if_is_homepage(url):
    url_parsed = urlparse(url)
    return  url_parsed.path == "" or url_parsed.path == "/"


def add_flag(df: pd.DataFrame):

    df["is_homepage"] = df.apply(lambda x: check_if_is_homepage(x['link']), axis=1)
    print(df)


add_flag(read_table.df)