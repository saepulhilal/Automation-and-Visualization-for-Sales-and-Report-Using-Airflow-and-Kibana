'''
================================================================================================================================================================

Nama : Saepul Hilal

Batch : HCK - 010

File ini bertujuan untuk membuat proses pengambilan data

================================================================================================================================================================
'''

import pandas as pd
from sqlalchemy import create_engine

'''
Membuat fungsi fetching_data. Fungsi ini bertugas untuk menarik data dari postgres
'''
def fetching_data():
    # Koneksi ke postgres
    engine = create_engine("postgresql+psycopg2://airflow:airflow@postgres:5432/airflow")
    conn = engine.connect()

    df = pd.read_sql_query("select * from table_m3", conn) # Memilih kolom yang akan di tarik datanya

    df.to_csv('/opt/airflow/data/P2M3_saepul_hilal_data_raw.csv' , sep=',', index=False) # Menyimpan data yang ditarik