import requests
import pandas as pd
import csv

df = pd.read_excel("/content/Train.xlsx", encoding='latin1')
df.head()
df['Text'] = df['Text'].replace(r'http\S+', '', regex=True).replace(r'www\S+', '', regex=True)
df.to_csv('Train_withouthyperlink.csv')
