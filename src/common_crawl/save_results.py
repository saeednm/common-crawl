import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa


def save_df_to_parquet(df: pd.DataFrame):

    # Convert the 'path' column to strings for compatibility with Parquet
    df["paths"] = df["paths"].apply(lambda x: ",".join(x))

    # Save to Parquet with partitioning by 'country'
    output_path = "output_partitioned"
    table = pa.Table.from_pandas(df)

    # Write the table partitioned by the 'country' column
    pq.write_to_dataset(
        table,
        root_path=output_path,
        partition_cols=["country"]
    )

    print(f"Data saved to {output_path} partitioned by 'country'")
