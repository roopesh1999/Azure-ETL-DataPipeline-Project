# Azure ETL Data Pipeline Project

This project demonstrates the implementation of an end-to-end ETL (Extract, Transform, Load) workflow using Azure services for data ingestion, transformation, and visualization. The pipeline processes data from an on-premises SQL Server database and visualizes it in Power BI.

---

## Workflow Overview

The pipeline integrates the following components:

1. **Data Source:**
   - On-premises SQL Server (AdventureWorksLT2022).

2. **Bronze Layer:**
   - Raw data ingested into Azure Data Lake Gen2 using Azure Data Factory.

3. **Silver Layer:**
   - Transformed data using Azure Databricks (e.g., date formatting, column renaming, binary conversion).

4. **Gold Layer:**
   - Cleaned and enriched data stored in Delta format, queried via Azure Synapse Analytics.

5. **Power BI Dashboard:**
   - Visualizes and updates data in real-time after ADF pipeline runs.

---

## Architecture Diagram

*I will insert this later*

---

## Tools Used

- **Azure Data Factory (ADF):** For data ingestion and pipeline scheduling.
- **Azure Data Lake Gen2:** For hierarchical storage with Bronze, Silver, and Gold layers.
- **Databricks:** For PySpark-based data transformations.
- **Azure Synapse Analytics:** Serverless SQL for querying data.
- **Power BI:** For interactive data visualization and reporting.

---

## Data Transformation Details

### **Level 1 Transformations (Bronze → Silver):**
1. Removed timestamps, retained only dates.

### **Level 2 Transformations (Silver → Gold):**
1. Renamed columns for better readability.
2. Converted `ThumbnailPhoto` column from string to binary.

---

## Key Features

- **Automated Data Updates:**
  - ADF pipelines fetch fresh data and update Power BI after transformation.

- **Real-Time Dashboard:**
  - Customer count dynamically updates when new rows are added.

- **Scalable Design:**
  - Prepared for larger datasets and future enhancements.

---

## Challenges Faced

1. **Power BI Binary Data Issue:**
   - Binary data (`ThumbnailPhoto`) was excluded due to Power BI limitations.

2. **Databricks Quota Limits:**
   - Resolved cluster creation issues by adjusting quotas for `standardDDSv5Family`.

---

## Future Enhancements

- Automate secrets management using Azure Key Vault.
- Optimize Delta table performance with partitioning.
- Expand Power BI dashboard for richer insights.

---

## How to Use

### Clone this repository:
```bash
git clone https://github.com/roopesh1999/Azure-ETL-DataPipeline-Project.git