-- Active: 1703424810609@@127.0.0.1@5434@postgres
/*
================================================================================

Nama : Saepul Hilal

Batch : HCK - 010

File ini bertujuan untuk membuat TABLE dan memasukan data pada TABLE tersebut

================================================================================
*/


CREATE Table Table_m3(
    id SERIAL PRIMARY KEY,
    Retailer VARCHAR NOT NULL, 
    Retailer_ID INT NOT NULL, 
    Invoice_Date DATE NOT NULL, 
    Region VARCHAR NOT NULL, 
    State VARCHAR NOT NULL, 
    City VARCHAR NOT NULL,
    Product VARCHAR NOT NULL, 
    Price_per_Unit FLOAT NOT NULL, 
    Units_Sold INT NOT NULL, 
    Total_Sales FLOAT NOT NULL,
    Operating_Profit FLOAT NOT NULL, 
    Operating_Margin FLOAT NOT NULL, 
    Sales_Method VARCHAR NOT NULL
)

COPY Table_m3(
    Retailer, 
    Retailer_ID, 
    Invoice_Date, 
    Region, 
    State, 
    City,
    Product, 
    Price_per_Unit, 
    Units_Sold, 
    Total_Sales,
    Operating_Profit, 
    Operating_Margin, 
    Sales_Method
)
FROM 'airflow/dags/P2M3_saepul_hilal_data_raw.csv' DELIMITER ','
CSV HEADER;


COPY table_m3
FROM 'airflow/dags/P2M3_saepul_hilal_data_raw.csv' DELIMITER ','
CSV HEADER;


SELECT * FROM table_m3
