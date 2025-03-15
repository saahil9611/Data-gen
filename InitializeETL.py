```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, max, min

# Initialize Spark session
spark = SparkSession.builder \
    .appName("ETL Model") \
    .getOrCreate()

# Define the path to the CSV file
csv_file_path = "/workspaces/Data-gen/healthcare_dataset.csv"

# Extract: Read the CSV file into a DataFrame
df = spark.read.csv(csv_file_path, header=True, inferSchema=True)

# Transform: Perform data transformations
# Example: Filter out rows with null values
df_filtered = df.dropna()

# Example: Add a new column with transformed data
df_transformed = df_filtered.withColumn("new_column", col("existing_column") * 2)

# Load: Show the transformed data
df_transformed.show()

# Reporting: Generate different reporting patterns
# Example 1: Sum of a column
sum_df = df_transformed.groupBy("group_column").agg(sum("numeric_column").alias("sum_column"))
sum_df.show()

# Example 2: Average of a column
avg_df = df_transformed.groupBy("group_column").agg(avg("numeric_column").alias("avg_column"))
avg_df.show()

# Example 3: Maximum value of a column
max_df = df_transformed.groupBy("group_column").agg(max("numeric_column").alias("max_column"))
max_df.show()

# Example 4: Minimum value of a column
min_df = df_transformed.groupBy("group_column").agg(min("numeric_column").alias("min_column"))
min_df.show()

# Stop the Spark session
spark.stop()
```