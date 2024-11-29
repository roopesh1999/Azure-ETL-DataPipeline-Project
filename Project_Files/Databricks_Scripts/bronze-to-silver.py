# Databricks notebook source
from pyspark.sql.functions import date_format, from_utc_timestamp
from pyspark.sql.types import TimestampType

# COMMAND ----------

input_path = "/mnt/bronze-layer/SalesLT/"

# COMMAND ----------

table_names = []
for i in dbutils.fs.ls(input_path):
  table_names.append(i.name.split("/")[0])

# COMMAND ----------

table_names

# COMMAND ----------

for name in table_names:
  df = spark.read.format("csv").option("header", "True").load(input_path + name + "/" + name + ".csv");
  for col in df.columns:
    if "Date" in col or "date" in col:
      df = df.withColumn(col, date_format(from_utc_timestamp(df[col].cast(TimestampType()),"UTC"), "yyyy-MM-dd"))
  output_path = "/mnt/silver-layer/SalesLT/" + name + "/"
  df.write.format("delta").mode("overwrite").save(output_path)