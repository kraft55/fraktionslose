import pandas as pd

def get_ja(row):
	return row['ja']

def get_nein(row):
	return row['nein']

def get_enthaltung(row):
	return row['enthaltung']

def get_ungueltig(row):
	return row['ungültig']

def get_nichtAbgegeben(row):
	return row['nichtabgegeben']


def count_votes(df):
	list = []



data = pd.read_csv('./output.csv')

sitzungsnummern = data['Sitzungsnr'].unique()

for sitzungsnr in sitzungsnummern:
	df_sitzungsnr = data[data['Sitzungsnr'] == sitzungsnr]
	print(sitzungsnr, df_sitzungsnr.head())