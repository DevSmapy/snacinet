from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("cinevault").getOrCreate()

def load_parquet_data():
    df = spark.read.parquet("/Users/leeyongkyun/Documents/CineVault/data")
    return df

def query_data(column_name, value):
    df = load_parquet_data()
    try:
        filtered_df = df.filter(df[column_name] == value).collect()
        json_result = [row.asDict() for row in filtered_df]
        return json_result
    except Exception as e:
        return ValueError(f"Error: {e}")


if __name__ == "__main__":
    print(query_data("prdtYear", "2020"))