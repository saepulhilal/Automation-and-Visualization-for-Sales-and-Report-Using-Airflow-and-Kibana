'''
================================================================================================================================================================

Nama : Saepul Hilal

Batch : HCK - 010

File ini bertujuan untuk membuat proses data cleaning

================================================================================================================================================================
'''

import pandas as pd

'''
Membuat fungsi cleaning_data. fungsi ini akan menghapus data duplicate, merubah tipe data,
merubah nama kolom, mengganti 'spasi' dengan '_', menghilangkan missing value, dan
akan menyimpan data csv baru.
'''

def cleaning_data():
    df= pd.read_csv('/opt/airflow/data/P2M3_saepul_hilal_data_raw.csv') # read data csv kotor
    
    df.drop_duplicates(inplace=True) # delete duplicate data
    df['Invoice Date'] = pd.to_datetime(df['Invoice Date']) # merubah tipe data
    df.columns = df.columns.map(str.lower) # membuat nama kolom menjadi lowercase

    # mengganti 'spasi' dengan '_'
    trans_table = str.maketrans(' ', '_')
    df.columns = [col.translate(trans_table) for col in df.columns] 

    df.dropna(inplace=True) # Delete missing value
    df.to_csv('/opt/airflow/data/P2M3_saepul_hilal_data_clean.csv', index=False) # menyimpan data yang sudah clean
