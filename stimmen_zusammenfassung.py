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

def count_enthaltung(df):
	count = 0
	for i, row in df.iterrows():
		if get_enthaltung(row):
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
def count_gesamt(df):
	return len(df)




def count_votes(df):
	output = []
	output.append(count_gesamt(df))
	output.append(count_ja(df))
	output.append(count_nein(df))
	output.append(count_enthaltung(df))
	# output.append(count_ungueltig(df))
	output.append(count_nichtAbgegeben(df))
	return output

def zusammenfassung_erzeugen(file_path_input, file_path_output):
	data = pd.read_csv(file_path_input)
	parteien_liste = data['Fraktion/Gruppe'].unique()

	column_labels = ['Sitzungsnr', 'Stimmnr', 'Partei', 'Gesamt', 'Ja', 'Nein', 'Enthaltung', 'nichtAbgegeben']
	output_df = pd.DataFrame(columns=column_labels)


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
				stimmen_partei_series = pd.Series(stimmen_partei, index=output_df.columns)
				output_df = pd.concat([output_df,stimmen_partei_series.to_frame().T], ignore_index=True)
	print(output_df)
	output_df.to_csv(file_path_output, index=False)


def majority_vote(inputpath, outputpath):
	df_majority = pd.read_csv(inputpath)
	mehrheiten = []
	for i, row in df_majority.iterrows():
		mehrheiten.append(row[['Ja', 'Nein', 'Enthaltung', 'nichtAbgegeben']].idxmax())
	df_majority['Mehrheitsstimme'] = mehrheiten
	df_majority.to_csv(outputpath, index=False)


# zusammenfassung_erzeugen('./output.csv', 'stimmen_zusammenfassung.csv')
majority_vote('stimmen_zusammenfassung.csv', 'stimmen_zusammenfassung_mehrheitsstimme.csv')