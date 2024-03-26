import pandas as pd




def column_labels(df):
	labels = ['Sitzungsnr', 'Stimmnr', 'Partei', 'Vorname', 'Nachname']
	partei_liste = df['Fraktion/Gruppe'].unique()
	labels.extend(partei_liste)
	return labels

def count_uebereinstimmung():
	[]


def party_comparison(input, input_mehrheitsstimme, outputpath):
	mdb = pd.read_csv(input)
	parteistimmen = pd.read_csv(input_mehrheitsstimme)
	parteien = parteistimmen['Partei'].unique()
	for partei in parteien:
		partei_bool = []
		for i, row in mdb.iterrows():
			sitzungsnr = row['Sitzungnr']
			abstimmnr = row['Abstimmnr']
			entsprechende_mehrheitsstimme = parteistimmen[(parteistimmen['Sitzungsnr'] == sitzungsnr) & (parteistimmen['Stimmnr'] == abstimmnr) & (parteistimmen['Partei'] == partei)].iloc[0]
			if row['stimme'].lower() == entsprechende_mehrheitsstimme['Mehrheitsstimme'].lower():
				partei_bool.append(True)
			else:
				partei_bool.append(False)
		mdb['wie_'+partei] = partei_bool
	mdb.to_csv(outputpath, index=False)



def fraktionsslose_stimmen(input, output):
	stimme = []
	data = pd.read_csv(input)
	data = data[data['Fraktion/Gruppe'] == 'Fraktionslos']
	for i, row in data.iterrows():
		stimme.append(row[['ja', 'nein', 'Enthaltung', 'nichtabgegeben']].idxmax())
	data['stimme'] = stimme
	data.to_csv(output, index=False)

# fraktionsslose_stimmen('output.csv', 'output_fraktionslose.csv')
party_comparison('output_fraktionslose.csv', 'stimmen_zusammenfassung_mehrheitsstimme.csv', 'fraktionslose_comparison.csv')