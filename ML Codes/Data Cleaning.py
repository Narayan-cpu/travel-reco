import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

df = pd.DataFrame()
for i in ['Agra', 'Andaman', 'Delhi', 'Goa', 'Himachal', 'Ooty', 'Tirupati', 'Varanasi']:
    loc = 'D:/Downloads/Sabre Hack/Datasets/' + i+'.csv'
    df1 = pd.read_csv(loc)
    df['Place'] = i
    df = pd.concat([df, df1], ignore_index=True)

df['Distance (Km.)'] = df['Description'].apply(lambda x: x[:50])
df['Distance (Km.)'] = df['Distance (Km.)'].str.extract('(\d+)')
df['Rating'] = np.random.uniform(3.1, 4.9, df.shape[0])
df['Expense (Per Head in Rs.)'] = np.random.randint(500, 1500, df.shape[0])
df['n_days'] = np.random.randint(1, 3, df.shape[0])
df['Boarding_pt'] = df['Description'].apply(lambda x: x[:25])
df.loc[(df['Boarding_pt'].str.startswith('from') == True) | df['Boarding_pt'].str.startswith('rom') == True,\
       'Boarding_pt'] = df['Boarding_pt'].apply(lambda x: x.replace('from', '').replace('rom', '').split(' ')[:2])
df['Place_id'] = range(1, len(df)+1)
df['Place_id'] = df['Place_id'].astype(str)
df['Place_id'] = 'TD-'+df['Place_id']
df['State'] = ''
df.loc[df['Place'] == 'Agra', 'State'] = 'Uttar Pradesh'
df.loc[df['Place'] == 'Andaman', 'State'] = 'Andaman & Nicobar Islands'
df.loc[df['Place'] == 'Delhi', 'State'] = 'Delhi'
df.loc[df['Place'] == 'Goa', 'State'] = 'Goa'
df.loc[df['Place'] == 'Himachal', 'State'] = 'Himachal Pradesh'
df.loc[df['Place'] == 'Ooty', 'State'] = 'Tamil Nadu'
df.loc[df['Place'] == 'Tirupati', 'State'] = 'Andhra Pradesh'
df.loc[df['Place'] == 'Varanasi', 'State'] = 'Uttar Pradesh'

df = df[['Place_id', 'Title', 'Description', 'Category', 'Distance (Km.)',
       'Rating', 'Expense (Per Head in Rs.)', 'n_days', 'Boarding_pt', 'Place', 'State']]

df.to_csv('D:/Downloads/Sabre Hack/Datasets/all_locs.csv', index=False)