# Retail-Data-Pipeline
![Architecture_Diagram](https://github.com/mihir170901/Retail-Data-Pipeline/assets/73994476/d9077f5f-fe63-451b-bca7-12a2cb1af8e9)

## Extract
Initially data in ingested from two sources i.e On-Premise SQL server and Azure Storage account.
Data stored in On-Premise SQL server is basically a Fact table for day-to-day transactions and data stored in Storage account is a small dimension table in csv format.
(All the data is generated synthetically using a Python script and dumped then dumped accordingly into sources to support the architecture)
Azure Data Factory is used to ingest data from these two sources and store it into a Azure Data Lake Storage(ADLS) in Parquet Format.

## Transform
Azure Databricks is used to transform the data stored in ADLS.
ADLS is first mounted onto the Databricks and then it used to perform necessary transformations according to the business logic and make the data ready for reporting needs.
Again this transformed data is stored into another container in ADLS.

## Load
Here we are using Azure Synapse Analytics as our Warehousing solution.
An External table is created in Synapse Analytics which lookups the transformed data stored in ADLS.
Synapse Analytics is also used to query the data and perform some adhoc request to support business requirements.
The External Table is conected to PowerBI to create reports and dashboards.
This reports are updtaed in realtime as soon as the data stored in our sources gets updated.

Below are some sample for our reports :
![Retail_Analysis](https://github.com/mihir170901/Retail-Data-Pipeline/assets/73994476/38fce857-ac84-4290-99b0-340758931457)
![Retail_Analysis_combined](https://github.com/mihir170901/Retail-Data-Pipeline/assets/73994476/10a1f76a-a51d-429e-b71f-c8b4d967dfcd)


