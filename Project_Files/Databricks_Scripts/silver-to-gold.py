# Databricks notebook source
from pyspark.sql.functions import col
from pyspark.sql.types import TimestampType, BinaryType

# COMMAND ----------

input_path = "/mnt/silver-layer/SalesLT/"
output_path = "/mnt/gold-layer/SalesLT/"

# COMMAND ----------

table_names = []
for i in dbutils.fs.ls(input_path):
  table_names.append(i.name.split("/")[0])

# COMMAND ----------

table_names

# COMMAND ----------

for name in table_names:
  df = spark.read.format("delta").load(input_path + name + "/")
  old_col = df.columns
  for old_col in df.columns:
    new_col = "".join(["_" + char if char.isupper() and not (i == 0 or old_col[i - 1].isupper()) else char for i, char in enumerate(old_col)]).lstrip("_")
    df = df.withColumnRenamed(old_col, new_col)

  # Check if the current table is 'Product' and apply the type cast
  if name.lower() == "product":  # Match table name to 'Product' table
      df = df.withColumn("Thumb_Nail_Photo", col("Thumb_Nail_Photo").cast(BinaryType()))
  df.write.format("delta").mode("overwrite").option("mergeSchema", "true").save(output_path + name + "/")