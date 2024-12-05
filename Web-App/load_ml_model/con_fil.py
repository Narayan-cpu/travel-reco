import pandas as pd
import re
import numpy as np
from collections import Counter

class content_filtering():

	def cnt_flt(self, user_df, df):
		print(user_df.columns)
		df['Category'] = df['Category'].str.strip()
		df = df[['Place_id', 'Title', 'Description', 'Category', 'Distance (Km.)',
       'Rating', 'Expense (Per Head in Rs.)', 'n_days', 'Boarding_pt','State', 'Place_sentiment', 'Overall_state_sentiment']]
		print(df['Category'].unique())
		metadata = df.copy()
		WORD = re.compile(r'\w+')

		def LD(s, t):
			if s == "":
				return len(t)
			if t == "":
				return len(s)
			if s[-1] == t[-1]:
				cost = 0
			else:
				cost = 1

			res = min([LD(s[:-1], t) + 1,
					   LD(s, t[:-1]) + 1,
					   LD(s[:-1], t[:-1]) + cost])
			return res

		def text_to_vector(text):
			words = WORD.findall(text)
			return Counter(words)

		# remove spaces from the category column of dataset
		def clean_data(x):
			if isinstance(x, list):
				return [str.lower(i.replace(" ", "")) for i in x]
			else:
				if isinstance(x, str):
					return str.lower(x.replace(" ", ""))
				else:
					return ''

		C = metadata['Rating'].mean()
		m = 1
		print(C)

		def weighted_rating(x, m=m, C=C):
			v = 1
			R = x['Rating']
			# Calculation based on the Bayesian Rating Formula
			return (v / (v + m) * R) + (m / (m + v) * C)

		metadata['Category'] = metadata['Category'].apply(clean_data)
		metadata.dropna(subset=['Title'], inplace=True)
		metadata.reset_index(drop=True, inplace=True)
		res_df = metadata[metadata['State'].str.strip().apply(lambda x: x.lower()).isin(
			(user_df['State'].apply(lambda x: x.lower())))]
		print(res_df.shape[0], '1st shape')
		res_df = res_df[res_df['Category'].str.strip().apply(lambda x: x.lower()).isin(
			(user_df['Category'].str.strip().apply(lambda x: x.lower())))]
		print(res_df.shape[0], '2nd shape')
		other_df = metadata[metadata['Category'].str.strip().apply(lambda x: x.lower()).isin((user_df['Category']. \
																							  apply(
			lambda x: x.lower())))]
		other_df = other_df[other_df['State'].str.strip().apply(lambda x: x.lower()) != user_df['State']. \
			apply(
			lambda x: x.lower()).values[0]]
		other_df['other_recomms'] = str(list(other_df['State'].unique()))
		other_df['other_recomms'] = other_df['other_recomms'].apply(
			lambda x: x.replace('[', '').replace(']', '').replace("'", ""))
		res_df['other_recomms'] = other_df['other_recomms'].values[0]
		res_df = res_df[
			['Title', 'Description', 'Category', 'Distance (Km.)', 'Expense (Per Head in Rs.)', 'Rating','n_days', 'Boarding_pt', \
			 'Place_sentiment', 'Overall_state_sentiment', 'other_recomms']]

		if(res_df.shape[0] != 0):
			res_df = res_df.sort_values(['Rating', 'Place_sentiment', 'Expense (Per Head in Rs.)', 'n_days'], ascending=False)
			res_df.reset_index(drop=True, inplace=True)
			print('res df', res_df)
			n_days_mean = res_df['n_days'].mean()
			budget_mean = ((res_df['Expense (Per Head in Rs.)'].mean())/1000)
			print('budget', budget_mean, 'n_days', n_days_mean)
			n_days_mean_l = user_df['n_days'].astype(int).unique() / n_days_mean
			budget_mean_l = user_df['Budget'].astype(int).unique() / budget_mean

			tot_mean = int((n_days_mean_l + budget_mean_l) / 2)
			res_df = res_df[:tot_mean]
			res_df = res_df[
				['Title', 'Description', 'Rating' ,'Category', 'Distance (Km.)', 'Expense (Per Head in Rs.)', 'n_days', 'Boarding_pt', \
				 'Place_sentiment', 'Overall_state_sentiment', 'other_recomms']]
			recomm_df = res_df.fillna('N.A.').copy()
			recomm_df = recomm_df.apply(lambda x: x.astype(str).str.upper())
			print(recomm_df.columns, recomm_df)

			return recomm_df
		else:
			recomm_df = pd.DataFrame({'Title': ["Sorry! No Recommendaitons found. Please refine your search."]})#, 'b': [2,3,4]})
			# recomm_df = pd.DataFrame(np.array(1), \
			# 						 columns = ['Title']), 'Description', 'Category', 'Distance (Km.)', 'Expense (Per Head in Rs.)', 'n_days', 'Boarding_pt', \
				 # 'Place_sentiment', 'Overall_state_sentiment'])

			recomm_df['Description'] = "-"
			recomm_df['Distance (Km.)'] = "-"
			recomm_df['Expense (Per Head in Rs.)'] = "-"
			recomm_df['n_days'] = "-"
			recomm_df['Boarding_pt'] = "-"
			recomm_df['Place_sentiment'] = "-"
			recomm_df['Overall_state_sentiment'] = "-"
			recomm_df['other_recomms'] = other_df['other_recomms'].values[0]
			print(recomm_df)
			return recomm_df