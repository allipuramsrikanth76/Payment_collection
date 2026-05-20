#importing the required libraries
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#f for warnings
import warnings
warnings.filterwarnings('ignore')

#Build a realiable path to dataset relative to this files
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
dataset_path = os.path.join(base_dir, 'Data/train', 'dataset.csv')

if not os.path.exists(dataset_path):
    raise FileExistsError(f"Dataset not found at expected path: {dataset_path}")


# Store the dataset into the dataframe
df_original = pd.read_csv(dataset_path)
df_original_dump = df_original.copy()
#print(df_original_dump.head())


#checking the shape i=of the datset
df_shape = df_original_dump.shape
#print(f"Dataset shape: {df_shape}")

#Info about the dataset
df_info = df_original_dump.info()
#print(f"Dataset info: {df_info}")

#Displaying the dataset columns names
df_columns = df_original_dump.columns
#print(f"Dataset columns: {df_columns}")

#Describing the dataset
df_description = df_original_dump.describe()
#print(f"Dataset description: {df_description}")


###### Data cleaning and preprocessing
#print(df_original_dump.head())

#Displaying the null values percentage against every clumns (compare to the total number of records)
null_values_percentage = df_original_dump.isnull().mean() * 100
#print(f"Null values percentage: {null_values_percentage}")

#Displaying invoice _id and Doc_id
invoice_doc_id = df_original_dump.loc[:, ['invoice_id', 'doc_id']]
#print(invoice_doc_id)

#Comparing between baselind and document create data
Comparison1 = pd.Series(np.where(df_original_dump['baseline_create_date'] == df_original_dump['document_create_date'], True, False))
#print("Compare between abseline create date and document create date: \n", Comparison1.value_counts())

Comparison2 = pd.Series(np.where(df_original_dump['document_create_date'] == df_original_dump['document_create_date.1'], True, False))
#print("Compare between documebt create date and document create date.1:\n", Comparison2.value_counts())

#comparing between document_create_date.1 and baseline create date
comparison3 = pd.Series(np.where(df_original_dump['document_create_date.1'] == df_original_dump['baseline_create_date'], True, False))
#print("Compare between document create date.1 and baseline create date:\n", comparison3.value_counts())


#Check  column posting_id is constant column or not
posting_id_unique_values = df_original_dump.posting_id.nunique()
#print(f"Unique values in posting id column: {posting_id_unique_values}")


#isOpen is a constant column and relavant column for this project or not
isOpen_unique_values = df_original_dump.isOpen.unique()
#print(f"unique values in isOpen column: {isOpen_unique_values}")
isOpen_unique_values_count = df_original_dump.isOpen.value_counts()
#print(f"Unique values count in isOpen column: \n{isOpen_unique_values_count}")

#Drop all the following columns from the dataset because they are constant columns
#"are_business"
#"posting_id"
#invoice_id
#document_create_date
#isOpen
#document type
#Document_create_date.1
#

df_original_dump.drop(['area_business', 'posting_id', 'invoice_id', 'document_create_date', 'isOpen', 'document type', 'document_create_date.1'], axis=1, inplace=True)
#print(df_original_dump.columns)

#please check the dataset after dropping the column
#print(df_original_dump.shape)
#print(df_original_dump.columns.to_list())


#show all the duplicate records in the dataframe
duplicate_records = df_original_dump[df_original_dump.duplicated()]
#print(duplicate_records)

#displaying the number of duplicate records in the dataset
duplicate_records_count = df_original_dump.duplicated().sum()
#print(f"Number of duplicate records in the dataset: {duplicate_records_count}")


#Drop the all duplicate records from the dataset
df_original_dump.drop_duplicates(inplace=True)

#check the duplcated records after dropping them
#print(df_original_dump.duplicated().sum())

#check the number of rows and columns in your dataset after the dropping
#print(df_original_dump.shape)

#find out the total count of null values in each columns
print(df_original_dump.isnull().sum())
















