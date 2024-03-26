import pandas as pd

def get_ja(row):
	return row['ja'] == True

def get_nein(row):
	return row['nein'] == True

def get_enthaltung(row):
	return row['Enthaltung'] == True

def get_ungueltig(row):
	return row['ungültig'] == True

def get_nichtAbgegeben(row):
	return row['nichtabgegeben'] == True


def count_ja(df):
	count = 0
	for i, row in df.iterrows():
		if get_ja(row):
			count += 1
	return count

def count_nein(df):
	count = 0
	for i, row in df.iterrows():
		if get_nein(row):
			count += 1
	return count

def count_ungueltig(df):
	count = 0
	for i, row in df.iterrows():
		if get_enthaltung(row):
			count += 1
	return count

def count_nichtAbgegeben(df):
	count = 0
	for i, row in df.iterrows():
		if get_nichtAbgegeben(row):
			count += 1
	return count





def count_votes(df):
	output = []
	output.append(count_ja(df))
	output.append(count_nein(df))
	output.append(count_ungueltig(df))
	output.append(count_nichtAbgegeben(df))
	return output

data = pd.read_csv('./output.csv')
parteien_liste = data['Fraktion/Gruppe'].unique()

output_df = pd.DataFrame()

sitzungsnummern = data['Sitzungnr'].unique()

for sitzungsnr in sitzungsnummern:
	df_sitzungsnr = data[data['Sitzungnr'] == sitzungsnr]
	unique_stimmnr = df_sitzungsnr['Abstimmnr'].unique()
	for stimmnr in unique_stimmnr:
		df_sitzungsnr_stimmnr = df_sitzungsnr[df_sitzungsnr['Abstimmnr'] == stimmnr]
		for partei in parteien_liste:
			stimmen_partei = [sitzungsnr, stimmnr, partei]
			df_sitzungsnr_stimmnr_partei = df_sitzungsnr_stimmnr[df_sitzungsnr_stimmnr['Fraktion/Gruppe'] == partei]
			stimmen_partei.extend(count_votes(df_sitzungsnr_stimmnr_partei))
			print(stimmen_partei)