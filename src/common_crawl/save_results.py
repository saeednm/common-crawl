import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa

# Example DataFrame
data = {
    "domain": ["example.com", "google.com", "wikipedia.org", "example.com"],
    "category": ["Business", "Search Engine", "Education", "Business"],
    "path": [["/about", "/products"], ["/search", "/maps"], ["/", "/wiki"], ["/contact"]],
}
df = pd.DataFrame(data)

def save_df_to_parquet(df: pd.DataFrame):

    # Convert the 'path' column to strings for compatibility with Parquet
    df["path"] = df["path"].apply(lambda x: ",".join(x))

    # Save to Parquet with partitioning by 'category'
    output_path = "output_partitioned"
    table = pa.Table.from_pandas(df)

    # Write the table partitioned by the 'category' column
    pq.write_to_dataset(
        table,
        root_path=output_path,
        partition_cols=["category"]
    )

    print(f"Data saved to {output_path} partitioned by 'category'")
